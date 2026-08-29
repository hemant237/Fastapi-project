import pytest
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
load_dotenv()

TEST_DATABASE_URL=os.getenv("TEST_DATABASE_URL")

test_engine=create_engine(TEST_DATABASE_URL)

TestingSessionLocal=sessionmaker(bind=test_engine,autoflush=False,autocommit=False)


@pytest.fixture
def db():
    db=TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()    