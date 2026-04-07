#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    lis = ["25", "abc", "100", "-50"]
    for i in lis:
        try:
            print("")
            print(f"Input data is '{i}'")
            num = input_temperature(i)
            if num < 0:
                raise ValueError(f"{i} is too cold for plants (min 0°C)")
            elif num > 40:
                raise ValueError(f"{i} is too hot for plants (max 40°C)")
            else:
                print(f"Temperature is now {i}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("")
    print("All tests completed - program didn't crash!")
