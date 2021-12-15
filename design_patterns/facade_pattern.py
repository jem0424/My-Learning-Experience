class Facade(object):
    def __init__(self):
        self.report_a = ReportA()
        self.report_b = ReportB()
        self.report_c = ReportC()

    def create(self):
        results = list()
        results.append(self.report_a.get_data())
        results.append(self.report_b.get_data())
        results.append(self.report_c.get_data())
        return results


class ReportA(object):
    @staticmethod
    def get_data():
        return dict(A="A")


class ReportB(object):
    @staticmethod
    def get_data():
        return dict(B="B")


class ReportC(object):
    @staticmethod
    def get_data():
        return dict(C="C")


if __name__ == '__main__':
    facade = Facade()
    result = facade.create()
    print("the result = %s" % result)