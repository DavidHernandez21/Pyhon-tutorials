from blog.models import ArticleManager
from blog.queries import GetArticleByIDQuery
from blog.queries import ListArticlesQuery


def test_list_articles():
    """
    GIVEN 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    ArticleManager().save(
        author='jane@doe.com',
        title='New Article',
        content='Super extra awesome article',
    )
    ArticleManager().save(
        author='jane@doe.com',
        title='Another Article',
        content='Super awesome article',
    )

    query = ListArticlesQuery()

    assert len(query.execute()) == 2


def test_get_article_by_id():
    """
    GIVEN ID of article stored in the database
    WHEN the execute method is called on GetArticleByIDQuery with an ID
    THEN it should return the article with the same ID
    """
    article = ArticleManager().save(
        author='jane@doe.com',
        title='New Article',
        content='Super extra awesome article',
    )

    query = GetArticleByIDQuery(id=article.id)

    assert query.execute().id == article.id
