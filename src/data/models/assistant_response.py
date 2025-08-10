class AssistantResponse:
    def __init__(self):
        self.response = None
    
    def set_response(self,response):
        self.response = response
        
    def get_response(self):
        return self.response