/*
  Copyright (c) 2016-2017 University of Helsinki

  Permission is hereby granted, free of charge, to any person
  obtaining a copy of this software and associated documentation files
  (the "Software"), to deal in the Software without restriction,
  including without limitation the rights to use, copy, modify, merge,
  publish, distribute, sublicense, and/or sell copies of the Software,
  and to permit persons to whom the Software is furnished to do so,
  subject to the following conditions:

  The above copyright notice and this permission notice shall be
  included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
  ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
 */

package fi.hiit.dime;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import fi.hiit.dime.data.Profile;
import fi.hiit.dime.xdi.XdiService;
import xdi2.client.XDIClientRoute;
import xdi2.client.exceptions.Xdi2ClientException;
import xdi2.client.impl.XDIAbstractClient;
import xdi2.client.impl.local.XDILocalClient;
import xdi2.core.ContextNode;
import xdi2.core.Graph;
import xdi2.core.LiteralNode;
import xdi2.core.constants.XDILinkContractConstants;
import xdi2.core.exceptions.Xdi2Exception;
import xdi2.core.features.aggregation.Aggregation;
import xdi2.core.features.linkcontracts.instance.LinkContract;
import xdi2.core.features.linkcontracts.instance.PublicLinkContract;
import xdi2.core.features.linkcontracts.instance.RelationshipLinkContract;
import xdi2.core.features.linkcontracts.instance.RootLinkContract;
import xdi2.core.syntax.XDIAddress;
import xdi2.core.util.XDIAddressUtil;
import xdi2.core.util.iterators.EmptyIterator;
import xdi2.core.util.iterators.ReadOnlyIterator;
import xdi2.messaging.Message;
import xdi2.messaging.MessageEnvelope;
import xdi2.messaging.container.MessagingContainer;
import xdi2.messaging.response.MessagingResponse;

/**
 * Requests API controller.
 *
 * @author Markus Sabadello, markus@danubetech.com
 */
@RestController
@RequestMapping("/api/linkcontracts")
public class LinkContractsController extends AuthorizedController {

	private static final Logger LOG = LoggerFactory.getLogger(LinkContractsController.class);

	LinkContractsController() {
	}

	@RequestMapping(value="/view", method = RequestMethod.GET)
	public ResponseEntity<List<XdiLinkContract>>
	linkContractsView(Authentication auth)
			throws NotFoundException, BadRequestException
	{
		List<XdiLinkContract> result = new ArrayList<XdiLinkContract> ();

		for (Profile profile : XdiService.get().profileDAO.profilesForUser(getUser(auth).getId())) {

			// look in XDI graph

			Graph graph = XdiService.get().myGraph(profile);
			if (graph == null) continue;

			ContextNode linkContractsContextNode = graph.getDeepContextNode(XDIAddress.create("[$contract]"));
			ReadOnlyIterator<ContextNode> linkContractContextNodes = linkContractsContextNode == null ? new EmptyIterator<ContextNode> () : Aggregation.getAggregationContextNodes(linkContractsContextNode);

			// result

			for (ContextNode linkContractContextNode : linkContractContextNodes) {

				if (linkContractContextNode.getXDIAddress().toString().contains("$defer")) continue;

				RelationshipLinkContract linkContract = (RelationshipLinkContract) LinkContract.fromContextNode(linkContractContextNode);
				Profile authorizingAuthorityProfile = XdiService.findProfileByDidXDIAddress(linkContract.getAuthorizingAuthority());
				Profile requestingAuthorityProfile = XdiService.findProfileByDidXDIAddress(linkContract.getRequestingAuthority());
				String address = linkContract.getContextNode().getXDIAddress().toString();
				String authorizingAuthority = linkContract.getAuthorizingAuthority().toString();
				String requestingAuthority = linkContract.getRequestingAuthority().toString();
				String profileName = authorizingAuthorityProfile != null ? authorizingAuthorityProfile.name : (requestingAuthorityProfile != null ? requestingAuthorityProfile.name : null);
				String direction = authorizingAuthorityProfile != null ? "outgoing" : "incoming";
				result.add(new XdiLinkContract(
						address, 
						authorizingAuthority,
						requestingAuthority,
						profileName,
						direction));
			}
		}

		// done

		return new ResponseEntity<List<XdiLinkContract>>(result, HttpStatus.OK);
	}

	@RequestMapping(value="/delete", method = RequestMethod.POST)
	public ResponseEntity<String>
	linkContractsDelete(Authentication auth, @RequestParam String address)
			throws NotFoundException, BadRequestException
	{
		XDIAddress XDIaddress = XDIAddress.create(address);

		for (Profile profile : XdiService.get().profileDAO.profilesForUser(getUser(auth).getId())) {

			XDIAddress didXDIAddress = XdiService.getProfileDidXDIAddress(profile);

			if (didXDIAddress == null)
			    continue;

			// XDI request to local messaging container

			try {

				MessagingContainer messagingContainer = XdiService.get().myLocalMessagingContainer(profile);
				MessageEnvelope messageEnvelope = new MessageEnvelope();
				Message message = messageEnvelope.createMessage(didXDIAddress, -1);
				message.setFromXDIAddress(didXDIAddress);
				message.setToXDIAddress(didXDIAddress);
				message.setLinkContractClass(RootLinkContract.class);
				message.createDelOperation(XDIaddress);

				XDILocalClient client = new XDILocalClient(messagingContainer);
				client.send(messageEnvelope);
			} catch (Xdi2ClientException ex) {

				LOG.error("Cannot execute local XDI message: " + ex.getMessage(), ex);
				return new ResponseEntity<String>(HttpStatus.INTERNAL_SERVER_ERROR);
			}
		}
		
		// done

		return new ResponseEntity<String>(HttpStatus.NO_CONTENT);
	}

	@RequestMapping(value="/data/{target}", method = RequestMethod.GET)
	public ResponseEntity<XdiData>
	linkContractsData(Authentication auth, @PathVariable String target)
			throws NotFoundException, BadRequestException
	{
		Profile profile = XdiService.get().profileDAO.profilesForUser(getUser(auth).getId()).get(0);
		XDIAddress didXDIAddress = XdiService.getProfileDidXDIAddress(profile);

		XDIAddress targetXDIAddress = XDIAddress.create(target);

		// find XDI route

		XDIClientRoute<?> route;

		try {

			route = XdiService.get().getXDIAgent().route(targetXDIAddress);
		} catch (Xdi2Exception ex) {

			throw new RuntimeException(ex.getMessage(), ex);
		}

		// build XDI message

		Message message = route.createMessage(didXDIAddress, -1);
		message.setFromXDIAddress(didXDIAddress);
		message.setToXDIAddress(targetXDIAddress);
		message.setLinkContractXDIAddress(RelationshipLinkContract.createRelationshipLinkContractXDIAddress(targetXDIAddress, didXDIAddress, XDILinkContractConstants.XDI_ADD_GET));
		message.createGetOperation(XDIAddressUtil.concatXDIAddresses(targetXDIAddress, XDIAddress.create("#dime")));

		// send to XDI target

		XDIAbstractClient<?> client = (XDIAbstractClient<?>) route.constructXDIClient();

		XdiData result = new XdiData();

		try {

/*			RSASignatureCreator signatureCreator = new RSAGraphPrivateKeySignatureCreator(XdiService.get().myGraph(getUser(auth)));
			SigningManipulator manipulator = new SigningManipulator();
			manipulator.setSignatureCreator(signatureCreator);
			client.getManipulators().addManipulator(manipulator);*/

			MessagingResponse response = client.send(message.getMessageEnvelope());
			
			Graph resultGraph = response.getResultGraph();
			
			for (LiteralNode literalNode : resultGraph.getRootContextNode().getAllLiteralNodes()) {
				
				XDIAddress key = XDIAddressUtil.localXDIAddress(literalNode.getContextNode().getXDIAddress(), -1);
				Object value = literalNode.getLiteralData();
				
				if (key != null) result.data.put(key.toString(), value == null ? null : value.toString());
			}
		} catch (Xdi2ClientException ex) {

			throw new RuntimeException(ex.getMessage(), ex);
		}

		// done

		return new ResponseEntity<XdiData>(result, HttpStatus.OK);
	}

	@RequestMapping(value="/publicdata/{target}", method = RequestMethod.GET)
	public ResponseEntity<XdiData>
	linkContractsPublicData(Authentication auth, @PathVariable String target)
			throws NotFoundException, BadRequestException
	{
		Profile profile = XdiService.get().profileDAO.profilesForUser(getUser(auth).getId()).get(0);
		XDIAddress didXDIAddress = XdiService.getProfileDidXDIAddress(profile);

		XDIAddress targetXDIAddress = XDIAddress.create(target);

		// find XDI route

		XDIClientRoute<?> route;

		try {

			route = XdiService.get().getXDIAgent().route(targetXDIAddress);
		} catch (Xdi2Exception ex) {

			throw new RuntimeException(ex.getMessage(), ex);
		}

		// build XDI message

		Message message = route.createMessage(didXDIAddress, -1);
		message.setFromXDIAddress(didXDIAddress);
		message.setToXDIAddress(targetXDIAddress);
		message.setLinkContractClass(PublicLinkContract.class);
		message.createGetOperation(XDIAddressUtil.concatXDIAddresses(targetXDIAddress, XDIAddress.create("#dime#profile[<#tag>]")));

		// send to XDI target

		XDIAbstractClient<?> client = (XDIAbstractClient<?>) route.constructXDIClient();

		XdiData result = new XdiData();

		try {

/*			RSASignatureCreator signatureCreator = new RSAGraphPrivateKeySignatureCreator(XdiService.get().myGraph(getUser(auth)));
			SigningManipulator manipulator = new SigningManipulator();
			manipulator.setSignatureCreator(signatureCreator);
			client.getManipulators().addManipulator(manipulator);*/

			MessagingResponse response = client.send(message.getMessageEnvelope());
			
			Graph resultGraph = response.getResultGraph();
			
			for (LiteralNode literalNode : resultGraph.getRootContextNode().getAllLiteralNodes()) {
				
				XDIAddress key = XDIAddressUtil.localXDIAddress(literalNode.getContextNode().getXDIAddress(), -1);
				Object value = literalNode.getLiteralData();
				
				if (key != null) result.data.put(key.toString(), value == null ? null : value.toString());
			}
		} catch (Xdi2ClientException ex) {

			throw new RuntimeException(ex.getMessage(), ex);
		}

		// done

		return new ResponseEntity<XdiData>(result, HttpStatus.OK);
	}

	private static class XdiLinkContract {
		public String address;
		public String authorizingAuthority;
		public String requestingAuthority;
		public String profileName;
		public String direction;
		public XdiLinkContract(String address, String authorizingAuthority, String requestingAuthority, String profileName, String direction) { this.address = address; this.authorizingAuthority = authorizingAuthority; this.requestingAuthority = requestingAuthority; this.profileName = profileName; this.direction = direction; } 
	}
	
	private static class XdiData {
		public Map<String, String> data = new HashMap<String, String>();
	}
}
