class UserQuery:
    def __init__(self):
        self.query = None
    
    def set_query(self,query):
        self.query = query
        
    def get_query(self):
        return self.query