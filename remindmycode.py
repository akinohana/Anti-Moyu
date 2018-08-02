#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32gui
import time
import winsound
import win32api

def send_email(user, pwd, recipient, subject, body):
	import smtplib

	FROM = user
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body

	# Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(user, pwd)
	server.sendmail(FROM, TO, message)
	server.close()
	print 'successfully sent the mail'
	time.sleep(10);


def remindtocode():
	print 'Do work now!!!!'
	send_email('xxxxxxxx@gmail.com','xxxxxxxxxxxx','xxxxxxxxxxxxx@gmail.com','起床写代码啦！！','~~~~');

notdoingwork = 0;
nottouchingPC = 0;
needremind = False;
lastinputtime =0;

AllowedWndTitle = ['Studio', 'Google 搜索','EditPlus','Gmail','XShell','Xftp','WebStorm']

while(1):
	
	if(lastinputtime == win32api.GetLastInputInfo()):
		print 'Get back to PC!!!'		
		nottouchingPC += 1;
		if(nottouchingPC > 600):
			needremind = True;
	else:
		nottouchingPC =0;

	lastinputtime = win32api.GetLastInputInfo();


	hwnd = win32gui.GetForegroundWindow();
	title_text = win32gui.GetWindowText(hwnd)
	title_text = title_text.decode('gbk').encode('utf-8')
	print type(title_text)


	isfindallowedtitle = False;
	for titlename in AllowedWndTitle:
		if titlename in title_text:
			isfindallowedtitle = True;
			print titlename;

	if (isfindallowedtitle == False):
		print 'Do work!!!!'
		notdoingwork += 1;
		if(notdoingwork > 300):
			needremind = True;
	else:
		notdoingwork = 0;
	if(needremind):
		remindtocode();
		needremind = False;

	time.sleep(1);