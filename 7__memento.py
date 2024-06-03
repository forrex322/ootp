class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print(f"Встановлення стану: {state}")
        self._state = state

    def get_state(self):
        return self._state

    def save_to_memento(self):
        print("Збереження стану в Memento")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Відновлення стану з Memento: {self._state}")

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

originator = Originator()
caretaker = Caretaker()

originator.set_state("Стан 1")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("Стан 2")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("Стан 3")
caretaker.add_memento(originator.save_to_memento())

originator.restore_from_memento(caretaker.get_memento(1))
originator.restore_from_memento(caretaker.get_memento(0))
