import datetime
import pickle as pickle_
from collections.abc import Mapping, MutableMapping, MutableSet
from contextlib import ContextDecorator, suppress
from logging import Handler, LogRecord
from re import Pattern
from types import ModuleType
from typing import (
    IO,
    Any,
    AnyStr,
    Callable,
    Collection,
    Generic,
    ItemsView,
    Iterable,
    Iterator,
    NoReturn,
    TypeVar,
)

import markupsafe
import xlsxwriter
import xlwt
from babel.core import Locale
from odoo.addons.base.models.res_currency import Currency
from odoo.addons.base.models.res_lang import Lang
from xlwt import Worksheet

from ..api import Environment
from ..loglevels import exception_to_unicode as exception_to_unicode
from ..loglevels import get_encodings as get_encodings
from .cache import *
from .parse_version import parse_version as parse_version

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_CallableT = TypeVar("_CallableT", bound=Callable)
_LowerLoggingT = TypeVar("_LowerLoggingT", bound=lower_logging)
_ReplaceExceptionsT = TypeVar("_ReplaceExceptionsT", bound=replace_exceptions)

SKIPPED_ELEMENT_TYPES: tuple
NON_BREAKING_SPACE: str

def find_in_path(name: str) -> str: ...
def exec_command_pipe(
    name: str, *args
) -> tuple[IO[AnyStr] | None, IO[AnyStr] | None]: ...
def find_pg_tool(name: str) -> str: ...
def exec_pg_environ() -> dict[str, str]: ...
def exec_pg_command(name: str, *args) -> None: ...
def exec_pg_command_pipe(
    name: str, *args
) -> tuple[IO[AnyStr] | None, IO[AnyStr] | None]: ...
def file_path(file_path: str, filter_ext: tuple[str, ...] = ...) -> str: ...
def file_open(
    name: str, mode: str = ..., filter_ext: tuple[str, ...] | None = ...
) -> IO: ...
def flatten(list) -> list: ...
def reverse_enumerate(l): ...
def partition(
    pred: Callable[[_T], bool], elems: Iterable[_T]
) -> tuple[list[_T], list[_T]]: ...
def topological_sort(elems: dict[_T, Any]) -> list[_T]: ...
def merge_sequences(*iterables: Iterable[_T]) -> list[_T]: ...

class PatchedWorkbook(xlwt.Workbook):
    def add_sheet(self, name: str, cell_overwrite_ok: bool = ...) -> Worksheet: ...

class PatchedXlsxWorkbook(xlsxwriter.Workbook):
    def add_worksheet(self, name: str | None = ..., **kw) -> Worksheet: ...

def to_xml(s: str) -> str: ...
def get_iso_codes(lang: str) -> str: ...
def scan_languages() -> list[tuple[str, str]]: ...
def mod10r(number: str) -> str: ...
def str2bool(s: str, default: Any | None = ...) -> bool: ...
def human_size(sz) -> str: ...
def logged(f: _CallableT) -> _CallableT: ...

class profile:
    fname: str | None
    def __init__(self, fname: str | None = ...) -> None: ...
    def __call__(self, f: _CallableT) -> _CallableT: ...

def detect_ip_addr() -> str: ...

DEFAULT_SERVER_DATE_FORMAT: str
DEFAULT_SERVER_TIME_FORMAT: str
DEFAULT_SERVER_DATETIME_FORMAT: str
DATE_LENGTH: int
DATETIME_FORMATS_MAP: dict[str, str]
POSIX_TO_LDML: dict[str, str]

def posix_to_ldml(fmt: str, locale: Locale) -> str: ...
def split_every(
    n: int, iterable: Iterable[_T], piece_maker: Callable[[Iterable[_T]], _T1] = ...
) -> Iterator[_T1]: ...

raise_error: object

def resolve_attr(obj, attr: str, default: object = ...): ...
def attrgetter(*items): ...
def discardattr(obj, key: str) -> None: ...
def remove_accents(input_str: str) -> str: ...

class unquote(str): ...

class mute_logger(Handler):
    loggers: tuple[str]
    old_params: dict[str, tuple[list[Handler], bool]]
    def __init__(self, *loggers: str) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: Any | None = ...,
        exc_val: Any | None = ...,
        exc_tb: Any | None = ...,
    ) -> None: ...
    def __call__(self, func: _CallableT) -> _CallableT: ...
    def emit(self, record: LogRecord) -> None: ...

class lower_logging(Handler):
    old_handlers: list[Handler] | None
    old_propagate: bool | None
    had_error_log: bool
    max_level: int | None
    to_level: int | None
    def __init__(self, max_level: int, to_level: int | None = ...) -> None: ...
    def __enter__(self: _LowerLoggingT) -> _LowerLoggingT: ...
    def __exit__(
        self,
        exc_type: Any | None = ...,
        exc_val: Any | None = ...,
        exc_tb: Any | None = ...,
    ) -> None: ...
    def emit(self, record: LogRecord) -> None: ...

class CountingStream(Generic[_T]):
    stream: Iterator[_T]
    index: int
    stopped: bool
    def __init__(self, stream: Iterable[_T], start: int = ...) -> None: ...
    def __iter__(self) -> CountingStream[_T]: ...
    def next(self) -> _T: ...
    __next__ = next

def stripped_sys_argv(*strip_args: str) -> list[str]: ...

class ConstantMapping(Mapping[_KT, _VT]):
    def __init__(self, val: _VT) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator: ...
    def __getitem__(self, item) -> _VT: ...

def dumpstacks(
    sig: Any | None = ..., frame: Any | None = ..., thread_idents: Any | None = ...
) -> None: ...
def freehash(arg) -> int: ...
def clean_context(context: dict[str, Any]) -> dict[str, Any]: ...

class frozendict(dict):
    def __delitem__(self, key) -> NoReturn: ...
    def __setitem__(self, key, val) -> NoReturn: ...
    def clear(self) -> NoReturn: ...
    def pop(self, key, default: Any | None = ...) -> NoReturn: ...
    def popitem(self) -> NoReturn: ...
    def setdefault(self, key, default: Any | None = ...) -> NoReturn: ...
    def update(self, *args, **kwargs) -> NoReturn: ...
    def __hash__(self) -> int: ...

class Collector(dict[_KT, tuple[_T]]):
    def __getitem__(self, key: _KT) -> tuple[_T]: ...
    def __setitem__(self, key: _KT, val: Iterable[_T]) -> None: ...
    def add(self, key: _KT, val: _T) -> None: ...
    def discard_keys_and_values(self, excludes: Collection): ...

class StackMap(MutableMapping):
    def __init__(self, m: MutableMapping | None = ...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def pushmap(self, m: MutableMapping | None = ...) -> None: ...
    def popmap(self) -> MutableMapping: ...

class OrderedSet(MutableSet):
    def __init__(self, elems: Iterable = ...) -> None: ...
    def __contains__(self, elem) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def add(self, elem) -> None: ...
    def discard(self, elem) -> None: ...
    def update(self, elems: Iterable) -> None: ...
    def difference_update(self, elems: Iterable) -> None: ...

class LastOrderedSet(OrderedSet):
    def add(self, elem) -> None: ...

class Callbacks:
    data: dict
    def __init__(self) -> None: ...
    def add(self, func: Callable) -> None: ...
    def run(self) -> None: ...
    def clear(self) -> None: ...

class ReversedIterable(Generic[_T]):
    iterable: Iterable[_T]
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __reversed__(self) -> Iterator[_T]: ...

def groupby(
    iterable: Iterable[_T], key: Callable[..., _T1] | None = ...
) -> ItemsView[_T1, _T]: ...
def unique(it: Iterable[_T]) -> Iterator[_T]: ...
def submap(mapping: Mapping[_KT, _VT], keys: Iterable[_KT]) -> dict[_KT, _VT]: ...

class Reverse:
    val: Any
    def __init__(self, val) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

def ignore(*exc) -> suppress: ...

class replace_exceptions(ContextDecorator):
    exceptions: tuple[type[Exception], ...]
    by: Exception
    def __init__(self, *exceptions: type[Exception], by: Exception) -> None: ...
    def __enter__(self: _ReplaceExceptionsT) -> _ReplaceExceptionsT: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

html_escape = markupsafe.escape

def get_lang(env: Environment, lang_code: str = ...) -> "Lang": ...
def babel_locale_parse(lang_code: str) -> Locale: ...
def formatLang(
    env: Environment,
    value,
    digits: int | None = ...,
    grouping: bool = ...,
    monetary: bool = ...,
    dp: bool = ...,
    currency_obj: "Currency" = ...,
) -> str: ...
def format_date(
    env: Environment,
    value: datetime.date | datetime.datetime | str,
    lang_code: str = ...,
    date_format: str = ...,
) -> str: ...
def parse_date(env: Environment, value: str, lang_code: str = ...) -> datetime.date: ...
def format_datetime(
    env: Environment,
    value: str | datetime.datetime,
    tz: str = ...,
    dt_format: str = ...,
    lang_code: str = ...,
) -> str: ...
def format_time(
    env: Environment, value, tz: str = ..., time_format: str = ..., lang_code: str = ...
) -> str: ...
def format_decimalized_number(number: float, decimal: int = ...) -> str: ...
def format_decimalized_amount(
    amount: float, currency: "Currency | None" = ...
) -> str: ...
def format_amount(
    env: Environment,
    amount: float,
    currency: "Currency",
    lang_code: str = ...,
) -> str: ...
def format_duration(value: float) -> str: ...

consteq: Callable[[str, str], bool]

class Unpickler(pickle_.Unpickler):
    def find_class(self, module_name: str, name: str): ...

pickle: ModuleType

class DotDict(dict):
    def __getattr__(self, attrib): ...

def get_diff(
    data_from: tuple[str, str], data_to: tuple[str, str], custom_style: bool = ...
) -> str: ...
def hmac(env: Environment, scope, message, hash_function=...) -> str: ...

ADDRESS_REGEX: Pattern

def street_split(street: str) -> dict[str, str]: ...
def is_list_of(values: list | tuple, type_: type | tuple[type, ...]) -> bool: ...
def has_list_types(
    values: list | tuple, types: Collection[type | tuple[type, ...]]
) -> bool: ...
