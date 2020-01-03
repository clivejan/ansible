from nose.tools import assert_equals, assert_false, assert_true

import imp
imp.load_source("check_user", "check_user_final.py")
from check_user import User

def test_check_user_positive():
    chkusr = User("root")
    success, ret_msg = chkusr.check_if_user_exists()
    assert_true(success)
    assert_equals('User root exists', ret_msg)
def test_check_user_negative():
    chkusr = User("twice")
    success, ret_msg = chkusr.check_if_user_exists()
    assert_false(success)
    assert_equals('User twice does not exist', ret_msg)
