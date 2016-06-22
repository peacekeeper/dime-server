/*
  Copyright (c) 2016 University of Helsinki

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

import com.fasterxml.jackson.annotation.*;
import org.springframework.data.jpa.domain.AbstractPersistable;

import java.util.Date;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

/**
   Class representing a DiMe profile.
*/
@JsonInclude(value=JsonInclude.Include.NON_NULL)
@JsonTypeInfo(use=JsonTypeInfo.Id.NAME, include=JsonTypeInfo.As.PROPERTY, property="@type")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler", "new"})
@Entity
public class Profile extends AbstractPersistable<Long> {
    public Profile() {
    }

    public Profile(String name) {
        this.name = name;
    }

    public void copyIdFrom(Profile p) {
        setId(p.getId());
    }

    /** Date and time when the object was first uploaded via the
        external API - automatically generated by DiMe.
     */
    public Date timeCreated;

    /** Date and time when the objects was last modified via the
        external API - automatically generated by DiMe.
    */
    public Date timeModified;
    
    /** Profile name: a free-form name specified by the user. */
    @Column(columnDefinition="text")
    public String name;

    /** List of saved searches. */
    @ElementCollection(targetClass = String.class)
    public List<String> searchKeywords;

    /** Tags, lists of associated tag strings. */
    @ElementCollection(targetClass = String.class)
    public List<String> tags;

    /** User that owns the profile - automatically generated by DiMe.
    */
    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "user_id")
    public User user;
}