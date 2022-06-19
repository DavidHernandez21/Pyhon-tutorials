import json
import pathlib
from typing import Dict

import pytest
from jsonschema import RefResolver
from jsonschema import validate

from blog.app import app
from blog.models import ArticleManager


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def validate_payload(payload: Dict, schema_name: str):
    """
    Validate payload with selected schema
    """
    schemas_dir = pathlib.Path(pathlib.Path(__file__).parent.absolute(), "schemas")
    schema = json.loads(pathlib.Path(schemas_dir,schema_name).read_text())
    # print(f"file://{str(pathlib.Path(schemas_dir, schema_name).absolute())}")
    validate(
        payload,
        schema,
        resolver=RefResolver(
            f"file://{str(pathlib.Path(schemas_dir, schema_name).absolute())}",
            schema  # it's used to resolve the file inside schemas correctly
        )
    )


def test_create_article(client):
    """
    GIVEN request data for new article
    WHEN endpoint /create-article/ is called
    THEN it should return Article in json format that matches the schema
    """
    data = {
        'author': "john@doe.com",
        "title": "New Article",
        "content": "Some extra awesome content"
    }
    response = client.post(
        "/create-article",
        data=json.dumps(
            data
        ),
        content_type="application/json",
    )

    validate_payload(response.json, "Article.json")


def test_get_article(client):
    """
    GIVEN ID of article stored in the database
    WHEN endpoint /article/<id-of-article>/ is called
    THEN it should return Article in json format that matches the schema
    """
    article = ArticleManager().save(author="jane@doe.com",
                                    title="New Article",
                                    content="Super extra awesome article")
    response = client.get(
        f"/article/{article.id}/",
        content_type="application/json",
    )

    validate_payload(response.json, "Article.json")


# def test_list_articles(client):
#     """
#     GIVEN articles stored in the database
#     WHEN endpoint /article-list/ is called
#     THEN it should return list of Article in json format that matches the schema
#     """
#     ArticleManager().save(author="jane@doe.com",
#                     title="New Article",
#                     content="Super extra awesome article")
#     response = client.get(
#         "/article-list/",
#         content_type="application/json",
#     )

#     print(response.json)

#     validate_payload(response.json, "ArticleList.json")

@pytest.mark.parametrize(
    "data",
    [
        {
            "author": "John Doe",
            "title": "New Article",
            "content": "Some extra awesome content"
        },
        {
            "author": "John Doe",
            "title": "New Article",
        },
        {
            "author": "John Doe",
            "title": None,
            "content": "Some extra awesome content"
        }
    ]
)
def test_create_article_bad_request(client, data):
    """
    GIVEN request data with invalid values or missing attributes
    WHEN endpoint /create-article/ is called
    THEN it should return status 400
    """
    response = client.post(
        "/create-article",
        data=json.dumps(
            data
        ),
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.json is not None
