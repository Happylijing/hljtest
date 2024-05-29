# -*- coding: utf-8 -*-
# @Time:2024/5/28 14:35
# @Author：huanglijing


import unittest


# 被测方法
class Search:
    def search_fun(self):
        print("search")
        return True


# 测试类
class TestSearch(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("set up class")
    #     cls.search = Search()
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("tear dowm class")

    def setUp(self) -> None:
        print("set up")
        self.search = Search()

    def tearDown(self) -> None:
        print("tear down")

    def test_search1(self):
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()


class TestSearch1(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("set up class")
    #     cls.search = Search()
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("tear dowm class")

    def setUp(self) -> None:
        print("set up class1")
        self.search = Search()

    def tearDown(self) -> None:
        print("tear down class1")

    def test_search1(self):
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()

    # def test_equal(self):
    #     print("断言相等")
    #     self.assertEqual(1, 1, "判断 1== 1")
    #
    # def test_notequal(self):
    #     print("断言不相等")
    #     self.assertNotEqual(1, 1, "判断1 ！=2")


if __name__ == '__main__':
    # 方法一：执行当前文件所有的unittest测试用例
    # unittest.main()

    # 方法二：执行指定的测试用例,将要执行的用例添加到测试套件里面，批量执行
    # 创建一个测试套件，testsuite
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch1("test_search1"))
    # suite.addTest(TestSearch1("test_search2"))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类,将测试类添加到测试套件里面，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
