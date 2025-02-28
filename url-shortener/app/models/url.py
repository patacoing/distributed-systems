from sqlmodel import SQLModel, Field
from sqlalchemy import BigInteger, Column


class Url(SQLModel, table=True):
    id: int = Field(sa_column=Column(BigInteger, primary_key=True))
    url: str
    shortened_url: str
