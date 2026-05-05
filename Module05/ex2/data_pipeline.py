#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    """
    The Protocol remains empty because it only defines the
    structural interface (duck typing) that plugins must implement
    """
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        # get class__name__("NumericProcessor" -> "Numeric Processor")
        name = type(proc).__name__.replace("Processor", " Processor")
        print(f"Registering {name}")
        # store object in DataStream
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        # self.processors = [NumericProcessor,TextProcessor,LogProcessor]
        for pro in self.processors:
            # list of nb items extract from storage
            data = []
            # nb loops for each processor
            for _ in range(nb):
                # if there are no items left, bye
                if len(pro.storage) == 0:
                    break
                # pro.output() delete from storage, returns (rank,value)
                data.append(pro.output())
                # save that (rank,value) to the data[]
            if data:
                # send de data[(0,"hi"),(1, "bye")]
                plugin.process_output(data)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        for tup in data:
            values.append(str(tup[1]))
        joined_str = ",".join(values)
        print(f"CSV Output:\n{joined_str}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        yei = []
        for tup in data:
            yei.append(f'"item_{tup[0]}": "{tup[1]}"')
        joined_str = ",".join(yei)
        print(f"JSON Output:\n{{{joined_str}}}")


if __name__ == "__main__":
    print("====== Code Nexus - Data Pipeline ======\n")
    data_stream = DataStream()
    print("Initialize Data Stream...\n")
    data_stream.print_processors_stats()

    print("\nRegistering Processors:")
    num_pro = NumericProcessor()
    text_pro = TextProcessor()
    log_pro = LogProcessor()
    data_stream.register_processor(num_pro)
    data_stream.register_processor(text_pro)
    data_stream.register_processor(log_pro)

    print("\nSend first batch of data on stream...")
    data_list = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}],
        [{'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(data_list)
    data_stream.process_stream(data_list)
    print("")
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    print("")
    data_stream.print_processors_stats()

    data_list2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {data_list2}")
    data_stream.process_stream(data_list2)
    print("")
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    print("")
    data_stream.print_processors_stats()
