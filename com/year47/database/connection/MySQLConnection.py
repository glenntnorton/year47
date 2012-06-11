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

import MySQLdb
from com.year47.database.connection import Connection


class MySQLConnection(Connection.Connection):
    """MySQLConnection(Connection.Connection) - inherits from Connection. 
    
    Objects inheriting from Connection MUST override the
    connect(), getExceptionHandler() and getQuoteHandler() methods or a
    NotImplementedError will be raised."""
    
    def __init__(self, host=None, user=None, passwd=None, db=None, 
            autocommit=1):
        """initiate a MySQLConnection.

        host, user, passwd, db & autocommit attributes may be assigned here or
        through appropriate set* methods.

        """
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.autocommit = autocommit


    def setHost(self, host):
        """assign mysql hostname"""
        self.host = host


    def setUser(self, user):
        """assign MySQL username"""
        self.user = user


    def setPasswd(self, passwd):
        """assign MySQL password"""
        self.passwd = passwd


    def setDb(self, db):
        """assign MySQL database"""
        self.db = db


    def setAutocommit(self, autocommit=1):
        """assign autocommit to bypass commit requirement. default is 1"""
        self.autocommit = autocommit



    def connect(self):
        """connect to a MySQL database"""
        try:
            self._mysql_dbh = MySQLdb.connect( 
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                db = self.db
            )

            self._mysql_dbh._transactional = self.autocommit
            return self._mysql_dbh

        except(StandardError, MySQLdb.Error), err:
            print err



    def getExceptionHandler(self):
        """returns the top level error handler"""
        return self._mysql_dbh.Error


    def getQuoteHandler(self):
        """returns the default quote handler"""
        return self._mysql_dbh.escape


# END: MySQLConnection.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
