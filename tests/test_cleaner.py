import unittest
from textminer.cleaner import remove_stopwords

class TestCleaner(unittest.TestCase):
    def test_remove_stopwords_english(self):
        # 영어 텍스트 테스트
        text = "This is a test sentence with some stopwords."
        result = remove_stopwords(text)
        
        # 불용어가 제거되었는지 확인
        self.assertNotIn("this", result)
        self.assertNotIn("is", result)
        self.assertNotIn("a", result)
        self.assertNotIn("with", result)
        self.assertNotIn("some", result)
        
        # 중요 단어는 유지되었는지 확인
        self.assertIn("test", result)
        self.assertIn("sentence", result)
        self.assertIn("stopwords", result)
    
    # 다른 테스트 케이스들...
