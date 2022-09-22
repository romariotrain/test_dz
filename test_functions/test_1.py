from main import *
import unittest


class Test_function(unittest.TestCase):
    def test_get_doc_owner_name(self):
        etalon = 'Аристарх Павлов'
        result = get_doc_owner_name('10006')
        self.assertEqual(etalon, result)


    def test_get_doc_shelf(self):
        etalon = '2'
        result = get_doc_shelf('10006')
        self.assertEqual(etalon, result)


    def test_add_new_doc(self):
        add_new_doc('123', 'passport', 'roman', '6')
        self.assertIn('6', directories)

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf('11-2')
        self.assertNotIn('11-2', directories['1'])








