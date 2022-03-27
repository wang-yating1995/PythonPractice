import unittest

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("case01")

    def test_case02(self):
        print("case02")

    def test_case03(self):
        print("case03")

class demo01(unittest.TestCase):
    def test_case04(self):
        print("case04")

    @unittest.skip("跳过case05")
    def test_case05(self):
        print("case05")

class demo02(unittest.TestCase):
    def test_case06(self):
        print("case06")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(TestCase("test_case01"))
    print(1)
    suite.addTest(demo02("test_case06"))
    unittest.TextTestRunner().run(suite)
