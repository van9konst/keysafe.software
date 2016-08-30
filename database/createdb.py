from sqlalchemy import create_engine
from models import User, Key, UserKeyLink, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe')

session = sessionmaker()
session.configure(bind=engine)

Base.metadata.create_all(engine)

print 'Databese created'
