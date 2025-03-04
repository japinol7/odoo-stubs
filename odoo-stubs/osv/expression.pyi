from typing import Any, Callable

from ..models import MAGIC_COLUMNS as MAGIC_COLUMNS
from ..models import BaseModel
from ..sql_db import Cursor
from ..tools.query import Query

NOT_OPERATOR: str
OR_OPERATOR: str
AND_OPERATOR: str
DOMAIN_OPERATORS: tuple[str, ...]
TERM_OPERATORS: tuple[str, ...]
NEGATIVE_TERM_OPERATORS: tuple[str, ...]
DOMAIN_OPERATORS_NEGATION: dict[str, str]
TERM_OPERATORS_NEGATION: dict[str, str]
TRUE_LEAF: tuple
FALSE_LEAF: tuple
TRUE_DOMAIN: list[tuple]
FALSE_DOMAIN: list[tuple]

def normalize_domain(domain: list) -> list: ...
def is_false(model, domain: list) -> bool: ...
def combine(operator: str, unit, zero, domains: list[list]) -> list: ...
def AND(domains: list[list]) -> list: ...
def OR(domains: list[list]) -> list: ...
def distribute_not(domain: list) -> list: ...
def normalize_leaf(element): ...
def is_operator(element) -> bool: ...
def is_leaf(element, internal: bool = ...) -> bool: ...
def is_boolean(element) -> bool: ...
def check_leaf(element, internal: bool = ...) -> None: ...
def get_unaccent_wrapper(cr: Cursor) -> Callable[[Any], str]: ...

class expression:
    root_model: BaseModel
    root_alias: str | None
    expression: list
    query: Query | None
    result: tuple[str, list]
    def __init__(
        self,
        domain: list,
        model: BaseModel,
        alias: str | None = ...,
        query: Query | None = ...,
    ) -> None: ...
    def get_tables(self) -> tuple[str, ...]: ...
    def parse(self): ...
    def to_sql(self) -> tuple[str, list]: ...
