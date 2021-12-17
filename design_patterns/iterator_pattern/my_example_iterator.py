from abc import ABCMeta, abstractmethod


class IteratorInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        pass

    @staticmethod
    @abstractmethod
    def next():
        pass


class ReportCollection(IteratorInterface):
    #concrete Iterator class
    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("EndOfIterator, End of list")

    def has_next(self):
        return self.index < len(self.aggregates)


class ReportInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def run():
        pass


class Report(ReportInterface):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running {self.name} Report")


if __name__ == '__main__':
    reports = [Report("ddos"), Report("netarch"), Report("nse")]
    iterable = ReportCollection(reports)
    while iterable.has_next():
        iterable.next().run()


