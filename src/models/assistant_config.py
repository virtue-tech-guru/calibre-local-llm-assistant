class AssistantConfig:
    
    def __init__(self,model:str, prompt:str):
        self.model = model
        self.prompt = prompt
    
    def set_model(self,model:str):
        self.model = model
        
    def get_model(self):
        return self.model    
    
    def set_prompt(self,prompt:str):
        self.prompt = prompt
        
    def get_prompt(self):
        return self.prompt