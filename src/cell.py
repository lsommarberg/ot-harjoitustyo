class Cell:
    def __init__(self, value=0):
        self.value = value
        self.is_locked = False
        self.notes = [0] * 9
        self.display_notes = False

    def set_value(self, value):
        self.value = value

    def lock_cell(self):
        self.is_locked = True

    def get_value(self):
        return self.value

    def get_notes(self):
        return self.notes

    def set_notes(self, value):
        if self.notes[value - 1] == 0:
            self.notes[value - 1] = value
        else:
            self.notes[value - 1] = 0
