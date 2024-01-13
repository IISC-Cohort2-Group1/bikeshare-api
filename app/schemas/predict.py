from typing import Any, List, Optional

from pydantic import BaseModel
from bikeshare_model.processing.validation import DataInputSchema
from datetime import datetime


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    # predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "dteday":datetime(2012, 11, 10),
                        "season": 'winter',
                        "hr": '6am',
                        "holiday": 'No',
                        "weekday": "Mon",
                        "workingday": 'Yes',
                        "weathersit": 'Mist',
                        "temp": 6.1,
                        "atemp": 3.23,
                        "hum": 49,
                        "windspeed": 19,
                        "casual":4,
                        "registered":136,
                    }
                ]
            }
        }