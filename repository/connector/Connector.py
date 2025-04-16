from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Conector del ORM con la DB. No tocar ni por el ptas
"""
print("Cargando SQLALCHEMY")
Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres.ywswwkqspwwewemckxsx:PDw2EVsDIg2uZtzf@aws-0-us-east-2.pooler.supabase.com:6543/postgres')

SessionLocal = sessionmaker(autocommit=False, bind=engine)
print("Estableciendo conexion con DB")
Base.metadata.create_all(engine)
