from urllib.parse import quote_plus

class URLBuilder:

    def __init__(self, base:str):
        self.base = base.lower()

    def __quote_str__(self, text):
        return quote_plus(text)
    
    def vacancy(self, vacancy):
        self.vacancy = f"&{vacancy}"
        return self
    
    def build(self) -> str:
        return f"{self.base}{self.vacancy}"
    

