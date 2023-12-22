# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import datetime
import json
from logging import Logger
from typing import Any

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
    BulkGameRecord,
    BulkGameRecordValidationResult,
    BulkPlayerRecord,
    BulkPlayerRecordValidationResult,
    GameRecord,
    GameRecordValidationResult,
    PlayerRecord,
    PlayerRecordValidationResult,
    DESCRIPTOR,
)

from ..proto.cloudsaveValidatorService_pb2_grpc import CloudsaveValidatorServiceServicer


class AsyncCloudsaveValidatorService(CloudsaveValidatorServiceServicer):
    full_name: str = DESCRIPTOR.services_by_name["CloudsaveValidatorService"].full_name

    def __init__(self, logger: Logger) -> None:
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
            record = CustomGameRecord(**payload_dict)

            validation_error = record.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)

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
            message = DailyMessage(**payload_dict)

            validation_error = message.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)

            now = datetime.datetime.utcnow()
            available_on = datetime.datetime.fromisoformat(message.availableOn)
            if now < available_on:
                result.isSuccess = False
                result.error.errorCode = 2
                result.error.errorMessage = "not accessible yet"

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
            try:
                record = CustomPlayerRecord(**payload_dict)
                validation_error = record.validate()
                if validation_error:
                    result.isSuccess = False
                    result.error.errorCode = 1
                    result.error.errorMessage = str(validation_error)
            except:
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
            record = CustomGameRecord(**payload_dict)

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
            activity = PlayerActivity(**payload_dict)

            validation_error = activity.validate()
            if validation_error:
                result.isSuccess = False
                result.error.errorCode = 1
                result.error.errorMessage = str(validation_error)

        return result


__all__ = [
    "AsyncCloudsaveValidatorService",
]
