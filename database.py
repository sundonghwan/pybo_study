
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlite database 세팅 Author: 선동환 modify: 2023-10-23
SQLALCHEMY_DATABASE_URL = "sqlite:///./pybo.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Depends api를 활용하여 contextlib.contextmanager 데코레이터 제거 Author: 선동환 modify: 2023-10-24
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()