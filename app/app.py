from fastapi import FastAPI, Depends
from database import get_db, engine
from datetime import datetime
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
	allow_headers=["*"],
    max_age=3600,
)

IP_ITBA = "181.165.98.149"

@app.get("/")
def front():
    return {'message': 'Hello World!'}

@app.post("/presente/{legajo}")
def guardar_presente(legajo: int, ip: str, db: Session = Depends(get_db)):
    if ip != IP_ITBA:
        return False
    existe = db.query(models.Presente).filter(models.Presente.legajo == legajo, models.Presente.fecha.date() == datetime.today().date()).first()
    if existe:
        return False
    db_presente = models.Presente(legajo=legajo, fecha=datetime.now())
    db.add(db_presente)
    db.commit()
    return True
