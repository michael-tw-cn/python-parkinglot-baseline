#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover('./','*_test.py')
    for case in all_cases:
        suite.addTests(case)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)