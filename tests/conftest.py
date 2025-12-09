import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from app.main import app
from app.db import get_db, Base # Base must be imported shouldn't create here because models in the code are using app.db.Base


# db url has to be local not the docker one
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/test_products_db",
    future=True
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


# this runs before every test
@pytest.fixture(autouse=True)
def clean_db(session: Session):
    # we must delete child tables before parent tables
    # parent tables come before child tables
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()


@pytest.fixture(name="session")
def session_fixture():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session

    app.dependency_overrides[get_db] = get_session_override  

    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()  
