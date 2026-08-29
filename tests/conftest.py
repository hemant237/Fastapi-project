import pytest
import os

from app.main import app

from app.models.user import User
from app.core.security import hash_password

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base ,get_db
load_dotenv()

TEST_DATABASE_URL=os.getenv("TEST_DATABASE_URL")

test_engine=create_engine(TEST_DATABASE_URL)

TestingSessionLocal=sessionmaker(bind=test_engine,autoflush=False,autocommit=False)


@pytest.fixture
def db():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    db=TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()    


def override_get_db():
    db=TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db]=override_get_db        


@pytest.fixture(scope="session",autouse=True)
def setup_database():
    Base.metadata.create_all(bind=test_engine)

    yield

    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def test_user(db):
    user = User(
        email="loginuser@gmail.com",
        password_hash=hash_password("password123")
    )    
    db.add(user)
    db.commit()
    db.refresh(user)

    return user