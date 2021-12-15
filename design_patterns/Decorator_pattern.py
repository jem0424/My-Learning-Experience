class DataSource:
    def write_data(self, data):
        pass

    def read_data(self) -> str:
        pass


class FileDataSource(DataSource):
    def __init__(self):
        pass

    def write_data(self, data):
        with open("demofile2.txt", "w") as f:
            f.write(data)

    def read_data(self) -> str:
        with open('demofile2.txt', 'r') as reader:
            return reader.read()


class DataSourceDecorator(DataSource):

    def __init__(self, DataSource):
        self._wrappee = DataSource

    def write_data(self, data):
        self._wrappee.write_data(data)

    def read_data(self) -> str:
        return self._wrappee.read_data()
