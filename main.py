from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/about')
def about():
    return {"A propos": "welecome to Celluloid API",
            "Objectif":"Annotation tool",
            "Technologies": "Python",
            "DataBase": "Noe4j"
            }
# Get Annotation
@app.get('/annotation')
def annotation():
    return [{"id":"1","Instance":"Smile","Start Time":"1:02","Stop Time":"1:20","Utilisateur":"Cécile","Projet":"Test"},
             {"id":"2","Instance":"Laugh","Start Time":"2:02","Stop Time":"2:11","User":"Fatiha","Project":"Test"}
            ]

# Get Annotation by id
@app.get('/annotation/{id}')
def annotationById(id: int):
    return {"id":id
                # {"id": "1", "Instance": "Smile", "Start Time": "1:02", "Stop Time": "1:20", "Utilisateur": "Cécile",
                 # "Projet": "Test"},


    }
#Creation of annotation
class Annotation(BaseModel):
    id: int
    instance: str
    text: Optional[str] = None
    startTime: str
    stopTime: str
    user: str
    project: str
@app.post('/create_annotation')
def CreateAnnotation(annotation: Annotation):
    return {"annotation": f"annotation created with{annotation.instance}"}
