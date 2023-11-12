from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ram import User

engine=create_engine('sqlite:///ram.db')
