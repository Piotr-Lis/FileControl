from abc import ABC, abstractmethod
from file import File


class EmptyFile(Exception):
    pass


class Control(ABC):

    @abstractmethod
    def control(self, file, met='r'):
        pass

    def read_lines(self, file, met='r'):
        with File(file, met) as file:
            lines = file.readlines()
        if not lines:
            raise EmptyFile('File is empty.')
        return lines
