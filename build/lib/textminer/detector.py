from langdetect import detect, detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# 일관된 결과를 위해 시드 설정
DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    """
    텍스트의 언어를 감지합니다.
    
    Args:
        text (str): 언어를 감지할 텍스트
    
    Returns:
        str: 언어 코드 (예: 'en', 'ko', 'fr')
    """
    # 구현 생략...

def detect_languages_with_probability(text: str) -> list:
    """
    텍스트의 언어를 확률과 함께 감지합니다.
    
    Args:
        text (str): 언어를 감지할 텍스트
    
    Returns:
        list: (언어코드, 확률) 튜플의 리스트
    """
    # 구현 생략...
