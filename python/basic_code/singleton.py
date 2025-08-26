class Singletone:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singletone, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

ob1 = Singletone()
ob2 = Singletone(42)

print(ob1 is ob2)  # True
print(ob1.value)   # None
print(ob2.value)   # None
