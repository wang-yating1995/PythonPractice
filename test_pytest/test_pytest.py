import pytest
import yaml
import os
import sys

def setup_module():
    print("setup module")
def teardown_module():
    print("teardown module")
def setup_function():
    print("setup_function")
def teardown_function():
    print("teardown_function")

def test_case01():
    print("case01")

def test_case02():
    print("case02")

class Test_Demo():

    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def setup_method(self):
        print("setup_method")
    def setup(self):
        print("setup")
    def teardown_method(self):
        print("teardown_method")
    def teardown(self):
        print("teardown")
    a = 1
    @pytest.mark.xfail()
    def test_case03(self):
        print("case03")
        # self.test_case04()

    @pytest.mark.parametrize("aa", yaml.safe_load(open("test_pytest/data.yml",encoding='utf-8')))
    def test_login1(self,aa):
        # sum = aa + bb
        print(aa)

if __name__ == '__main__':
    pytest.main('-v -s')
    # Test_Demo().test_case04()