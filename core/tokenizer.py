"""implementing class tokenizer main purupuse convert strings into lists 
e.g INPUT: 'Python, JAVA!! is great for data-analysis.' 
OUTPUT:["python", "java", "great", "data", "analysis"]"""
import string

class Tokenizer:
    STOPWORDS = {"the", "is", "and", "for", "to", "a", "of"}
    def __init__(self):
        pass
    
    #remove all punctuations from the text
    def _remove_punctuation(self,text):
        clean_text = "".join(c for c in text if c not in string.punctuation)
        return clean_text
    #split text into list of tokens        
    def _split_into_tokens(self,text):
        tokens = text.split()
        return tokens
    #normilize tokens now return lowercase words
    def _normalize(self,tokens):
        normilized_tokens = []
        for word in tokens:
            normilized_tokens.append(word.lower())
        return normilized_tokens
    #clear out the tokens from stopwrods for more efficienty
    def _remove_stopwords(self,tokens):
        return [t for t in tokens if t not in self.STOPWORDS]
        
    def tokenize(self,text: str):
        text_clear = self._remove_punctuation(text)
        tokens = self._split_into_tokens(text_clear)
        tokens = self._normalize(tokens)
        tokens = self._remove_stopwords(tokens)
        
        return tokens
    
