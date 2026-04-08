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


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError("Invalid plant name to water")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    plants = [
        ["Tomato", "Lettuce", "Carrots"],
        ["Tomato", "lettuce"]
        ]
    for arr in plants:
        print("Testing valid plants...")
        print("Opening watering system")
        try:
            for str in arr:
                water_plant(str)
        except Exception as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system")
            print("")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
