from typing import List

from pydantic import BaseModel

from blog.models import Article
from blog.models import ArticleManager


class ListArticlesQuery:

    def execute(self) -> List[Article]:
        return ArticleManager.list()


class GetArticleByIDQuery(BaseModel):
    id: str

    def execute(self) -> Article:
        return ArticleManager.get_by_id(article_id=self.id)
