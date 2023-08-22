from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating:float = Field(ge=1, le=10)
    category:str = Field(min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'id': 1,
                    'title': 'Modelo',
                    'overview': "Esta es una descripcion",
                    'year': 2023,
                    'rating': 10,
                    'category': 'Acción'
                }
            ]
        }
    }
