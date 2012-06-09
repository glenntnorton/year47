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
from com.year47.database.connection import OracleConnection


class TestOracleConnection(unittest.TestCase):

    def setUp(self):
        self.oracle_connection = OracleConnection.OracleConnection()


    def test_setUsername(self):
        self.oracle_connection.setUsername('y47test')
        self.assertEqual(self.oracle_connection.username, 'y47test')


    def test_setPasswd(self):
        self.oracle_connection.setPasswd('y47test')
        self.assertEqual(self.oracle_connection.passwd, 'y47test')


    def test_setIPAddress(self):
        self.oracle_connection.setIPAddress('127.0.0.1')
        self.assertEqual(self.oracle_connection.ip_address, '127.0.0.1')


    def test_setSID(self):
        self.oracle_connection.setSID('xe')
        self.assertEqual(self.oracle_connection.sid, 'xe')


    def test_setAutoCommit(self):
        self.oracle_connection.setAutocommit(1)
        self.assertEqual(self.oracle_connection.autocommit, 1)


    def test_connect(self):
        self.oracle_connection.setUsername('y47test')
        self.oracle_connection.setPasswd('y47test')
        self.oracle_connection.setIPAddress('127.0.0.1')
        self.oracle_connection.setSID('xe')
        self.oracle_connection.setAutocommit(1)

        self.connection_string = "%s/%s@%s/%s" % (
            self.oracle_connection.username,
            self.oracle_connection.passwd,
            self.oracle_connection.ip_address,
            self.oracle_connection.sid
        )
        self._oracle_dbh = self.oracle_connection.connect()
        self._oracle_dbh.autocommit = self.oracle_connection.autocommit


        self.assertTrue('cx_Oracle.Connection' in repr(self._oracle_dbh))
        self.assertEqual(self._oracle_dbh.autocommit, 1)
        self.assertEqual(self._oracle_dbh.dsn, '127.0.0.1/xe')
    

    def tearDown(self):
        del self.oracle_connection


if __name__ == '__main__':
    unittest.main()


# END: OracleConnection.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
