import typing
import strawberry


@strawberry.type
class Book:
    title: str
    author: str
    publish: str
    tahun: str
    type: str


@strawberry.type
class Query:
    books: typing.List[Book]

def get_books():
    return [
        Book(
            title="Analisa Sistem Distribusi",
            author="Suherman",
            publish="Confident Publisher",
            tahun="2024",
            type="Buku Ajar"
        ),
    ]

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)

schema = strawberry.Schema(query=Query)