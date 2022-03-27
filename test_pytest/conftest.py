import pytest

@pytest.fixture(scope='function')
def login():
    print("登录方法")
    yield
    print("退出")





