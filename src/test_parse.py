import unittest
from unittest import TestCase

from parse import Expr


class ParserTest(TestCase):
    def test(self):
        for input, output in [
            ('hello', Expr('hello')),
            ('hello(hello)', Expr('hello', Expr('hello'))),
            ('a(b(c))', Expr('a', Expr('b', Expr('c')))),
        ]:
            self.assertEqual(Expr.parse(input), output)


if __name__ == '__main__':
    unittest.main()
