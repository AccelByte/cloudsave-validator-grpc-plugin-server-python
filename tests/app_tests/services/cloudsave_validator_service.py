# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json
from datetime import datetime, timedelta
from unittest import IsolatedAsyncioTestCase

# noinspection PyPackageRequirements
import grpc.aio
# noinspection PyPackageRequirements
import responses
# noinspection PyPackageRequirements
import responses.matchers

from app.proto.cloudsaveValidatorService_pb2 import *
from app.proto.cloudsaveValidatorService_pb2_grpc import *
from app.services.cloudsave_validator_service import AsyncCloudsaveValidatorService
from app.services.models import *

from accelbyte_grpc_plugin_tests import create_server


class AsyncCloudsaveValidatorServiceTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.max_size_event_banner_in_kb = 100
        self.service = AsyncCloudsaveValidatorService(
            max_size_event_banner_in_kb=self.max_size_event_banner_in_kb,
        )

    async def asyncTearDown(self) -> None:
        self.service.max_size_event_banner_in_kb = self.max_size_event_banner_in_kb

    async def test_connection(self):
        addr = "localhost:50051"
        server = create_server(addr, [])
        add_CloudsaveValidatorServiceServicer_to_server(self.service, server)

        await server.start()

        try:
            async with grpc.aio.insecure_channel(addr) as channel:
                # assert
                stub = CloudsaveValidatorServiceStub(channel)
                request = GameRecord()
                request.key = "foo"

                # act
                response = await stub.BeforeWriteGameRecord(request)

                # assert
                self.assertIsNotNone(response)
        finally:
            await server.stop(grace=None)

    async def test_BeforeWriteGameRecord(self):
        # arrange 1
        payload = CustomGameRecord(
            locationId="locationId",
            name="name",
            totalResources=0,
            totalEnemy=0,
        )
        request = GameRecord()
        request.key = "foo_map"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 1
        response = await self.service.BeforeWriteGameRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        payload = CustomGameRecord()
        request = GameRecord()
        request.key = "foo_map"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 2
        response = await self.service.BeforeWriteGameRecord(request, None)

        # assert 2
        payload_validation_error = payload.validate()
        self.assertIsNotNone(payload_validation_error)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual(str(payload_validation_error), response.error.errorMessage)

    async def test_AfterReadGameRecord(self):
        # arrange 1
        available_on = datetime.utcnow().today() - timedelta(days=1)
        payload = DailyMessage(
            message="message",
            title="title",
            availableOn=available_on.isoformat(),
        )
        request = GameRecord()
        request.key = "foo_daily_msg"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 1
        response = await self.service.AfterReadGameRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        payload = DailyMessage()
        request = GameRecord()
        request.key = "foo_daily_msg"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 2
        response = await self.service.AfterReadGameRecord(request, None)

        # assert 2
        payload_validation_error = payload.validate()
        self.assertIsNotNone(payload_validation_error)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual(str(payload_validation_error), response.error.errorMessage)

        # arrange 3
        available_on = datetime.utcnow().today() + timedelta(days=1)
        payload = DailyMessage(
            message="message",
            title="title",
            availableOn=available_on.isoformat(),
        )
        request = GameRecord()
        request.key = "foo_daily_msg"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 3
        response = await self.service.AfterReadGameRecord(request, None)

        # assert 3
        payload_validation_error = payload.validate()
        self.assertIsNone(payload_validation_error)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual("not accessible yet", response.error.errorMessage)

    async def test_BeforeWritePlayerRecord(self):
        # arrange 1
        payload = CustomPlayerRecord(
            userId="userId",
            favouriteWeaponType="SWORD",
            favouriteWeapon="excalibur",
        )
        request = PlayerRecord()
        request.key = "favourite_weapon"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")
        request.userId = "userId"

        # act 1
        response = await self.service.BeforeWritePlayerRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        payload = CustomPlayerRecord()
        request = PlayerRecord()
        request.key = "favourite_weapon"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")
        request.userId = "userId"

        # act 2
        response = await self.service.BeforeWritePlayerRecord(request, None)

        # assert 2
        payload_validation_error = payload.validate()
        self.assertIsNotNone(payload_validation_error)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual(str(payload_validation_error), response.error.errorMessage)

    async def test_AfterReadPlayerRecord(self):
        # arrange 1
        request = PlayerRecord()
        request.key = "key"
        request.userId = "userId"

        # act 1
        response = await self.service.AfterReadPlayerRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertTrue(response.isSuccess)

    async def test_BeforeWriteAdminGameRecord(self):
        # arrange 1
        payload = CustomGameRecord(
            locationId="locationId",
            name="name",
            totalResources=0,
            totalEnemy=0,
        )
        request = GameRecord()
        request.key = "foo_map"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 1
        response = await self.service.BeforeWriteAdminGameRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        payload = CustomGameRecord()
        request = GameRecord()
        request.key = "foo_map"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")

        # act 2
        response = await self.service.BeforeWriteAdminGameRecord(request, None)

        # assert 2
        payload_validation_error = payload.validate()
        self.assertIsNotNone(payload_validation_error)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual(str(payload_validation_error), response.error.errorMessage)

    async def test_BeforeWriteAdminPlayerRecord(self):
        # arrange 1
        payload = PlayerActivity(
            userId="userId",
            activity="activity",
        )
        request = PlayerRecord()
        request.key = "player_activity"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")
        request.userId = "userId"

        # act 1
        response = await self.service.BeforeWriteAdminPlayerRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        payload = PlayerActivity()
        request = PlayerRecord()
        request.key = "player_activity"
        request.payload = json.dumps(payload.__dict__).encode(encoding="utf-8")
        request.userId = "userId"

        # act 2
        response = await self.service.BeforeWriteAdminPlayerRecord(request, None)

        # assert 2
        payload_validation_error = payload.validate()
        self.assertIsNotNone(payload_validation_error)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual(str(payload_validation_error), response.error.errorMessage)

    @responses.activate
    async def test_BeforeWriteGameBinaryRecord_unreachable(self):
        url = "https://example.com/event_banner.png"

        # arrange
        responses.reset()
        request = GameBinaryRecord()
        request.key = "foo_event_banner"
        request.binaryInfo.url = url

        # act
        response = await self.service.BeforeWriteGameBinaryRecord(request, None)

        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertEqual("unable to reach binary info url", response.error.errorMessage)

    @responses.activate
    async def test_BeforeWriteGameBinaryRecord_success(self):
        url = "https://example.com/event_banner.png"

        # arrange
        responses.reset()
        responses.get(
            url=url,
            body=b'foo',
            auto_calculate_content_length=True,
        )
        request = GameBinaryRecord()
        request.key = "foo_event_banner"
        request.binaryInfo.url = url

        # act
        response = await self.service.BeforeWriteGameBinaryRecord(request, None)

        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertTrue(response.isSuccess)

    @responses.activate
    async def test_BeforeWriteGameBinaryRecord_maximumSize(self):
        url = "https://example.com/event_banner.png"

        # arrange
        responses.reset()
        responses.get(
            url=url,
            body=b'foo',
            auto_calculate_content_length=True,
        )
        request = GameBinaryRecord()
        request.key = "foo_event_banner"
        request.binaryInfo.url = url
        self.service.max_size_event_banner_in_kb = 0.0

        # act
        response = await self.service.BeforeWriteGameBinaryRecord(request, None)

        # assert
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertEqual("maximum size for event banner is 0.0 kB", response.error.errorMessage)

    async def test_AfterReadGameBinaryRecord(self):
        # arrange 1
        updated_at = datetime.utcnow().today()
        request = GameBinaryRecord()
        request.key = "foo_daily_event_stage"
        request.binaryInfo.updatedAt.FromDatetime(updated_at)

        # act 1
        response = await self.service.AfterReadGameBinaryRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        updated_at = datetime.utcnow().today() - timedelta(days=1)
        request = GameBinaryRecord()
        request.key = "foo_daily_event_stage"
        request.binaryInfo.updatedAt.FromDatetime(updated_at)

        # act 2
        response = await self.service.AfterReadGameBinaryRecord(request, None)

        # assert 2
        self.assertIsNotNone(response)
        self.assertIsInstance(response, GameRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual(f"today's {request.key} is not ready yet", response.error.errorMessage)

    async def test_BeforeWritePlayerBinaryRecord(self):
        # arrange 1
        request = PlayerBinaryRecord()
        request.key = "foo_id_card"
        request.binaryInfo.version = 1

        # act 1
        response = await self.service.BeforeWritePlayerBinaryRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertTrue(response.isSuccess)

        # arrange 2
        request = PlayerBinaryRecord()
        request.key = "foo_id_card"
        request.binaryInfo.version = 2

        # act 2
        response = await self.service.BeforeWritePlayerBinaryRecord(request, None)

        # assert 2
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertFalse(response.isSuccess)
        self.assertIsNotNone(response.error)
        self.assertEqual("id card can only be created once", response.error.errorMessage)

    async def test_AfterReadPlayerBinaryRecord(self):
        # arrange 1
        request = PlayerRecord()
        request.key = "key"
        request.userId = "userId"

        # act 1
        response = await self.service.AfterReadPlayerBinaryRecord(request, None)

        # assert 1
        self.assertIsNotNone(response)
        self.assertIsInstance(response, PlayerRecordValidationResult)
        self.assertTrue(response.isSuccess)
