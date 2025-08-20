from pydantic import BaseModel

class AgentResponse(BaseModel):
    agent_name: str
    discuss_round: int
    scratchpad: str
    speech: str
    vote: str