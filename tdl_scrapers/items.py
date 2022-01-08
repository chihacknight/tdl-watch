import typing
from datetime import datetime

import attr

from .constants import CATEGORY_OPTIONS, OTHER, SOURCE_OPTIONS


@attr.s
class TdlItem:
    created_at: datetime = attr.ib(factory=datetime.now)
    address: str = attr.ib(default="")
    text: str = attr.ib(default="")
    entity: str = attr.ib(default="")
    latitude: typing.Optional[float] = attr.ib(default=None)
    longitude: typing.Optional[float] = attr.ib(default=None)
    source: str = attr.ib(validator=attr.validators.in_(SOURCE_OPTIONS), default=OTHER)
    category: str = attr.ib(
        validator=attr.validators.in_(CATEGORY_OPTIONS), default=OTHER
    )
    extra: typing.Dict = attr.ib(factory=dict)
