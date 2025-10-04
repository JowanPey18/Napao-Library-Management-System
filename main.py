#Window Design

import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

con=sqlite3.connect('library.db')

class Main(object):
    def __init__(self, master):
        self.master = master

        # Make root window responsive
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Main frame
        mainFrame = Frame(self.master, bg="white")
        mainFrame.grid(row=0, column=0, sticky="nsew")
        mainFrame.rowconfigure(1, weight=1)
        mainFrame.columnconfigure(0, weight=1)

        # Top frame
        topFrame = Frame(mainFrame, bd=2, height=70, padx=20, pady=10, bg="light blue", relief=RIDGE, borderwidth=2)
        topFrame.grid(row=0, column=0, sticky="ew")
        topFrame.columnconfigure(0, weight=1)

        # Center frame
        centerFrame = Frame(mainFrame, bd=2, bg="white", relief=RIDGE, borderwidth=2)
        centerFrame.grid(row=1, column=0, sticky="nsew")
        centerFrame.rowconfigure(0, weight=1)
        centerFrame.columnconfigure(0, weight=3)
        centerFrame.columnconfigure(1, weight=1)

        # Left panel
        centerLeftFrame = Frame(centerFrame, bg="#e0f0f0", borderwidth=2, relief=SUNKEN)
        centerLeftFrame.grid(row=0, column=0, sticky="nsew")

        # Right panel
        centerRightFrame = Frame(centerFrame, bg="white", borderwidth=2, relief=SUNKEN)
        centerRightFrame.grid(row=0, column=1, sticky="nsew")

        # Search Box
        search_bar = Frame(centerRightFrame, bg="White", border=2, relief=RIDGE)
        search_bar.pack(side=TOP, fill=X, padx=10, pady=10)
        self.lbl_search = Label(search_bar, text="Search:", font='TIMES 12', bg="White", fg="black")
        self.lbl_search.pack(side=LEFT, padx=(0, 10))
        self.txt_search = Entry(search_bar, width=45, bd=1, font='arial 10 bold', relief=FLAT)
        self.txt_search.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
        ToolTip(self.lbl_search, "Enter book title or author to search")

        # Load search icon
        search_icon_path = os.path.join(os.path.dirname(__file__),"icons", "search.png")
        search_img = Image.open(search_icon_path)
        search_img = search_img.resize((20, 20), Image.LANCZOS)
        self.iconsearch = ImageTk.PhotoImage(search_img)
        self.btn_search = Button(search_bar, image=self.iconsearch, relief=FLAT, bg='#fcc324', bd=1, cursor='hand2')
        self.btn_search.pack(side=LEFT, anchor='center')
        ToolTip(self.btn_search, "Click to search for books")  # Tooltip
        
        # Book List Frame
        list_bar = LabelFrame(centerRightFrame, text="Book List", bg="white", relief=RIDGE, borderwidth=2)
        list_bar.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=True)

        # Make the grid responsive
        for i in range(5):
            list_bar.grid_columnconfigure(i, weight=1)

        # Instruction Label
        lbl_list = Label(list_bar, text="Sort By:", compound=LEFT, font='Arial 8 italic', bg="white", fg="black")
        lbl_list.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Radio Buttons
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text="All Books", variable=self.listChoice, value=1, bg="white", font='Arial 10')
        rb2 = Radiobutton(list_bar, text="In Library", variable=self.listChoice, value=2, bg="white", font='Arial 10')
        rb3 = Radiobutton(list_bar, text="Borrowed Books", variable=self.listChoice, value=3, bg="white", font='Arial 10')
        rb1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        rb2.grid(row=0, column=2, padx=10, pady=5, sticky="ew")
        rb3.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

        # Button
        btn_list = Button(list_bar, text="Show List", bg="#fcc324", font='Times 10', bd=1, cursor='hand2')
        btn_list.grid(row=0, column=4, padx=10, pady=10, sticky="ew")

        # Default selection
        self.listChoice.set(1)

        
        # Image and Title
        image_bar = Frame(centerRightFrame, bg="white", borderwidth=2)
        image_bar.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=True)
        image_bar.grid_columnconfigure(0, weight=1)
        self.title = Label(image_bar, text="Napao Library Management System", font='Arial 20 bold', bg="white", fg="black")
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        self.img_library_path = os.path.join(os.path.dirname(__file__), "icons", "Napao.png")
        self.lblImg = Image.open(self.img_library_path)
        self.lblImg = self.lblImg.resize((300, 300), Image.LANCZOS)
        self.img_library = ImageTk.PhotoImage(self.lblImg)
        self.library_logo = Label(image_bar, image=self.img_library, bg="white")
        self.library_logo.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        # Add Book Button
        icon_path = os.path.join(os.path.dirname(__file__),"icons", "addbook.png")
        img = Image.open(icon_path)
        img = img.resize((40, 40), Image.LANCZOS)
        self.iconbook = ImageTk.PhotoImage(img)
        self.btnbook = Button(topFrame, text='Add Book', compound=TOP, font='arial 8 bold', image=self.iconbook, bg="light blue", bd=0)
        self.btnbook.pack(side=LEFT, anchor="nw", padx=10, pady=10)
        ToolTip(self.btnbook, "Add a new book to the library")

        # Add Member Button
        icon_path = os.path.join(os.path.dirname(__file__),"icons", "addperson.png")
        img = Image.open(icon_path)
        img = img.resize((40, 40), Image.LANCZOS)
        self.iconmember = ImageTk.PhotoImage(img)
        self.btnmember = Button(topFrame, text='Add Member', compound=TOP, font='arial 8 bold', image=self.iconmember, bg="light blue", bd=0)
        self.btnmember.pack(side=LEFT, anchor="nw", padx=10, pady=10)
        ToolTip(self.btnmember, "Add a new member to the library")

        # Donate Book Button
        icon_path = os.path.join(os.path.dirname(__file__),"icons", "donate_book.png")
        img = Image.open(icon_path)
        img = img.resize((40, 40), Image.LANCZOS)
        self.icondonate = ImageTk.PhotoImage(img)
        self.btndonate = Button(topFrame, text='Donate A Book', compound=TOP, font='arial 8 bold', image=self.icondonate, bg="light green", bd=0)
        self.btndonate.pack(side=LEFT, anchor="nw", padx=10, pady=10)
        ToolTip(self.btndonate, "Donate a book to the library")  # Tooltip
        
      #########################################TABS##############################################
        style = ttk.Style()
        style.theme_use('default')

        style.configure('TNotebook.Tab',background='#f2f2f2',foreground='#000',padding=(12, 6),font=('Segoe UI', 10),borderwidth=0)
        style.map('TNotebook.Tab',background=[('selected', '#ffffff'), ('active', '#e6e6e6')],foreground=[('selected', '#000')],expand=[('selected', [1, 1, 1, 0])])

        # To Remove dotted line border
        style.layout('TNotebook.Tab', [('Notebook.tab', {'children': [('Notebook.padding', {'children': [('Notebook.label', {'side': 'top', 'sticky': ''})],'sticky': 'nswe'})],'sticky': 'nswe'})])
        
        books_img = Image.open(os.path.join(os.path.dirname(__file__), "icons", "Books.png"))
        books_img = books_img.resize((32, 32), Image.Resampling.LANCZOS)
        self.tab1_icon = ImageTk.PhotoImage(books_img)

        members_img = Image.open(os.path.join(os.path.dirname(__file__), "icons", "members.png"))
        members_img = members_img.resize((32, 32), Image.Resampling.LANCZOS)
        self.tab2_icon = ImageTk.PhotoImage(members_img)

        self.tabs = ttk.Notebook(centerLeftFrame, width=900, height=660)
        self.tabs.pack(expand=1, fill='both')

        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)

        self.tabs.add(self.tab1, text='Books', image=self.tab1_icon, compound=TOP)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=TOP)
        
        self.tab1.grid_rowconfigure(0, weight=1)
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab1.grid_columnconfigure(1, weight=0)
        self.tab1.grid_columnconfigure(2, weight=3)
        
        #BOOKS TAB
        # List of Books
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=5, relief=RIDGE, font='Times 12')
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")

        # Scrollbar for list_books
        self.sb = Scrollbar(self.tab1, orient=VERTICAL, command=self.list_books.yview)
        self.sb.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ns")

        self.list_books.config(yscrollcommand=self.sb.set)

        # Listbox for details (larger width)
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, relief=RIDGE, font='Times 12')
        self.list_details.grid(row=0, column=2, padx=(10, 10), pady=10, sticky="nsew")
        
        #STATISTICS TAB
        #Stats
        self.lbl_book_count = Label(self.tab2, text="Total of Books: ", font='Arial 14')
        self.lbl_book_count.grid(row=0, sticky="w", padx=10, pady=10)
        self.lbl_member_count = Label(self.tab2, text="Total Members: ", font='Arial 14')
        self.lbl_member_count.grid(row=1, sticky="w", padx=10, pady=10)
        self.lbl_borrowed_count = Label(self.tab2, text="Books Borrowed: ", font='Arial 14')
        self.lbl_borrowed_count.grid(row=2, column=0,sticky="w", padx=10, pady=10)
        self.lbl_available_count = Label(self.tab2, text="Books Available: ", font='Arial 14')
        self.lbl_available_count.grid(row=3,sticky="w", padx=10, pady=10)

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 40
        y = self.widget.winfo_rooty() + 20
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = Label(tw, text=self.text, background="#ffffe0", relief=SOLID, borderwidth=1, font=("tahoma", "7", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def main():
    root = Tk()
    app = Main(root)
    root.title("Napao Library Management System")
    root.geometry("1350x750+350+200")

    icon_path = os.path.join(os.path.dirname(__file__), "icons", "icon.ico")
    root.iconbitmap(icon_path)

    root.mainloop()

if __name__ == '__main__':
    main()
