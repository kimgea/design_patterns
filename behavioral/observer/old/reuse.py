from collections import defaultdict

# TODO: Add an observable simple pattern
# TODO: Add an extended ObservableSelectable with posibility of having class variable list but
# TODO      have diferent observer list depending on key. Instances with same key will share observers

"""
    IDEAS:
        - Try to make an composition version instead of inheritance... how will classvariables work there?
"""



class ObservableSelectableBase:
    """

    """

    """
        - Subclasses thath dos not overwrite this will share all ther observers among all their instances
        - Overwtie in subclass in same place as a class variable to lett subclass of same class share
            observers among all its instances
        - Overwrite this in subclass __init__ to keep observers local to each instance
    """


    def __init__(self):
        self._running = False
        self._remove = set([])

    def register(self, variable, callback):
        self._observers[variable].add(callback)

    def unregister(self, variable, callback):
        if self._running:
            self._remove.add(callback)
        else:
            if callback in self._observers[variable]:
                self._observers[variable].remove(callback)

    def notefy(self, variable, *args, **kwargs):
        self._running = True
        for callback in self._observers[variable]:
            callback(self, *args, **kwargs)
        self._running = False
        for callback in self._remove:
            self.unregister(variable, callback)

class ObservableSelectableGlobal(ObservableSelectableBase):
    """
    _observers = defaultdict(set):
        - Subclasses thath dos not overwrite this will share all ther observers among all their instances
        - Overwtie in subclass in same place as a class variable to lett subclass of same class share
            observers among all its instances, but not instances of other subclasses of this class
    """
    _observers = defaultdict(set)

class ObservableSelectableLocal(ObservableSelectableBase):
    """
        Observers are local to each instance
    """
    def __init__(self):
        super(ObservableSelectableLocal,self).__init__()
        self._observers = defaultdict(set)