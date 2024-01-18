class Config:
    def __init__(self, ranking='tfidf', query_type='OR', test=False):
        self.use_compression = True
        self.ranking = ranking
        self.query_type = query_type
        self.test = test
