#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    lis = ["25", "abc"]
    for i in lis:
        try:
            print(f"Input data is '{i}'")
            input_temperature(i)
            print(f"Temperature is now {i}°C")
            print("")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
    print("")
    print("All tests completed - program didn't crash!")
