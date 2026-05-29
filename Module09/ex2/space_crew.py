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
    launch_date: datetimeexcept Exception as e:
        print(e)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def _has_coman_capt(self) -> bool:
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                return True
        return False

    def _experienced_crew(self) -> bool:
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
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        elif self.duration_days > 365 and self._experienced_crew() is False:
            raise ValueError(
                "Mission must need 50% experienced crew (5+ years)"
            )
        elif self._members_active() is False:
            raise ValueError("All crew members must be active")
        # always at the end
        return self


def main() -> None:
    # Veteran and active leader
    sarah = CrewMember(
        member_id="CREW01",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=45,
        specialization="Mission Command",
        years_experience=15,
        is_active=True
    )
    # Experienced and active officer
    john = CrewMember(
        member_id="CREW02",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=34,
        specialization="Navigation",
        years_experience=8,
        is_active=True
    )
    # Active rookie(novato) cadet
    alice = CrewMember(
        member_id="CREW03",
        name="Alice Johnson",
        rank=Rank.CADET,
        age=22,
        specialization="Engineering",
        years_experience=1,
        is_active=True
    )
    # ========================================
    # Block 1: VALID Mission
    # ========================================
    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 15, 10, 30),
            duration_days=900,
            crew=[sarah, john, alice],
            mission_status="Greetings from Zeta Reticuli",
            budget_millions=2500.0
        )
        print("\nSpace Mission Crew Validation")
        print("========================================")
        print("Valid mission created")
        print("Mission:", mission1.mission_name)
        print("ID:", mission1.mission_id)
        print("Destination:", mission1.destination)
        print(f"Duration: {mission1.duration_days} days")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")
        for member in mission1.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except Exception as e:
        print(f"\n{e}")

    # ========================================
    # Block 2: INVALID Mission (No lider and Fails)
    # ========================================
    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 15, 10, 30),
            duration_days=900,
            crew=[john, alice],
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Valid mission created")
    except Exception as e:
        # e.errors() returns the cleaned-up list of errors from Pydantic
        if hasattr(e, 'errors'):
            # ("Value error, Must have...")
            raw_msg = e.errors()[0]['msg']
            clean_msg = raw_msg.replace("Value error, ", "")
            # We only show the first error
            print(f"{clean_msg}")
        # fails for a reason other than Pydantic
        else:
            print(f"{e}")


if __name__ == "__main__":
    main()
