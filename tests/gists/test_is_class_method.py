import unittest
import pytest
from scripts.gists.is_class_method import Cat



class TestCat(unittest.TestCase):
    
    def setUp(self):
        """ Executed before every test case """
        self.test_obj = Cat(name="Git", age=7)
        self.from_cat_years = Cat.from_cat_years(name="Jit", cat_years=49)
        
    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result: ")
        
    def test_purr_cls_method(self):
        self.assertEqual(self.test_obj.purr(), "meow")        
        self.assertEqual(self.from_cat_years.purr(), "meow")

    def test_init_ok(self):
        assert self.test_obj.name == "Git"
        assert self.test_obj.age == 7
        
        assert self.from_cat_years.name == "Jit"
        assert self.from_cat_years.age == 7
        
    def test_class_type(self):
        # no assert if use self.assert...
        # assert True == isinstance(self.test_obj, Cat)
        self.assertIsInstance(self.test_obj, Cat)
        self.assertIsInstance(self.from_cat_years, Cat)


# Execute all the tests when the file is executed
if __name__ == "__main__":
    unittest.main()
