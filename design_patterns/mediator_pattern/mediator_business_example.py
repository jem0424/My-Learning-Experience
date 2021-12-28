from abc import ABCMeta, abstractmethod


class MediatorInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def ddos_method():
        pass

    @staticmethod
    @abstractmethod
    def nse_method():
        pass


class Mediator(MediatorInterface):
    def __init__(self):
        self.ddos = DDOS()
        self.nse = NSE()

    def ddos_method(self):
        return self.ddos.ddos_method()

    def nse_method(self):
        return self.nse.nse_method()


class DDOS(MediatorInterface):
    def ddos_method(self):
        return "here is some ddos data"

    def nse_method(self):
        pass


class NSE(MediatorInterface):
    def ddos_method(self):
        pass

    def nse_method(self):
        return "here is some nse data"


if __name__ == '__main__':
    mediator = Mediator()
    data = mediator.nse_method()
    print(f"DDOS <--> {data}")
    data = mediator.ddos_method()
    print(f"NSE <--> {data}")