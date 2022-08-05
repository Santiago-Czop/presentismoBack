from fastapi import FastAPI, Depends
from database import get_db, engine
from datetime import datetime
from sqlalchemy.orm import Session
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

IP_ITBA = "" # TODO Llenar con dato de mamá

@app.get("/")
def front():
    return {'message': 'Hello World!'}

@app.post("/presente/{legajo}")
def guardar_presente(legajo: int, ip: str, db: Session = Depends(get_db)):
    if ip != IP_ITBA:
        return False
    db_presente = models.Presente(legajo=legajo, fecha=datetime.now())
    db.add(db_presente)
    db.commit()
    return True
