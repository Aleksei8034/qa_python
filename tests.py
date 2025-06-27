import pytest
from main import BooksCollector


class TestBooksCollector:
    # добавление двух книг
    def test_add_new_book_add_two_books(self, books_collector):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_genre()) == 2

#добавления книг с именем 0 и больше 40 символов
    @pytest.mark.parametrize('book', 
                             ['', 'МушкетёрыМушкетёрыМушкетёрыМушкетёрыМушкетёры']
                             )
    def test_add_new_book_add_incorrect_name_not_added(self, book, books_collector):
        books_collector.add_new_book(book)
        assert len(books_collector.get_books_genre()) == 0

    #установления жанра в добавленной книге
    def test_add_new_book_check_genre_success(self, books_collector):
        first_book = 'кот в сапогах'
        books_collector.add_new_book(first_book)
        assert books_collector.get_book_genre(first_book) == ''


     # добавления одинаковых книг
    def test_add_new_book_add_double_books_not_added(self, books_collector):
        books = ['Война и мир', 'Война и мир']
        for book in books:
            books_collector.add_new_book(book)
        assert len(books_collector.get_books_genre()) == 1


    #добавления жанра из списка genre книге из списка books_genre
    def test_set_book_genre_added(self, books_collector):
        first_book = 'звездные воины'
        genre = 'Фантастика'
        books_collector.add_new_book(first_book)
        books_collector.set_book_genre(first_book, genre)
        assert books_collector.get_book_genre(first_book) == genre


    #изменение жанра из списка genre книге из списка books_genre
    def test_set_book_genre_changed(self, books_collector):
        first_book = 'звездные воины'
        genre = 'Фантастика'
        other_genre = 'Детективы'
        books_collector.add_new_book(first_book)
        books_collector.set_book_genre(first_book, genre)
        books_collector.set_book_genre(first_book, other_genre)
        assert books_collector.get_book_genre(first_book) == other_genre


    #добавление жанра не из списка genre книге из списка books_genre
    def test_set_book_genre_missing_genre_not_added(self, books_collector):
        first_book = 'звездные воины'
        missing_genre = 'Приключения'
        books_collector.add_new_book(first_book)
        books_collector.set_book_genre(first_book, missing_genre)
        assert books_collector.get_book_genre(first_book) == ''
    

    # вывод книги определенного жанра
    def test_get_books_with_specific_genre_success(self, collection_five_books):
        assert collection_five_books.get_books_with_specific_genre('Ужасы') == ['Коралина']

    #вывод отсутствующей книги определенного жанра
    def test_get_books_with_specific_genre_missing_book(self, collection_five_books):
        assert len(collection_five_books.get_books_with_specific_genre('Приключения')) == 0


    #вывод списка книг с жанром для детей
    def test_get_books_for_children_success(self, collection_five_books):
        children_books = collection_five_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['звездные воины', 'Чип и Дейл', '12 стульев']


    # добавление книги из списка books_genre в избранное
    def test_add_book_in_favorites_add_one_book_added(self, books_collector):
        first_book = 'воин'
        books_collector.add_new_book(first_book)
        books_collector.add_book_in_favorites(first_book)
        favorites = books_collector.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book


    #добавление книги не из списка books_genre в избранное
    def test_add_book_in_favorites_add_missing_book_not_added(self, books_collector):
        first_book = 'звездные воины'
        books_collector.add_book_in_favorites(first_book)
        assert len(books_collector.get_list_of_favorites_books()) == 0


    # повторное добавления книги в избранное
    def test_add_book_in_favorites_add_double_books_not_added(self, books_collector):
        first_book = 'звездные воины'
        books_collector.add_new_book(first_book)
        books_collector.add_book_in_favorites(first_book)
        books_collector.add_book_in_favorites(first_book)
        favorites = books_collector.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book


    #удаление книги из списка избранное
    def test_delete_book_from_favorites_book_deleted(self, books_collector):
        first_book = 'звездные воины'
        books_collector.add_new_book(first_book)
        books_collector.add_book_in_favorites(first_book)
        books_collector.delete_book_from_favorites(first_book)
        assert len(books_collector.get_list_of_favorites_books()) == 0


    #удаление не добавленной книги в избранное
    def test_delete_book_from_favorites_missing_book_not_deleted(self, books_collector):
        first_book = 'воин'
        second_book = 'звездные воины'
        books_collector.add_new_book(first_book)
        books_collector.add_book_in_favorites(first_book)
        books_collector.delete_book_from_favorites(second_book)
        favorites = books_collector.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book