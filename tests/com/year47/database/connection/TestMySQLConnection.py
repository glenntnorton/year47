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
from com.year47.database.connection import MySQLConnection


class TestMySQLConnection(unittest.TestCase):

    def setUp(self):
        self.mysql_connection = MySQLConnection.MySQLConnection()



    def test_setHost(self):
        self.mysql_connection.setHost('localhost')
        self.assertEqual(self.mysql_connection.host, 'localhost')


    def test_setUser(self):
        self.mysql_connection.setUser('y47test')
        self.assertEqual(self.mysql_connection.user, 'y47test')


    def test_setPasswd(self):
        self.mysql_connection.setPasswd('y47test')
        self.assertEqual(self.mysql_connection.passwd, 'y47test')


    def test_setDb(self):
        self.mysql_connection.setDb('y47test')
        self.assertEqual(self.mysql_connection.db, 'y47test')


    def test_setAutoCommit(self):
        self.mysql_connection.setAutocommit(1)
        self.assertEqual(self.mysql_connection.autocommit, 1)


    def test_connect(self):
        self.mysql_connection.setHost('localhost')
        self.mysql_connection.setUser('y47test')
        self.mysql_connection.setPasswd('y47test')
        self.mysql_connection.setDb('y47test')
        self.mysql_connection.setAutocommit(1)

        self._mysql_dbh = self.mysql_connection.connect()

        self.assertTrue('_mysql.connection' in repr(self._mysql_dbh))
        self.assertEqual(self._mysql_dbh._transactional, 1)
        self.assertEqual(self._mysql_dbh.get_host_info(), 'Localhost via UNIX socket')
    

    def tearDown(self):
        del self.mysql_connection


if __name__ == '__main__':
    unittest.main()


# END: TestMySQLConnection.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
