#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.processed_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # standard
    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data to output")
        # get the oldest item[0] and remove
        data = self.storage.pop(0)
        # get current rank and counter+=1
        rank = self.processed_count
        self.processed_count += 1
        return (rank, data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # is number(int, float)
        if isinstance(data, (int, float)):
            return True
        # is list
        elif isinstance(data, list):
            # check if all are number(int, float)
            for num in data:
                if not isinstance(num, (int, float)):
                    return False
            return True
        # is (string, dict, etc.)
        else:
            return False

    def ingest(self, data: Any) -> None:
        # call self.validate() raise if is nor int/float
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for num in data:
                self.storage.append(str(num))
        else:
            self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
        else:
            self.storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            # keys exist?
            return "log_level" in data and "log_message" in data
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                # check both keys
                if "log_level" not in item or "log_message" not in item:
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                format = f"{item['log_level']}: {item['log_message']}"
                self.storage.append(format)
        else:
            format = f"{data['log_level']}: {data['log_message']}"
            self.storage.append(format)


if __name__ == "__main__":
    print("\n=== Code Nexus - Data Processor ===")
    # Numeric----------------------------------
    print("\n\nTesting Numeric Processor...")
    num_proces = NumericProcessor()
    print(f"Trying to validate input '42': {num_proces.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proces.validate('Hello')}")
    try:
        # invalid ingestion
        print(
            "Test invalid ingestion of string",
            " 'foo' without prior validation:"
        )
        num_proces.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    # correct ingestion lis[int]
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proces.ingest(num_data)
    print("Extracting 3 values...")
    for i in range(3):
        rank, val = num_proces.output()
        print(f"Numeric value {rank}: {val}")
    # Text-------------------------------------
    print("\n\nTesting Text Processor...")
    text_proces = TextProcessor()
    print(f"Trying to validate input '42': {text_proces.validate(42)}")
    str_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {str_data}")
    text_proces.ingest(str_data)
    print("Extracting 1 value...")
    rank, val = text_proces.output()
    print(f"Text value {rank}: {val}")
    # Log--------------------------------------
    print("\n\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
