"""
Globaly binded. All Subject instances has the same observer list
Do not inherit from Subject if inherited classes shall not share observer list
"""

class Subject:
    _observers = set([])

    def register(self, observer):
        self._observers.add(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notefy_observers(self):
        for observer in self._observers:
            observer.notefy()


class Observer:
    """
    NOTE: Observer could be exhanged with registering callback in subject
    """
    def __init__(self, name, subject):
        self.subject = subject
        self.subject.register(self)
        self.name = name

    def notefy(self):
        print(self.name)

def main():
    subject = Subject()

    observer1 = Observer("1",subject)
    observer2 = Observer("2",subject)
    observer3 = Observer("3",subject)

    subject.notefy_observers()
    print("__________________")

    subject2 = Subject()
    subject2.notefy_observers()
    print("__________________")

    subject2.unregister(observer1)

    subject.notefy_observers()

if __name__ == "__main__":
    main()