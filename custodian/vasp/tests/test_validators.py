from custodian.vasp.validators import VasprunXMLValidator

import os
import unittest

test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                        'test_files')
cwd = os.getcwd()

class VasprunXMLValidatorTest(unittest.TestCase):

    def test_check_and_correct(self):
        os.chdir(os.path.join(test_dir, "bad_vasprun"))
        h = VasprunXMLValidator()
        self.assertTrue(h.check())

        #Unconverged still has a valid vasprun.
        os.chdir(os.path.join(test_dir, "unconverged"))
        self.assertFalse(h.check())

    @classmethod
    def tearDownClass(cls):
        os.chdir(cwd)
