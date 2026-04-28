#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        # count how many have been printed via output()
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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        # get class__name__("NumericProcessor" -> "Numeric Processor")
        name = type(proc).__name__.replace("Processor", " Processor")
        print(f"Registering {name}")
        # store object in DataStream
        self.processors.append(proc)

    def process_stream(self, stream: list) -> None:
        # iterate through each element of stream[]
        for element in stream:
            # processed????
            is_processed = False
            # test each processor(object) on the list
            for proc in self.processors:
                # use object-specific methods
                if proc.validate(element):
                    proc.ingest(element)
                    is_processed = True
                    # found one to deal with it out. Bye
                    break
            # nobody processed it
            if not is_processed:
                print(
                    "DataStream error - Can't process "
                    f"element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for pro in self.processors:
                name = type(pro).__name__.replace("Processor", " Processor")
                total = pro.processed_count + len(pro.storage)
                print(
                    f"{name}: total {total} items processed,"
                    f" remaining {len(pro.storage)} on processor"
                )


if __name__ == "__main__":
    print("====== Code Nexus - Data Stream ======\n")
    data_stream = DataStream()
    print("Initialize Data Stream...")
    data_stream.print_processors_stats()

    # record ONLY numbers
    print("")
    num_pro = NumericProcessor()
    data_stream.register_processor(num_pro)

    data_list = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access!'}],
        [{'log_level': 'INFO', 'log_message': 'User wil is User wil is'}],
        42,
        ['Hi', 'five']
    ]
    # send the data, but text and logs error (are not registered)
    print("\nSend first batch of data on stream...")
    print(data_list)
    data_stream.process_stream(data_list)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors:")
    text_pro = TextProcessor()
    log_pro = LogProcessor()
    data_stream.register_processor(text_pro)
    data_stream.register_processor(log_pro)

    print("\nSend the same batch again")
    data_stream.process_stream(data_list)
    data_stream.print_processors_stats()

    # take out some data to show that the "remaining" counter--
    print(
        "\nConsume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
    )
    # take out 3 numbers
    num_pro.output()
    num_pro.output()
    num_pro.output()
    # take out 2 text
    text_pro.output()
    text_pro.output()
    # take out 1 log
    log_pro.output()

    data_stream.print_processors_stats()
