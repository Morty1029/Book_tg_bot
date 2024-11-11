import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def bot_token() -> str:
    return os.getenv("tg_token")


def test_bot_connection(bot_token) -> None:
    assert bot_token is not None
