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


from com.year47.database.connection import Connection

# import pysqlite or sqlite3
try:
    import sqlite
except ImportError:
    import sqlite3 as sqlite


class SQLiteConnection(Connection.Connection):

    def __init__(self): pass


    def connect(self, f):
        try:
            self._sqlite_dbh = sqlite.connect(f, isolation_level=None)
            self._sqlite_dbh.text_factory = str
            return self._sqlite_dbh
        except(StandardError, sqlite.Error), err:
            print err       


    def getExceptionHandler(self):
        return self._sqlite_dbh.DatabaseError


    def getQuoteHandler(self):
        return self._quoteHandler


    def _quoteHandler(self, s):
        # handles single & double qoutes
        #
        # FIXME
        # consider removal, should be using parameters
        # i.e. ("""SELECT * FROM test WHERE name = ?""", ('Glenn',))
        # originally created to handle single quotes in strings i.e. "O''Reilly"
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


# END: SQLiteConnection.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
