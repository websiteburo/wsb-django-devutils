# -*- coding:utf-8 -*-

from django.test.simple import reorder_suite, build_test, build_suite
from django.db.models import get_apps, get_app
from django.test.testcases import TestCase
import unittest
from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner

    

class IgnoreTestSuiteRunner(DjangoTestSuiteRunner):
    
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = unittest.TestSuite()

        if test_labels:
            for label in test_labels:
                if '.' in label:
                    suite.addTest(build_test(label))
                else:
                    app = get_app(label)
                    suite.addTest(build_suite(app))
        else:
            # Get ignored app
            ignored_apps_names = getattr(settings, "IGNORE_APP_TESTS", ())
            ignored_apps = [
                get_app(app_.split(".")[-1]) for app_ in ignored_apps_names
                ]
            for app in get_apps():
                if app not in ignored_apps:
                    suite.addTest(build_suite(app))
        return reorder_suite(suite, (TestCase,))
