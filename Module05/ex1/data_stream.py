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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list) -> None:
    for element in stream:           # recorre cada elemento del stream
        handled = False              # aún nadie lo ha procesado
        
        for proc in self.processors: # prueba cada procesador de la lista
            if proc.validate(element):   # ¿este procesador puede con él?
                proc.ingest(element)     # sí → lo ingesta
                handled = True           # marcamos que ya fue procesado
                break                    # para, no hace falta seguir probando
        
        if not handled:              # si nadie pudo procesarlo...
            print(f"DataStream error - Can't process element in stream: {element}")


if __name__ == "__main__":
