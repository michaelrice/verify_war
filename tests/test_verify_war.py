"""
Written by Michael Rice
Github: https://github.com/michaelrice
Website: https://michaelrice.github.io/
Blog: http://www.errr-online.com/
This code has been released under the terms of the MIT licenses
http://opensource.org/licenses/MIT
"""
__author__ = 'michael rice <michael@michaelrice.org>'

import sys
sys.path.append('../')
if sys.version_info[:3] < (2, 7, 0):
    import unittest2 as unittest
else:
    import unittest
import verify_war


class TestVerifyWar(unittest.TestCase):
    def setUp(self):
        pass

    def test_verify_war(self):
        self.assertRaises(verify_war.FileNotFoundException,
                          verify_war.find_config,
                          war_file="Bad")

        self.assertRaises(verify_war.InvalidFileFormat,
                          verify_war.find_config,
                          war_file="/etc/passwd")

        self.assertRaises(verify_war.FileNotFoundException,
                          verify_war.find_config,
                          war_file="./data/bad/bad.zip")

        self.assertTrue(verify_war.find_config(war_file="./data/good/good.zip") is None)