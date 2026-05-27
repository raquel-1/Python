#!/usr/bin/env python3
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def _has_coman_capt(self) -> bool:
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                return True
        return False

    def experienced_crew(self) -> bool:
        count: int = 0
        for member in self.crew:
            if member.years_experience >= 5:
                count += 1
        if count < (len(self.crew) / 2):
            return False
        else:
            return True

    def _members_active(self) -> bool:
        for member in self.crew:
            if member.is_active is False:
                return False
        return True

    @model_validator(mode='after')
    def my_validator(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with “M”")
        elif self._has_coman_capt() is False:
            raise ValueError("Must have at least one Commander or Captain")
        elif self.duration_days > 365 and self.experienced_crew() is False:
            raise ValueError("Must need 50% experienced crew (5+ years)")
        elif self._members_active() is False:
            raise ValueError("All crew members must be active")
        # always at the end
        return self
