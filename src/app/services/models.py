# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import inspect
from dataclasses import dataclass
from typing import Optional
from typing import Protocol, runtime_checkable


@runtime_checkable
class Validatable(Protocol):
    def validate(self) -> Optional[Exception]:
        ...


@dataclass
class CustomGameRecord:
    locationId: Optional[str] = None
    name: Optional[str] = None
    totalResources: Optional[int] = None
    totalEnemy: Optional[int] = None

    def validate(self) -> Optional[Exception]:
        validation_errors = []
        if not self.locationId:
            validation_errors.append("locationId cannot be empty")
        if not self.name:
            validation_errors.append("name cannot be empty")
        if self.totalResources is None:
            validation_errors.append("totalResources cannot be empty")
        if self.totalEnemy is None:
            validation_errors.append("totalEnemy cannot be empty")
        if validation_errors:
            return Exception(";".join(validation_errors))
        return None

    @classmethod
    def from_dict(cls, dikt: dict):
        return cls(**{
            k: v for k, v in dikt.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass
class CustomPlayerRecord:
    userId: Optional[str] = None
    favouriteWeaponType: Optional[str] = None
    favouriteWeapon: Optional[str] = None

    def validate(self) -> Optional[Exception]:
        validation_errors = []
        if not self.userId:
            validation_errors.append("userId cannot be empty")
        if not self.favouriteWeaponType:
            validation_errors.append("favouriteWeaponType cannot be empty")
        if self.favouriteWeaponType not in ("SWORD", "GUN"):
            validation_errors.append("invalid weapon type")
        if self.favouriteWeapon is None:
            validation_errors.append("favouriteWeapon cannot be empty")
        if validation_errors:
            return Exception(";".join(validation_errors))
        return None

    @classmethod
    def from_dict(cls, dikt: dict):
        return cls(**{
            k: v for k, v in dikt.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass
class DailyMessage:
    message: Optional[str] = None
    title: Optional[str] = None
    availableOn: Optional[str] = None

    def validate(self) -> Optional[Exception]:
        validation_errors = []
        if not self.message:
            validation_errors.append("message cannot be empty")
        if not self.title:
            validation_errors.append("title cannot be empty")
        if self.availableOn is None:
            validation_errors.append("availableOn cannot be empty")
        if validation_errors:
            return Exception(";".join(validation_errors))
        return None

    @classmethod
    def from_dict(cls, dikt: dict):
        return cls(**{
            k: v for k, v in dikt.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass
class PlayerActivity:
    userId: Optional[str] = None
    activity: Optional[str] = None

    def validate(self) -> Optional[Exception]:
        validation_errors = []
        if not self.userId:
            validation_errors.append("userId cannot be empty")
        if not self.activity:
            validation_errors.append("activity cannot be empty")
        if validation_errors:
            return Exception(";".join(validation_errors))
        return None

    @classmethod
    def from_dict(cls, dikt: dict):
        return cls(**{
            k: v for k, v in dikt.items()
            if k in inspect.signature(cls).parameters
        })


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
