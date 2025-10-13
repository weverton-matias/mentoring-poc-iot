from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from models import SensorData
from mqtt_handler import start_mqtt

app = FastAPI(title="IoT FastAPI - pH Sensor")

# Cria tabelas se não existirem
Base.metadata.create_all(bind=engine)

# Inicia listener MQTT
start_mqtt()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/data")
def get_data(db: Session = Depends(get_db)):
    return db.query(SensorData).order_by(SensorData.timestamp.desc()).all()
