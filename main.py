from Notebook import Notebook, Note
from Attachment import Audio, Image

note1 = Note("title1", "txt1", True)
note2 = Note("title2", "txt2", True)
note3 = Note("title3", "txt3")


audio_attach = Audio("FLAC", 1300, 4000)
image_attach = Image("png", 1200, "1920x1080")

note1.add_attachment(audio_attach)
note1.add_attachment(image_attach)

notebook = Notebook()

notebook.add_notes(note1)
notebook.add_notes(note2)
notebook.add_notes(note3)
notebook.remove_note(note3)

notebook.display_notes()



