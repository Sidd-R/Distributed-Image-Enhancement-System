from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageRequest(_message.Message):
    __slots__ = ("id", "image_data", "lamport_timestamp", "choice")
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    LAMPORT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    id: str
    image_data: bytes
    lamport_timestamp: int
    choice: int
    def __init__(self, id: _Optional[str] = ..., image_data: _Optional[bytes] = ..., lamport_timestamp: _Optional[int] = ..., choice: _Optional[int] = ...) -> None: ...

class ImageResponse(_message.Message):
    __slots__ = ("id", "image_data")
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    image_data: bytes
    def __init__(self, id: _Optional[str] = ..., image_data: _Optional[bytes] = ...) -> None: ...
