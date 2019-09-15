from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root@localhost/cheep', echo=True)
Session = sessionmaker(bind=engine)
