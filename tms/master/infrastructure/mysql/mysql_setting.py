from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

user_name = "tmsuser"
password = "tmsuser"
host = "localhost"
database_name = "tms"


DATABASE = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (
    user_name,
    password,
    host,
    database_name
)

ENGINE = create_engine(
    DATABASE,
    echo=True
)

session = scoped_session(
    sessionmaker(
            autocommit=True,
            autoflush=True,
            bind=ENGINE
        )
)
Base = declarative_base()
Base.query = session.query_property()
