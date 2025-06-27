import pytest
from main import BooksCollector

@pytest.fixture(scope='function')
def books_collector():
    books_collector = BooksCollector()

    return books_collector

#Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val): 
    return repr(val)

@pytest.fixture
def collection_five_books(books_collector):
    collect = books_collector
    books = ['звездные воины', 'Коралина', 'Улицы разбитых фонарей', 'Чип и Дейл', '12 стульев']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])

    return collect