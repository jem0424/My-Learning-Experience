import random
from abc import ABCMeta, abstractmethod


class ReportInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass


class Creator:
    def __init__(self):
        self._reports = {}

    def register(self, name, report):
        self._reports[name] = report

    def call(self, name):
        if name in self._reports.keys():
            self._reports[name].execute()
        else:
            print(f"{name} not registered in report book")


class Controller:

    @staticmethod
    def run_waf_report():
        print("Running report 1")

    @staticmethod
    def run_ddos_report():
        print("Running report 2")


class WAFReport(ReportInterface):
    def __init__(self, controller):
        self._controller = controller

    def execute(self):
        self._controller.run_waf_report()


class DdosReport(ReportInterface):
    def __init__(self, controller):
        self._controller = controller

    def execute(self):
        self._controller.run_ddos_report()


if __name__ == '__main__':
    controller = Controller()
    waf_report = WAFReport(controller)
    ddos_report = DdosReport(controller)
    creator = Creator()
    creator.register("waf report", waf_report)
    creator.register("ddos report", ddos_report)
    creator.call("waf report")
    creator.call("ddos report")
    creator.call("nse report")

