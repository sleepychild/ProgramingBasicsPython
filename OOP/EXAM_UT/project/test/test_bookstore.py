from unittest import TestCase
from project.bookstore import Bookstore


class Test_Bookstore(TestCase):
    def test_init_books_limit(self):
        bs: Bookstore = Bookstore(20)

        self.assertEqual(bs.books_limit, 20)

    def test_init_books_limit_zero(self):
        with self.assertRaises(ValueError):
            Bookstore(0)

    def test_init_books_limit_zero_msg(self):
        try:
            Bookstore(0)
        except ValueError as e:
            self.assertEqual("Books limit of 0 is not valid", e.args[0])

    def test_init_books_limit_below_zero(self):
        with self.assertRaises(ValueError):
            Bookstore(-1)

    def test_init_books_limit_below_zero_msg(self):
        try:
            Bookstore(-1)
        except ValueError as e:
            self.assertEqual("Books limit of -1 is not valid", e.args[0])

    def test_availability_in_store_by_book_titles(self):
        bs: Bookstore = Bookstore(5)
        self.assertEqual(bs.availability_in_store_by_book_titles, dict())

    def test_availability_in_store_by_book_titles_available(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 5)
        bs.receive_book("Other", 5)

        self.assertEqual(
            bs.availability_in_store_by_book_titles, {"Any": 5, "Other": 5}
        )

    def test__total_sold_books_initial(self):
        bs: Bookstore = Bookstore(20)

        self.assertEqual(bs.total_sold_books, 0)

    def test__total_sold_books(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)
        bs.sell_book("Any", 2)

        self.assertEqual(bs.total_sold_books, 2)

    def test_books_limit_setter_ok(self):
        bs: Bookstore = Bookstore(20)
        bs.books_limit = 10

        self.assertEqual(bs.books_limit, 10)

    def test_books_limit_setter_zero(self):
        bs: Bookstore = Bookstore(20)

        with self.assertRaises(ValueError):
            bs.books_limit = 0

    def test_books_limit_setter_below_zero(self):
        bs: Bookstore = Bookstore(20)

        with self.assertRaises(ValueError):
            bs.books_limit = -1

    def test___len__(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)

        self.assertEqual(len(bs), 2)

    def test_receive_book(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 20)

        self.assertEqual(len(bs), 20)

    def test_receive_book_not_enough_space(self):
        bs: Bookstore = Bookstore(20)

        with self.assertRaises(Exception):
            bs.receive_book("Any", 30)

    def test_receive_book_not_enough_space_msg(self):
        bs: Bookstore = Bookstore(20)

        try:
            bs.receive_book("Any", 30)
        except Exception as e:
            self.assertEqual(
                "Books limit is reached. Cannot receive more books!", e.args[0]
            )

    def test_receive_book_message(self):
        bs: Bookstore = Bookstore(20)
        msg: str = bs.receive_book("Any", 5)
        expected: str = "5 copies of Any are available in the bookstore."
        self.assertEqual(msg, expected)

    def test_receive_book_negative_message(self):
        bs: Bookstore = Bookstore(20)
        msg: str = bs.receive_book("Any", -5)
        expected: str = "-5 copies of Any are available in the bookstore."
        self.assertEqual(msg, expected)

    def test_sell_book_not_enough_copies(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)

        with self.assertRaises(Exception):
            bs.sell_book("Any", 3)

    def test_sell_book_not_enough_copies_message(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 10)

        try:
            bs.sell_book("Any", 30)
        except Exception as e:
            self.assertEqual("Any has not enough copies to sell. Left: 10", e.args[0])

    def test_sell_book_unavailable(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)

        with self.assertRaises(Exception):
            bs.sell_book("Other", 3)

    def test_sell_book_unavailable_msg(self):
        bs: Bookstore = Bookstore(20)

        try:
            bs.sell_book("Any", 30)
        except Exception as e:
            self.assertEqual("Book Any doesn't exist!", e.args[0])

    def test_sell_book_message(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 5)
        msg: str = bs.sell_book("Any", 2)
        expected: str = "Sold 2 copies of Any"
        self.assertEqual(msg, expected)

    def test___str__initial(self):
        bs: Bookstore = Bookstore(20)

        expect: str = """Total sold books: 0
Current availability: 0"""

        self.assertEqual(str(bs), expect)

    def test___str__(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)
        bs.receive_book("Other", 4)

        expect: str = """Total sold books: 0
Current availability: 6
 - Any: 2 copies
 - Other: 4 copies"""

        self.assertEqual(str(bs), expect)

    def test___str___sells(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)
        bs.receive_book("Other", 4)
        bs.sell_book("Any", 1)
        bs.sell_book("Other", 3)

        expect: str = """Total sold books: 4
Current availability: 2
 - Any: 1 copies
 - Other: 1 copies"""

        self.assertEqual(str(bs), expect)

    def test___str___sold_out(self):
        bs: Bookstore = Bookstore(20)
        bs.receive_book("Any", 2)
        bs.receive_book("Other", 4)
        bs.sell_book("Any", 2)
        bs.sell_book("Other", 4)

        expect: str = """Total sold books: 6
Current availability: 0
 - Any: 0 copies
 - Other: 0 copies"""

        self.assertEqual(str(bs), expect)
