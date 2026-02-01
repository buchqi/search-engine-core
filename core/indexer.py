"""inverted indexer for search engine,
it should build inverted index:word->set of document IDs,t
rak term frequency per document for ranking later"""

class Indexer:
    def __init__(self):
        #dict of inverted indexes
        self.inverted_index = {}
        #Term frecuencies doc_id:{word:count}
        self.term_freqs = {}
        
    def add_document(self,doc_id:int,tokens: list[str]):
        """Add document to the index"""
        #update inverted_index for each toke
        
        if doc_id not in self.term_freqs:
            self.term_freqs[doc_id] = {}
        
        for token in tokens:
            if token in self.inverted_index:
                self.inverted_index[token].add(doc_id)
            else:
                self.inverted_index[token] = {doc_id}
        
            if token in self.term_freqs[doc_id]:
                self.term_freqs[doc_id][token] +=1
            else:
                self.term_freqs[doc_id][token] = 1
    def get_docs(self,term:str):
        
        return self.inverted_index.get(term,set())
        