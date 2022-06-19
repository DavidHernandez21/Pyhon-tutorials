import os
import sqlite3
import uuid
from functools import wraps
from typing import Any
from typing import List

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class NotFound(Exception):
    pass


def conn_decorator_sqlite3(row_factory:Any):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as conn:
                    conn.row_factory = row_factory
                    kwargs['conn'] = conn

                    return func(*args, **kwargs)
                    
            except sqlite3.OperationalError as e:
                raise e
            except NotFound as e:
                raise e
            finally:
                conn.close()
        return wrapper
    return decorator

# class SQLLiteConnManager():
#     conn=None

#     def get_conn(path: str):
#         if not self.conn:
#             self.conn = sqlite3.connect(path)

    
#     def set_row_factory(path: str, factory: sqlite3.Row) -> None:
#         if not self.conn:
#             self.get_conn(path)
        
#         self.conn.row_factory = factory
        

#     def close_conn(self) -> None:
#         self.conn.close()
#         self.conn = None


# conn_manager = SQLLiteConnManager()

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    author: EmailStr
    title: str
    content: str
    

class ArticleManager:

    @staticmethod
    @conn_decorator_sqlite3(row_factory=sqlite3.Row)
    def get_by_id(*,article_id: str, conn: sqlite3.Connection) -> "Article":

        cur = conn.cursor()
        cur.execute("SELECT * FROM articles WHERE id=?", (article_id,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        id, author, title, content = record
        return Article(id=id,author=author, title=title, content=content)

    @staticmethod
    @conn_decorator_sqlite3(row_factory=sqlite3.Row)
    def get_by_title(*,title: str, conn: sqlite3.Connection) -> "Article":
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM articles WHERE title = ?", (title,))

        record = cur.fetchone()

        if record is None:
            raise NotFound
        
        id, author, title, content = record
        return Article(id=id, author=author, title=title, content=content)
        
    
    @staticmethod
    @conn_decorator_sqlite3(row_factory=sqlite3.Row)
    def list(*,conn: sqlite3.Connection) -> List["Article"]:

        cur = conn.cursor()
        cur.execute("SELECT * FROM articles")

        return [Article(id=record[0],author=record[1], title=record[2], content=record[3])
                for record in cur.fetchall()]
        

    @staticmethod
    def save(*,author: str, title: str, content: str) -> Article:
        try:
            with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as conn:
                article = Article(author=author, title=title, content=content)
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO articles (id,author,title,content) VALUES(?, ?, ?, ?)",
                    (article.id, article.author, article.title, article.content)
                )

                return article

        except sqlite3.OperationalError as e:
            raise e

        finally:
            conn.close()        
        

    @staticmethod
    def create_table(database_name: str, table_name: str = "articles") -> None:

        try:
            with sqlite3.connect(database_name) as conn:

                conn.execute(
                    f"CREATE TABLE IF NOT EXISTS {table_name} (id TEXT, author TEXT, title TEXT, content TEXT)"
                )
        except sqlite3.OperationalError as e:
            raise e

        finally:
            conn.close()
