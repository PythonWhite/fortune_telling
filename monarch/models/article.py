from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import LONGTEXT

from monarch.models.base import Base, TimestampMixin


class ArticleModel(Base, TimestampMixin):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(32), nullable=False, comment="管理员ID")
    title = Column(String(255))
    introduction = Column(Text, comment="简介")
    content = Column(LONGTEXT)
    cover = Column(String(255), comment="封面")
    author = Column(String(32), comment="作者")
    type = Column(Integer, default=0, comment="0原创，1转载，2书籍")
