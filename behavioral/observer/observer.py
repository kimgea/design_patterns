
from collections import defaultdict

#TODO: rename obj to something more descriptive
#TODO: make test cases to test everything

class Observable:

    def __init__(self, observers=defaultdict(set), shared=False):
        if not observers and not shared:
            self._observers = defaultdict(set)
        else:
            self._observers = observers
        self._key = None
        self._remove = set([])
        self.notefy_key_only = False

    def _call_instance(self, obj):
        if self._key is not None:
            return getattr(obj, self._key)()
        else:
            return None

    def set_key(self, key):
        """
        Key makes it possible for class/glovbal observer lists to be accessed by a key
        Thath way not all observers need to bee called.

        :param key: callback function to be used as a key
        :return:
        """
        self._key = key.__name__

    def register(self, callback, obj=None):
        """

        :param callback:
        :param obj: If set then observer is only notifyed when key from obj is used for notification
        :return:
        """
        if obj is not None:
            self._observers[self._call_instance(obj)].add(callback)
        else:
            self._observers[None].add(callback)

    def unregister(self, callback, obj=None):
        """
        :param callback:
        :param obj:
        :return:
        """
        key = None if obj is None else self._call_instance(obj)
        if callback in self._observers[key]:
            self._observers[key].remove(callback)

    def unregister_everywhere(self, callback):
        """
        Unregister observer for every key
        :param callback:
        :return:
        """
        for key, _ in self._observers.items():
            if callback in self._observers[key]:
                self._observers[key].remove(callback)

    def unregister_all(self):
        """
        Unregister all observers
        :return:
        """
        self._observers.clear()

    def notefy(self, obj=None, **kwargs):
        """
        Note: Could have iterated ove a copied list instead of placing unregister requests in a temp list like now... less code thath way
        """
        notefied = set()

        # Notefy those observing a specific key
        if obj is not None:
            for callback in list(self._observers[self._call_instance(obj)]):
                if callback in notefied:
                    continue
                callback(self, **kwargs)
                notefied.add(callback)

        # Notefy those observing all
        if not self.notefy_key_only or obj is None:
            for callback in list(self._observers[None]):
                if callback in notefied:
                    continue
                callback(self, **kwargs)
                notefied.add(callback)

    def notefy_all(self, **kwargs):
        """
        Notefy all observers
        :param kwargs:
        :return:
        """
        notefied = set()
        for _, val in self._observers.items():
            for callback in list(val):
                if callback in notefied:
                    continue
                callback(self, **kwargs)
                notefied.add(callback)



class ObservableInstance(Observable):
    def __init__(self):
        super(ObservableInstance, self).__init__()

class ObservableAll(Observable):    # TODO: should this also get a key???
    def __init__(self):
        super(ObservableAll, self).__init__(shared=True)


class ObservableShared(Observable): # TODO: split if class level gets a key and instance level sos not
    def __init__(self, observers):
        super(ObservableShared, self).__init__(observers=observers, shared=True)



#######################################################################################################





