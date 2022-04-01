from abc import ABCMeta, abstractmethod


class ReportInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def run_report():
        pass


class ReportFactory:

    @staticmethod
    def get_report(report):
        if report == "ddos":
            return DDOS()
        if report == "netarch":
            return NetArch()
        if report == "nse":
            return NetStatEngine()


class DDOS(ReportInterface):
    def __init__(self):
        self.results = "DDOS data"

    def run_report(self):
        return {"results": self.results}


class NetArch(ReportInterface):
    def __init__(self):
        self.results = "NetArch data"

    def run_report(self):
        return {"results": self.results}


class NetStatEngine(ReportInterface):
    def __init__(self):
        self.results = "NSE data"

    def run_report(self):
        return {"results": self.results}


if __name__ == '__main__':
    ddos = ReportFactory().get_report("ddos")
    netarch = ReportFactory().get_report("netarch")
    nse = ReportFactory().get_report("nse")
    print(ddos.run_report())
    print(netarch.run_report())
    print(nse.run_report())


