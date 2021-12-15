import random
from abc import ABCMeta, abstractmethod


class QueryInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass


class Creator:
    def __init__(self):
        self._queries = {}

    def register(self, name, report):
        self._queries[name] = report

    def call(self, name):
        if name in self._queries.keys():
            self._queries[name].execute()
        else:
            print(f"{name} not registered in query book")


class QueryController:

    @staticmethod
    def run_query(query):
        print(f"Running query:{query}")

    # @staticmethod
    # def run_ddos_query():
    #     print("Running report 2")


class WAFReport(QueryInterface):
    def __init__(self, controller):
        self._controller = controller

    def execute(self):
        self._controller.run_query("select statement")


class DdosReport(QueryInterface):
    def __init__(self, controller):
        self._controller = controller

    def execute(self):
        self._controller.run_query("select statement")


if __name__ == '__main__':
    query_controller = QueryController()
    waf_report = WAFReport(query_controller)
    ddos_report = DdosReport(query_controller)
    creator = Creator()
    creator.register("waf query", waf_report)
    creator.register("ddos query", ddos_report)
    creator.call("waf query")
    creator.call("ddos query")
    creator.call("nse query")

