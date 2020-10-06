#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from monarch.models.base import Base, TimestampMixin


class Menu(Base, TimestampMixin):
    """菜单表"""

    __tablename__ = "menu"

    id = Column(Integer, nullable=False)
