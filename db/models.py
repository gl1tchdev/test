from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import MetaData, ForeignKey
from datetime import datetime


metadata = MetaData()

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    username: Mapped[str] = mapped_column()
    registered_at: Mapped[str] = mapped_column(default=datetime.utcnow)
    tweets: Mapped[list['Tweet']] = relationship()


class Tweet(Base):
    __tablename__= 'tweets'
    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    text: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
