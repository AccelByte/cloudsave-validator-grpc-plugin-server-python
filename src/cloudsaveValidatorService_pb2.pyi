from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdminGameRecord(_message.Message):
    __slots__ = ["createdAt", "key", "namespace", "payload", "updatedAt"]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    key: str
    namespace: str
    payload: bytes
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AdminPlayerRecord(_message.Message):
    __slots__ = ["createdAt", "key", "namespace", "payload", "updatedAt", "userId"]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    key: str
    namespace: str
    payload: bytes
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BinaryInfo(_message.Message):
    __slots__ = ["contentType", "createdAt", "updatedAt", "url", "version"]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    contentType: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    url: str
    version: int
    def __init__(self, url: _Optional[str] = ..., version: _Optional[int] = ..., contentType: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BulkAdminGameRecord(_message.Message):
    __slots__ = ["adminGameRecords"]
    ADMINGAMERECORDS_FIELD_NUMBER: _ClassVar[int]
    adminGameRecords: _containers.RepeatedCompositeFieldContainer[AdminGameRecord]
    def __init__(self, adminGameRecords: _Optional[_Iterable[_Union[AdminGameRecord, _Mapping]]] = ...) -> None: ...

class BulkAdminPlayerRecord(_message.Message):
    __slots__ = ["adminPlayerRecords"]
    ADMINPLAYERRECORDS_FIELD_NUMBER: _ClassVar[int]
    adminPlayerRecords: _containers.RepeatedCompositeFieldContainer[AdminPlayerRecord]
    def __init__(self, adminPlayerRecords: _Optional[_Iterable[_Union[AdminPlayerRecord, _Mapping]]] = ...) -> None: ...

class BulkGameBinaryRecord(_message.Message):
    __slots__ = ["gameBinaryRecords"]
    GAMEBINARYRECORDS_FIELD_NUMBER: _ClassVar[int]
    gameBinaryRecords: _containers.RepeatedCompositeFieldContainer[GameBinaryRecord]
    def __init__(self, gameBinaryRecords: _Optional[_Iterable[_Union[GameBinaryRecord, _Mapping]]] = ...) -> None: ...

class BulkGameRecord(_message.Message):
    __slots__ = ["gameRecords"]
    GAMERECORDS_FIELD_NUMBER: _ClassVar[int]
    gameRecords: _containers.RepeatedCompositeFieldContainer[GameRecord]
    def __init__(self, gameRecords: _Optional[_Iterable[_Union[GameRecord, _Mapping]]] = ...) -> None: ...

class BulkGameRecordValidationResult(_message.Message):
    __slots__ = ["validationResults"]
    VALIDATIONRESULTS_FIELD_NUMBER: _ClassVar[int]
    validationResults: _containers.RepeatedCompositeFieldContainer[GameRecordValidationResult]
    def __init__(self, validationResults: _Optional[_Iterable[_Union[GameRecordValidationResult, _Mapping]]] = ...) -> None: ...

class BulkPlayerBinaryRecord(_message.Message):
    __slots__ = ["playerBinaryRecords"]
    PLAYERBINARYRECORDS_FIELD_NUMBER: _ClassVar[int]
    playerBinaryRecords: _containers.RepeatedCompositeFieldContainer[PlayerBinaryRecord]
    def __init__(self, playerBinaryRecords: _Optional[_Iterable[_Union[PlayerBinaryRecord, _Mapping]]] = ...) -> None: ...

class BulkPlayerRecord(_message.Message):
    __slots__ = ["playerRecords"]
    PLAYERRECORDS_FIELD_NUMBER: _ClassVar[int]
    playerRecords: _containers.RepeatedCompositeFieldContainer[PlayerRecord]
    def __init__(self, playerRecords: _Optional[_Iterable[_Union[PlayerRecord, _Mapping]]] = ...) -> None: ...

class BulkPlayerRecordValidationResult(_message.Message):
    __slots__ = ["validationResults"]
    VALIDATIONRESULTS_FIELD_NUMBER: _ClassVar[int]
    validationResults: _containers.RepeatedCompositeFieldContainer[PlayerRecordValidationResult]
    def __init__(self, validationResults: _Optional[_Iterable[_Union[PlayerRecordValidationResult, _Mapping]]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ["errorCode", "errorMessage"]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class GameBinaryRecord(_message.Message):
    __slots__ = ["binaryInfo", "createdAt", "key", "namespace", "setBy", "updatedAt"]
    BINARYINFO_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    binaryInfo: BinaryInfo
    createdAt: _timestamp_pb2.Timestamp
    key: str
    namespace: str
    setBy: str
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., binaryInfo: _Optional[_Union[BinaryInfo, _Mapping]] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GameRecord(_message.Message):
    __slots__ = ["createdAt", "key", "namespace", "payload", "setBy", "updatedAt"]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    key: str
    namespace: str
    payload: bytes
    setBy: str
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GameRecordValidationResult(_message.Message):
    __slots__ = ["error", "isSuccess", "key"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    error: Error
    isSuccess: bool
    key: str
    def __init__(self, isSuccess: bool = ..., key: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class PlayerBinaryRecord(_message.Message):
    __slots__ = ["binaryInfo", "createdAt", "isPublic", "key", "namespace", "setBy", "updatedAt", "userId"]
    BINARYINFO_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    ISPUBLIC_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    binaryInfo: BinaryInfo
    createdAt: _timestamp_pb2.Timestamp
    isPublic: bool
    key: str
    namespace: str
    setBy: str
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., binaryInfo: _Optional[_Union[BinaryInfo, _Mapping]] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., isPublic: bool = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PlayerRecord(_message.Message):
    __slots__ = ["createdAt", "isPublic", "key", "namespace", "payload", "setBy", "updatedAt", "userId"]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    ISPUBLIC_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SETBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    isPublic: bool
    key: str
    namespace: str
    payload: bytes
    setBy: str
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    def __init__(self, key: _Optional[str] = ..., namespace: _Optional[str] = ..., payload: _Optional[bytes] = ..., setBy: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., isPublic: bool = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PlayerRecordValidationResult(_message.Message):
    __slots__ = ["error", "isSuccess", "key", "userId"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    error: Error
    isSuccess: bool
    key: str
    userId: str
    def __init__(self, isSuccess: bool = ..., key: _Optional[str] = ..., userId: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
