from typing import List, Union
from pydantic import BaseModel

class Job(BaseModel):
        id:int
        job:str

        class Config:
            orm_mode = True