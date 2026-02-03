"""inverted indexer for search engine,
it should build inverted index:word->set of document IDs,t
rak term frequency per document for ranking later"""

class Indexer:
    def __init__(self):
        #dict of inverted indexes
        self.inverted_index = {}
        #Term frecuencies doc_id:{word:count}
        self.term_freqs = {}
        
    def _add_document(self,doc_id:int,tokens: list[str]):
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
    def _get_docs(self,term:str):
        """it should return set of document ids where term word is found"""
        return self.inverted_index.get(term,set())
    def _rank_docs(self,doc_id:set[int],tokens:set[str]):
        """it should return ranked list of documents,after getting do_id's where list of tokens appeared"""
        ranking = []
        for ID in doc_id:
            score = 0
            for token in tokens:
                score += self.term_freqs[ID].get(token,0)
            if score >0:
                ranking.append({"doc_id":ID,"score":score})
        #sort by descending order 
        ranking.sort(key = lambda x: -x["score"])                 
        return ranking
        
    
    def search(query:str,mode = "AND"):
       pass
        
indexer = Indexer()
indexer._add_document(1,['apple','orange','python',])
indexer._add_document(2,['orange','python','apple','apple'])
indexer._rank_docs({1,2}, {'apple'})
