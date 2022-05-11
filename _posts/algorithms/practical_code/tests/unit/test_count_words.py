import unittest

from count_words_new import CountWords

class TestSum(unittest.TestCase):

    def test_count_words(self):
        driver=CountWords("words1.txt")
        result=driver.DoIt()    
        self.assertEqual(result,[('vinayak', 1)])


if __name__ == '__main__':
    unittest.main()