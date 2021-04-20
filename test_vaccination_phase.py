"""
test_vaccination_phase.py

Description:
This module contains unit tests for the vaccination_phase module. Each test case covers specific
functionality and scenarios to ensure the proper functioning of the vaccination_phase module.

Author:
[Your Name]

Date:
20/04/2021

Usage:
Run this file to execute the unit tests for the vaccination_phase module.

Note:
Make sure to have the 'unittest' and 'mock' modules installed before running the tests.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import vaccination_phase

class TestVaccinationPhase(unittest.TestCase):
    """
    A test class for the vaccination_phase module.

    This class contains test cases for various functions within the vaccination_phase module.
    Each test case focuses on specific scenarios to ensure the proper functionality of the module.
    """

    def test_determine_phase_1a(self):
        """
        Test the determine_phase_1a function.

        This test case covers scenarios where the user may or may not belong to Phase 1a.
        """
        print('\nPhase 1a test(s) starting...')
        # Test when the user is a quarantine and border worker
        with patch("builtins.input", side_effect=["yes"]):
            self.assertEqual(vaccination_phase.determine_phase_1a(), "Phase 1a")
            print('Test if the user belongs to Phase 1a')

        # Test when the user is not a quarantine and border worker
        with patch("builtins.input", side_effect=["no"]):
            self.assertEqual(vaccination_phase.determine_phase_1a(), "Not eligible for Phase 1a")
            print('Test if the user does not belong to Phase 1a')

        print('Phase 1a test(s) complete...\n')

    def test_determine_phase_1b(self):
        """
        Test the determine_phase_1b function.

        This test case covers scenarios where the user may or may not belong to Phase 1b.
        """
        print('\nPhase 1b test(s) starting...')
        # Test when the user is a health care worker
        with patch("builtins.input", side_effect=["yes"]):
            self.assertEqual(vaccination_phase.determine_phase_1b(), "Phase 1b")
            print('Test if the user belongs to Phase 1b')

        # Test when the user is not a health care worker
        with patch("builtins.input", side_effect=["no"]):
            self.assertEqual(vaccination_phase.determine_phase_1b(), "Not eligible for Phase 1b")
            print('Test if the user does not belong to Phase 1b')

        print('Phase 1b test(s) complete...\n')

    def test_indigenous_australian(self):
        """
        Test the indigenous_australian function.

        This test case covers scenarios related to users identifying as Aboriginal and/or Torres Strait Islander.
        """
        print('\nIndigenous Australian test(s) starting...')
        # Test when the user identifies as an Aboriginal and/or Torres Strait Islander person, age < 55
        with patch("builtins.input", side_effect=["yes"]):
            self.assertEqual(vaccination_phase.indigenous_australian(50), "Phase 2a")
            print('Test when the user identifies as an Aboriginal and/or Torres Strait Islander person, age < 55')

        # Test when the user identifies as an Aboriginal and/or Torres Strait Islander person, age >= 55
        with patch("builtins.input", side_effect=["yes"]):
            self.assertEqual(vaccination_phase.indigenous_australian(60), "Phase 1b")
            print('Test when the user identifies as an Aboriginal and/or Torres Strait Islander person, age >= 55')

        # Test when the user does not identify as an Aboriginal and/or Torres Strait Islander person, age >= 50
        with patch("builtins.input", side_effect=["no"]):
            self.assertEqual(vaccination_phase.indigenous_australian(55), "Phase 2a")
            print('Test when the user does not identify as an Aboriginal and/or Torres Strait Islander person, age >= 50')

        # Test when the user does not identify as an Aboriginal and/or Torres Strait Islander person, age < 50
        with patch("builtins.input", side_effect=["no"]):
            self.assertEqual(vaccination_phase.indigenous_australian(45), "Phase 2b")
            print('Test when the user does not identify as an Aboriginal and/or Torres Strait Islander person, age < 50')

        print('Indigenous Australian test(s) complete...\n')

    def test_other_category(self):
        """
        Test the other_category function.

        This test case covers scenarios related to users who may or may not be in another critical or high-risk category.
        """
        print('\nOther category test(s) starting...')
        # Test when the user is another critical or high-risk worker
        with patch("builtins.input", side_effect=["yes"]):
            self.assertEqual(vaccination_phase.other_category(60), "Phase 2a")
            print('Test when the user is another critical or high-risk worker')

        # Test when the user is not another critical or high-risk worker, age >= 50
        with patch("builtins.input", side_effect=["no"]):
            self.assertEqual(vaccination_phase.other_category(55), "Phase 2a")
            print('Test when the user is not another critical or high-risk worker, age >= 50')

        print('Other category test(s) complete...\n')

    def test_determine_phase_2(self):
        """
        Test the determine_phase_2 function.

        This test case covers scenarios related to users entering their age and determining vaccine eligibility.
        """
        print('\nPhase 2 test(s) starting...')
        # Test when the user enters a valid age and is recommended to obtain a vaccine
        with patch("builtins.input", side_effect=["12", "yes"]):
            self.assertEqual(vaccination_phase.determine_phase_2(), "Phase 3")
            print('Test when the user enters a valid age between > 0 and < 18 and is recommended to obtain a vaccine')

        # Test when the user enters a valid age and is not recommended to obtain a vaccine
        with patch("builtins.input", side_effect=["6", "no"]):
            self.assertEqual(vaccination_phase.determine_phase_2(), "not recommended")
            print('Test when the user enters a valid age between > 0 and < 18 and is not recommended to obtain a vaccine')

        # Test when the user enters an age between 18 and 69 and has an underlying medical condition or disability
        with patch("builtins.input", side_effect=["30", "yes"]):
            self.assertEqual(vaccination_phase.determine_phase_2(), "Phase 1b")
            print('Test when the user enters an age between 18 and 69 and has an underlying medical condition or disability')

        # Test when the user enters an age greater than or equal to 70
        with patch("builtins.input", side_effect=["75"]):
            self.assertEqual(vaccination_phase.determine_phase_2(), "Phase 1b")
            print('Test when the user enters an age greater than or equal to 70')

        print('Phase 2 test(s) complete...\n')

if __name__ == '__main__':
    """
    Entry point for running the test suite.

    This block checks whether the script is being run as the main program.
    If so, it invokes the test suite, initiating the execution of all test cases defined in the TestVaccinationPhase class.
    """
    unittest.main()
