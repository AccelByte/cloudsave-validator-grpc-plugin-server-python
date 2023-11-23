# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

from dataclasses import dataclass
from typing import Optional
from typing import Protocol, runtime_checkable


@runtime_checkable
class Validatable(Protocol):
    def validate(self) -> Optional[Exception]:
        ...


@dataclass
class CustomGameRecord:
    locationId: Optional[str]
    name: Optional[str]
    totalResources: Optional[int]
    totalEnemy: Optional[int]

    def validate(self) -> Optional[Exception]:
        if not self.locationId:
            return Exception("locationId cannot be empty")
        if not self.name:
            return Exception("name cannot be empty")
        if self.totalResources is None:
            return Exception("totalResources cannot be empty")
        if self.totalEnemy is None:
            return Exception("totalEnemy cannot be empty")
        return None


@dataclass
class CustomPlayerRecord:
    userId: Optional[str]
    favouriteWeaponType: Optional[str]
    favouriteWeapon: Optional[str]

    def validate(self) -> Optional[Exception]:
        if not self.userId:
            return Exception("userId cannot be empty")
        if not self.favouriteWeaponType:
            return Exception("favouriteWeaponType cannot be empty")
        if self.favouriteWeaponType not in ("SWORD", "GUN"):
            return Exception("invalid weapon type")
        if self.favouriteWeapon is None:
            return Exception("favouriteWeapon cannot be empty")
        return None


@dataclass
class DailyMessage:
    message: Optional[str]
    title: Optional[str]
    availableOn: Optional[str]

    def validate(self) -> Optional[Exception]:
        if not self.message:
            return Exception("message cannot be empty")
        if not self.title:
            return Exception("title cannot be empty")
        if self.availableOn is None:
            return Exception("availableOn cannot be empty")
        return None


@dataclass
class PlayerActivity:
    userId: Optional[str]
    activity: Optional[str]

    def validate(self) -> Optional[Exception]:
        if not self.userId:
            return Exception("userId cannot be empty")
        if not self.activity:
            return Exception("activity cannot be empty")
        return None


assert issubclass(CustomGameRecord, Validatable)
assert issubclass(CustomPlayerRecord, Validatable)
assert issubclass(DailyMessage, Validatable)
assert issubclass(PlayerActivity, Validatable)

__all__ = [
    "CustomGameRecord",
    "CustomPlayerRecord",
    "DailyMessage",
    "PlayerActivity",
    "Validatable",
]
