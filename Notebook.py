from datetime import datetime
from setup_logger import logger
import uuid


class Notebook:
    def __init__(self):
        self._notes = self.read_from_db()

    @staticmethod
    def read_from_db() -> list:
        # TODO: Need to implement database
        logger.info('import notes from db and return a list of notes')
        return []

    def add_note(self, note):
        self._notes.append(note)

    def remove_note_by_instance(self, note):
        if not isinstance(note, Note):
            logger.error(f'{note} is not an instance of Note')
            return
        try:
            self._notes.remove(note)
        except ValueError:
            logger.error(f'{note} is not in the list')
        else:
            logger.info(f'succeed removing {note} from notebook')

    def remove_all_notes(self):
        self._notes.clear()
        logger.info(f'clearing notebook')

    def remove_note_by_id(self, identifier):
        for note in self._notes:
            if note.get_id() == identifier:
                self._notes.remove(note)
                logger.info(f'succeed removing {note} from notebook')
                return
        logger.error(f'{id} did not match any note')

    def get_notes(self):
        return self._notes


class Note:
    max_length = 125

    def __init__(self, title, text='', is_favorite=False):
        assert len(text) < self.max_length, (
            f"The length of the text must be less than {self.max_length}")

        self._id = str(uuid.uuid4())
        self.title = title
        self.text = text
        self.is_favorite = is_favorite
        self.created_at = datetime.now()
        self._attachments = []

    def add_attachment(self, attachment):
        self._attachments.append(attachment)

    def get_attachments_attar(self):
        return [attachment.__dict__ for attachment in self._attachments]

    def get_attachments_path(self):
        return self.get_attachments_attar()[0].get('_path')

    def remove_attachment(self, attachment):
        self._attachments.remove(attachment)

    def get_id(self):
        return self._id

