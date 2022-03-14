from abc import ABC, abstractmethod


class DataSource(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """

    def run_template(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """

        self.fetch_db()
        self.aggregate()
        self.parse()
        self.validate()
        self.serialize()
        self.export()
        self.close_connections()

    # These operations already have implementations.

    def fetch_db(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def parse(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def export(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def aggregate(self) -> None:
        pass

    @abstractmethod
    def serialize(self) -> None:
        pass

    # These are "hooks." Subclasses may override them, but it's not mandatory
    # since the hooks already have default (but empty) implementation. Hooks
    # provide additional extension points in some crucial places of the
    # algorithm.

    def validate(self) -> None:
        pass

    def close_connections(self) -> None:
        pass


class DDOS(DataSource):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def aggregate(self) -> None:
        print("DDOS says: Implemented Operation1")

    def serialize(self) -> None:
        print("DDOS says: Implemented Operation2")


class NSE(DataSource):
    """
    Usually, concrete classes override only a fraction of base class'
    operations.
    """

    def aggregate(self) -> None:
        print("NSE says: Implemented Operation1")

    def serialize(self) -> None:
        print("NSE says: Implemented Operation2")

    def validate(self) -> None:
        print("NSE says: Overridden Hook1")


def client_code(abstract_class: DataSource) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """

    # ...
    abstract_class.run_template()
    # ...


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(DDOS())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(NSE())