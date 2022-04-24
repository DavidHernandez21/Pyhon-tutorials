from typing import List
from flask import Flask, jsonify, request
from blog.commands import CreateArticleCommand, CreateTableCommand, AlreadyExists
from blog.queries import GetArticleByIDQuery, ListArticlesQuery
from blog.models import NotFound
from pydantic import ValidationError
app = Flask(__name__)


def display_error(error_list: ValidationError.errors):
    """
    Parse error list and return a Dict with all errors
    """
    err_dict = {"missing_fields": [error['loc'][0] for error in error_list]}
    return jsonify(err_dict)


@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Article not found"}), 404

@app.errorhandler(ValidationError)
def handle_validation_exception(error):

    response = display_error(error.errors())
    response.status_code = 400
    return response

@app.route("/create-article", methods=["POST"])
def create_article():
    payload = request.get_json()
    # cmd = CreateArticleCommand(author=payload["author"], title=payload["title"], content=payload["content"])
    cmd = CreateArticleCommand(**payload)
    try:
        return jsonify(cmd.execute().dict())
    except AlreadyExists:
        return jsonify(error="Article with this title already exists"), 200
    

@app.route("/article/<article_id>/", methods=["GET"])
def get_article(article_id):
    query = GetArticleByIDQuery(id=article_id)
    return jsonify(query.execute().dict())


@app.route("/article-list/", methods=["GET"])
def list_articles():
    query = ListArticlesQuery()
    records = [record.dict() for record in query.execute()]
    return jsonify(records)

@app.route("/create-table/<table_name>", methods=["POST"])
def create_table(table_name):
    CreateTableCommand(table_name=table_name).execute()
    return jsonify(table=table_name), 200


if __name__ == "__main__":
    app.run(debug=True)