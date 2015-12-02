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

package fi.hiit.dime.search;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//------------------------------------------------------------------------------

public class KeywordSearchQuery extends SearchQuery {
    public List<WeightedKeyword> weightedKeywords;

    public KeywordSearchQuery() {
	weightedKeywords = new ArrayList<WeightedKeyword>();
    }

    public KeywordSearchQuery(WeightedKeyword[] query) {
	this.weightedKeywords = Arrays.asList(query);
    }

    public void add(String word, double weight) {
	weightedKeywords.add(new WeightedKeyword(word, weight));
    }

    @Override
    public boolean isEmpty() {
	return weightedKeywords == null || weightedKeywords.size() == 0;
    }

    @Override
    public String toString() {
	StringBuilder s = new StringBuilder();
	for (WeightedKeyword kw : weightedKeywords) 
	    s.append(String.format("%s (%f) ", kw.word, kw.weight));
	return s.toString();
    }
}