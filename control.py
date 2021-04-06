from abc import ABC, abstractmethod


class Control(ABC):

    @abstractmethod
    def control(self, lines):
        pass
