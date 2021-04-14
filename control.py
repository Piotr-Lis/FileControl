from abc import ABC, abstractmethod
from file import File


class EmptyFile(Exception):
    pass


class Control(ABC):

    @abstractmethod
    def control(self, file, met='r'):
        pass

    def file_gen(self, file, met='r'):
        with File(file, met) as file:
            for line in file:
                yield line
