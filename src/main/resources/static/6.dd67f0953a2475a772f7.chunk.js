webpackJsonp([6,20],{1033:function(e,t,n){"use strict";function r(){return{type:m.a}}function o(e){return{type:m.b,events:e}}function i(e){return{type:m.c,error:e}}function a(e){return{type:m.d,keyword:e}}function s(e){return{type:m.e,documents:e}}function u(e){return{type:m.f,error:e}}function c(e){return{type:m.m,event:e}}function f(e){return{type:m.g,eventID:e}}function h(e,t){return{type:m.i,error:e,eventID:t}}function d(e,t){return{type:m.h,respond:e,eventID:t}}function p(e,t){return{type:m.j,tag:e,eventID:t}}function l(e,t){return{type:m.k,respond:e,tag:t}}function y(e){return{type:m.l,error:e}}var m=n(981);t.i=r,t.a=o,t.b=i,t.j=a,t.c=s,t.d=u,t.k=c,t.l=f,t.f=h,t.e=d,t.m=p,t.g=l,t.h=y},1034:function(e,t,n){"use strict";var r=n(136);n.d(t,"b",function(){return a}),n.d(t,"c",function(){return s}),n.d(t,"d",function(){return u}),n.d(t,"e",function(){return c}),n.d(t,"a",function(){return i});var o=function(){return function(e){return e.get("eventsPage")}},i=function(){return function(e){return e.getIn(["app","auth"]).toJS()}},a=function(){return function(e){return e.getIn(["app","API"]).toJS()}},s=function(){return n.i(r.a)(o(),function(e){return e.get("data").toJS()})},u=function(){return n.i(r.a)(o(),function(e){return e.get("loading")})},c=function(){return n.i(r.a)(o(),function(e){return e.get("error").toJS()})}},864:function(e,t,n){"use strict";function r(){var e,t,r,o,i,a,s;return regeneratorRuntime.wrap(function(u){for(;;)switch(u.prev=u.next){case 0:return u.next=2,n.i(m.select)(n.i(T.a)());case 2:return e=u.sent,t=e.token,u.next=6,n.i(m.select)(n.i(T.b)());case 6:return r=u.sent,o=r.url,i="http://"+o+"/api/data/events",a={method:"GET",headers:{Authorization:"Basic "+t}},u.next=12,n.i(m.call)(x.a,i,a);case 12:if(s=u.sent,s.err){u.next=18;break}return u.next=16,n.i(m.put)(n.i(k.a)(s.data));case 16:u.next=20;break;case 18:return u.next=20,n.i(m.put)(n.i(k.b)(s));case 20:case"end":return u.stop()}},P[0],this)}function o(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.delegateYield(n.i(v.b)(w.a,r),"t0",1);case 1:case"end":return e.stop()}},P[1],this)}function i(){var e;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,n.i(m.fork)(o);case 2:return e=t.sent,t.next=5,n.i(m.take)(g.LOCATION_CHANGE);case 5:return t.next=7,n.i(m.cancel)(e);case 7:case"end":return t.stop()}},P[2],this)}function a(e){var t,r,o,i,a,s,u,c;return regeneratorRuntime.wrap(function(f){for(;;)switch(f.prev=f.next){case 0:return f.next=2,n.i(m.select)(n.i(T.a)());case 2:return t=f.sent,r=t.token,f.next=6,n.i(m.select)(n.i(T.b)());case 6:return o=f.sent,i=o.url,a=e.keyword,s=a.length>0?"http://"+i+"/api/eventsearch?query="+a:"http://"+i+"/api/data/events",u={method:"GET",headers:{Authorization:"Basic "+r}},f.next=13,n.i(m.call)(x.a,s,u);case 13:if(c=f.sent,c.err){f.next=19;break}return f.next=17,n.i(m.put)(n.i(k.c)(a.length>0?c.data.docs:c.data));case 17:f.next=21;break;case 19:return f.next=21,n.i(m.put)(n.i(k.d)(c));case 21:case"end":return f.stop()}},P[3],this)}function s(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.delegateYield(n.i(v.b)(w.d,a),"t0",1);case 1:case"end":return e.stop()}},P[4],this)}function u(){var e;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,n.i(m.fork)(s);case 2:return e=t.sent,t.next=5,n.i(m.take)(g.LOCATION_CHANGE);case 5:return t.next=7,n.i(m.cancel)(e);case 7:case"end":return t.stop()}},P[5],this)}function c(e){var t=e.event;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:n.i(m.put)({type:"SET_MODAL_OPEN",payload:t});case 1:case"end":return e.stop()}},P[6],this)}function f(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.delegateYield(n.i(v.b)(w.m,c),"t0",1);case 1:case"end":return e.stop()}},P[7],this)}function h(){var e;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,n.i(m.fork)(f);case 2:return e=t.sent,t.next=5,n.i(m.take)(g.LOCATION_CHANGE);case 5:return t.next=7,n.i(m.cancel)(e);case 7:case"end":return t.stop()}},P[8],this)}function d(e){var t,r,o,i,a,s,u;return regeneratorRuntime.wrap(function(c){for(;;)switch(c.prev=c.next){case 0:return c.next=2,n.i(m.select)(n.i(T.a)());case 2:return t=c.sent,r=t.token,c.next=6,n.i(m.select)(n.i(T.b)());case 6:return o=c.sent,i=o.url,a="http://"+i+"/api/data/event/"+e.eventID+"/",s={method:"DELETE",headers:{Authorization:"Basic "+r}},c.next=12,n.i(m.call)(x.a,a,s);case 12:if(u=c.sent,u.err){c.next=18;break}return c.next=16,n.i(m.put)(n.i(k.e)(u.data,e.eventID));case 16:c.next=20;break;case 18:return c.next=20,n.i(m.put)(n.i(k.f)(u,e.eventID));case 20:case"end":return c.stop()}},P[9],this)}function p(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.delegateYield(n.i(v.c)(w.g,d),"t0",1);case 1:case"end":return e.stop()}},P[10],this)}function l(e){var t,r,o,i,a,s,u,c,f,h,d,p;return regeneratorRuntime.wrap(function(l){for(;;)switch(l.prev=l.next){case 0:return t=e.tag,r=e.eventID,l.next=4,n.i(m.select)(n.i(T.a)());case 4:return o=l.sent,i=o.token,l.next=8,n.i(m.select)(n.i(T.b)());case 8:return a=l.sent,s=a.url,u="http://"+s+"/api/data/informationelement/"+r+"/removetag",c={method:"POST",headers:{Authorization:"Basic "+i,"Content-Type":"application/json"},body:JSON.stringify(t)},f="http://"+s+"/api/data/informationelement/"+r+"/addtag",h={method:"POST",headers:{Authorization:"Basic "+i,"Content-Type":"application/json"},body:JSON.stringify({"@type":"Tag",text:t.text,auto:!t.auto,actor:"dime-ui",time:(new Date).toISOString()})},l.next=16,n.i(m.call)(x.a,u,c);case 16:if(d=l.sent,d.err){l.next=30;break}return l.next=20,n.i(m.call)(x.a,f,h);case 20:if(p=l.sent,p.err){l.next=26;break}return l.next=24,n.i(m.put)(n.i(k.g)(p.data,t));case 24:l.next=28;break;case 26:return l.next=28,n.i(m.put)(n.i(k.h)(p.err));case 28:l.next=32;break;case 30:return l.next=32,n.i(m.put)(n.i(k.h)(d.err));case 32:case"end":return l.stop()}},P[11],this)}function y(){return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.delegateYield(n.i(v.c)(w.j,l),"t0",1);case 1:case"end":return e.stop()}},P[12],this)}var m=n(975),b=m&&m.__esModule?function(){return m["default"]}:function(){return m};n.d(b,"a",b);var v=n(332),g=n(99),E=g&&g.__esModule?function(){return g["default"]}:function(){return g};n.d(E,"a",E);var w=n(981),x=n(958),T=n(1034),k=n(1033);t.getEvents=r,t.getEventsWatcher=o,t.eventsData=i,t.searchEvent=a,t.searchWatcher=s,t.searchData=u,t.clickEvent=c,t.clickEventWatcher=f,t.clickEventWatcherPlusLocationChangeCanceler=h,t.deleteEvent=d,t.deleteEntityWatcher=p,t.toogleEventTagAutoLabel=l,t.clickTagWatcher=y;var P=[r,o,i,a,s,u,c,f,h,d,p,l,y].map(regeneratorRuntime.mark);t["default"]=[i,u,h,p,y]},958:function(e,t,n){"use strict";(function(e){function r(e){if(e.ok)return e[204===e.status?"text":"json"]();var t=new Error(e.statusText);throw t.response=e,t}function o(t,n){return e(t,n).then(r).then(function(e){return{data:e}})["catch"](function(e){return{err:e}})}var i=n(979),a=i&&i.__esModule?function(){return i["default"]}:function(){return i};n.d(a,"a",a),t.a=o}).call(t,n(974))},974:function(e,t){!function(e){"use strict";function t(e){if("string"!=typeof e&&(e=String(e)),/[^a-z0-9\-#$%&'*+.\^_`|~]/i.test(e))throw new TypeError("Invalid character in header field name");return e.toLowerCase()}function n(e){return"string"!=typeof e&&(e=String(e)),e}function r(e){var t={next:function(){var t=e.shift();return{done:void 0===t,value:t}}};return y.iterable&&(t[Symbol.iterator]=function(){return t}),t}function o(e){this.map={},e instanceof o?e.forEach(function(e,t){this.append(t,e)},this):e&&Object.getOwnPropertyNames(e).forEach(function(t){this.append(t,e[t])},this)}function i(e){return e.bodyUsed?Promise.reject(new TypeError("Already read")):void(e.bodyUsed=!0)}function a(e){return new Promise(function(t,n){e.onload=function(){t(e.result)},e.onerror=function(){n(e.error)}})}function s(e){var t=new FileReader;return t.readAsArrayBuffer(e),a(t)}function u(e){var t=new FileReader;return t.readAsText(e),a(t)}function c(){return this.bodyUsed=!1,this._initBody=function(e){if(this._bodyInit=e,"string"==typeof e)this._bodyText=e;else if(y.blob&&Blob.prototype.isPrototypeOf(e))this._bodyBlob=e;else if(y.formData&&FormData.prototype.isPrototypeOf(e))this._bodyFormData=e;else if(y.searchParams&&URLSearchParams.prototype.isPrototypeOf(e))this._bodyText=e.toString();else if(e){if(!y.arrayBuffer||!ArrayBuffer.prototype.isPrototypeOf(e))throw new Error("unsupported BodyInit type")}else this._bodyText="";this.headers.get("content-type")||("string"==typeof e?this.headers.set("content-type","text/plain;charset=UTF-8"):this._bodyBlob&&this._bodyBlob.type?this.headers.set("content-type",this._bodyBlob.type):y.searchParams&&URLSearchParams.prototype.isPrototypeOf(e)&&this.headers.set("content-type","application/x-www-form-urlencoded;charset=UTF-8"))},y.blob?(this.blob=function(){var e=i(this);if(e)return e;if(this._bodyBlob)return Promise.resolve(this._bodyBlob);if(this._bodyFormData)throw new Error("could not read FormData body as blob");return Promise.resolve(new Blob([this._bodyText]))},this.arrayBuffer=function(){return this.blob().then(s)},this.text=function(){var e=i(this);if(e)return e;if(this._bodyBlob)return u(this._bodyBlob);if(this._bodyFormData)throw new Error("could not read FormData body as text");return Promise.resolve(this._bodyText)}):this.text=function(){var e=i(this);return e?e:Promise.resolve(this._bodyText)},y.formData&&(this.formData=function(){return this.text().then(d)}),this.json=function(){return this.text().then(JSON.parse)},this}function f(e){var t=e.toUpperCase();return m.indexOf(t)>-1?t:e}function h(e,t){t=t||{};var n=t.body;if(h.prototype.isPrototypeOf(e)){if(e.bodyUsed)throw new TypeError("Already read");this.url=e.url,this.credentials=e.credentials,t.headers||(this.headers=new o(e.headers)),this.method=e.method,this.mode=e.mode,n||(n=e._bodyInit,e.bodyUsed=!0)}else this.url=e;if(this.credentials=t.credentials||this.credentials||"omit",!t.headers&&this.headers||(this.headers=new o(t.headers)),this.method=f(t.method||this.method||"GET"),this.mode=t.mode||this.mode||null,this.referrer=null,("GET"===this.method||"HEAD"===this.method)&&n)throw new TypeError("Body not allowed for GET or HEAD requests");this._initBody(n)}function d(e){var t=new FormData;return e.trim().split("&").forEach(function(e){if(e){var n=e.split("="),r=n.shift().replace(/\+/g," "),o=n.join("=").replace(/\+/g," ");t.append(decodeURIComponent(r),decodeURIComponent(o))}}),t}function p(e){var t=new o,n=(e.getAllResponseHeaders()||"").trim().split("\n");return n.forEach(function(e){var n=e.trim().split(":"),r=n.shift().trim(),o=n.join(":").trim();t.append(r,o)}),t}function l(e,t){t||(t={}),this.type="default",this.status=t.status,this.ok=this.status>=200&&this.status<300,this.statusText=t.statusText,this.headers=t.headers instanceof o?t.headers:new o(t.headers),this.url=t.url||"",this._initBody(e)}if(!e.fetch){var y={searchParams:"URLSearchParams"in e,iterable:"Symbol"in e&&"iterator"in Symbol,blob:"FileReader"in e&&"Blob"in e&&function(){try{return new Blob,!0}catch(e){return!1}}(),formData:"FormData"in e,arrayBuffer:"ArrayBuffer"in e};o.prototype.append=function(e,r){e=t(e),r=n(r);var o=this.map[e];o||(o=[],this.map[e]=o),o.push(r)},o.prototype["delete"]=function(e){delete this.map[t(e)]},o.prototype.get=function(e){var n=this.map[t(e)];return n?n[0]:null},o.prototype.getAll=function(e){return this.map[t(e)]||[]},o.prototype.has=function(e){return this.map.hasOwnProperty(t(e))},o.prototype.set=function(e,r){this.map[t(e)]=[n(r)]},o.prototype.forEach=function(e,t){Object.getOwnPropertyNames(this.map).forEach(function(n){this.map[n].forEach(function(r){e.call(t,r,n,this)},this)},this)},o.prototype.keys=function(){var e=[];return this.forEach(function(t,n){e.push(n)}),r(e)},o.prototype.values=function(){var e=[];return this.forEach(function(t){e.push(t)}),r(e)},o.prototype.entries=function(){var e=[];return this.forEach(function(t,n){e.push([n,t])}),r(e)},y.iterable&&(o.prototype[Symbol.iterator]=o.prototype.entries);var m=["DELETE","GET","HEAD","OPTIONS","POST","PUT"];h.prototype.clone=function(){return new h(this)},c.call(h.prototype),c.call(l.prototype),l.prototype.clone=function(){return new l(this._bodyInit,{status:this.status,statusText:this.statusText,headers:new o(this.headers),url:this.url})},l.error=function(){var e=new l(null,{status:0,statusText:""});return e.type="error",e};var b=[301,302,303,307,308];l.redirect=function(e,t){if(b.indexOf(t)===-1)throw new RangeError("Invalid status code");return new l(null,{status:t,headers:{location:e}})},e.Headers=o,e.Request=h,e.Response=l,e.fetch=function(e,t){return new Promise(function(n,r){function o(){return"responseURL"in a?a.responseURL:/^X-Request-URL:/m.test(a.getAllResponseHeaders())?a.getResponseHeader("X-Request-URL"):void 0}var i;i=h.prototype.isPrototypeOf(e)&&!t?e:new h(e,t);var a=new XMLHttpRequest;a.onload=function(){var e={status:a.status,statusText:a.statusText,headers:p(a),url:o()},t="response"in a?a.response:a.responseText;n(new l(t,e))},a.onerror=function(){r(new TypeError("Network request failed"))},a.ontimeout=function(){r(new TypeError("Network request failed"))},a.open(i.method,i.url,!0),"include"===i.credentials&&(a.withCredentials=!0),"responseType"in a&&y.blob&&(a.responseType="blob"),i.headers.forEach(function(e,t){a.setRequestHeader(t,e)}),a.send("undefined"==typeof i._bodyInit?null:i._bodyInit)})},e.fetch.polyfill=!0}}("undefined"!=typeof self?self:this),e.exports=self.fetch},975:function(e,t,n){e.exports=n(976)},976:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(977);Object.defineProperty(t,"take",{enumerable:!0,get:function(){return r.take}}),Object.defineProperty(t,"takem",{enumerable:!0,get:function(){return r.takem}}),Object.defineProperty(t,"put",{enumerable:!0,get:function(){return r.put}}),Object.defineProperty(t,"race",{enumerable:!0,get:function(){return r.race}}),Object.defineProperty(t,"call",{enumerable:!0,get:function(){return r.call}}),Object.defineProperty(t,"apply",{enumerable:!0,get:function(){return r.apply}}),Object.defineProperty(t,"cps",{enumerable:!0,get:function(){return r.cps}}),Object.defineProperty(t,"fork",{enumerable:!0,get:function(){return r.fork}}),Object.defineProperty(t,"spawn",{enumerable:!0,get:function(){return r.spawn}}),Object.defineProperty(t,"join",{enumerable:!0,get:function(){return r.join}}),Object.defineProperty(t,"cancel",{enumerable:!0,get:function(){return r.cancel}}),Object.defineProperty(t,"select",{enumerable:!0,get:function(){return r.select}}),Object.defineProperty(t,"actionChannel",{enumerable:!0,get:function(){return r.actionChannel}}),Object.defineProperty(t,"cancelled",{enumerable:!0,get:function(){return r.cancelled}})},977:function(e,t,n){"use strict";function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){if(arguments.length>=2)(0,E.check)(e,E.is.notUndef,"take(channel, pattern): channel is undefined"),(0,E.check)(e,E.is.take,"take(channel, pattern): argument "+String(e)+" is not a valid channel (channel argument must have a take method)"),(0,E.check)(t,E.is.notUndef,"take(channel, pattern): pattern is undefined"),(0,E.check)(t,E.is.pattern,"take(channel, pattern): argument "+String(t)+" is not a valid pattern (pattern must be String | Function: a => boolean | Array<String>)");else if(1===arguments.length)if((0,E.check)(e,E.is.notUndef,"take(patternOrChannel): undefined argument"),E.is.take(e))t="*";else{if(!E.is.pattern(e))throw new Error("take(patternOrChannel): argument "+String(e)+" is not valid channel or a valid pattern");t=e,e=null}else t="*";return D(x,{channel:e,pattern:t})}function i(){var e=o.apply(void 0,arguments);return e[x].maybe=!0,e}function a(e,t){return arguments.length>1?((0,E.check)(e,E.is.notUndef,"put(channel, action): argument channel is undefined"),(0,E.check)(e,E.is.put,"put(channel, action): argument "+e+" is not a valid channel (channel argument must have a put method)"),(0,E.check)(t,E.is.notUndef,"put(channel, action): argument action is undefined")):((0,E.check)(e,E.is.notUndef,"put(action): argument action is undefined"),t=e,e=null),D(T,{channel:e,action:t})}function s(e){return D(k,e)}function u(e,t,n){(0,E.check)(t,E.is.notUndef,e+": argument fn is undefined");var r=null;if(E.is.array(t)){var o=t,i=g(o,2);r=i[0],t=i[1]}else if(t.fn){var a=t;r=a.context,t=a.fn}return(0,E.check)(t,E.is.func,e+": argument "+t+" is not a function"),{context:r,fn:t,args:n}}function c(e){for(var t=arguments.length,n=Array(t>1?t-1:0),r=1;r<t;r++)n[r-1]=arguments[r];return D(P,u("call",e,n))}function f(e,t){var n=arguments.length<=2||void 0===arguments[2]?[]:arguments[2];return D(P,u("apply",{context:e,fn:t},n))}function h(e){for(var t=arguments.length,n=Array(t>1?t-1:0),r=1;r<t;r++)n[r-1]=arguments[r];return D(_,u("cps",e,n))}function d(e){for(var t=arguments.length,n=Array(t>1?t-1:0),r=1;r<t;r++)n[r-1]=arguments[r];return D(O,u("fork",e,n))}function p(e){for(var t=arguments.length,n=Array(t>1?t-1:0),r=1;r<t;r++)n[r-1]=arguments[r];var o=d.apply(void 0,[e].concat(n));return o[O].detached=!0,o}function l(e){if((0,E.check)(e,E.is.notUndef,"join(task): argument task is undefined"),!j(e))throw new Error("join(task): argument "+e+" is not a valid Task object \n(HINT: if you are getting this errors in tests, consider using createMockTask from redux-saga/utils)");return D(R,e)}function y(e){if((0,E.check)(e,E.is.notUndef,"cancel(task): argument task is undefined"),!j(e))throw new Error("cancel(task): argument "+e+" is not a valid Task object \n(HINT: if you are getting this errors in tests, consider using createMockTask from redux-saga/utils)");return D(S,e)}function m(e){for(var t=arguments.length,n=Array(t>1?t-1:0),r=1;r<t;r++)n[r-1]=arguments[r];return 0===arguments.length?e=E.ident:((0,E.check)(m,E.is.notUndef,"select(selector,[...]): argument selector is undefined"),(0,E.check)(e,E.is.func,"select(selector,[...]): argument "+e+" is not a function")),D(A,{selector:e,args:n})}function b(e,t){return(0,E.check)(e,E.is.notUndef,"actionChannel(pattern,...): argument pattern is undefined"),arguments.length>1&&((0,E.check)(t,E.is.notUndef,"actionChannel(pattern, buffer): argument buffer is undefined"),(0,E.check)(t,E.is.notUndef,"actionChannel(pattern, buffer): argument "+t+" is not a valid buffer")),D(C,{pattern:e,buffer:t})}function v(){return D(U,{})}Object.defineProperty(t,"__esModule",{value:!0}),t.asEffect=void 0;var g=function(){function e(e,t){var n=[],r=!0,o=!1,i=void 0;try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(u){o=!0,i=u}finally{try{!r&&s["return"]&&s["return"]()}finally{if(o)throw i}}return n}return function(t,n){if(Array.isArray(t))return t;if(Symbol.iterator in Object(t))return e(t,n);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}();t.take=o,t.takem=i,t.put=a,t.race=s,t.call=c,t.apply=f,t.cps=h,t.fork=d,t.spawn=p,t.join=l,t.cancel=y,t.select=m,t.actionChannel=b,t.cancelled=v;var E=n(978),w=(0,E.sym)("IO"),x="TAKE",T="PUT",k="RACE",P="CALL",_="CPS",O="FORK",R="JOIN",S="CANCEL",A="SELECT",C="ACTION_CHANNEL",U="CANCELLED",D=function(e,t){var n;return n={},r(n,w,!0),r(n,e,t),n};a.sync=function(){var e=a.apply(void 0,arguments);return e[T].sync=!0,e};var j=function(e){return e[E.TASK]};t.asEffect={take:function(e){return e&&e[w]&&e[x]},put:function(e){return e&&e[w]&&e[T]},race:function(e){return e&&e[w]&&e[k]},call:function(e){return e&&e[w]&&e[P]},cps:function(e){return e&&e[w]&&e[_]},fork:function(e){return e&&e[w]&&e[O]},join:function(e){return e&&e[w]&&e[R]},cancel:function(e){return e&&e[w]&&e[S]},select:function(e){return e&&e[w]&&e[A]},actionChannel:function(e){return e&&e[w]&&e[C]},cancelled:function(e){return e&&e[w]&&e[U]}}},978:function(e,t){"use strict";function n(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t,n){if(!t(e))throw h("error","uncaught at check",n),new Error(n)}function o(e,t){var n=e.indexOf(t);n>=0&&e.splice(n,1)}function i(){var e=arguments.length<=0||void 0===arguments[0]?{}:arguments[0],t=d({},e),n=new Promise(function(e,n){t.resolve=e,t.reject=n});return t.promise=n,t}function a(e){for(var t=[],n=0;n<e;n++)t.push(i());return t}function s(e){var t=arguments.length<=1||void 0===arguments[1]||arguments[1],n=void 0,r=new Promise(function(r){n=setTimeout(function(){return r(t)},e)});return r[m]=function(){return clearTimeout(n)},r}function u(){var e,t=!0,r=void 0,o=void 0;return e={},n(e,y,!0),n(e,"isRunning",function(){return t}),n(e,"result",function(){return r}),n(e,"error",function(){return o}),n(e,"setRunning",function(e){return t=e}),n(e,"setResult",function(e){return r=e}),n(e,"setError",function(e){return o=e}),e}function c(){var e=arguments.length<=0||void 0===arguments[0]?0:arguments[0];return function(){return++e}}function f(e){var t=arguments.length<=1||void 0===arguments[1]?g:arguments[1],n=arguments.length<=2||void 0===arguments[2]?"":arguments[2],r={name:n,next:e,"throw":t};return"undefined"!=typeof Symbol&&(r[Symbol.iterator]=function(){return r}),r}function h(e,t,n){"undefined"==typeof window?console.log("redux-saga "+e+": "+t+"\n"+(n&&n.stack||n)):console[e].call(console,t,n)}Object.defineProperty(t,"__esModule",{value:!0});var d=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},p="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol?"symbol":typeof e};t.check=r,t.remove=o,t.deferred=i,t.arrayOfDeffered=a,t.delay=s,t.createMockTask=u,t.autoInc=c,t.makeIterator=f,t.log=h;var l=t.sym=function(e){return"@@redux-saga/"+e},y=t.TASK=l("TASK"),m=(t.MATCH=l("MATCH"),t.CANCEL=l("cancelPromise")),b=t.konst=function(e){return function(){return e}},v=(t.kTrue=b(!0),t.kFalse=b(!1),t.noop=function(){},t.ident=function(e){return e},t.is={undef:function(e){return null===e||void 0===e},notUndef:function(e){return null!==e&&void 0!==e},func:function(e){return"function"==typeof e},number:function(e){return"number"==typeof e},array:Array.isArray,promise:function(e){return e&&v.func(e.then)},iterator:function(e){return e&&v.func(e.next)&&v.func(e["throw"])},task:function(e){return e&&e[y]},take:function(e){return e&&v.func(e.take)},put:function(e){return e&&v.func(e.put)},observable:function(e){return e&&v.func(e.subscribe)},buffer:function(e){return e&&v.func(e.isEmpty)&&v.func(e.take)&&v.func(e.put)},pattern:function(e){return e&&("string"==typeof e||"symbol"===("undefined"==typeof e?"undefined":p(e))||v.func(e)||v.array(e))}}),g=function(e){throw e};t.internalErr=function(e){return new Error("\n  redux-saga: Error checking hooks detected an inconsisten state. This is likely a bug\n  in redux-saga code and not yours. Thanks for reporting this in the project's github repo.\n  Error: "+e+"\n")}},979:function(e,t){!function(e){"use strict";function t(e){if("string"!=typeof e&&(e=String(e)),/[^a-z0-9\-#$%&'*+.\^_`|~]/i.test(e))throw new TypeError("Invalid character in header field name");return e.toLowerCase()}function n(e){return"string"!=typeof e&&(e=String(e)),e}function r(e){var t={next:function(){var t=e.shift();return{done:void 0===t,value:t}}};return y.iterable&&(t[Symbol.iterator]=function(){return t}),t}function o(e){this.map={},e instanceof o?e.forEach(function(e,t){this.append(t,e)},this):e&&Object.getOwnPropertyNames(e).forEach(function(t){this.append(t,e[t])},this)}function i(e){return e.bodyUsed?Promise.reject(new TypeError("Already read")):void(e.bodyUsed=!0)}function a(e){return new Promise(function(t,n){e.onload=function(){t(e.result)},e.onerror=function(){n(e.error)}})}function s(e){var t=new FileReader;return t.readAsArrayBuffer(e),a(t)}function u(e){var t=new FileReader;return t.readAsText(e),a(t)}function c(){return this.bodyUsed=!1,this._initBody=function(e){if(this._bodyInit=e,"string"==typeof e)this._bodyText=e;else if(y.blob&&Blob.prototype.isPrototypeOf(e))this._bodyBlob=e;else if(y.formData&&FormData.prototype.isPrototypeOf(e))this._bodyFormData=e;else if(y.searchParams&&URLSearchParams.prototype.isPrototypeOf(e))this._bodyText=e.toString();else if(e){if(!y.arrayBuffer||!ArrayBuffer.prototype.isPrototypeOf(e))throw new Error("unsupported BodyInit type")}else this._bodyText="";this.headers.get("content-type")||("string"==typeof e?this.headers.set("content-type","text/plain;charset=UTF-8"):this._bodyBlob&&this._bodyBlob.type?this.headers.set("content-type",this._bodyBlob.type):y.searchParams&&URLSearchParams.prototype.isPrototypeOf(e)&&this.headers.set("content-type","application/x-www-form-urlencoded;charset=UTF-8"))},y.blob?(this.blob=function(){var e=i(this);if(e)return e;if(this._bodyBlob)return Promise.resolve(this._bodyBlob);if(this._bodyFormData)throw new Error("could not read FormData body as blob");return Promise.resolve(new Blob([this._bodyText]))},this.arrayBuffer=function(){return this.blob().then(s)},this.text=function(){var e=i(this);if(e)return e;if(this._bodyBlob)return u(this._bodyBlob);if(this._bodyFormData)throw new Error("could not read FormData body as text");return Promise.resolve(this._bodyText)}):this.text=function(){var e=i(this);return e?e:Promise.resolve(this._bodyText)},y.formData&&(this.formData=function(){return this.text().then(d)}),this.json=function(){return this.text().then(JSON.parse)},this}function f(e){var t=e.toUpperCase();return m.indexOf(t)>-1?t:e}function h(e,t){t=t||{};var n=t.body;if(h.prototype.isPrototypeOf(e)){if(e.bodyUsed)throw new TypeError("Already read");this.url=e.url,this.credentials=e.credentials,t.headers||(this.headers=new o(e.headers)),this.method=e.method,this.mode=e.mode,n||(n=e._bodyInit,e.bodyUsed=!0)}else this.url=e;if(this.credentials=t.credentials||this.credentials||"omit",!t.headers&&this.headers||(this.headers=new o(t.headers)),this.method=f(t.method||this.method||"GET"),this.mode=t.mode||this.mode||null,this.referrer=null,("GET"===this.method||"HEAD"===this.method)&&n)throw new TypeError("Body not allowed for GET or HEAD requests");this._initBody(n)}function d(e){var t=new FormData;return e.trim().split("&").forEach(function(e){if(e){var n=e.split("="),r=n.shift().replace(/\+/g," "),o=n.join("=").replace(/\+/g," ");t.append(decodeURIComponent(r),decodeURIComponent(o))}}),t}function p(e){var t=new o,n=(e.getAllResponseHeaders()||"").trim().split("\n");return n.forEach(function(e){var n=e.trim().split(":"),r=n.shift().trim(),o=n.join(":").trim();t.append(r,o)}),t}function l(e,t){t||(t={}),this.type="default",this.status=t.status,this.ok=this.status>=200&&this.status<300,this.statusText=t.statusText,this.headers=t.headers instanceof o?t.headers:new o(t.headers),this.url=t.url||"",this._initBody(e)}if(!e.fetch){var y={searchParams:"URLSearchParams"in e,iterable:"Symbol"in e&&"iterator"in Symbol,blob:"FileReader"in e&&"Blob"in e&&function(){try{return new Blob,!0}catch(e){return!1}}(),formData:"FormData"in e,arrayBuffer:"ArrayBuffer"in e};o.prototype.append=function(e,r){e=t(e),r=n(r);var o=this.map[e];o||(o=[],this.map[e]=o),o.push(r)},o.prototype["delete"]=function(e){delete this.map[t(e)]},o.prototype.get=function(e){var n=this.map[t(e)];return n?n[0]:null},o.prototype.getAll=function(e){return this.map[t(e)]||[]},o.prototype.has=function(e){return this.map.hasOwnProperty(t(e))},o.prototype.set=function(e,r){this.map[t(e)]=[n(r)]},o.prototype.forEach=function(e,t){Object.getOwnPropertyNames(this.map).forEach(function(n){this.map[n].forEach(function(r){e.call(t,r,n,this)},this)},this)},o.prototype.keys=function(){var e=[];return this.forEach(function(t,n){e.push(n)}),r(e)},o.prototype.values=function(){var e=[];return this.forEach(function(t){e.push(t)}),r(e)},o.prototype.entries=function(){var e=[];return this.forEach(function(t,n){e.push([n,t])}),r(e)},y.iterable&&(o.prototype[Symbol.iterator]=o.prototype.entries);var m=["DELETE","GET","HEAD","OPTIONS","POST","PUT"];h.prototype.clone=function(){return new h(this)},c.call(h.prototype),c.call(l.prototype),l.prototype.clone=function(){return new l(this._bodyInit,{status:this.status,statusText:this.statusText,headers:new o(this.headers),url:this.url})},l.error=function(){var e=new l(null,{status:0,statusText:""});return e.type="error",e};var b=[301,302,303,307,308];l.redirect=function(e,t){if(b.indexOf(t)===-1)throw new RangeError("Invalid status code");return new l(null,{status:t,headers:{location:e}})},e.Headers=o,e.Request=h,e.Response=l,e.fetch=function(e,t){return new Promise(function(n,r){function o(){return"responseURL"in a?a.responseURL:/^X-Request-URL:/m.test(a.getAllResponseHeaders())?a.getResponseHeader("X-Request-URL"):void 0}var i;i=h.prototype.isPrototypeOf(e)&&!t?e:new h(e,t);var a=new XMLHttpRequest;a.onload=function(){var e={status:a.status,statusText:a.statusText,headers:p(a),url:o()},t="response"in a?a.response:a.responseText;n(new l(t,e))},a.onerror=function(){r(new TypeError("Network request failed"))},a.ontimeout=function(){r(new TypeError("Network request failed"))},a.open(i.method,i.url,!0),"include"===i.credentials&&(a.withCredentials=!0),"responseType"in a&&y.blob&&(a.responseType="blob"),i.headers.forEach(function(e,t){a.setRequestHeader(t,e)}),a.send("undefined"==typeof i._bodyInit?null:i._bodyInit)})},e.fetch.polyfill=!0}}("undefined"!=typeof self?self:this)},981:function(e,t,n){"use strict";n.d(t,"a",function(){return r}),n.d(t,"b",function(){return o}),n.d(t,"c",function(){return i}),n.d(t,"d",function(){return a}),n.d(t,"e",function(){return s}),n.d(t,"f",function(){return u}),n.d(t,"m",function(){return c}),n.d(t,"g",function(){return f}),n.d(t,"h",function(){return h}),n.d(t,"i",function(){return d}),n.d(t,"j",function(){return p}),n.d(t,"k",function(){return l}),n.d(t,"l",function(){return y});var r="app/EventsPage/LOAD_EVENTS",o="app/EventsPage/LOAD_EVENTS_SUCCESS",i="app/EventsPage/LOAD_EVENTS_ERROR",a="app/EventsPage/SEARCH_EVENTS",s="app/EventsPage/SEARCH_EVENTS_SUCCESS",u="app/EventsPage/SEARCH_EVENTS_ERROR",c="app/EventsPage/CLICK_EVENT_CARD",f="app/EventsPage/DELETE_EVENT",h="app/EventsPage/DELETE_EVENT_SUCESS",d="app/EventsPage/DELETE_EVENT_ERROR",p="app/EventsPage/CLICK_EVENT_TAG",l="app/EventsPage/TOOGLE_EVENT_TAG_SUCESS",y="app/EventsPage/CONFIRM_EVENT_TAG_ERROR"}});