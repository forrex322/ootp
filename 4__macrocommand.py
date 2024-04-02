import abc


class Command(abc.ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abc.abstractmethod
    def process(self):
        ...


class FirstCommand(Command):
    def process(self):
        self.receiver.do_something(message=self.__class__.__name__ + ".")


class SecondCommand(Command):
    def process(self):
        self.receiver.do_something(message=self.__class__.__name__ + ".")


class Receiver:
    def do_something(self, message):
        print(self.__class__.__name__ + " retrieve " + message)


class Invoker:
    def __init__(self):
        self.cmd = None

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()


if __name__ == "__main__":
    invoker = Invoker()
    receiver = Receiver()

    first_command = FirstCommand(receiver=receiver)
    invoker.command(cmd=first_command)
    invoker.execute()

    second_command = SecondCommand(receiver=receiver)
    invoker.command(cmd=second_command)
    invoker.execute()
