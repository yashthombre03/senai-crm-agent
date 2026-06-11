from pydantic import BaseModel
from datetime import datetime

class EmailSchema(BaseModel):

    message_id: str

    sender: str

    subject: str

    body: str

    timestamp: datetime

    thread_id: str