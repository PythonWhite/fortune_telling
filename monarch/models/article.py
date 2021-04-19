from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import LONGTEXT

from monarch.models.base import Base, TimestampMixin


class ArticleModel(Base, TimestampMixin):
    """书籍"""
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(String(32), nullable=False, comment="管理员ID")
    title = Column(String(255), nullable=False)
    introduction = Column(Text, comment="简介", nullable=False)
    content = Column(LONGTEXT, nullable=False)
    cover = Column(String(255), comment="封面", nullable=True)
    author = Column(String(32), comment="作者", nullable=True)
    type = Column(Integer, default=1, comment="1原创，2转载，3书籍")
    likes = Column(Integer, default=0, comment="点赞数")

    @classmethod
    def query_article(cls, keyword, query_field, _type, **kwargs):
        query = cls.query
        if keyword and query_field:
            query = query.filter_by(**{query_field: keyword})
        if _type == 0:
            query = query.filter(cls.type != 3)
        elif _type:
            query = query.filter(cls.type == _type)

        return query.order_by(cls.created_at.desc())

    @classmethod
    def get_article(cls, title, is_books=True, bans_id=None):
        query = cls.query.filter(
            cls.title == title
        )
        if is_books:
            query = query.filter(
                cls.type != 3
            )
        if bans_id:
            query = query.filter(
                cls.id != bans_id
            )
        return query.first()

    @classmethod
    def get_articles_likes_top5(cls, is_books=True):
        query = cls.query
        if is_books:
            query = query.filter(
                cls.type == 3
            )
        else:
            query = query.filter(
                cls.type != 3
            )
        query = query.order_by(
            cls.likes.desc()
        ).order_by(
            cls.updated_at.desc()
        ).limit(5).all()
        return query
