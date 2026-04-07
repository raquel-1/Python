#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except Exception as e:
        print(f"Caught PlantError: {e}")
    print("")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except Exception as e:
        print(f"Caught WaterError: {e}")
    print("")
    print("Testing catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
        ]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("")
    print("All custom error types work correctly!")
