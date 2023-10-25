# pylint: disable=redefined-outer-name
import time
from pathlib import Path

import pytest
import requests
from requests.exceptions import ConnectionError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from algo_wallet_watcher.Infrastructure.orm_mapper.orm import metadata, start_mappers
from algo_wallet_watcher.Infrastructure import config

from tenacity import retry, stop_after_delay

pytest.register_assert_rewrite("tests.e2e.test_api")

@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)


@pytest.fixture
def mappers():
    start_mappers()
    yield
    clear_mappers()


@retry(stop=stop_after_delay(10))
def wait_for_postgres_to_come_up(engine):
    return engine.connect()


@retry(stop=stop_after_delay(10))
def wait_for_webapp_to_come_up():
    return requests.get(config.get_api_url())


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()
    
    
@pytest.fixture
def session(session_factory):
    return session_factory()

def wait_for_webapp_to_come_up():
    deadline = time.time() + 10
    url = config.get_api_url()
    while time.time() < deadline:
        try:
            return requests.get(url)
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail("API never came up")
    
@pytest.fixture
def restart_api():
    (Path(__file__).parent / "../src/algo_wallet_watcher/api/endpoints/app.py").touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up()
