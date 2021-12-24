from Notebook import Notebook, Note
from Attachment import Audio, Image
import tkinter as tk
from tkinter import ttk, filedialog

media_file = None


def submit():
    note = Note(title_input.get(), text_entry.get("1.0", "end-1c"), v.get().__bool__())
    if media_file:
        note.add_attachment(media_file)
    notebook.add_note(note)
    insert_node(note)
    title_input.set('')
    text_entry.delete("1.0", "end-1c")


def insert_node(note):
    treeview.insert("", 0, note.id, values=(note.title, note.text,
                                            note.is_favorite, note.created_at, note.get_attachments_attar()))

# def display():
#     listbox.delete(0, 'end')  # clear textbox
#     for note in notebook.get_notes():
#         listbox.insert("end", f'title: {note.__dict__.get("title")}  '
#                               f'text: {note.__dict__.get("text")}  '
#                               f'uuid: {note.__dict__.get("id")}')


# def call_back(event):
#     selection = event.widget.curselection()
#     if selection:
#         index = selection[0]
#         data = event.widget.get(index)
#     else:
#         pass

def delete_all_notes(is_filter=True):  # clear all notes from tree view
    for row in treeview.get_children():
        treeview.delete(row)
    if is_filter:
        notebook.remove_all_notes()


def delete():
    if elected_item := treeview.selection()[0]:
        treeview.delete(elected_item)


def filter_by():
    delete_all_notes(False)
    for note in notebook.get_notes():
        if note.is_favorite:
            insert_node(note)


def display_notebook():
    delete_all_notes(False)
    for note in notebook.get_notes():
        insert_node(note)


def upload_file():
    # selected_item = treeview.selection()[0]  # get selected item
    global media_file
    try:
        filename = filedialog.askopenfilename()
        media_file = Image(filename, 423, '4x5')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # TODO: create App object
    # app = App()
    notebook = Notebook()
    font = ('calibre', 10, 'bold')
    root = tk.Tk()
    root.geometry("1200x1000")

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

    upload_file_btn = tk.Button(root, text='Upload image/audio', command=upload_file).grid(row=4)

    root.mainloop()


