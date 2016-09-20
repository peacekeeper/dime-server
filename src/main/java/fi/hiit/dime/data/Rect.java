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

import java.util.List;

import org.springframework.data.jpa.domain.AbstractPersistable;
import com.fasterxml.jackson.annotation.*;

import javax.persistence.Embedded;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.ElementCollection;

/**
   Class representing a rectangle in a two dimensions (maps to the ReadingRect struct in PeyeDF).
*/
@JsonInclude(value=JsonInclude.Include.NON_NULL)
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler", "new"})
@Entity
public class Rect extends AbstractPersistable<Long> {
    /** Position of the origin of this rectangle (origin: bottom left).
     */
    @Embedded
    public Point origin;

    /** Size of this rectangle.
     */
    @Embedded
    public Size size;

    /** Page (starting from 0) on which this rectangle appears.
     */
    public int pageIndex;

    /** Reading class of this rectangle, or why is it marked (refer to the CLASS_* constants, Importance enum in PeyeDF).
     */
    public int readingClass;

    /** Source of classification for this rectangle, or what marked it (refer to the CLASSSOURCE_* constants, ClassSource enum in PeyeDF.
     */
    public int classSource;

    /** Plain text contained within this rectangle.
     */
    @Column(columnDefinition="text")
    public String plainTextContent;

    /** Floating rectangles have this flag set to true.
     * Floating rectangles are created immediately and are sent in non-summary reading events (only summary reading events can contain non-floating rectangles).
     * Non-floating rectangles are a union of floating rectangles created at the end of the reading session (document close).
     */ 
    public Boolean floating;

    /** The scale factor (zoom level) used when this rect was created (1 = 100% size, 2 = 200%, etc) -1 if the scaleFactor is invalid.
     * Scale factor will be invalid if the current rect was generated by the union of two rects of different scale factor, or
     * if it was not possible to determine it.
     */
    public Double scaleFactor;

    /** The user's distance from screen, in mm, when this rectangle was originally created.
     * Can be from eye tracking, or an estimated constant.
     */
    public Double screenDistance;

    /** Attention value for this rect.
     * It is an aggregate for eye tracking data. Present only if classification was run on a reading session.
     */
    public Double attnVal;

    /** Vector of unix times (timestamps, note: milliseconds) representing when this rectangle was created.
     * If this rectangle is floating (see above) this array contains only one timestamp. If this rectangle is from a union
     * (floating flag is false) it contains a timestamp for each "smaller" rectangle that was united into a bigger one.
     */
    @ElementCollection(targetClass = Long.class)
    public List<Long> unixt;

    /** Unspecified reading class
     */
    public static final int CLASS_UNSET = 0;

    /** Class for reading viewport rectangles (standard without eye tracking).
     */
    public static final int CLASS_VIEWPORT = 10;

    /** A paragraph (probably) exists at this point (currently generated by fixations).
     */
    public static final int CLASS_PARAGRAPH = 15;

    /** Class for read text.
     */
    public static final int CLASS_READ = 20;

    /** Class for searched for, found and selected strings.
     */
    public static final int CLASS_FOUNDSTRING = 25;

    /** Class for "interesting" rectangles.
     */
    public static final int CLASS_INTERESTING = 30;

    /** Class for "critical" rectangles.
     */
    public static final int CLASS_CRITICAL = 40;

    /** Class source for rectangles marked from an unkown source.
     */ 
    public static final int CLASSSOURCE_UNSET = 0;
    
    /** Class source for rectangles marked by the UI as viewports.
     */ 
    public static final int CLASSSOURCE_VIEWPORT = 1;

    /** Class source for rectangles marked by user clicking on paragraphs.
     */
    public static final int CLASSSOURCE_CLICK = 2;
    
    /** Class source for rectangles marked by eye tracking  (input to dime, before machine learning).
     */
    public static final int CLASSSOURCE_SMI = 3;
    
    /** Class source for rectangles marked by machine learning.
     */
    public static final int CLASSSOURCE_ML = 4;
    
    /** Class source for rectangles generated by (user) searching.
     */
    public static final int CLASSSOURCE_SEARCH = 5;

    /** Class source for rectangles generated by a local peer.
     */
    public static final int CLASSSOURCE_LOCALPEER = 6;

    /** Class source for rectangles generated by a newtork peer.
     */
    public static final int CLASSSOURCE_NETWORKPEER = 7;

    /** Class source for rectangles generated by manual selection (click and drag).
     */
    public static final int CLASSSOURCE_MANUALSELECTION = 8;
}
