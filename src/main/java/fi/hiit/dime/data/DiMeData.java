/*
  Copyright (c) 2015 University of Helsinki

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

package fi.hiit.dime.data;

import fi.hiit.dime.authentication.User;

import org.springframework.data.jpa.domain.AbstractPersistable;

import java.util.Date;

import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.MappedSuperclass;
import javax.persistence.Transient;

/**
*/
@MappedSuperclass
public class DiMeData extends AbstractPersistable<Long> {
    public String appId;

    public void copyIdFrom(DiMeData e) {
	setId(e.getId());
    }

    public void resetId() {
	setId(null);
    }

    /** Date and time when the object was first uploaded via the
	external API - automatically generated by DiMe.
     */
    public Date timeCreated;

    /** Date and time when the objects was last modified via the
	external API - automatically generated by DiMe.
    */
    public Date timeModified;

    /** User associated with the object - automatically generated by
	DiMe.
    */
    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "user_id")
    public User user;

    /** Detailed data type according to the Semantic Desktop ontology: 
	http://www.semanticdesktop.org/ontologies/2007/03/22/nfo
     */
    public String type;

    /** Method to call when ever a new object has been uploaded, e.g.
	to clean up user provided data, or perform some house keeping
	before storing in the database.
    */
    public void autoFill() {} 

    @Transient
    public Float score;
}
