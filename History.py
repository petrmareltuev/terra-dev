import json


class History:

    def __init__(self):
        self.history_arr = {}
        self.duplicate_counter = 0

    def set_history(self, sequence, score):
        sequence = str(sequence)
        if sequence in self.history_arr:
            if self.history_arr[sequence] > score:
                self.history_arr[sequence] = score
            self.duplicate_counter += 1
        else:
            self.history_arr[sequence] = score

    def is_it_dupe_sequence(self, sequence):
        sequence = str(sequence)
        is_it_dupe = False
        if sequence in self.history_arr:
            is_it_dupe = True
        return is_it_dupe

    def save_history(self, filepath):
        with open(filepath, "w") as file_to_write:
            json.dump(self.history_arr, file_to_write)

    def load_history(self, filepath):
        with open(filepath, "r") as file_to_read:
            self.history_arr = json.load(file_to_read)
