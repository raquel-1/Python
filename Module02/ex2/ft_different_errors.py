#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 5  # type: ignore[operator]
    else:
        return


def test_error_types() -> None:
    for i in range(0, 5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as ve:
            print(f"Caught ValueError: {ve}")
        except ZeroDivisionError as zde:
            print(f"Caught ZeroDivisionError: {zde}")
        except FileNotFoundError as fnfe:
            print(f"Caught FileNotFoundError: {fnfe}")
        except TypeError as te:
            print(f"Caught TypeError: {te}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("")
    print("All error types tested successfully!")
