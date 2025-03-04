from email.message import Message
from re import Pattern
from typing import Callable, Collection, FrozenSet, Literal

from lxml.etree import _Element
from markupsafe import Markup

safe_attrs: FrozenSet
SANITIZE_TAGS: dict[str, Collection[str]]

def tag_quote(el: _Element) -> None: ...
def html_normalize(
    src: str, filter_callback: Callable[[_Element], _Element] | None = ...
) -> str: ...
def html_sanitize(
    src: str,
    silent: bool = ...,
    sanitize_tags: bool = ...,
    sanitize_attributes: bool = ...,
    sanitize_style: bool = ...,
    sanitize_form: bool = ...,
    strip_style: bool = ...,
    strip_classes: bool = ...,
) -> Markup: ...

URL_REGEX: str
TEXT_URL_REGEX: str
HTML_TAG_URL_REGEX: str
HTML_TAGS_REGEX: Pattern
HTML_NEWLINES_REGEX: Pattern

def validate_url(url: str) -> str: ...
def is_html_empty(html_content: str) -> bool: ...
def html_keep_url(text: str) -> str: ...
def html_to_inner_content(html: str) -> str: ...
def create_link(url: str, label: str) -> str: ...
def html2plaintext(
    html: str, body_id: str | None = ..., encoding: str = ...
) -> str: ...
def plaintext2html(text: str, container_tag: str = ...) -> Markup: ...
def append_content_to_html(
    html: str,
    content: str,
    plaintext: bool = ...,
    preserve: bool = ...,
    container_tag: str = ...,
) -> Markup: ...
def prepend_html_content(html_body: str, html_content: str) -> str: ...

email_re: Pattern
single_email_re: Pattern
mail_header_msgid_re: Pattern
email_addr_escapes_re: Pattern

def generate_tracking_message_id(res_id: str) -> str: ...
def email_split_tuples(text: str) -> list[str]: ...
def email_split(text: str) -> list[str]: ...
def email_split_and_format(text: str) -> list[str]: ...
def email_normalize(text: str, strict: bool = ...) -> str | Literal[False]: ...
def email_normalize_all(text: str) -> list[str]: ...
def email_domain_extract(email: str) -> str | Literal[False]: ...
def email_domain_normalize(domain: str) -> str | Literal[False]: ...
def url_domain_extract(url: str) -> str | Literal[False]: ...
def email_escape_char(email_address: str) -> str: ...
def decode_message_header(
    message: Message, header: str, separator: str = ...
) -> str: ...
def formataddr(pair: tuple[str, str], charset: str = ...) -> str: ...
def encapsulate_email(old_email: str, new_email: str) -> str: ...
