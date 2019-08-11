class EntriesMeta(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("Entries.__new__(mcs, name, bases, namespace, **kwargs)")
        print(" kwargs =", kwargs)
        num_entries = kwargs['num_entries']
        print(" num_entries =", num_entries)
        namespace.update({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(self, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)
   
