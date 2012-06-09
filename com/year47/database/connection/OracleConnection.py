#####
#
# Year47 Software Library Resource
# Copyright (C) 2010-2012 Year47. All Rights Reserved.
# 
# Author: Glenn T Norton
# Contact: glenn@year47.com
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# 
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
#
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.
#
#####

import cx_Oracle
from com.year47.database.connection import Connection

class OracleConnection(Connection.Connection):
    
    def __init__(self, username=None, passwd=None, ip_address='127.0.0.1', sid=None, autocommit=0):
        self.username = username
        self.passwd = passwd
        self.ip_address = ip_address
        self.sid = sid
        self.autocommit = autocommit

    
    def setUsername(self, u):
        self.username = u

    
    def setPasswd(self, p):
        self.passwd = p


    def setIPAddress(self, ip_address='127.0.0.1'):
        self.ip_address = ip_address


    def setSID(self, s):
        self.sid = s


    def setAutocommit(self, autocommit=0):
        self.autocommit = autocommit


    def connect(self, **kwargs):
        if not self.username: self.username = kwargs['username']
        if not self.passwd: self.passwd = kwargs['passwd']
        if not self.ip_address: self.ip_address = kwargs['ip_address'],
        if not self.sid: self.sid = kwargs['sid'],
        if not self.autocommit: self.autocommit = kwargs['autocommit']

        try:
            self.connection_string = "%s/%s@%s/%s" % (
                self.username,
                self.passwd,
                self.ip_address,
                self.sid
            )
            self._oracle_dbh = cx_Oracle.connect(self.connection_string)
            self._oracle_dbh.autocommit = self.autocommit

        except(StandardError, cx_Oracle.Error), err:
            raise cx_Oracle.Error(err)

        return self._oracle_dbh

    def getExceptionHandler(self):
        return cx_Oracle.Error

    def getQuoteHandler(self):
        return self._quoteHandler

    def _quoteHandler(self, s):
        # handles single & double qoutes
        new_s = ""
        tmp = s.split("'")
        for t in tmp[0:-1]:
            new_s += t
            new_s += "''"
        new_s += tmp[-1]

        tmp = new_s.split('"')
        new_s = ""
        for t in tmp[0:-1]:
            new_s += t
            new_s += '""'
        new_s += tmp[-1]

        return new_s



# END: OracleConnection.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
