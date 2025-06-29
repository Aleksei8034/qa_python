# qa_python

проект 4-го спринта

Файлы:
conftest.py - вспомогательная функция (фикстура)
main.py - класс BooksCollector
tests.py - тестовый класс TestBooksCollector

Набор тестовых методов класса TestBooksCollector:

test_add_new_book_adding_two_books_success добавления двух книг в словарь books_genre

test_add_new_book_add_incorrect_name_not_added:  добавления книг с именем 0 и больше 40 символов (параметризированный тест с двумя аргументами 0 и 'МушкетёрыМушкетёрыМушкетёрыМушкетёрыМушкетёры')

test_add_new_book_check_genre_success:  установления жанра по  в добавленной книге

test_add_new_book_add_double_books_not_added:  повторное добавления одинаковых книг

test_set_book_genre_added:  добавления жанра из списка genre книге из списка books_genre

test_set_book_genre_changed: изменения жанра из списка genre книге из списка books_genre

test_set_book_genre_missing_genre_not_added: добавления жанра не из списка genre книге из списка books_genre

test_get_books_with_specific_genre_success:  вывода книги определенного жанра

test_get_books_with_specific_genre_missing_book: вывода отсутствующей книги определенного жанра

test_get_books_for_children_success: вывод списка книг с жанром для детей

test_add_book_in_favorites_add_one_book_added: добавление книги из списка books_genre в избранное

test_add_book_in_favorites_add_missing_book_not_added:  добавления книги не из списка books_genre в избранное

test_add_book_in_favorites_add_double_books_not_added:  повторного добавления книги в избранное

test_delete_book_from_favorites_book_deleted: удаление книги из списка избранное

test_delete_book_from_favorites_missing_book_not_deleted:удаление книги не из списка избранное

добавленные тесты

test_get_list_of_favorites_books: получаем список избранных книг

test_get_book_genre_by_name: получаем жанр книги по имени

test_get_book_genre_by_name2: получаем жанр книги по имени

test_get_books_genre_dict: получаем словарь books_genre

test_get_books_genre_dict2: получаем словарь books_genre

Команда для запуска тестов

pytest -v tests.py
