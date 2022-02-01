from abc import ABCMeta, abstractmethod


class DataSourceInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(audience):
        pass

    @staticmethod
    @abstractmethod
    def unsubscribe(audience):
        pass

    @staticmethod
    @abstractmethod
    def notify(audience):
        pass


class DataSource(DataSourceInterface):

    def __init__(self):
        self._audience = set()

    def subscribe(self, audience):
        self._audience.add(audience)

    def unsubscribe(self, audience):
        self._audience.remove(audience)

    def notify(self, *args):
        for member in self._audience:
            member.notify(self, *args)


class AudienceInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args):
        pass


class Audience(AudienceInterface):
    def __init__(self, member):
        member.subscribe(self)

    def notify(self, observable, *args):
        print(f"Member ID:{id(self)} received {args}")


if __name__ == '__main__':
    ddos = DataSource()
    paul = Audience(ddos)
    joel = Audience(ddos)
    ddos.notify("First notification, Some numbers")
    ddos.unsubscribe(joel)
    ddos.notify("second notification, Some other message")


