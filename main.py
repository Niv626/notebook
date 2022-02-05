from Notebook import Notebook, Note
from Attachment import Audio, Image
import os

current_path = os.path.abspath(os.getcwd())


class Main:
    def __init__(self):
        self.notebook1 = Notebook()
        self.note1 = Note('title-self.note1', 'text-note1', is_favorite=True)
        self.note2 = Note('title-note2', 'text-note2', is_favorite=False)
        self.note3 = Note('title-note3', 'text-note3')
        # size in bytes, duration in sec
        self.audio1 = Audio(path=r'{}\file_example_WAV_1MG.wav'.format(current_path), size=15000, duration=45)
        self.audio2 = Audio(path=r'{}\CantinaBand3.wav'.format(current_path), size=10000, duration=3)
        self.image1 = Image(path=r'{}\view.jfif'.format(current_path), size=10000, resolution='180X220')

    def attachments_example(self):
        print('---------Audio------------')
        print('----audio1----')
        print(f'audio1 path: {self.audio1.path}')
        print(f'audio1 size in kb: {self.audio1.get_size()}')
        print(f'audio1 duration in sec: {self.audio1.get_duration()}')
        print('-----audio2----')
        print(f'audio2 path: {self.audio2.path}')
        print(f'audio2 size in kb: {self.audio2.get_size()}')
        print(f'audio2 duration in sec: {self.audio2.get_duration()}')
        print('now playing audio2: ')
        self.audio2.play_media()  # must enter valid path (local path)
        print('----audio1----')
        print(f'image1 path: {self.image1.path}')
        self.image1.path = r'{}\tree-736885__480.jpg'.format(current_path)
        print(f'after setting a new path {self.image1.path}')
        print(f'image1 size in kb: {self.image1.get_size()}')
        print(f'image1 resolution in pixels: {self.image1.get_resolution()}')
        print('displaying image2:')
        self.image1.play_media()

    def note_example(self):
        print('---------Note------------')
        print('----note1----')
        print(f'note1 title: {self.note1.title}')
        print(f'note1 text (body): {self.note1.text}')
        print(f'note1 is favorite: {self.note1.is_favorite}')
        print(f'note1 created at (time): {self.note1.created_at}')
        print(f'note1 id: {self.note1.get_id()}')
        print('adding audio1 and image1 to note 1')
        self.note1.add_attachment(self.audio1)
        self.note1.add_attachment(self.image1)
        print(f'get note1 attachments list: {self.note1.get_attachments_attar()}')
        self.note1.remove_attachment(self.audio1)
        print(f'get note1 attachments list (after removing audio1 from list): {self.note1.get_attachments_attar()}')
        print('-----note2----')
        print(self.note2.title)
        print(self.note2.text)
        print(self.note2.is_favorite)
        print(self.note2.created_at)
        print(self.note2.get_id())
        print('----note3----')
        print(self.note3.__dict__)

    def notebook_example(self):
        print('-----------Notebook-------')
        print(f'Notebook content before adding any notes: {self.notebook1.get_notes()}')
        self.notebook1.add_note(self.note1)
        self.notebook1.add_note(self.note2)
        self.notebook1.add_note(self.note3)
        print(f'Notebook content after adding note 1/2/3: {self.notebook1.get_notes()}')
        self.notebook1.remove_note_by_id(self.note1.get_id())
        print(f'Notebook content after removing note1 by id: {self.notebook1.get_notes()}')
        self.notebook1.remove_note_by_instance(self.note3)
        print(f'Notebook content after removing note3 by instance: {self.notebook1.get_notes()}')
        self.notebook1.add_note(self.note1)
        self.notebook1.add_note(self.note3)
        print(f'Notebook content after adding note 1/3: {self.notebook1.get_notes()}')
        self.notebook1.remove_all_notes()
        print(f'Notebook content after clearing all notes: {self.notebook1.get_notes()}')


if __name__ == '__main__':
    main = Main()
    main.attachments_example()
    main.note_example()
    main.notebook_example()
