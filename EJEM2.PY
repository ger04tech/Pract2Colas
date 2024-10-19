from abc import ABC, abstractmethod


class Pila(ABC):

    @abstractmethod
    def push(self, obj):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def size(self):
        pass



class Cola(ABC):

    @abstractmethod
    def enqueue(self, obj):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def size(self):
        pass


class Deque(ABC):

    @abstractmethod
    def insertFirst(self, obj):
        pass

    @abstractmethod
    def insertLast(self, obj):
        pass

    @abstractmethod
    def removeFirst(self):
        pass

    @abstractmethod
    def removeLast(self):
        pass

    @abstractmethod
    def size(self):
        pass
