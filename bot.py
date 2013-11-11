import socket

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#config

server = "irc.esper.net"
nick = "Lbot"
channel = "#testingmyswag"
#functions! :D
def join(chan):
    irc.send("JOIN "+ chan +"\n")

def ping():
      irc.send("PONG :Pong\n")

def sendmsg(chan , msg):
      irc.send("PRIVMSG "+ chan +" :"+ msg +"\n")
#connect
irc.connect((server, 6667))
irc.send("USER "+ nick +" "+ nick +" "+ nick + " :This is a bot by Lucy \n")
irc.send("NICK "+ nick +"\n")
join(channel)

while 1:
    ircmsg = irc.recv(500)
    ircmsg = ircmsg.strip('\r\n')
    print(ircmsg)
    if ircmsg.find("PING :") != -1:
        ping()

