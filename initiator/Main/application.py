#!/usr/bin/python
# -*- coding: utf8 -*-
"""FIX Application"""
import sys
from datetime import datetime
import quickfix as fix
import time
import logging
#from model.logger import setup_logger
from initiator.model.logger import setup_logger
#rom initiator.model import Field

# configured
__SOH__ = chr(1)

# Logger
setup_logger('FIX', 'Logs/message.log')
logfix = logging.getLogger('FIX')


class Application(fix.Application):
    """FIX Application"""


    def onCreate(self, sessionID):
        self.sessionID = sessionID
        print("On Create")
        return
    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("I'm in !.. hello Rofex")
        return
    def onLogout(self, sessionID): 
        return

    def toAdmin(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("S >> (%s)" % msg)
        if message.getHeader().getField(35) is "A":
            message.setField(self.username)
            message.setField(self.mypass)

            print("Mensaje toAdmin")


        return
    def fromAdmin(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("R >> (%s)" % msg)
        return
    def toApp(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("S >> (%s)" % msg)
        return
    def fromApp(self, message, sessionID):
        msg = message.toString().replace(__SOH__, "|")
        logfix.info("R >> (%s)" % msg)
        self.onMessage(message, sessionID)
        return

   
    def onMessage(self, message, sessionID):
        """on Message"""
        pass

    def run(self):
        """Run"""
        while 1:
            time.sleep(2)