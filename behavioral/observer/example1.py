from collections import defaultdict
from behavioral.observer.observer import (Observable, ObservableAll, ObservableShared, ObservableInstance)


class SharedData:
    _all_class_instance_observers = Observable()        # This option shares observers among all instancs of this class
    __selectd_observer_list = defaultdict(set)

    def __init__(self, stock=10, complaints=0):
        self.name = "Book"
        self._stock = stock
        self._complaints = complaints

        self._all_observers = ObservableAll()   # This option shares observers with all places Observable is called with this option. D
        self._instance_observers = ObservableInstance()         # This option keeps list of observers local to class instance they are added to

        self._shared1_class_instances_observers = ObservableShared(self.__selectd_observer_list) # The option done for method1 and method2
        self._shared2_class_instances_observers = ObservableShared(self.__selectd_observer_list) # shares observers between each other over all instances, but only for this class




def main_observer_sharing():
    """
    NB: Adding to observer list like below is not correct. A calback function must be added, not a type
    """
    item1 = SharedData(9)
    item2 = SharedData(0)

    item1._all_class_instance_observers.register(1)
    item2._all_class_instance_observers.register(2)

    item1._instance_observers.register(1)
    item2._instance_observers.register(2)

    item1._all_observers.register(1)
    item2._all_observers.register(2)

    obs = Observable(shared=True)
    obs.register(3)

    item1._shared1_class_instances_observers.register(1)
    item2._shared1_class_instances_observers.register(2)
    item1._shared2_class_instances_observers.register(3)
    item2._shared2_class_instances_observers.register(4)

    print("instance_observers")
    print(item1._instance_observers._observers, item2._instance_observers._observers)
    print("shared_class_instances_observers")
    print(item1._shared1_class_instances_observers._observers, item2._shared1_class_instances_observers._observers)
    print(item1._shared2_class_instances_observers._observers, item2._shared2_class_instances_observers._observers)
    print("all_class_instance_observers")
    print(item1._all_class_instance_observers._observers, item2._all_class_instance_observers._observers)
    print("all_observers")
    print(item1._all_observers._observers, item2._all_observers._observers)



if __name__ == "__main__":
    main_observer_sharing()