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
    def my_validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must begin with the letters “AC”")
        elif (
            self.contact_type == ContactType.PHYSICAL and not self.is_verified
        ):
            raise ValueError("The report must be verified")
        elif (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        elif self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("It must include the message received")
        # always at the end
        return self


def main() -> None:
    # Block 1: VALID station
    try:
        contac1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 15, 10, 30),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print("\nAlien Contact Log Validation")
        print("========================================")
        print("Valid  contact report:")
        print("ID:", contac1.contact_id)
        print("Type:", contac1.contact_type.value)
        print("Location:", contac1.location)
        print(f"Signal: {contac1.signal_strength}/10")
        print(f"Duration: {contac1.duration_minutes} minutes")
        print(f"Witnesses: {contac1.witness_count}")
        print(f"Message: '{contac1.message_received}'")
    except Exception as e:
        print(f"\n{e}")

    # Block 2: INVALID station
    print("\n========================================")
    print("Expected validation error:")
    try:
        contac2 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 15, 10, 30),
            location=" Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print("\nAlien Contact Log Validation")
        print("========================================")
        print("Valid  contact report:")
        print("ID:", contac2.contact_id)
        print("Type:", contac2.contact_type.value)
        print("Location:", contac2.location)
        print(f"Signal: {contac2.signal_strength}/10")
        print(f"Duration: {contac2.duration_minutes} minutes")
        print(f"Witnesses: {contac2.witness_count}")
        print(f"Message: '{contac2.message_received}'")
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
