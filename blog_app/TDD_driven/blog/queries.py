from typing import List

from blog.models import Article
from blog.models import ArticleManager
from pydantic import BaseModel


class ListArticlesQuery:
    def execute(self) -> List[Article]:
        return ArticleManager.list()


class GetArticleByIDQuery(BaseModel):
    id: str

    def execute(self) -> Article:
        return ArticleManager.get_by_id(article_id=self.id)
