#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from monarch.models.base import Base, TimestampMixin


class Menu(Base, TimestampMixin):
    """菜单表"""

    __tablename__ = "menu"

    id = Column(Integer, nullable=False)
    name = Column(String(32), nullable=False, comment="菜单名称")
    pid = Column(Integer, nullable=False, comment="父ID")
