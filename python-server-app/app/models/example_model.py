class ExampleModel:
    def __init__(self, data):
        self.data = data

    def update_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data

    def to_dict(self):
        return {"data": self.data}