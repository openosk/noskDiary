#!/usr/bin/env python2.7
from datetime import datetime
from twisted.internet import reactor, protocol
from twisted.words.protocols import irc
class IRCLogger(irc.IRCClient):
    logfile = file('/tmp/freenode.txt', 'a+')
    nickname = 'noskDiary'
    def signedOn(self):
        self.join('#nosk')
    def privmsg(self, user, channel, message):
        d=datetime.today()
        print "%s %s  %s " % (d.strftime("%Y/%m/%d %I:%M%p"),user.split('!')[0],message)
	d.strftime("%A %d/%m/%Y %I:%M%p")
        self.logfile.write(" %s :  %s said %s \n" % ( d.strftime("%Y/%m/%d %I:%M%p %A") ,user.split('!')[0], message ))
        self.logfile.flush()
def main():
    f = protocol.ReconnectingClientFactory()
    f.protocol = IRCLogger
    reactor.connectTCP('irc.freenode.net', 6667, f)
    reactor.run()
if __name__ == '__main__':
    main()
