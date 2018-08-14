#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import win32gui
import time
import winsound
import win32api
import os
import subprocess
import glob, os,signal


def outputuseage():
	print 'useage: start|stop|restart [delay in mintues]';

def makestop():
	fn ="stop";
	try:
		file = open(fn, 'r')
	except IOError:
		file = open(fn, 'w')

def trystart(delaytime):
	os.chdir("./")
	for file in glob.glob("*.running"):

		finalpid = file.replace(".running","");

		print("kill:" + finalpid);
		os.system("taskkill /pid "+ finalpid);
		os.remove(file)
	startcmd = "start python remindmycode.py " + str(delaytime *60 + 1);
	antimoyuproc = subprocess.Popen(["cmd","/c " + startcmd])



if(len(sys.argv) < 2):
	outputuseage();
	exit();
if(sys.argv[1] == 'start'):
	trystart(0)
elif(sys.argv[1] == 'stop'):
	makestop();
elif(sys.argv[1].find("restart") != -1):
	trystart(int(sys.argv[2]))

else:
	outputuseage();