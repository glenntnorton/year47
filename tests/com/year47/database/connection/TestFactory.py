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
from com.year47.database.connection import Factory

class TestFactory(unittest.TestCase):
    
    def setUp(self):
        self.factory = Factory.Factory()


    def test_getConnection(self):
        with self.assertRaises(NotImplementedError):
            self.factory.getConnection('foo')
        
    
    def tearDown(self):
        del self.factory


if __name__ == '__main__':
    unittest.main()


# END: TestFactory.py
# vim: set ai tw=79 sw=4 sts=4 set ft=python # 
