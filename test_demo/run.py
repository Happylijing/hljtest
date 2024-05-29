# -*- coding: utf-8 -*-
# @Time:2024/5/28 15:25
# @Author：huanglijing

import unittest

if __name__ == '__main__':
    testdir = "./testcases"
    discover = unittest.defaultTestLoader.discover(testdir, pattern="test_*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)
