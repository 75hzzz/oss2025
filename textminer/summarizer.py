from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize

def extract_keywords(text: str, top_n=5) -> list:
    """
    TF-IDF를 사용하여 핵심 키워드를 추출합니다.
    
    Args:
        text (str): 분석할 텍스트
        top_n (int): 추출할 키워드 수
    
    Returns:
        list: 키워드와 점수의 튜플 리스트
    """
    # 구현 생략...

def summarize(text: str, ratio=0.2) -> str:
    """
    텍스트를 요약합니다.
    
    Args:
        text (str): 요약할 텍스트
        ratio (float): 요약 비율 (0.0-1.0)
    
    Returns:
        str: 요약된 텍스트
    """
    # 구현 생략...
