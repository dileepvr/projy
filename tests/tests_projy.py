# -*- coding: utf-8 -*-
""" Test suite for the utils.py file. """

# system
import os
import sys
# projy
from projy.cmdline import execute
# nose
from nose.tools import with_setup
from nose.tools import raises
from nose.tools import assert_equal
from nose.tools import assert_not_equal


@SystemExit
def test_info():
    sys.argv = ['projy', '-i']
    execute()




