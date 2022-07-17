'''
This module test the translator module
'''
import unittest
import sys

sys.path.insert(0, "/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/")

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    '''
    This class test the english_to_french method from translator module
    '''
    def test_e2f(self):
        '''
        Test english_to_french method by passing three tests word: "yes", "hello", and "bread"
        Also test if ValueError is raised when method is feed with null as argument
        '''
        self.assertEqual(english_to_french("yes"), "Oui")
        self.assertEqual(english_to_french("hello"), "Bonjour")
        self.assertNotEqual(english_to_french("bread"), "Oui")
        #Test if ValueError is given when the input is null
        with self.assertRaises(ValueError):
            english_to_french(None)

class TestF2E(unittest.TestCase):
    '''
    This class test the french_to_english method from translator module
    '''
    def test_f2e(self):
        '''
        Test french_to_english method by passing three tests word: "oui", "bonjour", and "rouge"
        Also test if ValueError is raised when method is feed with null as argument
        '''
        #Test translation from French to English with input "oui", "bonjour", and "rouge"
        self.assertEqual(french_to_english("oui"), "Yes")
        self.assertEqual(french_to_english("bonjour"), "Hello")
        self.assertNotEqual(french_to_english("rouge"), "Blue")
        #Test if ValueError is given when the input is null
        with self.assertRaises(ValueError):
            french_to_english(None)

unittest.main()
