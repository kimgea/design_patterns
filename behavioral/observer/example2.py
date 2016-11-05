from collections import defaultdict
from behavioral.observer.observer import (Observable, ObservableInstance)

class Item:
    complaints_observers = Observable()

    def __init__(self, name, stock=10, complaints=0):
        super(Item,self).__init__()
        self.name = name
        self._stock = stock
        self._complaints = complaints
        self.stock_observers = ObservableInstance()
        self.complaints_observers.set_key(self.key)


    def key(self):
        return Item.__name__ + self.name

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            value = 0
        notify = (self._stock is 0 and value > 0)
        self._stock = value
        if notify:
            self.stock_observers.notefy(
                obj    = self,
                subject     = self,
                old_stock   = 0,
                new_stock   = value)

    @property
    def complaints(self):
        return self._complaints

    @complaints.setter
    def complaints(self, value):
        if value < 0:
            value = 0
        prev_complaints = self._complaints
        notefy = self._complaints is not value
        self._complaints = value
        if notefy:
            self.complaints_observers.notefy(
                obj       = self,
                subject        = self,
                old_complaints = prev_complaints,
                new_complaints = self._complaints,
                extra          = "HAHAHA")

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class Shipment:         # TODO: make this a subject to and send messages to Customer class thath item has been sent
    def __init__(self, customer, item, auto_send=True):
        super(Shipment,self).__init__()
        self._customer = customer
        self._item = item
        if(auto_send):
            self.send()

    def send(self, *args, **kwargs):
        if self._item.stock > 0:
            self._item.stock -= 1
            print("Item: {0} is shipped to customer: {1}".format(self._item, self._customer))
            self._item.stock_observers.unregister(self.send)
        else:
            self._item.stock_observers.register(self.send)
            print("Item: {0} out of stock, customer {1} has to wait".format(self._item, self._customer))

    def __str__(self):
        return self._customer + " " + str(self._item)
    def __repr__(self):
        return self._customer + " " + str(self._item)


class Support:
    def __init__(self, name, item = None):
        if item is None:
            Item.complaints_observers.register(self.hadle_complaints)    # Registert toi all items
        else:
            item.complaints_observers.register(self.hadle_complaints, obj=item)    # Only register to input item
        self.name = name

    def hadle_complaints(self, *args, **kwargs):
        subject = kwargs.get("subject",False)
        if not subject:
            return
        if subject.complaints > 50:
            print("{0} from support has taken {1} of the shelf".format(self, subject))
            if kwargs.get("extra", None):
                print(kwargs["extra"])
        elif subject.complaints > 10:
            print("{0} from support has started investigation of {1}".format(self, subject))

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


def main_observer_sharing2():
    item1 = Item("Book", 9)
    item2 = Item("Movie", 0)

    print("Observers:", item1.stock_observers._observers, item2.stock_observers._observers)
    print("______________________")

    print ("Stock og item: {0} is {1}".format(item1, item1.stock))
    shipment1 = Shipment("customer1", item1)
    print ("Stock og item: {0} is {1}".format(item1, item1.stock))

    print("______________________")

    print ("Stock og item: {0} is {1}".format(item2, item2.stock))
    print("______________________")
    print("Observers:", item1.stock_observers._observers, item2.stock_observers._observers)
    print("______________________")
    shipment1 = Shipment("customer2", item2)
    print("______________________")
    print("Observers:", item1.stock_observers._observers, item2.stock_observers._observers)
    print("______________________")
    print ("Stock og item: {0} is {1}".format(item2, item2.stock))
    item2.stock = 10
    print ("Stock og item: {0} is {1}".format(item2, item2.stock))

    print("______________________")
    print("Observers:", item1.stock_observers._observers, item2.stock_observers._observers)

    print("______________________")
    print("______________________")
    print("Observers:", item1.complaints_observers._observers, item2.complaints_observers._observers)


    print("______________________")
    support1 = Support("Bush")
    support1 = Support("Obama", item2)
    print("Observers:", item1.complaints_observers._observers, item2.complaints_observers._observers)

    print("Setting 9 complaints")
    item1.complaints = 9
    print("Setting 11 complaints")
    item1.complaints = 11
    print("______________________")
    print("Setting 55 complaints")
    item2.complaints = 55



if __name__ == "__main__":
    main_observer_sharing2()