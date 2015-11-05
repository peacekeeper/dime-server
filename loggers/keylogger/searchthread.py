#import sys, time
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5 import QtGui

# For Keylogger
import sys
import datetime #For import date and time
from time import sleep, time
import ctypes as ct
from ctypes.util import find_library

import os
import queue
import threading

from update_files import *

from dime_search2 import *

#Includes the definition of clickable label
#from ExtendedQLabel import *

#For getting web page title
#import lxml.html
import urllib.request, urllib.error, urllib.parse
#from BeautifulSoup import BeautifulSoup

#
import re

#
import math

#For checking data types
import types

#
class SearchThread(QThread):

 send_links = pyqtSignal(list)
 send_keywords = pyqtSignal(list)
 start_search = pyqtSignal()
 all_done = pyqtSignal()
 
 def __init__(self):
  QThread.__init__(self)
  self.query = ''
  self.oldquery  = None
  self.oldquery2 = None
  self.searchfuncid = 0
  self.extrasearch = False
  #Exploration/Exploitation -coefficient
  self.c          = 0.0

  #DiMe server path, username and password
  self.srvurl, self.usrname, self.password, self.time_interval, self.nspaces, self.numwords, self.updateinterval, self.data_update_interval, self.nokeypress_interval, self.mu, self.n_results = read_user_ini()
  self.dataupdateinterval = 600

  #
  json_data = open('data/json_data.txt')
  
  #DiMe data in json -format
  #self.data       = json.load(json_data)
  
  #Load df-matrix (document frequency matrix)
  #self.sXdoctm    = load_sparse_csc('data/sXdoctm.sparsemat.npz')
  #print("Search thread: Size of a loaded tfidf matrix ",self.sXdoctm.data.nbytes)
  
  #Load dictionary
  self.dictionary = corpora.Dictionary.load('data/tmpdict.dict')
  
  #Remove common words from dictionary
  #df_word_removal(self.sXdoctm, self.dictionary)
  #self.dictionary = corpora.Dictionary.load('/tmp/tmpdict.dict')
  
  #Load updated tfidf-matrix of the corpus
  self.sX         = load_sparse_csc('data/sX.sparsemat.npz')
  
  #Load updated df-matrix
  #self.sXdoctm    = load_sparse_csc('data/sXdoctm.sparsemat.npz')      
    
  #Load cosine similarity model for computing cosine similarity between keyboard input with documents
  #self.index      = similarities.docsim.Similarity.load('/tmp/similarityvec')
  self.index      = similarities.docsim.Similarity.load('data/similarityvec')

  if os.path.isfile('data/r_old.npy'):
    os.remove('data/r_old.npy')


 def __del__(self):
   self.wait()

 def change_search_function(self, searchfuncid):
  self.searchfuncid = searchfuncid
  print('Search thread: search function changed to', str(searchfuncid))
  if searchfuncid == 1 or searchfuncid == 2 or searchfuncid == 3:
    #Update LinRel data files
    print('Search thread: Updating Linrel data files!!!')
    print('Search thread: path: ', os.getcwd())
    #check_update()

 def get_new_c(self, value):
  #print "Search thread: new c value: ", value
  self.c = math.log(value+1)

 def recompute_keywords(self,value):
  #print(value)
  self.c = math.log(value+1)
  print("Exploration/Exploitation value: ",self.c)
  #kws = recompute_keywords(math.log(value+1))
  kws = recompute_keywords(self.c)
  self.send_keywords.emit(kws)

 def get_new_word(self, newquery):
  #newquer is a QString, so it has to be changed to a unicode string
  #print "XXX", type(newquery)
  #asciiquery = newquery.toAscii()
  #Convert to Unicode
  #newquery = unicode(asciiquery, 'utf-8')
  #newquery = unicode(newquery)
  newquery = newquery.strip() # to get rid of extra spaces, enters
  print("Search thread: got new query from logger: [%s]" % newquery)
  self.query = newquery

 def clear_query_string(self):
  self.query = ''
  print("searchthread: query string cleared!!")

 def get_new_word_from_main_thread(self, keywords):
  if self.query is None:
    self.query = ''
  #
  #utf8keyword = keywords.toUtf8()
  #print 'ASCII KEYWORD: ', utf8keyword
  #keywords = unicode(utf8keyword, 'utf-8')
  self.query = self.query + ' ' + keywords

  print("Search thread: got new query from main:", self.query)
  self.extrasearch = True

 def run(self):
   self.search()

 def search(self):

  #nokeypress_interval = 5.0
  timestamp = time()
  dataupdatetimestamp = time()

  #Check that all data files exist
  check_update()

  #
  while True:
    #
    cmachtime = time()

    #Update data
    if cmachtime > self.dataupdateinterval + dataupdatetimestamp:
      print("Update data!!!!!")
      #update_all_data()
      dataupdatetimestamp = time()
      #
      json_data = open('data/json_data.txt')
      #DiMe data in json -format
      #self.data       = json.load(json_data)
      #Load df-matrix (document frequency matrix)
      #self.sXdoctm    = load_sparse_csc('data/sXdoctm.sparsemat.npz')
      #Load dictionary
      self.dictionary = corpora.Dictionary.load('data/tmpdict.dict')
      #Remove common words from dictionary
      #df_word_removal(self.sXdoctm, self.dictionary)
      #self.dictionary = corpora.Dictionary.load('/tmp/tmpdict.dict')
      #Load updated tfidf-matrix of the corpus
      self.sX         = load_sparse_csc('data/sX.sparsemat.npz')
      #Load updated df-matrix
      #self.sXdoctm    = load_sparse_csc('data/sXdoctm.sparsemat.npz')      
      
      #Load 
      #self.index      = similarities.docsim.Similarity.load('/tmp/similarityvec')
      self.index      = similarities.docsim.Similarity.load('data/similarityvec')
      
      #Load cosine similarity model for computing cosine similarity between keyboard input with documents
      #self.index      = similarities.docsim.Similarity.load('/tmp/similarityvec')
      self.index      = similarities.docsim.Similarity.load('data/similarityvec')
      #Clean the history buffer
      if os.path.isfile('data/r_old.npy'):
        os.remove('data/r_old.npy')


    #
    if self.extrasearch:
      print('Search thread: got extra search command from main!')      
      #Search function causing clicking results up to 4.10.2015
      #jsons, docinds = search_dime_docsim(dstr, self.data, self.index, self.dictionary)
      #
      jsons = search_dime(self.srvurl, self.usrname, self.password, dstr, self.n_results)
      self.extrasearch = False    

    #
    if self.query is not None and self.query != self.oldquery2:
      #print 'self.query!!!!!'
      timestamp = time()
      self.oldquery2 = self.query

    if self.query is not None and self.query != self.oldquery and cmachtime > timestamp + self.nokeypress_interval:
      dstr = self.query      
      print('Search thread:', dstr)
        #dstr = unicode(dstr, 'utf-8')

      self.start_search.emit()
      if self.searchfuncid == 0:
        #jsons, docinds = search_dime_docsim(dstr, self.data, self.index, self.dictionary)
        print('Search thread: Ready for new search!')
      elif self.searchfuncid == 1:
        #Create/update relevant data files if necessary and store into 'data/' folder in current path 
        #jsons, kws = search_dime_linrel_summing_previous_estimates(dstr)
        jsons, kws, winds = search_dime_linrel_keyword_search_dime_search(dstr, self.sX, self.dictionary, self.c, self.mu, self.srvurl, self.usrname, self.password, self.n_results)        
        print('Search thread: Ready for new search!')
        print(len(jsons))
        if len(jsons) > 0:
          #Return keyword list
          self.send_keywords.emit(kws)
      elif self.searchfuncid == 2:
        #Create/update relevant data files if necessary and store into 'data/' folder in current path 
        n_kws = 10
        jsons, kws, winds = search_dime_using_linrel_keywords(dstr, n_kws, self.sX, self.dictionary, self.c, self.mu, self.srvurl, self.usrname, self.password, self.n_results)
        #jsons = search_dime_linrel_without_summing_previous_estimates(dstr)
        if len(jsons) > 0:
          #Return keyword list
          self.send_keywords.emit(kws)        
        print('Search thread: Ready for new search!')   
      # elif self.searchfuncid == 3:
      #   #Create/update relevant data files if necessary and store into 'data/' folder in current path 
      #   #jsons, kws = search_dime_linrel_keyword_search(dstr, self.sX, self.data, self.index, self.dictionary, self.c, self.mu)
      #   if len(jsons) > 0:
      #     #Return keyword list
      #     self.send_keywords.emit(kws)
      #   print('Search thread: Ready for new search!')      

      print('Search thread: len jsons ', len(jsons))
      if len(jsons) > 0:
        #Return keyword list
        #self.emit( QtCore.SIGNAL('finished(PyQt_PyObject)'), kws)
        #Return jsons
        self.send_links.emit(jsons)

        #Write first url's appearing in jsons list to a 'suggested_pages.txt'
        cdate = datetime.datetime.now().date()
        ctime = datetime.datetime.now().time()
        f = open("suggested_pages.txt","a")
        f.write(str(cdate) + ' ' + str(ctime) + ' ' + str(jsons[0]["uri"]) + '\n')
        f.close()
      self.oldquery = dstr
      self.all_done.emit()

    else:
      sleep(0.3) # artificial time delay    
