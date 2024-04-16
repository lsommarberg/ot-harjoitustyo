class Cell:
    def __init__(self, value=0):
        self.value = value
        self.is_locked = False

    #    self.notes = []

    def set_value(self, value):
        self.value = value

    def lock_cell(self):
        self.is_locked = True

    def get_value(self):
        return self.value
