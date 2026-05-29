#!/usr/bin/env python3

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


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
