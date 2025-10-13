import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://iot:iot123@mysql:3306/iotdb"

# Retry loop para esperar o MySQL estar pronto
while True:
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("MySQL pronto! Conectando...")
        break
    except Exception as e:
        print("MySQL não pronto, tentando novamente em 5s...")
        print(e)
        time.sleep(5)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
