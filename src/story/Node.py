from abc import ABC, abstractmethod
class Node(ABC):
    @abstractmethod
    def execute(self, player):
        pass