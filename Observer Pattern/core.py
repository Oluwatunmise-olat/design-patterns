class Inventory:
    def __init__(self) -> None:
        self._observers = {}
        self._quantity = 0

    def attach(self, observer, event_type: str):
        if self._observers.get(event_type) == None:
            self._observers[event_type] = {observer}
        self._observers[event_type].add(observer)
    
    @property
    def product(self):
        return self._quantity

    @product.setter
    def product(self, value):
        self._quantity = value
        event = {
            'name': 'bot',
            'date': 'october 2021'
        }
        self._update_observers(event)

    def _update_observers(self, event):
        for event_type in self._observers:
            for callable in self._observers[event_type]:
                callable(event)


inventory = Inventory()