from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# echo - debugging not good for production
# future - enables sqlalchemy 2.0
engine = create_engine(settings.database_url, echo=False, future=True)

# will be used to create a conversation with db per req
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

# will be used by models to be managed by ORM
Base = declarative_base()

# will be used for dependecy injection
# TODO need to know the exact working of this
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()