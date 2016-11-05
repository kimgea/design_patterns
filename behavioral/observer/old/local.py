"""

Subject(Auctioner) and observers(Bidders) are localy binded.
A new Subject class dos not contain the others observers

"""



class Subject:
    def __int__(self):
        self._observers = set([])

    def register(self, observer):
        self._observers.add(observer)

    def unregister(self, observer):
        if observer in self._observers:
            del self._observers[observer]

    def notefy_observers(self):
        for observer in self._observers:
            observer.notefy()


class Observer:
    """
    NOTE: Observer could be exhanged with registering callback in subject
    """
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notefy(self):
        pass





class Auctioner(Subject):
    def __init__(self):
        super().__int__()
        self._current_bid = 0
        self._bid_ovner = None

    def request_bidd(self):
        self.notefy_observers()

    def bidding(self):
        while 1:
            bid = self._current_bid
            self.request_bidd()
            if self._current_bid is bid:
                break
        if self._bid_ovner is not None:
            print("Winner is {0} with a bid of {1}".format(self._bid_ovner, self._current_bid))


    def bid(self, bid, ovner):
        if bid <= self._current_bid:
            return False
        print("{0} bid {1}".format(ovner, bid))
        self._current_bid = bid
        self._bid_ovner = ovner

    def min_bid(self):
        return self._current_bid + 10

    @property
    def bid_ovner(self):
        return self._bid_ovner

    
    
class Bidder(Observer):
    def __init__(self,name, auctioner, max_bid=0):
        super(Bidder, self).__init__(auctioner)
        self.name = name
        self.max_bid = max_bid

    def notefy(self):
        if self.max_bid <= self.subject.min_bid():
            return
        if self.subject.bid_ovner is self:
            return
        bid = int(max(  self.subject.min_bid() + 10,
                    self.subject.min_bid() + (self.max_bid - self.subject.min_bid()) * 0.1))
        if bid > self.max_bid:
            return
        self.subject.bid(bid, self)

    def __str__(self):
        return self.name


def main():
    auctioner = Auctioner()

    bidder1 = Bidder("John Snow", auctioner, 150)
    bidder1 = Bidder("Kin John", auctioner, 300)
    bidder1 = Bidder("Reskin", auctioner, 250)

    auctioner.bidding()


if __name__ == "__main__":
    main()