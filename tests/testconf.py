import pytest

import sys  # isort:skip

sys.path.append("src")
# sys.path.append("/Users/v/code/nikita/aika-mail/src")
from src import main


@pytest.fixture
def client():
    with main.app.test_client() as client:
        yield client


#

#
