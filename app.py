from Notebook import Notebook, Note
from Attachment import Audio, Image as c_Image
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image as pImage
from formats import image_prefix, audio_prefix
import os
from play_audio import run
from tkinter.messagebox import showinfo


media_file = None


def submit():
    global media_file
    note = Note(title_input.get(), text_entry.get("1.0", "end-1c"), v.get().__bool__())
    if media_file:
        note.add_attachment(media_file)
    notebook.add_note(note)
    insert_node(note)
    title_input.set('')
    media_file = None
    text_entry.delete("1.0", "end-1c")


def insert_node(note):
    if note.get_attachments_attar():
        treeview.insert("", 0, note.get_id(), values=(note.title, note.text, note.is_favorite,
                                                      note.created_at, note.get_attachments_path()))
    else:
        treeview.insert("", 0, note.get_id(), values=(note.title, note.text, note.is_favorite,
                                                      note.created_at, ""))


def delete_all_notes(is_filter=True):  # clear all notes from tree view
    for row in treeview.get_children():
        treeview.delete(row)
    if is_filter:
        notebook.remove_all_notes()


def delete():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item[0])


def play_media():
    selected_item = treeview.selection()
    if selected_item:
        try:
            path = treeview.item(selected_item).get('values')[-1]
            if formatted_file(path).endswith(image_prefix):
                with pImage.open(path) as im:
                    im.show()
            elif formatted_file(path).endswith(audio_prefix):
                popup_showinfo()
                run(path)
            else:
                print('select note first')

        except Exception as e:
            print(e)


def filter_by():
    delete_all_notes(False)
    for note in notebook.get_notes():
        if note.is_favorite:
            insert_node(note)


def display_notebook():
    delete_all_notes(False)
    for note in notebook.get_notes():
        insert_node(note)


def get_file_size(path):  
    return os.path.getsize(path)


def formatted_file(path):
    return path.split('/')[-1].lower()


def upload_file():
    global media_file
    try:
        path = filedialog.askopenfilename()
        formatted_file_name = formatted_file(path)
        file_size = get_file_size(path)

        if formatted_file_name.endswith(image_prefix):
            media_file = c_Image(path)
        elif formatted_file_name.endswith(audio_prefix):
            media_file = Audio(path, file_size)
    except Exception as e:
        print(e)


def popup_showinfo():
    showinfo("Help", "space to pause, esc to exit")


if __name__ == "__main__":
    # TODO: create App object
    # app = App()
    notebook = Notebook()
    font = ('calibre', 10, 'bold')
    root = tk.Tk()
    root.geometry("1700x2000")

    title_input = tk.StringVar()
    v = tk.IntVar()

    checkbox_btn = tk.Checkbutton(root, text="Favorite?",
                                  variable=v,
                                  onvalue=True,
                                  offvalue=False,
                                  height=2,
                                  width=10).grid(row=5)
    filter_input = tk.StringVar(root, 1)

    # Dictionary to create multiple buttons
    values = {"Display all notes": display_notebook,
              "Favorites notes only": filter_by}
    btn_list = []
    i = 10
    for (text, value) in values.items():
        btn = tk.Radiobutton(root, text=text, variable=filter_input,
                             value=text, command=value)
        btn.grid(row=i)
        btn_list.append(btn)
        i += 1
    if btn_list:
        btn_list[0].select()
    note_title = tk.Label(root, text='Insert title', font=font).grid(row=0)
    note_title_entry = tk.Entry(root, textvariable=title_input, font=font)
    note_title_entry.grid(row=1)

    text_label = tk.Label(root, text='insert text', font=font).grid(row=2)
    text_entry = tk.Text(root, height=12, width=50)
    text_entry.grid(row=3)

    sub_btn = tk.Button(root, text='insert new note', command=submit).grid(row=6)

    treeview = ttk.Treeview(root)
    treeview.grid(row=7)
    treeview["columns"] = ["title", "text", "is favorite", "created at", "attachments"]
    treeview.column("attachments", minwidth=0, width=700)
    treeview["show"] = "headings"
    for header in treeview["columns"]:
        treeview.heading(header, text=header)
    treeview.bind("<<TreeviewSelect>>")

    btn_del = tk.Button(root, text="Delete selected note", command=delete).grid(row=8)
    btn_del_all = tk.Button(root, text="Delete all notes", command=delete_all_notes).grid(row=9)

    btn_display_media = tk.Button(root, text="play media", command=play_media).grid(row=12)

    upload_file_btn = tk.Button(root, text='Upload image/audio', command=upload_file).grid(row=4)

    root.mainloop()
