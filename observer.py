class Subscriber:
    "setting string to name field"
    def __init__(self, name):
        self.name = name

    def update(self, message):
        "printing message from parameter"
        print('Subscriber {} got message "{}"'.format(self.name, message))


class Blog:
    def __init__(self, topics):
        """
        setting a dict with topics as keys and empty sets for
        subscribers as values to subscribers field
        """
        self.subscribers = {topic: set() for topic in topics}

    def get_subscribers(self, topic):
        "get subscribers by certain topic"
        return self.subscribers[topic]

    def register(self, topic, who):
        "register subscriber for certain topic"
        self.get_subscribers(topic).add(who)

    def unregister(self, topic, who):
        "unregister subscriber from certain topic"
        self.get_subscribers(topic).discard(who)

    def dispatch(self, topic, message):
        "dispatch some info to subscribers of certain topic"
        for subscriber in self.get_subscribers(topic):
            subscriber.update(message)
