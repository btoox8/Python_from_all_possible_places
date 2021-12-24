# Import what you need from tkinter module
from tkinter import Tk, Button, PhotoImage, Label, LabelFrame, W, E,N,S, Entry, END,StringVar ,Scrollbar,Toplevel
from tkinter import ttk   # Provides access to the Tk themed widgets.
import sqlite3


# widgets to add :
# [Labels,LabelFrame, Entrys,Buttons,Treeview,Scrollbar,Logo]
# [label to display messages, treeview from ttk]

#W,E,S,N == the fourth directions
class Contacts:
    # variable = 'store my db path', then make function to interact with db
    db_filename = 'contacts.db'

    def __init__(self,root): # when run intialise it self and root
        self.root = root    # variable to our containeer
        self.create_gui()   # instead call all function here we make function to call them then call it here
        # using css to style or Treeview
        # ttk.style.configure('our widget', css to change)
        ttk.style = ttk.Style()
        ttk.style.configure("Treeview", font=('helvetica',10))
        ttk.style.configure("Treeview.Heading", font=('helvetica',12, 'bold'))

    # contact with DB
    # query = what we write on sqlite
    # parameters = what we use to interact with that on sqlite
    # both are variables

    def execute_db_query(self, query, parameters=()):
        # calling it with variable containg it
        with sqlite3.connect(self.db_filename) as conn:
            print(conn)
            print('You have successfully connected to the Database')
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result     # show what execute from interact between query and parameters


    # our bag to call all sub functions
    def create_gui(self):
        self.create_left_icon()
        self.create_label_frame()
        self.create_message_area()
        self.create_tree_view()
        self.create_scrollbar()
        self.create_bottom_buttons()
        # self.view_contacts()


    def create_left_icon(self):
        photo = PhotoImage(file='contacts/icons/logo.png')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0)

    # our create_left_icon == row =0 so we create frame on same row but different column [we go to right]
    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text='Create New Contact',bg="sky blue",font="helvetica 10")
        labelframe.grid(row=0, column=1, padx=8, pady=8, sticky='ew')
        
        ## on LabelFrame add :
        Label(labelframe, text='Name:',bg="green",fg="white").grid(row=1, column=1, sticky=W, pady=2,padx=15)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        Label(labelframe, text='Email:',bg="brown",fg="white").grid(row=2, column=1, sticky=W,  pady=2,padx=15)
        self.emailfield = Entry(labelframe)
        self.emailfield.grid(row=2, column=2, sticky=W, padx=5, pady=2)

        Label(labelframe, text='Number:',bg="black",fg="white").grid(row=3, column=1, sticky=W,  pady=2,padx=15)
        self.numfield = Entry(labelframe)
        self.numfield.grid(row=3, column=2, sticky=W, padx=5, pady=2)

        # our button opposite sticky to entry
        Button(labelframe, text='Add Contact',bg="blue",fg="white").grid(row=4, column=2, sticky=E, padx=5, pady=5)

        #command=self.on_add_contact_button_clicked

    # we make this function with empty text to adjust it later with other function according to certain status    
    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=1, sticky=W)

    def create_tree_view(self):
        # height = rows nums ,columns == may nums or (strings)
        self.tree = ttk.Treeview(height=10, columns=("email","number"),style='Treeview')
        self.tree.grid(row=6, column=0, columnspan=3)   # columnspan = heading = 3
        self.tree.heading('#0', text='Name', anchor=W)  # anchor = position to containeer == text start from left
        self.tree.heading("email", text='Email Address', anchor=W)
        self.tree.heading("number", text='Contact Number', anchor=W)

    #we use rowspan and sn = up to down
    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=3,rowspan=10,sticky='sn')

    def create_bottom_buttons(self):
        Button(text='Delete Selected', command='',bg="red",fg="white").grid(row=8, column=0, sticky=W,pady=10,padx=20)
        Button(text='Modify Selected', command='',bg="purple",fg="white").grid(row=8, column=1, sticky=W)

    # self.on_delete_selected_button_clicked
    # self.on_modify_selected_button_clicked

    # def on_add_contact_button_clicked(self):
    #     self.add_new_contact()

    # def on_delete_selected_button_clicked(self):
    #     self.message['text'] = ''
    #     try:
    #         self.tree.item(self.tree.selection())['values'][0]
    #     except IndexError as e:
    #         self.message['text'] = 'No item selected to delete'
    #         return
    #     self.delete_contacts()

    # def on_modify_selected_button_clicked(self):
    #     self.message['text'] = ''
    #     try:
    #         self.tree.item(self.tree.selection())['values'][0]

    #     except IndexError as e:
    #         self.message['text'] = 'No item selected to modify'
    #         return
    #     self.open_modify_window()

###############################################################
# creating functions:
# [add new contacts into DB, validate inputs, call add new contact to DB]
# [fetch all records from DB and display in treeview]


    def add_new_contact(self):
        # by using validate function
        # when it true == there are some entrys
        if self.new_contacts_validated():
            # INSERT INTO DB_table_name VALUES(NULL,?,?,?)
            # start with value NULL then ? to others, cols_nums = ? nums
            query = 'INSERT INTO contacts_list VALUES(NULL,?, ?,?)'

            # get what enter on our entrys
            parameters = (self.namefield.get(),self.emailfield.get(), self.numfield.get())

            # we should execute these value to DB
            self.execute_db_query(query, parameters)

            # deal with message 
            self.message['text'] = 'New Contact {} added'.format(self.namefield.get())

            # delete any old entry before add new once 
            # we make it ready to add next, because all fileds will be empty now
            self.namefield.delete(0, END)
            self.emailfield.delete(0, END)
            self.numfield.delete(0, END)
           # self.view_contacts()

        # all 3 fileds are empty
        else:
            self.message['text'] = 'name,email and number cannot be blank'
         #   self.view_contacts()

    # V != 0 == there something written
    # it mean some info are written
    def new_contacts_validated(self):
        return len(self.namefield.get()) != 0 and len(self.emailfield.get()) != 0 and len(self.numfield.get()) != 0

    def view_contacts(self):
        items = self.tree.get_children() # method to retuen item IDs
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM contacts_list ORDER BY name desc'
        contact_entries = self.execute_db_query(query)
        for row in contact_entries:
                self.tree.insert('', 0, text=row[1], values=(row[2],row[3]))

    # def delete_contacts(self):
    #     self.message['text'] = ''
    #     name = self.tree.item(self.tree.selection())['text']
    #     query = 'DELETE FROM contacts_list WHERE name = ?'
    #     self.execute_db_query(query, (name,))
    #     self.message['text'] = 'Contacts for {} deleted'.format(name)
    #     self.view_contacts()

    # def open_modify_window(self):
    #     name = self.tree.item(self.tree.selection())['text']
    #     old_number = self.tree.item(self.tree.selection())['values'][1]
    #     self.transient = Toplevel()
    #     self.transient.title('Update Contact')
    #     Label(self.transient, text='Name:').grid(row=0, column=1)
    #     Entry(self.transient, textvariable=StringVar(
    #         self.transient, value=name), state='readonly').grid(row=0, column=2)
    #     Label(self.transient, text='Old Contact Number:').grid(row=1, column=1)
    #     Entry(self.transient, textvariable=StringVar(
    #         self.transient, value=old_number), state='readonly').grid(row=1, column=2)

    #     Label(self.transient, text='New Phone Number:').grid(
    #         row=2, column=1)
    #     new_phone_number_entry_widget = Entry(self.transient)
    #     new_phone_number_entry_widget.grid(row=2, column=2)


    #     Button(self.transient, text='Update Contact', command=lambda: self.update_contacts(
    #         new_phone_number_entry_widget.get(), old_number, name)).grid(row=3, column=2, sticky=E)


    #     self.transient.mainloop()

    # def update_contacts(self, newphone, old_phone,name):
    #     query = 'UPDATE contacts_list SET number=? WHERE number =? AND name =?'
    #     parameters = (newphone, old_phone, name)
    #     self.execute_db_query(query, parameters)
    #     self.transient.destroy()
    #     self.message['text'] = 'Phone number of {} modified'.format(name)
    #     self.view_contacts()



# special variable to execute all below it
if __name__ == '__main__':
    root =Tk()  # our containner assign to Tk()
    root.title('My Contact List')
    root.geometry("650x450")
    root.resizable(width=False, height=False)
    application = Contacts(root)    # our reference to access all class(containner) to certain variablr = application
    root.mainloop()
