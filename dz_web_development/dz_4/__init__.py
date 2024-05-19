from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine(
    url='mysql+pymysql://root:root@localhost:3306/dz_4'
)

Base = declarative_base()