from datetime import datetime


def read_from_db() -> list:
    # import notes from db and return a list of notes
    return []


class Notebook:
    def __init__(self):
        self._notes = read_from_db()

    def add_notes(self, note):
        self._notes.append(note)

    def remove_note(self, note):
        try:
            self._notes.remove(note)
        except ValueError:
            print(f'{note} is not in the list')

    def display_notes(self):
        print(self._notes)


class Note:
    max_length = 5

    def __init__(self, title, text='', is_favorite=False):
        assert len(text) < self.max_length, (
            f"The length of the text must be less than {self.max_length}")

        self.title = title
        self.text = text
        self.is_favorite = is_favorite
        self.created_at = datetime.now()
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def remove_attachment(self, attachment):
        self.notes.remove(attachment)