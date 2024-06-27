# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
import requests
from datetime import datetime, timezone
from logging import Logger
from typing import Any, Optional

from google.protobuf.json_format import MessageToJson

from .models import (
    CustomGameRecord,
    CustomPlayerRecord,
    DailyMessage,
    PlayerActivity,
)
from ..proto.cloudsaveValidatorService_pb2 import (
    AdminGameRecord,
    AdminPlayerRecord,
    BinaryInfo,
    BulkGameBinaryRecord,
    BulkGameRecord,
    BulkGameRecordValidationResult,
    BulkPlayerBinaryRecord,
    BulkPlayerRecord,
    BulkPlayerRecordValidationResult,
    Error,
    GameBinaryRecord,
    GameRecord,
    GameRecordValidationResult,
    PlayerBinaryRecord,
    PlayerRecord,
    PlayerRecordValidationResult,
    DESCRIPTOR,
)

from ..proto.cloudsaveValidatorService_pb2_grpc import CloudsaveValidatorServiceServicer


class AsyncCloudsaveValidatorService(CloudsaveValidatorServiceServicer):
    full_name: str = DESCRIPTOR.services_by_name["CloudsaveValidatorService"].full_name

    def __init__(
        self,
        max_size_event_banner_in_kb: float = 100,
        logger: Optional[Logger] = None
    ) -> None:
        self.max_size_event_banner_in_kb = max_size_event_banner_in_kb
        self.logger = logger

    # noinspection PyShadowingBuiltins
    def log_payload(self, format: str, payload: Any) -> None:
        if not self.logger:
            return
        payload_json = MessageToJson(payload, preserving_proto_field_name=True)
        self.logger.info(format.format(payload_json))

    async def BeforeWriteGameRecord(
        self, request: GameRecord, context: Any
    ) -> GameRecordValidationResult:
        assert isinstance(request.key, str) and request.key

        result = GameRecordValidationResult()
        result.isSuccess = True
        result.key = request.key

        if request.key.endswith("map"):
            assert isinstance(request.payload, bytes)
            payload_dict = json.loads(request.payload)
            record = CustomGameRecord.from_dict(payload_dict)

            validation_error = record.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)
                return result

        return result

    async def AfterReadGameRecord(
        self, request: GameRecord, context: Any
    ) -> GameRecordValidationResult:
        assert isinstance(request.key, str) and request.key

        result = GameRecordValidationResult()
        result.isSuccess = True
        result.key = request.key

        if request.key.endswith("daily_msg"):
            assert isinstance(request.payload, bytes)
            payload_dict = json.loads(request.payload)
            message = DailyMessage.from_dict(payload_dict)

            validation_error = message.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)
                return result

            now = datetime.utcnow()
            available_on = datetime.fromisoformat(message.availableOn)
            if now < available_on:
                result.isSuccess = False
                result.error.errorCode = 2
                result.error.errorMessage = "not accessible yet"
                return result

        return result

    async def AfterBulkReadGameRecord(
        self, request: BulkGameRecord, context
    ) -> BulkGameRecordValidationResult:
        bulk_result = BulkGameRecordValidationResult()

        for req in request.gameRecords:
            result = await self.AfterReadGameRecord(request=req, context=context)
            bulk_result.validationResults.append(result)

        return bulk_result

    async def BeforeWritePlayerRecord(
        self, request: PlayerRecord, context: Any
    ) -> PlayerRecordValidationResult:
        assert isinstance(request.key, str) and request.key
        assert isinstance(request.userId, str) and request.userId

        result = PlayerRecordValidationResult()
        result.isSuccess = True
        result.key = request.key
        result.userId = request.userId

        if request.key.endswith("favourite_weapon"):
            assert isinstance(request.payload, bytes)
            payload_dict = json.loads(request.payload)
            # noinspection PyBroadException
            try:
                record = CustomPlayerRecord.from_dict(payload_dict)
                validation_error = record.validate()
                if validation_error:
                    result.isSuccess = False
                    result.error.errorCode = 1
                    result.error.errorMessage = str(validation_error)
            except Exception:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = "Parsing failed"

        return result

    async def AfterReadPlayerRecord(
        self, request: PlayerRecord, context: Any
    ) -> PlayerRecordValidationResult:
        assert isinstance(request.key, str) and request.key
        assert isinstance(request.userId, str) and request.userId

        result = PlayerRecordValidationResult()
        result.isSuccess = True
        result.key = request.key
        result.userId = request.userId

        return result

    async def AfterBulkReadPlayerRecord(
        self, request: BulkPlayerRecord, context: Any
    ) -> BulkPlayerRecordValidationResult:
        bulk_result = BulkPlayerRecordValidationResult()

        for req in request.playerRecords:
            result = await self.AfterReadGameRecord(request=req, context=context)
            bulk_result.validationResults.append(result)

        return bulk_result

    async def BeforeWriteAdminGameRecord(
        self, request: AdminGameRecord, context: Any
    ) -> GameRecordValidationResult:
        assert isinstance(request.key, str) and request.key

        result = GameRecordValidationResult()
        result.isSuccess = True
        result.key = request.key

        if request.key.endswith("map"):
            assert isinstance(request.payload, bytes)
            payload_dict = json.loads(request.payload)
            record = CustomGameRecord.from_dict(payload_dict)

            validation_error = record.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)

        return result

    async def BeforeWriteAdminPlayerRecord(
        self, request: AdminPlayerRecord, context: Any
    ) -> PlayerRecordValidationResult:
        assert isinstance(request.key, str) and request.key
        assert isinstance(request.userId, str) and request.userId

        result = PlayerRecordValidationResult()
        result.isSuccess = True
        result.key = request.key
        result.userId = request.userId

        if request.key.endswith("player_activity"):
            assert isinstance(request.payload, bytes)
            payload_dict = json.loads(request.payload)
            activity = PlayerActivity.from_dict(payload_dict)

            validation_error = activity.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)

        return result

    async def BeforeWriteGameBinaryRecord(
        self, request: GameBinaryRecord, context: Any
    ) -> GameRecordValidationResult:
        assert isinstance(request.key, str) and request.key

        result = GameRecordValidationResult()
        result.isSuccess = True
        result.key = request.key

        if request.key.endswith("event_banner") and request.binaryInfo:
            assert isinstance(request.binaryInfo, BinaryInfo)
            assert isinstance(request.binaryInfo.url, str) and request.binaryInfo.url
            resp = None
            # noinspection PyBroadException
            try:
                resp = requests.get(request.binaryInfo.url)
            except Exception:
                pass
            if resp is None or not resp.ok:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = "unable to reach binary info url"
                return result
            content_length_str = resp.headers.get("Content-Length", None)
            if not content_length_str:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = "unable to get binary info content length"
                return result
            content_length_int = self.try_parse_int(content_length_str)
            if content_length_int is None:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = "unable to convert binary info content length"
                return result
            content_length_kb = content_length_int / 1000.0
            if content_length_kb > self.max_size_event_banner_in_kb:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = f"maximum size for event banner is {self.max_size_event_banner_in_kb} kB"
                return result

        return result

    async def AfterReadGameBinaryRecord(
        self, request: GameBinaryRecord, context: Any
    ) -> GameRecordValidationResult:
        assert isinstance(request.key, str) and request.key

        result = GameRecordValidationResult()
        result.isSuccess = True
        result.key = request.key

        if request.key.endswith("daily_event_stage") and request.binaryInfo:
            assert isinstance(request.binaryInfo, BinaryInfo)
            if request.binaryInfo.updatedAt:
                now_dt = datetime.utcnow()
                updated_at_dt = request.binaryInfo.updatedAt.ToDatetime()
                if not self.is_same_date(now_dt, updated_at_dt):
                    result.isSuccess = False
                    result.error.errorCode = 1
                    result.error.errorMessage = f"today's {request.key} is not ready yet"
                    return result

        return result

    async def AfterBulkReadGameBinaryRecord(
        self, request: BulkGameBinaryRecord, context: Any
    ) -> BulkGameRecordValidationResult:
        bulk_result = BulkGameRecordValidationResult()

        for req in request.gameBinaryRecords:
            result = await self.AfterReadGameBinaryRecord(request=req, context=context)
            bulk_result.validationResults.append(result)

        return bulk_result

    async def BeforeWritePlayerBinaryRecord(
        self, request: PlayerBinaryRecord, context: Any
    ) -> PlayerRecordValidationResult:
        assert isinstance(request.key, str) and request.key

        result = PlayerRecordValidationResult()
        result.isSuccess = True
        result.key = request.key
        result.userId = request.userId

        if request.key.endswith("id_card") and request.binaryInfo:
            assert isinstance(request.binaryInfo, BinaryInfo)
            if request.binaryInfo.version > 1:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = "id card can only be created once"
                return result

        return result

    async def AfterReadPlayerBinaryRecord(
        self, request: PlayerBinaryRecord, context: Any
    ) -> PlayerRecordValidationResult:
        assert isinstance(request.key, str) and request.key
        assert isinstance(request.userId, str) and request.userId

        result = PlayerRecordValidationResult()
        result.isSuccess = True
        result.key = request.key
        result.userId = request.userId

        return result

    async def AfterBulkReadPlayerBinaryRecord(
        self, request: BulkPlayerBinaryRecord, context: Any
    ) -> BulkPlayerRecordValidationResult:
        bulk_result = BulkPlayerRecordValidationResult()

        for req in request.playerBinaryRecords:
            result = await self.AfterReadPlayerBinaryRecord(request=req, context=context)
            bulk_result.validationResults.append(result)

        return bulk_result

    @staticmethod
    def is_same_date(a: datetime, b: datetime) -> bool:
        a = a.astimezone(timezone.utc)
        b = b.astimezone(timezone.utc)
        if a.day != b.day:
            return False
        if a.month != b.month:
            return False
        if a.year != b.year:
            return False
        return True

    @staticmethod
    def try_parse_int(s: str) -> Optional[int]:
        try:
            i = int(s)
            return i
        except ValueError:
            return None


__all__ = [
    "AsyncCloudsaveValidatorService",
]
