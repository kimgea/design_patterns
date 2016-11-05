"""

    This simpler and better in that it removes observer class and uses callback insetad. This can be done in all earlier examples to

    It is however a more complex example

    It is also more data driven, changes happends when data is changed

"""

#TODO: make a multi subject too.... dict  (split on types of item - name?)

from enum import Enum

from behavioral.observer.old.reuse import (ObservableSelectableGlobal)



class Item(ObservableSelectableGlobal):
    #_observers = defaultdict(set)   # Add this place for common callbacks for all Items

    class RegistrVariables(Enum):
        stock = 0
        complaints = 1

    def __init__(self, stock=10, complaints=0):
        super(Item,self).__init__()
        self.name = "Book"
        self._stock = stock
        self._complaints = complaints
        #self._callbacks = defaultdict(set) # Add this place to keep calbacks local to specirfic item instances

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            return
        if self._stock is 0 and value > 0:
            self._stock = value
            self.notefy(self.RegistrVariables.stock)
        else:
            self._stock = value

    @property
    def complaints(self):
        return self._complaints

    @complaints.setter
    def complaints(self, value):
        if value < 0:
            value = 0
        notefy = self._complaints is not value
        self._complaints = value
        if notefy:
            self.notefy(self.RegistrVariables.complaints, extra="HAHAHA")

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
            self._item.unregister(self._item.RegistrVariables.stock,self.send)
        else:
            self._item.register(self._item.RegistrVariables.stock,self.send)
            print("Item: {0} out of stock, customer {1} has to wait".format(self._item, self._customer))

    def __str__(self):
        return self._customer + " " + str(self._item)
    def __repr__(self):
        return self._customer + " " + str(self._item)


class Support:
    def __init__(self, name):
        Item().register(Item.RegistrVariables.complaints, self.hadle_complaints)    # NB: this will not work if observer list is local
        self.name = name

    def hadle_complaints(self, subject, *args, **kwargs):
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




def main():
    item1 = Item(9)
    item2 = Item(0)


    print("Observers", item1._observers, item2._observers)
    print("______________________")

    print ("Stock og item: {0} is {1}".format(item1, item1.stock))
    shipment1 = Shipment("customer1", item1)
    print ("Stock og item: {0} is {1}".format(item1, item1.stock))

    print("______________________")

    print ("Stock og item: {0} is {1}".format(item2, item2.stock))
    print("______________________")
    print("Observers", item1._observers, item2._observers)
    print("______________________")
    shipment1 = Shipment("customer2", item2)
    print("______________________")
    print("Observers", item1._observers, item2._observers)
    print("______________________")
    print ("Stock og item: {0} is {1}".format(item2, item2.stock))
    item2.stock = 10
    print ("Stock og item: {0} is {1}".format(item2, item2.stock))

    print("______________________")
    print("Observers", item1._observers, item2._observers)


    print("______________________")
    support1 = Support("Frank")

    item1.complaints = 9
    item1.complaints = 11
    print("______________________")
    item2.complaints = 55

if __name__ == "__main__":
    main()