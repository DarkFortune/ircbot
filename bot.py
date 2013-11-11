import socket

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#config

server = "irc.esper.net"
nick = "Lbot"
channel = "#testingmyswag"
#functions! :D
def join(chan):
    irc.send("JOIN "+ chan +"\r\n")

def ping():
      irc.send("PONG :Pong \r\n")

def sendmsg(chan, msg):
      irc.send("PRIVMSG "+ chan +" :"+ msg +"\r\n")

#connect
irc.connect((server, 6667))
irc.send("USER "+ nick +" "+ nick +" "+ nick + " :This is a bot by Lucy " + "\r\n")
irc.send("NICK "+ nick +"\r\n")
join(channel)

while 1:
    ircmsg = irc.recv(500)
    ircmsg = ircmsg.strip('\r\n')
    print(ircmsg)
    if ircmsg.find("PING :") != -1:
          irc.send("PONG "+ ircmsg.split() [1] + "\r\n" )
