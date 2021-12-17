from Notebook import Notebook, Note
from Attachment import Audio, Image
import tkinter as tk


def submit():
    label = title_input.get()
    text = text_entry.get("1.0", "end-1c")
    is_favorite = True
    print(Note(label, text, is_favorite).__dict__)
    notebook.add_note(Note(label, text, is_favorite))


def display():
    listbox.delete(0, 'end')  # clear textbox
    for note in notebook.get_notes():
        listbox.insert("end", f'title: {note.__dict__.get("title")}  '
                              f'text: {note.__dict__.get("text")}')

def call_back(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
    else:
        pass



if __name__ == "__main__":
    notebook = Notebook()

    font = ('calibre', 10, 'bold')
    root = tk.Tk()
    root.geometry("800x600")

    title_input = tk.StringVar()

    note_title = tk.Label(root, text='insert title', font=font)
    note_title_entry = tk.Entry(root, textvariable=title_input, font=font)

    text_label = tk.Label(root, text='insert text', font=font)
    text_entry = tk.Text(root, height=12, width=50)

    sub_btn = tk.Button(root, text='insert new note', command=submit)
    display_note_btn = tk.Button(root, text='display notes', command=display)

    list_label = tk.Label(root, text='notes', font=font)
    listbox = tk.Listbox(root, selectmode='extended', height=20, width=50)
    listbox.bind("<<ListboxSelect>>", call_back)

    # Grid arrange
    note_title.grid(row=0, column=0)
    note_title_entry.grid(row=0, column=1)

    text_label.grid(row=1, column=0)
    text_entry.grid(row=1, column=1)

    sub_btn.grid(row=2, column=1)

    list_label.grid(row=0, column=2)
    listbox.grid(row=1, column=2)
    display_note_btn.grid(row=3, column=2)

    root.mainloop()

    # note1 = Note("title1", "txt1", True)
    # note2 = Note("title2", "txt2", True)
    # note3 = Note("title3", "txt3")
    # audio_attach = Audio("FLAC", 1300, 4000)
    # image_attach = Image("png", 1200, "1920x1080")
    # note1.add_attachment(audio_attach)
    # note1.add_attachment(image_attach)
    # print(note1.__dict__)
    # notebook = Notebook()
    #
    # notebook.add_notes(note1)
    # notebook.add_notes(note2)
    # notebook.add_notes(note3)
    # notebook.remove_note(note2)
    # notebook.remove_note(note3)
    #
    # notebook.display_notes()
