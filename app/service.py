class Service:
 def __init__(self): self.n=0
 def run(self,value): self.n+=1; return {'session_id':f'session-{self.n}','transcript':value,'next':'tool_or_response','handoff_available':True}