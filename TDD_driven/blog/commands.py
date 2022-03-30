from pydantic import BaseModel, EmailStr
import contextlib

from blog.models import Article, NotFound, ArticleManager


class AlreadyExists(Exception):
    pass


class CreateArticleCommand(BaseModel):
    author: EmailStr
    title: str
    content: str

    def execute(self) -> Article:
        with contextlib.suppress(NotFound):
            ArticleManager.get_by_title(title=self.title)
            raise AlreadyExists
        
        return ArticleManager.save(author=self.author, title=self.title, content=self.content)

class CreateTableCommand(BaseModel):
    database_name: str = "database.db"
    table_name: str

    def execute(self) -> None:
        ArticleManager.create_table(database_name=self.database_name, table_name=self.table_name)      
            


if __name__ == "__main__":
    # article = Article(content="Super awesome article",
    #     title="New Article",
    #     author="john@doe.com")
    # print(article.author)
    
    ArticleManager.create_table(database_name="database.db")
    cmd = CreateArticleCommand(
        content="Super awesome article",
        title="New Article",
        author="john@doe.com",
    )
    print(cmd.execute())
    
    # Article.get_by_id(article_id="sddf")
