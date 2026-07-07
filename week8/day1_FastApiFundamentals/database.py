from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:Gnani%402005@localhost:5432/telusko"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)