from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Streem is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Streem is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NeetworkStream(Stream):
    def read(self):
        print("Reading data from network")

class MemoryStream(Stream):
    def read(self):
        print("Reading from memory")
        
stream = MemoryStream()
stream.open()

