import os
import tempfile

import pytest
from blog.models import ArticleManager


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    ArticleManager.create_table(database_name=file_name)
    yield
    try:
        os.unlink(file_name)
    except PermissionError as e:
        print(e)
