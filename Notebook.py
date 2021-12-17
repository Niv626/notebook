from datetime import datetime
import uuid


def read_from_db() -> list:
    # import notes from db and return a list of notes
    return []


class Notebook:
    def __init__(self):
        self._notes = read_from_db()

    def add_note(self, note):
        self._notes.append(note)

    def remove_note(self, note):
        if not isinstance(note, Note):
            print(f'{note} is not an instance of Note')
        try:
            self._notes.remove(note)
        except ValueError:
            print(f'{note} is not in the list')
        else:
            print(f'succeed removing {note} from notebook')

    def remove_note_by_id(self, id):
        for note in self._notes:
            if note.id == id:
                self._notes.remove(note)
                return
        print(f'{id} did not match any note')

    def get_notes(self):
        return self._notes


class Note:
    max_length = 125

    def __init__(self, title, text='', is_favorite=False):
        assert len(text) < self.max_length, (
            f"The length of the text must be less than {self.max_length}")

        self.id = uuid.uuid4()
        self.title = title
        self.text = text
        self.is_favorite = is_favorite
        self.created_at = datetime.now()
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def remove_attachment(self, attachment):
        self.notes.remove(attachment)
