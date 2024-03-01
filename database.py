import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:Kstech070@localhost/ExploreDev'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()