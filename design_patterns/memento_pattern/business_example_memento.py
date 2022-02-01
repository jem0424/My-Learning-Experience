from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters



class Accountant():
    _state = None

    def __init__(self, state: str):
        self._state = state
        print(f"Acccountant: My initial state is: {self._state}")

    def track_report(self) -> None:
        print("Accountant: creating report state")
        self._state = self._generate_random_string(30)
        print(f"Report state changed to {self._state}")

    def _generate_random_string(self, length):
        return "".join(sample(ascii_letters, length))

    def save(self):
        return Report(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"Accountant: Report state changed to: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class Report(Memento):
    def __init__(self, state:str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

class Caretaker:
    def __init__(self, accountant):
        self._reports = []
        self._accountant = accountant

    def backup(self) -> None:
        print("Saving Accountant's State")
        self._reports.append(self._accountant.save())

    def undo(self):
        if not len(self._reports):
            return

        memento = self._reports.pop()
        print(f"Restoring state to {memento.get_name()}")
        try:
            self._accountant.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Here is the list of Report mementos:")
        for memento in self._reports:
            print(memento.get_name())


if __name__ == "__main__":
    accountant = Accountant("Zero State")
    caretaker = Caretaker(accountant)

    caretaker.backup()
    accountant.track_report()

    caretaker.backup()
    accountant.track_report()

    caretaker.backup()
    accountant.track_report()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()
