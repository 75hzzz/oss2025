import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def remove_stopwords(text: str, lang='en') -> str:
    """
    텍스트에서 불용어를 제거합니다.
    
    Args:
        text (str): 처리할 텍스트
        lang (str): 언어 코드 (기본값: 'en')
    
    Returns:
        str: 불용어가 제거된 텍스트
    """
    try:
        # NLTK 데이터 다운로드 (필요한 경우)
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt', quiet=True)
        
        # 토큰화
        tokens = word_tokenize(text.lower())
        
        # 불용어 목록 가져오기
        stop_words = set(stopwords.words(lang))
        
        # 불용어 및 구두점 제거
        filtered_tokens = [
            token for token in tokens 
            if token not in stop_words and token not in string.punctuation
        ]
        
        return ' '.join(filtered_tokens)
    
    except Exception as e:
        raise ValueError(f"불용어 제거 중 오류 발생: {str(e)}")
