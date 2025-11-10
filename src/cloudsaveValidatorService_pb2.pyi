import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameRecord(_message.Message):
    __slots__ = ("key", "namespace", "payload", "setBy", "createdAt", "updatedAt")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    payload: bytes
    setBy: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkGameRecord(_message.Message):
    __slots__ = ("gameRecords",)
    GAMERECORDS_FIELD_NUMBER: _ClassVar[int]
    gameRecords: _containers.RepeatedCompositeFieldContainer[GameRecord]
    def __init__(self, gameRecords: _Optional[_Iterable[_Union[GameRecord, _Mapping]]] = ...) -> None: ...

class PlayerRecord(_message.Message):
    __slots__ = ("key", "namespace", "payload", "setBy", "createdAt", "userId", "isPublic", "updatedAt")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ISPUBLIC_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    payload: bytes
    setBy: str
    createdAt: _timestamp_pb2.Timestamp
    userId: str
    isPublic: bool
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., isPublic: bool = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkPlayerRecord(_message.Message):
    __slots__ = ("playerRecords",)
    PLAYERRECORDS_FIELD_NUMBER: _ClassVar[int]
    playerRecords: _containers.RepeatedCompositeFieldContainer[PlayerRecord]
    def __init__(self, playerRecords: _Optional[_Iterable[_Union[PlayerRecord, _Mapping]]] = ...) -> None: ...

class AdminGameRecord(_message.Message):
    __slots__ = ("key", "namespace", "payload", "createdAt", "updatedAt")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    payload: bytes
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkAdminGameRecord(_message.Message):
    __slots__ = ("adminGameRecords",)
    ADMINGAMERECORDS_FIELD_NUMBER: _ClassVar[int]
    adminGameRecords: _containers.RepeatedCompositeFieldContainer[AdminGameRecord]
    def __init__(self, adminGameRecords: _Optional[_Iterable[_Union[AdminGameRecord, _Mapping]]] = ...) -> None: ...

class AdminPlayerRecord(_message.Message):
    __slots__ = ("key", "namespace", "payload", "createdAt", "userId", "updatedAt")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    payload: bytes
    createdAt: _timestamp_pb2.Timestamp
    userId: str
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkAdminPlayerRecord(_message.Message):
    __slots__ = ("adminPlayerRecords",)
    ADMINPLAYERRECORDS_FIELD_NUMBER: _ClassVar[int]
    adminPlayerRecords: _containers.RepeatedCompositeFieldContainer[AdminPlayerRecord]
    def __init__(self, adminPlayerRecords: _Optional[_Iterable[_Union[AdminPlayerRecord, _Mapping]]] = ...) -> None: ...

class BinaryInfo(_message.Message):
    __slots__ = ("url", "version", "contentType", "createdAt", "updatedAt")
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    url: str
    version: int
    contentType: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, url: _Optional[str] = ..., version: _Optional[int] = ..., contentType: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GameBinaryRecord(_message.Message):
    __slots__ = ("key", "namespace", "binaryInfo", "setBy", "createdAt", "updatedAt")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BINARYINFO_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    binaryInfo: BinaryInfo
    setBy: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., binaryInfo: _Optional[_Union[BinaryInfo, _Mapping]] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkGameBinaryRecord(_message.Message):
    __slots__ = ("gameBinaryRecords",)
    GAMEBINARYRECORDS_FIELD_NUMBER: _ClassVar[int]
    gameBinaryRecords: _containers.RepeatedCompositeFieldContainer[GameBinaryRecord]
    def __init__(self, gameBinaryRecords: _Optional[_Iterable[_Union[GameBinaryRecord, _Mapping]]] = ...) -> None: ...

class PlayerBinaryRecord(_message.Message):
    __slots__ = ("key", "namespace", "binaryInfo", "setBy", "createdAt", "userId", "isPublic", "updatedAt")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BINARYINFO_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ISPUBLIC_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    binaryInfo: BinaryInfo
    setBy: str
    createdAt: _timestamp_pb2.Timestamp
    userId: str
    isPublic: bool
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., binaryInfo: _Optional[_Union[BinaryInfo, _Mapping]] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., isPublic: bool = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkPlayerBinaryRecord(_message.Message):
    __slots__ = ("playerBinaryRecords",)
    PLAYERBINARYRECORDS_FIELD_NUMBER: _ClassVar[int]
    playerBinaryRecords: _containers.RepeatedCompositeFieldContainer[PlayerBinaryRecord]
    def __init__(self, playerBinaryRecords: _Optional[_Iterable[_Union[PlayerBinaryRecord, _Mapping]]] = ...) -> None: ...

class GameRecordValidationResult(_message.Message):
    __slots__ = ("isSuccess", "key", "error")
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    isSuccess: bool
    key: str
    error: Error
    def __init__(self, isSuccess: bool = ..., key: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class BulkGameRecordValidationResult(_message.Message):
    __slots__ = ("validationResults",)
    VALIDATIONRESULTS_FIELD_NUMBER: _ClassVar[int]
    validationResults: _containers.RepeatedCompositeFieldContainer[GameRecordValidationResult]
    def __init__(self, validationResults: _Optional[_Iterable[_Union[GameRecordValidationResult, _Mapping]]] = ...) -> None: ...

class PlayerRecordValidationResult(_message.Message):
    __slots__ = ("isSuccess", "key", "userId", "error")
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    isSuccess: bool
    key: str
    userId: str
    error: Error
    def __init__(self, isSuccess: bool = ..., key: _Optional[str] = ..., userId: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class BulkPlayerRecordValidationResult(_message.Message):
    __slots__ = ("validationResults",)
    VALIDATIONRESULTS_FIELD_NUMBER: _ClassVar[int]
    validationResults: _containers.RepeatedCompositeFieldContainer[PlayerRecordValidationResult]
    def __init__(self, validationResults: _Optional[_Iterable[_Union[PlayerRecordValidationResult, _Mapping]]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("errorCode", "errorMessage")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ...) -> None: ...
