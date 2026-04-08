import re
from dataclasses import dataclass

@dataclass
class TextCleaner:
    """Basic NLP-style text cleaning utility."""

    def clean(self, text: str) -> str:
        # remove non-alphanumeric + lowercase normalization
        return re.sub(r'[^a-zA-Z0-9]', '', text).lower()


class PalindromeAnalyzer:
    """Analyzes whether cleaned text is a palindrome."""

    def __init__(self):
        self.cleaner = TextCleaner()

    def is_palindrome(self, text: str) -> bool:
        clean_text = self.cleaner.clean(text)
        return clean_text == clean_text[::-1]

    def explain(self, text: str) -> dict:
        clean_text = self.cleaner.clean(text)
        return {
            "original": text,
            "cleaned": clean_text,
            "is_palindrome": clean_text == clean_text[::-1],
            "length": len(clean_text)
        }


# ---------------- TEST ----------------
analyzer = PalindromeAnalyzer()

print(analyzer.is_palindrome("A sadad''dsad@sdsa"))

print(analyzer.explain("Was it a car or a cat I saw?"))