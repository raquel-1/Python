#!/usr/bin/env python3
from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def my_validator(self) -> 'MiModelo':
        # aquí tienes acceso a self.campo1, self.campo2...
        # si algo falla lanzas un ValueError
        return self  # siempre al final


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    # Block 1: VALID station
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30)
        )
        print("\n Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print("Crew:", station.crew_size, "people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            "Status:",
            "Operational" if station.is_operational else "No Operational"
        )
    except Exception as e:
        print(f"\n{e}")

    # Block 2: INVALID station
    print("\n========================================")
    print("Expected validation error:")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=42,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30)
        )
        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print("Crew:", station.crew_size, "people")
        print("Power:", station.power_level)
        print("Oxygen:", station.oxygen_level)
        print(
            "Status:",
            "Operational" if station.is_operational else "Not Operational"
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
