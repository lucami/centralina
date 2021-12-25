class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message, subscriber_name):
        print('{} ricevuto messaggio "{} da {}'.format(self.name, message, subscriber_name))


class Publisher:
    def __init__(self):
        self.subscribers = dict()

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message,subscriber)


if __name__ == "__main__":
    pub = Publisher()
    bob = Subscriber('Bob')
    john = Subscriber('John')

    pub.register(bob, bob.update)
    pub.register(john)

    pub.dispatch("It's lunchtime!")
    pub.unregister(john)
    pub.dispatch("Time for dinner")
