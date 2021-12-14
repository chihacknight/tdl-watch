import typing
from datetime import datetime

import attr

from .constants import OTHER, SOURCE_OPTIONS


@attr.s
class TdlItem:
    created_at: datetime = attr.ib(factory=datetime.now)
    address: str = attr.ib(default="")
    text: str = attr.ib(default="")
    source: str = attr.ib(validator=attr.validators.in_(SOURCE_OPTIONS), default=OTHER)
    extra: typing.Dict = attr.ib(factory=dict)
