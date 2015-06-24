#!/usr/bin/python
# -*- coding: utf-8 -*-

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

# For DiMe server queries
import requests
import socket
import json

import subprocess   # for running bash script

# For opening links
import webbrowser

#For GUI
from PyQt4 import QtCore, QtGui, uic

#Includes the definition of clickable label
import ExtendedQLabel

from PyQt4.QtGui import *
from PyQt4.QtCore import *

#
import re

class WindowClass(QtGui.QMainWindow):
#class WindowClass(QtGui.QWidget):
    
    def __init__(self):
      super(WindowClass, self).__init__()

      #Set the window title
      self.setWindowTitle('Proactive Search')

      #Always on top
      self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

      #Create menubar
      menubar = self.menuBar()
      filemenu = menubar.addMenu('&File')
      filemenu.addAction('Quit', self.quitting)

      #Quit button
      self.quitbutton = QtGui.QPushButton("Quit",self)
      self.quitbutton.resize(40,20)
      self.quitbutton.clicked.connect(self.quitting)
      self.quitbutton.move(270,7)

      #Stop/Start button
      ssbuttonstr = "Stop logging"
      self.ssbutton = QtGui.QPushButton(ssbuttonstr,self)
      self.ssbutton.setStyleSheet("color: red")
      self.ssbutton.resize(90,20)
      self.ssbutton.clicked.connect(self.stopstart)
      self.ssbutton.move(10,7)

      #Set color of labels
      palette = QtGui.QPalette()
      palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkGreen)

      #Create QGroupbox
      self.mygroupbox = QtGui.QGroupBox()
      #Create layout
      self.myform = QtGui.QFormLayout()
      #Add self.myform to self.mygroupbox layout
      self.mygroupbox.setLayout(self.myform)

      #Make labellist
      self.labellist = []

      #Create status label    
      self.statuslabel = QtGui.QLabel("Logging ongoing")
      self.statuslabel.setStyleSheet("color: darkGreen")
      self.myform.addRow(self.statuslabel)

      #Create infolabel    
      self.infolabel = QtGui.QLabel("Links to suggested resources:")
      self.myform.addRow(self.infolabel)

      #Make clickable labels
      for i in range(5):
        #
        dumlabel = ExtendedQLabel.ExtendedQLabel("", self)
	dumlabel.connect(dumlabel, SIGNAL('clicked()'), dumlabel.open_url)
	dumlabel.setPalette(palette)
	#Add to label list
	self.labellist.append(dumlabel) 
	#
	self.myform.addRow(self.labellist[i])

      #Create scrollbar area
      self.scrollArea = QtGui.QScrollArea(self)
      self.scrollArea.setWidget(self.mygroupbox)
      self.scrollArea.setWidgetResizable(True)
      self.scrollArea.setFixedHeight(200)
      self.scrollArea.setFixedWidth(300)
      self.scrollArea.move(10,30)
      
      #
      self.setGeometry(0, 0, 320, 240)

      #Get the current path
      self.pathstr = os.path.dirname(os.path.realpath(sys.argv[0]))

      #Read user.ini file
      self.username, self.password, self.time_interval, self.nspaces = self.read_user_ini()

      #Initial time
      self.cdate          = str(datetime.datetime.now().date())
      self.time           = str(datetime.datetime.now().time())
      #
      self.done           = False
      #
      self.sleep_interval = 1.005

    def startlog(self):
        threading.Thread(target = log, args = (self,) ).start()

    def show_link(self):
	threading.Thread(target = update_visible_link, args = (self,)).start()

    def update_links(self, urlstr):
        #pass
        i = 0
        #sleep(2.0)
        #for i in len(r.json())
        if urlstr != None:
                for i in range( len(urlstr.json()) ):
                                linkstr = str( urlstr.json()[i]["uri"] )
                                self.labellist[i].setText(linkstr)
                                plaintext    = urlstr.json()[i]["plainTextContent"]
                                tooltipstr   = re.sub("[^\w]", " ", plaintext)
                                self.labellist[i].setToolTip(tooltipstr[0:120])


    def read_user_ini(self):

        f          = open('user.ini','r')
        dumstr     = f.read()
        stringlist = dumstr.split()

        for i in range( len(stringlist) ):
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

        return usrname, password, time_interval, nspaces

    #
    def open_url(self):
      global urlstr
      webbrowser.open(urlstr)

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
              self.startlog()

    def quitting(self):
      global var
      var = False
      QtCore.QCoreApplication.instance().quit()

    #Quit
    def closeEvent(self, event):
        self.quitting()


################################################################


# linux only!
assert("linux" in sys.platform)


x11 = ct.cdll.LoadLibrary(find_library("X11"))
display = x11.XOpenDisplay(None)


# this will hold the keyboard state.  32 bytes, with each
# bit representing the state for a single key.
keyboard = (ct.c_char * 32)()

# these are the locations (byte, byte value) of special
# keys to watch
shift_keys = ((6,4), (7,64))
modifiers = {
    "left shift": (6,4),
    "right shift": (7,64),
    "left ctrl": (4,32),
    "right ctrl": (13,2),
    "left alt": (8,1),
    "right alt": (13,16)
}
last_pressed = set()
last_pressed_adjusted = set()
last_modifier_state = {}
caps_lock_state = 0

# key is byte number, value is a dictionary whose
# keys are values for that byte, and values are the
# keys corresponding to those byte values
key_mapping = {
    1: {
        0b00000010: "<esc>",
        0b00000100: ("1", "!"),
        #0b00001000: ("2", "@"),
        0b00001000: ("2", "@"),
        0b00010000: ("3", "#"),
        0b00100000: ("4", "$"),
        0b01000000: ("5", "%"),
        #0b10000000: ("6", "^"),
        0b10000000: ("6", "&"),
    },
    2: {
        #0b00000001: ("7", "&"),
        0b00000001: ("7", "/"),
        #0b00000010: ("8", "*"),
        0b00000010: ("8", "("),
        #0b00000100: ("9", "("),
        0b00000100: ("9", ")"),
        #0b00001000: ("0", ")"),
        0b00001000: ("0", "="),
        #0b00010000: ("-", "_"),
        0b00010000: ("+", "?"),
        #0b00100000: ("=", "+"),
        0b00100000: ("´", "`"),
        0b01000000: "<backspace>",
        0b10000000: "<tab>",
    },
    3: {
        0b00000001: ("q", "Q"),
        0b00000010: ("w", "W"),
        0b00000100: ("e", "E"),
        0b00001000: ("r", "R"),
        0b00010000: ("t", "T"),
        0b00100000: ("y", "Y"),
        0b01000000: ("u", "U"),
        0b10000000: ("i", "I"),
    },
    4: {
        0b00000001: ("o", "O"),
        0b00000010: ("p", "P"),
        0b00000100: ("[", "{"),
        0b00001000: ("]", "}"),
        0b00010000: "<enter>",
        0b00100000: "<left ctrl>",
        0b01000000: ("a", "A"),
        0b10000000: ("s", "S"),
    },
    5: {
        0b00000001: ("d", "D"),
        0b00000010: ("f", "F"),
        0b00000100: ("g", "G"),
        0b00001000: ("h", "H"),
        0b00010000: ("j", "J"),
        0b00100000: ("k", "K"),
        0b01000000: ("l", "L"),
        0b10000000: ("ö", "Ö"),
        #0b10000000: (";", ":"),
    },
    6: {
        #0b00000001: ("'", "\""),
        0b00000001: ("ä", "Ä"),
        0b00000010: ("`", "~"),
        #0b00000100: "<left shift>",
        0b00001000: ("\\", "|"),
        0b00010000: ("z", "Z"),
        0b00100000: ("x", "X"),
        0b01000000: ("c", "C"),
        0b10000000: ("v", "V"),
    },
    7: {
        0b00000001: ("b", "B"),
        0b00000010: ("n", "N"),
        0b00000100: ("m", "M"),
        #0b00001000: (",", "<"),
        0b00001000: (",", ";"),
        #0b00010000: (".", ">"),
        0b00010000: (".", ":"),
        #0b00100000: ("/", "?"),
        0b00100000: ("-", "_"),
        #0b01000000: "<right shift>",
    },
    8: {
        #0b00000001: "<left alt>",
        0b00000010: " ",
        0b00000100: "<caps lock>",
    },
    13: {
        0b00000010: "<right ctrl>",
        #0b00010000: "<right alt>",
    },
}




def fetch_keys_raw():
    x11.XQueryKeymap(display, keyboard)
    return keyboard


def fetch_keys():
    global caps_lock_state, last_pressed, last_pressed_adjusted, last_modifier_state
    keypresses_raw = fetch_keys_raw()

    # check modifier states (ctrl, alt, shift keys)
    modifier_state = {}
    for mod, (i, byte) in modifiers.iteritems():
        modifier_state[mod] = bool(ord(keypresses_raw[i]) & byte)
    
    # shift pressed?
    shift = 0
    for i, byte in shift_keys:
        if ord(keypresses_raw[i]) & byte:
            shift = 1
            break

    # caps lock state
    if ord(keypresses_raw[8]) & 4: caps_lock_state = int(not caps_lock_state)


    # aggregate the pressed keys
    pressed = []
    for i, k in enumerate(keypresses_raw):
        o = ord(k)
        if o:
            for byte,key in key_mapping.get(i, {}).iteritems():
                if byte & o:
                    if isinstance(key, tuple): key = key[shift or caps_lock_state]
                    pressed.append(key)

    
    tmp = pressed
    pressed = list(set(pressed).difference(last_pressed))
    state_changed = tmp != last_pressed and (pressed or last_pressed_adjusted)
    last_pressed = tmp
    last_pressed_adjusted = pressed

    if pressed: pressed = pressed[0]
    else: pressed = None


    state_changed = last_modifier_state and (state_changed or modifier_state != last_modifier_state)
    last_modifier_state = modifier_state

    return state_changed, modifier_state, pressed


###
def log(win):

      #global urlstr
      global var

      countspaces = 0
      sleep_interval = 0.005
      timeinterval = 10

      #starttime = datetime.datetime.now().time().second
      now = time()
      flag = 0
      flag2= 0
      dumstr = ''
      wordlist = []
      #Show the links of suggested resources in the window
      #update_kurllabel2(self)

      #f = open('typedwords.txt', 'a')
      while var:

        sleep(sleep_interval)
        changed, modifiers, keys = fetch_keys()
        keys  = str(keys)


        #Take current time
        cdate = datetime.datetime.now().date()
        ctime = datetime.datetime.now().time()

        cmachtime = time()
        var2 = cmachtime > now + win.time_interval

        if keys == 'None':
                keys = ''

        elif keys == '<backspace>':
                keys = ''
                #Convert current string into list of characters
                duml = list(dumstr)
                if len(duml) > 0:
                        #Delete the last character from the list
                        del( duml[len(duml)-1] )
                        #Convert back to string
                        dumstr = "".join(duml)
	
        elif keys in ['<enter>', '<tab>','<right ctrl>','<left ctrl>'," "]:

        	#keys = ' '
	        wordlist.append(dumstr)
                #dumstr = dumstr + keys
	        countspaces = countspaces + 1
	        dumstr = ''
	
		if var2:
              		#
			dumstr2 = ''
        	        for i in range( len(wordlist) ):
                 	       dumstr2 = dumstr2 + wordlist[i] + ' '

	                #
                        f = open("typedwords.txt","a")
        	        f.write(str(cdate) + ' ' + str(ctime) + ' ' + dumstr2 + '\n')
		        f.close()

                	#Make query to DiMe
	                urlstr = search_dime(win.username, win.password, dumstr2)
        	        #Update visible links
                	win.update_links(urlstr)

	                #Add the suggested url into a history file
        	        if urlstr != None:
                	        f2 = open("suggested_pages.txt","a")
                        	f2.write(str(cdate) + ' ' + str(ctime) + ' ' + str(urlstr.json()[0]["uri"]) + '\n')
	                        f2.close()

        	        #Clear the dummy string
                	dumstr = ''
	                dumstr2= ''
	
        	        #Remove content from wordlist
                	del wordlist[:]

	                countspaces = 0

        	        flag = 1
                	flag2= 0

	                now = time()

        else:
                cdate = datetime.datetime.now().date()
                ctime = datetime.datetime.now().time()
                dumstr = dumstr + keys



def search_dime(username, password, query):
	#------------------------------------------------------------------------------

	server_url = 'http://localhost:8080/api'
	server_username = str(username)
	server_password = str(password)

	#------------------------------------------------------------------------------

	# ping server (not needed, but fun to do :-)
	r = requests.post(server_url + '/ping')

	if r.status_code != requests.codes.ok:
	    print('No connection to DiMe server!')
	    sys.exit(1)

	# make search query
	#query = "dime"
	#query = "python"

	r = requests.get(server_url + '/search?query={}&limit=5'.format(query),
        	         headers={'content-type': 'application/json'},
                	 auth=(server_username, server_password),
	                 timeout=10)
	
	print query
	print len(r.json())

	if len(r.json()) > 0:
		if r.status_code != requests.codes.ok:
		    #print('ErrorNo connection to DiMe server!')
		    r = None
		    #sys.exit(1)

		return r


if __name__ == "__main__":

  #Important global variables!
  global urlstr
  #Initialize urlstr
  urlstr = search_dime("petrihiit","p3tr1h11t","python")

  global var
  var = True

  #Make the QGui.QApplication object
  app = QtGui.QApplication(sys.argv)
  #Set Taskbar icon for app object
  app.setWindowIcon(QtGui.QIcon('keyboard.png'))

  #Get screen dimensions
  screen = app.desktop()
  sl = screen.width()
  sh = screen.height()

  #Make a WindowClass object
  newwindow = WindowClass()
  newwindow.show()

  #Move the window into the right corner
  newwindow.move(sl-350,0)

  #Start keylogger
  newwindow.startlog()

  #Start
  app.exec_()