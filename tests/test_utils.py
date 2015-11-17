# -*- coding: utf-8 -*-

"""
    Test ramlient.utils module.
"""

from unittest import TestCase
from sure import expect

from ramlient import utils


class TestUtils(TestCase):
    """
        Test utils module
    """
    def test_download_existing_url(self):
        """
            Test downloading an existing file from an URL
        """
        testurl = "https://raw.githubusercontent.com/timofurrer/testfiles/master/awesome"
        expect(utils.download_file(testurl).strip()).to.be.equal("Awesome!")

    def test_download_notexisting_url(self):
        """
            Test downloading a not existing file from an URL
        """
        testurl = "https://raw.githubusercontent.com/timofurrer/testfiles/master/doesnotexist"
        expect(utils.download_file(testurl)).to.be.none

    def test_is_url_function(self):
        """
            Test if "is_url" function works
        """
        expect(utils.is_url("http://foo.com")).to.be.true
        expect(utils.is_url("/usr/bin")).to.be.false
