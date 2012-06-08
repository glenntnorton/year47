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

import unittest
from com.year47.database.connection import SQLiteConnection


# import pysqlite or sqlite3
try:
    import sqlite
except ImportError:
    import sqlite3 as sqlite


class TestSQLiteConnection(unittest.TestCase):

    def setUp(self):
        self.sqlite_connection = SQLiteConnection.SQLiteConnection()


    def test_connect_to_file(self):
        self.filename = 'test.db'
        self.db = self.sqlite_connection.connect(self.filename)
        self.assertTrue('Connection' in repr(self.db))


    def test_connect_to_memory(self):
        self.db = self.sqlite_connection.connect(':memory')
        self.assertTrue('Connection' in repr(self.db))


    def test_getExceptionHandler(self):
        self.filename = 'test.db'
        self.db = self.sqlite_connection.connect(self.filename)
        self.handler = self.sqlite_connection.getExceptionHandler()
        self.assertTrue('DatabaseError' in repr(self.handler))


    def test_getQouteHandler(self):
        self.filename = 'test.db'
        self.db = self.sqlite_connection.connect(self.filename)
        self.handler = self.sqlite_connection.getQuoteHandler()
        self.assertTrue('_quoteHandler' in repr(self.handler))


    def tearDown(self):
        del self.sqlite_connection


if __name__ == '__main__':
    unittest.main()


# END: SQLiteConnection.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
