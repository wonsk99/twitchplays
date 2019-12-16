#!/usr/bin/env python3

import socket
import threading
import pyautogui

# GLOBALS
SERVER = "irc.twitch.tv"
PORT = 6667
OAUTH = "oauth:6f1ieh366ll5r89qn5sc52t2mlw43g"
NAME = "AnotherTwitchPlays"
CHAN = "onesockgg"
OWNER = "onesockgg"
MYMSG = ""

# SOCKET SERVER CONNECTION
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + OAUTH + "\n" + "NICK " + NAME + "\n" + "JOIN #" + CHAN + "\n").encode())

def twitch_connect():
	# READ
	def access_chat():
		reading = True
		while reading:
			buffer_read = irc.recv(1024).decode()
			for line in buffer_read.split("\n")[0:-1]:
				print(line)
				reading = finished_read(line)

	# READ HAS FINISHED
	def finished_read(line):
		if "End of /NAMES list" in line:
			display_msg(irc, "I Have Arrived!")
			print("Entered Another Twitch Plays")
			return False
		return True

	# DISPLAY AFTER CONNECT
	def display_msg(irc, msg):
		msgtemp = "PRIVMSG #" + CHAN + " :" + msg + "\n"
		irc.send(msgtemp.encode())	

	# GET USERNAME
	def user_name(line):
		line = line.split(":")
		user = line[1].split("!", 1)[0]
		return user

	# ISOLATE THE MESSAGE
	def get_msg(line):
		global MYMSG
		try:
			MYMSG = line.split(":")[2]
		except:
			MYMSG = ""
		return MYMSG

	# USER or SERVER
	def console(line):
		if "PRIVMSG" in line:
			return False
		return True


	access_chat()

	while True:
		try:
			buffer_read = irc.recv(1024).decode()
		except:
			buffer_read = ""
		for line in buffer_read.split("\r\n"):
			if line == "":
				continue
			elif "PING" in line and console(line):
				alivemsg = "PONG tmi.twitch.tv\r\n".encode()
				irc.send(alivemsg)
				print(alivemsg)
				continue
			# print(line)
			uname = user_name(line)
			MYMSG = get_msg(line)
			print(uname + ": " + MYMSG)

# ONTO THE CONTROLS
def controller():
	global MYMSG
	while True:
		if MYMSG.strip().lower() == "up":
			pyautogui.keyDown("up")
			MYMSG = ""
			pyautogui.keyUp("up")
		elif MYMSG.strip().lower() == "down":
			pyautogui.keyDown("down")
			MYMSG = ""
			pyautogui.keyUp("down")
		elif MYMSG.strip().lower() == "left":
			pyautogui.keyDown("left")
			MYMSG = ""
			pyautogui.keyUp("left")
		elif MYMSG.strip().lower() == "right":
			pyautogui.keyDown("right")
			MYMSG = ""
			pyautogui.keyUp("right")

		elif MYMSG.strip().lower() == "a":
			pyautogui.keyDown("up")
			MYMSG = ""
			pyautogui.keyUp("up")
		elif MYMSG.strip().lower() == "b":
			pyautogui.keyDown("up")
			MYMSG = ""
			pyautogui.keyUp("up")
		elif MYMSG.strip().lower() == "start":
			pyautogui.keyDown("up")
			MYMSG = ""
			pyautogui.keyUp("up")
		elif MYMSG.strip().lower() == "select" or MYMSG.strip().lower == "sel":
			pyautogui.keyDown("up")
			MYMSG = ""
			pyautogui.keyUp("up")
		elif MYMSG.strip().lower() == "l":
			pyautogui.keyDown("up")
			MYMSG = ""
			pyautogui.keyUp("up")
		elif MYMSG.strip().lower() == "r":
			pyautogui.keyDown("r")
			MYMSG = ""
			pyautogui.keyUp("r")
		else:
			pass

# MAIN
if __name__ == "__main__":
	# Game controls and twitch on separate threads
	t1 = threading.Thread(target=twitch_connect)
	t1.start()
	t2 = threading.Thread(target=controller)
	t2.start()


