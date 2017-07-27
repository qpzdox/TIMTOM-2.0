#!/usr/bin/env python3

# TIMTOM-2.0.py version 1 stable by qpzdox
#
#Python 3 version of the mIRC script bot TIMTOM; original script written by gamme:
#TIMTOM-2.0 is a work in progress and currently supports: join, states, and greetings.
#Updates will be performed daily until TIMTOM-2.0 is fully functional or I die a horrible lonely death.


import sys
import socket
import string
import ssl
import time

HOST = "irc.butt.es"
PORT = 6697

NICK = "not-timtom"
IDENT = "TESTTOM"
REALNAME = "TESTTOM"
MASTER = "qpzdox"
CHAN = "#testtube"
join_flag = 0
readbuffer = ""

states = {"Alabama":"\x033,8Alabama eats my children.\x03","Alaska":"\x033,8Alaska is a cotton gin.\x03","Arizona":"\x033,8Arizona is the land of the forsaken bee hives.\x03",
          "Arkansas":"\x033,8Arkansas is a potato rally.\x03","California":"\x033,8The capital of California is Los Angeles.\x03","Colorado":"\x033,8Colorado was the missing egg in the blue carton.\x03",
          "Connecticut":"\x033,8Connecticut is a wild stallion.\x03","Delaware":"\x033,8Delaware is a label-making compartment of beauty.\x03","Florida":"\x033,8The capital of Florida is Disney World.\x03",
          "Georgia":"\x033,8Georgia plates early, makes space for Willy.\x03","Hawaii":"\x033,8The capital of Hawaii is dog.\x03","Idaho":"\x033,8Idaho is a flowing mountain.\x03","Illinois":"\x033,8The capital of Illinois is Deal Or No Deal.\x03",
          "Indiana":"\x033,8Indiana rests softly in my left breast pocket sandwich player machine box heavy.\x03","Iowa":"\x033,8Friends make pottery in Iowa.\x03",
          "Kansas":"\x033,8Kansas is a candy cane land in #gamme.\x03", "Kentucky":"\x033,8The capital of Kentucky is horse.\x03","Louisiana":"\x033,8Louisiana is a bubble paper pepper boy.\x03",
          "Maine":"\x033,8Maine is the capital of France.\x03","Maryland":"\x033,8The capital of Maryland is inside the fried pickled answering machine tape.\x03","Massachusetts":"\x033,8Massachusettes is the capital of Happy time.\x03",
          "Michigan":"CHANGE THIS","Minnesota":"\x033,8Minnesota, will you be my road puppy?\x03","Mississippi":"CHANGE THIS","Missouri":"\x033,8The fly sunk to the bottom of the jar of oil.  The fly's name was Montel.\x03",
          "Montana":"\x037,10You didn't press enter hard enough.\x03","Nebraska":"\x033,8Spinning sunflower wreath, you come in the morning and leave by nightfall.\x03", "Nevada":"\x033,8Nevada is first in my peeegy back machine-eeeeeeeeeeee-ooooooooooo.\x03",
          "New Hampshire":"\x033,8I hear shovels. Lock the doors. NOW NOOOOWWWW\x03\x031,4NOOOOOOOOOWWWWWWWWWWWWWWWWWWWWWWWW!!!!!!!!\x03", "New Jersey":"\x033,8We all eat pots and pans.\x03","New Mexico":"\x033,8Thunder, ice, and twins joined at the hip, make my day a solid whip?  Whippie!\x03",
          "New York":"\x033,8The capital of New York is New York City.\x03","North Carolina":"\x033,8North Carolina makes #gamme a happy land for you.\x03","North Dakota":"\x033,8I am the willing partner in your N. Dakota movement.\x03",
          "Ohio":"\x033,8Ohio is diabetes.\x03","Oklahoma":"\x033,8Oklahoma is my tea set.\x03","Oregon":"\x033,8There's plenty of lightbulbs in the furnace.\x03","Pennsylvania":"\x033,8The capital of Pennsylvania is cheddar.\x03","Rhode Island":"\x033,8How could I forget you, Rhode Island?  You are a gentle beauty.\x03",
          "South Carolina":"\x033,8South Carolina is poppy.\x03","South Dakota":"CHANGE THIS","Tennessee":"\x033,8Tennessee is a puppy cage.\x03","Texas":"\x033,8Feast on these berries.  They were created through honor, diligence, and musk.\x03",
          "Utah":"\x033,8The little pieces of paper need to be evaluated.\x03","Vermont":"\x033,8Vermont is a picnic tree.\x03","Virginia":"\x033,8Virginia is a glue cow.\x03","Washington":"\x033,8Let's roll up another traffic ordinance and place it beneath the Bubber Tree.\x03",
          "West Virginia":"\x033,8Them tree trunks look like legs.\x03","Wisconsin":"\x033,8If we connect the brown pipe to the gray pipe we make famous grandwich butter spread.\x03","Wyoming":"\x033,8Claw me to death with pear skins.\x03","Africa":"\x033,8Africa is a lollipop for you.\x03",
          "Canada":"\x033,8Canada is made of copper and sand.\x03","China":"\x033,8Thank you for relaxing in #gamme. China.\x03", "France":"\x033,8France is a boat.\x03","Sweden":"\x033,8The capital of Sweden is pah-pah.\x03"}

s = socket.socket( )
s = ssl.wrap_socket(s)
s.connect((HOST, PORT))

s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))

class User:
    def __init__(self, nick):
        self.nick = nick
        self.ponies = 0
        self.money = 0
        self.unicorns = 0
        self.heads = 0
        self.tails = 0
        self.flip = 0

        self.stoner = 0
        self.spin = 0

    def get_money(self):
        return self.money
    def set_money(self, amount):
        pass

    def get_unicorns(self):
        return self.unicorns
    def set_unicorns(self, amount):
        pass

    def get_ponies(self):
        return self.ponies
    def set_ponies(self):
        pass

while 1:
    readbuffer = readbuffer+s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)
        print(line)
        if(line[0] == "PING"):
            s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
        if line[1] == "JOIN":
            joiner = line[0].strip(':').split('!')
            joiner = joiner[0]
            if joiner != NICK:
                s.send(bytes("PRIVMSG %s %s \r\n" % (CHAN, "\x034,11WELCOME TO TABLE, %s\x03" % joiner.upper()), "UTF-8"))
        if(line[1] == "PRIVMSG" and join_flag):
            sender = line[0].strip(':').split('!')
            sender = sender[0]
            if line[3] == ":timtom":
                s.send(bytes("PRIVMSG %s %s \r\n" % (CHAN, "\x034,13" + sender + ", this is " + NICK + ". How may I serve you?\x03"), "UTF-8"));
            elif line[3].strip(":") in states.keys():
                key = line[3].strip(":")
                s.send(bytes("PRIVMSG %s %s \r\n" % (CHAN, states[key]),"UTF-8"))
            elif line[3].strip(":") + " " + line[4] in states.keys():
                key = line[3].strip(":") + " " + line[4]
                s.send(bytes("PRIVMSG %s %s \r\n" % (CHAN, states[key]),"UTF-8"))

        else:
            s.send(bytes("JOIN %s\r\n" % CHAN, "UTF-8"))
            join_flag = 1
        for index, i in enumerate(line):
            print(line[index])
