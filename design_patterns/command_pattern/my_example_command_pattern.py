import random
from abc import ABCMeta, abstractmethod


class PlayInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass


class Coach:
    def __init__(self):
        self._plays = {}

    def register(self, name, play):
        self._plays[name] = play

    def call(self, name):
        if name in self._plays.keys():
            self._plays[name].execute()
        else:
            print(f"{name} p lay not registered in playbook")


class Quarterback:

    @staticmethod
    def execute_pass():
        print(f"Execution pass: gain for {random.randrange(0,40)}")

    @staticmethod
    def execute_run():
        print(f"Executing run: gain for {random.randrange(0,40)}")


class PassPlay(PlayInterface):
    def __init__(self, player):
        self._player = player

    def execute(self):
        self._player.execute_pass()


class RunPlay(PlayInterface):
    def __init__(self, player):
        self._player = player

    def execute(self):
        self._player.execute_run()


if __name__ == '__main__':
    quarterback = Quarterback()
    play1 = PassPlay(quarterback)
    play2 = RunPlay(quarterback)
    coach = Coach()
    coach.register("WR post", play1)
    coach.register("RB pitch", play2)
    coach.call("WR post")
    coach.call("RB pitch")
    coach.call("field goal")

