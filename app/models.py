from typing import Optional

from pydantic import BaseModel


class Idx(BaseModel):
    name: str
    txt_field: str
    bucket_field: Optional[str] = None
    json_schema: str

    class Config:
        schema_extra = {
            "example": {
                "name": "talk",
                "txt_field": "content",
                "bucket_field": "talk-type",
                "json_schema": """{
                    'title': 'talk',
                    'type': 'object',
                    'properties': {
                        'id': { 'type': 'string', 'description': 'The id of a talk' },
                        'start': {'type': 'float', 'description': 'Start of audio segment'},
                        'end': {'type': 'float', 'description': 'End of audio segment'},
                        'year': {'type': 'int', 'description': 'Year the talk was held'},
                        'speaker': { 'type': 'string', 'description': 'The name of the speaker' },
                        'content': { 'type': 'string', 'description': 'The content of a talk' },
                        'talk-type': { 'type': 'string', 'description': 'The host that published this talk' }
                    }
                }""",
            }
        }


class Item(BaseModel):
    id: str

    class Config:
        extra = "allow"
        schema_extra = {
            "example": {
                "id": "1bda8b6e-8408-11eb-8dcd-0242ac130003",
                "start": 0.0,
                "end": 20.400000000000002,
                "year": 2008,
                "speaker": "Craig Venter",
                "content": "A very long speech on super interesting stuff.",
                "talk-type": "ted",
            }
        }


class Qry(BaseModel):
    query: str
    bucket: Optional[str] = None
    limit: int

    class Config:
        schema_extra = {
            "example": {
                "query": "Some text that might match an existing item.",
                "bucket": "ted",
                "limit": 200,
            }
        }


class ResponseItem(BaseModel):
    item: Item
    embedding: list

    class Config:
        schema_extra = {
            "example": {
                "item": {
                    "id": "1bda8b6e-8408-11eb-8dcd-0242ac130003",
                    "start": 0.0,
                    "end": 20.400000000000002,
                    "year": 2008,
                    "speaker": "Craig Venter",
                    "content": "A very long speech on super interesting stuff.",
                    "talk-type": "ted",
                },
                "embedding": [0, 0, 0, 0, 0, 0],
            }
        }
