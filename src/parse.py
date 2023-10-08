import sys
from typing import Generator, Optional, List
from dataclasses import dataclass

from lark import Lark, Transformer, v_args
from lark.ast_utils import Ast as LarkAST, WithMeta, create_transformer
from lark.tree import Meta


class AST(LarkAST):
    pass


@dataclass
class Name(AST):
    name: str


@dataclass(unsafe_hash=True)
class Expr(AST):
    name: Name
    expr: Optional['Expr'] = None

    @property
    def names(self) -> Generator[str, None, None]:
        node = self
        while node is not None:
            name = node.name
            s = name[0]
            if s != s.lower():
                name = f"'{name}'"
            yield name
            node = node.expr

    def __str__(self) -> str:
        result = ''

        i = 0
        for name in self.names:
            if 1 <= i:
                result += '('
            result += name
            i += 1
        result += ')' * (i - 1)

        return result
    
    @property
    def is_existing(self) -> bool:
        return 'existing' in self.names
    
    def __repr__(self) -> str:
        names = list(self.names)
        name = names[-1]
        type = names[-2]
        return f'{name} {type}'.replace('\'', '')

    @classmethod
    def parse(cls, input: str) -> 'Expr':
        result = transformer.transform(lark.parse(input))
        prev = result
        if isinstance(prev, str):
            return Expr(prev)
        curr = prev.expr
        while not isinstance(curr, str):
            prev = curr
            curr = curr.expr
        prev.expr = Expr(curr)
        return result


class ToAst(Transformer):
    def WORD(self, x):
        return x.value

    @v_args(inline=True)
    def start(self, x):
        return x


transformer = create_transformer(sys.modules[__name__], ToAst())

grammar = '''
start: expr

?expr: "'"? ID "'"? "(" expr ")" 
     | "'"? ID "'"?

%import common.CNAME -> ID
%ignore " "
'''

lark = Lark(grammar)
