# Builder Design Pattern Example
class Computer:
    def __init__(self, processor, memory, storage):
        self.processor = processor
        self.memory = memory
        self.storage = storage

    def __str__(self):
        return f"Computer with {self.processor}, {self.memory} RAM, and {self.storage} storage"

class ComputerBuilder:
    def __init__(self):
        self.computer = {}

    def add_processor(self, processor):
        self.computer['processor'] = processor
        return self

    def add_memory(self, memory):
        self.computer['memory'] = memory
        return self

    def add_storage(self, storage):
        self.computer['storage'] = storage
        return self

    def build(self):
        return Computer(self.computer['processor'],
                        self.computer['memory'],
                        self.computer['storage'])

#uses
builder = ComputerBuilder()
my_computer = (builder.add_processor("Intel i7")
                .add_memory("16GB")
                .add_storage("512GB SSD")
                .build())
print(my_computer)  # Output: Computer with Intel i7, 16GB RAM, and 512GB SSD storage
