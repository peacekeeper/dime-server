#import sys, time
from PyQt4 import QtCore, QtGui

# For Keylogger
import sys
import datetime #For import date and time
from time import sleep, time
import ctypes as ct
from ctypes.util import find_library

import datetime
import os
import Queue
import threading

from fetch_keys_linux import *

from update_dict_lda_and_Am import *

from dime_search import *

#Includes the definition of clickable label
from ExtendedQLabel import *

#For getting web page title
#import lxml.html
import urllib2
from BeautifulSoup import BeautifulSoup

#
import re

################################################################

# linux only!
assert("linux" in sys.platform)

class MyApp(QtGui.QWidget):
 def __init__(self, parent=None):
  QtGui.QWidget.__init__(self, parent)

  #Read user.ini file
  self.srvurl, self.username, self.password, self.time_interval, self.nspaces, self.nwords, self.updateinterval = self.read_user_ini()

  #Create visible stuff
  val = 5
  iconfile = 'web.png'
  self.gbtitle = QtGui.QLabel('Web sites')
  self.listWidget1 = self.create_QListWidget(20, iconfile)

  iconfile = 'mail.png'
  self.gbtitle2 = QtGui.QLabel('E-Mails')
  self.listWidget2 = self.create_QListWidget(20, iconfile)

  iconfile = 'doc.png'
  self.gbtitle3 = QtGui.QLabel('Docs')
  self.listWidget3 = self.create_QListWidget(20, iconfile)


  #Buttons
  #Start button
  self.testButton  = QtGui.QPushButton("Start")
  self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test_pressed)
  #Radio buttons for choosing search function
  self.radiobutton1= QtGui.QRadioButton("DocSim")
  #self.radiobutton1.emit(QtCore.SIGNAL('released()'))
  self.connect(self.radiobutton1, QtCore.SIGNAL("released()"), self.choose_search_function1)

  self.radiobutton2= QtGui.QRadioButton("LinRel")
  #self.radiobutton2.emit( QtCore.SIGNAL('released()'))
  self.connect(self.radiobutton2, QtCore.SIGNAL("released()"), self.choose_search_function2)


  #Add to layout
  self.vlayout1 = QtGui.QVBoxLayout()
  self.vlayout1.addWidget(self.gbtitle)
  self.vlayout1.addWidget(self.listWidget1)
  
  self.vlayout2 = QtGui.QVBoxLayout()
  self.vlayout2.addWidget(self.gbtitle2)
  self.vlayout2.addWidget(self.listWidget2)
  
  self.vlayout3 = QtGui.QVBoxLayout()
  self.vlayout3.addWidget(self.gbtitle3)
  self.vlayout3.addWidget(self.listWidget3)
  
  #
  self.vlayout4 = QtGui.QVBoxLayout()
  self.vlayout4.addWidget(self.testButton)
  self.vlayout4.addWidget(self.radiobutton1)
  self.vlayout4.addWidget(self.radiobutton2)

  #Add layouts
  self.hlayout = QtGui.QHBoxLayout(self)
  self.hlayout.addLayout(self.vlayout1)
  self.hlayout.addLayout(self.vlayout2)
  self.hlayout.addLayout(self.vlayout3)
  self.hlayout.addLayout(self.vlayout4)

  #Set title
  self.setWindowTitle("ProActive Search") 

 #Runs the Keylogger and Search 
 def test_pressed(self):
  print 'Main: Test'
  self.testButton.setDisabled(True)
  #self.listwidget.clear()

  #Create thread objects
  self.LoggerThreadObj  = LoggerThread()
  self.SearchThreadObj = SearchThread()

  #Connect the signals and receivers between threads
  self.connect(self.LoggerThreadObj, QtCore.SIGNAL("update(QString)"), self.SearchThreadObj.get_new_word)
  self.connect(self.SearchThreadObj, QtCore.SIGNAL("finished(PyQt_PyObject)"), self.update_links)
  self.connect(self, QtCore.SIGNAL("finished(PyQt_PyObject)"), self.SearchThreadObj.change_search_function)
  self.connect(self, QtCore.SIGNAL("finished(PyQt_PyObject)"), self.SearchThreadObj.change_search_function)

  
  #Start thread processes
  self.LoggerThreadObj.start()
  self.SearchThreadObj.start()


 def choose_search_function1(self):
  #if searchfuncid == 0:
    print 'Main: Search function is DocSim'
    self.emit(QtCore.SIGNAL('finished(PyQt_PyObject)'), 0)
  # elif searchfuncid == 1:
  #   print 'Main: Search function is LinRel'

 def choose_search_function2(self):
  #if searchfuncid == 0:
    print 'Main: Search function is LinRel'
    self.emit(QtCore.SIGNAL('finished(PyQt_PyObject)'), 1)
  #elif searchfuncid == 1:
  #  print 'Main: Search function is LinRel'



 def create_QListWidget(self, val, icon_file):
    listWidget = QListWidget()
    for i in range(val):
        dumitem = QListWidgetItem(listWidget)
        dstr = ''
        dumitem.setText(dstr)
        dumitem.setWhatsThis('')
        dumitem.setToolTip('')
        icon = QIcon(icon_file)
        dumitem.setIcon(icon)
        dumitem.setHidden(True)

    listWidget.connect(listWidget,SIGNAL("itemClicked(QListWidgetItem*)"),
              self.open_url)

    return listWidget

 def update_QListWidget(self, listWidget, data):
    nrows = listWidget.count()
    njsons= len(data)
    for i in range(nrows):
        listitem = listWidget.item(i)
        listitem.setText('No heippa!')
        listitem.setWhatsThis('https://www.gmail.com')


 def safe_get_value(self, dicti, key):
  if dicti.has_key(key):
   return dicti[key]
  return ''

 #
 def update_links(self, urlstrs):
    i = 0
    j = 0
    k = 0

    for dj in range(self.listWidget1.count()):
      self.listWidget1.item(dj).setHidden(True)    
    for dj in range(self.listWidget2.count()):
      self.listWidget2.item(dj).setHidden(True)
    for dj in range(self.listWidget3.count()):
      self.listWidget3.item(dj).setHidden(True)      

    #Initialize rake object
    #rake_object = rake.Rake("SmartStoplist.txt", 5, 5, 4)

    nlinks = 15
    nsuggestedlinks = 5
    for ijson in range( len(urlstrs) ):
                                linkstr  = self.unicode_to_str( urlstrs[ijson]["uri"] )
                                ctime    = str(urlstrs[ijson]["timeCreated"])
                                typestr  = str(urlstrs[ijson]["type"])
                                storedas = str(urlstrs[ijson]["isStoredAs"])
                                dataid   = str(urlstrs[ijson]["id"])
                                storedasl = storedas.split('#')[1]
                                #print 'Main: storedasl: ', storedasl
                                #content  = self.safe_get_value(urlstrs[ijson], "plainTextContent") 
                                content = ''
                                #keywords = rake_object.run(content)
                                keywords = ''
                                #print ctime 
                                timeint = int(ctime) / 1000
                                #print timeint
                                date = datetime.datetime.fromtimestamp(timeint)
                                datestr = date.__str__()

                                if len(linkstr) > 20:
                                  linkstrshort = linkstr[0:40]
                                

                                if len(keywords) > 0:
                                  tooltipstr = re.sub("[^\w]", " ", content)
                                  #self.labellist[i].setToolTip(tooltipstr)
                                  tooltipstr = "Keywords: " + keywords[0][0]
                                else:
                                  tooltipstr = 'Keywords: '
                                  #self.labellist[i].setText(keywords[0][0])

                                if storedasl in ["LocalFileDataObject" ]:
                                    #print 'Main: doc', linkstr

                                    visiblestr = linkstrshort + '  ' + datestr
                                    self.listWidget3.item(j).setText(visiblestr) 
                                    self.listWidget3.item(j).setWhatsThis(linkstr)
                                    self.listWidget3.item(j).setToolTip(tooltipstr)
                                    self.listWidget3.item(j).setHidden(False)
                                    #self.datelist3[j].setText(datestr)
                                    #self.labellist3[j].setAlignment(Qt.AlignLeft)
                                    j = j + 1
                                elif storedasl in ["MailboxDataObject"]:
                                    #print 'Main: mail ', storedasl
                                    dumlink = self.srvurl.split('/')[2]
                                    linkstr = 'http://' + dumlink + '/message?id=' + dataid
                                    #print 'Main: linkstr ', linkstr
                                    visiblestr = linkstrshort + '  ' + datestr
                                    self.listWidget2.item(k).setText(visiblestr) 
                                    self.listWidget2.item(k).setWhatsThis(linkstr)
                                    self.listWidget2.item(k).setToolTip(tooltipstr)
                                    self.listWidget2.item(j).setHidden(False)
                                    #self.labellist3[j].setAlignment(Qt.AlignLeft)

                                    k = k + 1                                  
                                else:
                                  #print 'Main: web ', linkstr
                                  title = None
                                  try:
                                    #print 'Finding Web page title:'
                                    dumt = urllib2.urlopen(linkstr)
                                    soup = BeautifulSoup(dumt)
                                    #print 'Soup title: ', soup.title.string
                                    try: 
                                      if soup.title.string is not None:                                        
                                        title = soup.title.string
                                        #print 'Soup title2 :', title
                                    except (AttributeError, ValueError):
                                      #print 'attr. error'
                                      pass
                                  except (urllib2.HTTPError, urllib2.URLError, ValueError):
                                    pass

                                  if title is None:
                                    #print 'Main: Web page title is: ', title
                                    title = linkstrshort

                                  visiblestr = title + '  ' + datestr
                                  self.listWidget1.item(i).setText(visiblestr) 
                                  self.listWidget1.item(i).setWhatsThis(linkstr)
                                  self.listWidget1.item(i).setToolTip(tooltipstr)
                                  self.listWidget1.item(i).setHidden(False)
                                  i = i + 1  
 #
 def read_user_ini(self):

    f          = open('user.ini','r')
    dumstr     = f.read()
    stringlist = dumstr.split()

    for i in range( len(stringlist) ):
            if stringlist[i] == "server_url:":
                    srvurl = stringlist[i+1]
            if stringlist[i] == "usrname:":
                    usrname = stringlist[i+1]
            if stringlist[i] == "password:":
                    password = stringlist[i+1]
            if stringlist[i] == "time_interval:":
                    time_interval_string = stringlist[i+1]
                    time_interval = float(time_interval_string)
            if stringlist[i] == "nspaces:":
                    nspaces_string = stringlist[i+1]
                    nspaces = int(nspaces_string)
            if stringlist[i] == "numwords:":
                    dum_string = stringlist[i+1]
                    numwords = int(dum_string)                      
            if stringlist[i] == "updating_interval:":
                    dum_string = stringlist[i+1]
                    updateinterval = float(dum_string)                        

    return srvurl, usrname, password, time_interval, nspaces, numwords, updateinterval


 #
 def unicode_to_str(self, ustr):
    """Converts unicode strings to 8-bit strings."""
    try:
        return ustr.encode('utf-8')
    except UnicodeEncodeError:
        print "Main: UnicodeEncodeError"
    return ""


 #
 def open_url(self, listWidgetitem):
  #global urlstr
  #webbrowser.open(urlstr)
  webbrowser.open(str(listWidgetitem.whatsThis()))


 #
 def stopstart(self):
  global var

  if var == True:
    var = False
    self.ssbutton.setText("Start logging")
    self.ssbutton.setStyleSheet("background-color: lightGreen")
    self.statuslabel.setText("Logging disabled")
    self.statuslabel.setStyleSheet("color: red")
  elif var == False:
    var = True
    self.ssbutton.setText("Stop logging")
    self.ssbutton.setStyleSheet("color: red")
    self.statuslabel.setText("Logging ongoing")
    self.statuslabel.setStyleSheet("color: green")
    #self.statuslabel.setStyleSheet("background-color: lightRed")

 def quitting(self):
  global var
  var = False
  QtCore.QCoreApplication.instance().quit()

 #Quit
 def closeEvent(self, event):
     self.quitting()





#--------------------------------------------------------

#
class SearchThread(QtCore.QThread):

 def __init__(self):
  QtCore.QThread.__init__(self)
  self.query = None
  self.oldquery = None
  self.searchfuncid = 0

 def __del__(self):
   self.wait()

 def change_search_function(self, searchfuncid):
  self.searchfuncid = searchfuncid
  print 'Search thread: search function changed to', str(searchfuncid)
  if searchfuncid == 1:
    #Update LinRel data files
    print 'Search thread: Updating Linrel data files!!!'
    check_update()


 def get_new_word(self, newquery):
  print "Search thread: got new query:", newquery
  self.query = newquery

 def run(self):
   self.search()

 def search(self):
  while True:
   sleep(0.3) # artificial time delay
   if self.query is not None and self.query != self.oldquery:
    dstr = str(self.query)
    print 'Search thread:', dstr 
    
    if self.searchfuncid == 0:
      jsons, docinds = search_dime_docsim(dstr)      
      print 'Search thread: Ready for new search!'
    elif self.searchfuncid == 1:
      #Create/update relevant data files if necessary and store into 'data/' folder in current path batman 
      jsons = search_dime_linrel_summing_previous_estimates(dstr)
      print 'Search thread: Ready for new search!'

    print 'Search thread: len jsons ', len(jsons)
    if len(jsons) > 0:
     #Return jsons
     self.emit( QtCore.SIGNAL('finished(PyQt_PyObject)'), jsons)

    self.oldquery = self.query


#
class LoggerThread(QtCore.QThread):

  def __init__(self):
    QtCore.QThread.__init__(self)

  #Keylogger
  def run(self):
        print 'Logger thread: Run Run'
        #Read user.ini
        srvurl, username, password, time_interval, nspaces, nwords, updateinterval = read_user_ini()
        settingsl = [srvurl, username, password, time_interval, nspaces, nwords, updateinterval]

        #Number 
        numoftopics = 10

        #List of urls
        urlstr = []

        #global urlstr
        global var

        countspaces = 0
        sleep_interval = 0.005

        #starttime = datetime.datetime.now().time().second
        now = time()
        dumstr = ''
        wordlist = []

        print "Logger thread: Ready for logging"

        #f = open('typedwords.txt', 'a')
        while True:

          sleep(0.005)
          changed, modifiers, keys = fetch_keys()

          #print modifiers
          #print changed, modifiers, keys
          keys  = str(keys)
          

          #Take care that ctrl is not pressed at the same time
          if not (modifiers['left ctrl'] or modifiers['right ctrl']):
            #Take current time
            cdate = datetime.datetime.now().date()
            ctime = datetime.datetime.now().time()

            cmachtime = time()
            var2 = cmachtime > now + float(time_interval)
            var3 = cmachtime > now + float(updateinterval)

            if keys == 'None':
                    keys = ''

            elif keys == '<backspace>':
                    keys = ''
                    #Convert current string into list of characters
                    duml = list(dumstr)
                    if len(duml) > 0:
                            #Delete the last character from the string list
                            del( duml[len(duml)-1] )
                            #Convert back to string
                            dumstr = "".join(duml)

            elif keys in ['<enter>', '<tab>','<right ctrl>','<left ctrl>',' ']:
                    print 'Logger thread: keys: ', keys
                    print 'Logger thread: changed: ', changed[0]
                    #keys = ' '
                    wordlist.append(dumstr)
                    #print wordlist
                    print 'Logger thread: wordlist:', wordlist[-nwords:]
                    dwordlist = wordlist[-nwords:]
                    #dumstr = dumstr + keys
                    countspaces = countspaces + 1
                    dumstr = ''
                    dumstr2 = ''
                    for i in range( len(dwordlist) ):
                        dumstr2 = dumstr2 + dwordlist[i] + ' '

                    self.emit( QtCore.SIGNAL('update(QString)'), dumstr2)

                    if var2:
                      #Empty the dumstr2 after time_interval period of time
                      dumstr2 = ''

            else:
                    cdate = datetime.datetime.now().date()
                    ctime = datetime.datetime.now().time()
                    dumstr = dumstr + keys


def read_user_ini():

    f          = open('user.ini','r')
    dumstr     = f.read()
    stringlist = dumstr.split()

    for i in range( len(stringlist) ):
            if stringlist[i] == "server_url:":
                    srvurl = stringlist[i+1]
            if stringlist[i] == "usrname:":
                    usrname = stringlist[i+1]
            if stringlist[i] == "password:":
                    password = stringlist[i+1]
            if stringlist[i] == "time_interval:":
                    time_interval_string = stringlist[i+1]
                    time_interval = float(time_interval_string)
            if stringlist[i] == "nspaces:":
                    nspaces_string = stringlist[i+1]
                    nspaces = int(nspaces_string)
            if stringlist[i] == "numwords:":
                    dum_string = stringlist[i+1]
                    numwords = int(dum_string)                      
            if stringlist[i] == "updating_interval:":
                    dum_string = stringlist[i+1]
                    updateinterval = float(dum_string)  

    return srvurl, usrname, password, time_interval, nspaces, numwords, updateinterval


# run
app  = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()
