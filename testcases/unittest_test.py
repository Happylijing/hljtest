# -*- coding: utf-8 -*-
# @Time:2024/5/28 14:18
# @Author：huanglijing

import unittest


class TestStringMethods(unittest.TestCase):

    # setUp tearDown 方法是在每条用例的前分别调用的方法
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tearDown")

    # setUpClass 和 tearDownClass是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_abc(self):
        print('test_abc')


if __name__ == '__main__':
    unittest.main()
