from abc import ABCMeta, abstractmethod


class Context:
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def promote_request(self):
        self._state.promote()


class State(metaclass=ABCMeta):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def promote(self) -> None:
        pass


class OpenState(State):
    def promote(self) -> None:
        print("Promoting to In Progress State")
        self.context.transition_to(InProgressState())


class InProgressState(State):
    def promote(self) -> None:
        print("Promoting to Closed State")
        self.context.transition_to(ClosedState())


class ClosedState(State):
    def promote(self) -> None:
        print("reached last state")


if __name__ == '__main__':
    context = Context(OpenState())
    context.promote_request()
    context.promote_request()
