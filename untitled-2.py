########################################################################
###  This programme lets Julie track items hired from her store      ###
########################################################################
from tkinter import *
# solves the issue of button text not appearing on OSX, see https://stackoverflow.com/questions/59006014/python-tkinter-button-text-is-not-visible
from tkinter import ttk 
import random

# Function to generate a random receipt number between 1000000 and 9999999
def generate_receipt_number():
    receipt_number = random.randint(1000000, 9999999)
    entry_receipt.delete(0, END)
    entry_receipt.insert(0, receipt_number)

# quit subroutine
def quit():
    main_window.destroy()

#print details of the hired items
def PrintHireDetails():
    name_count = 0
    #Create the column headings for the details
    #font
    Label(main_window, font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Full Name").grid(column=1,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Item Hired").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="No of Items Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Receipt Number").grid(column=4,row=7)

    #add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=hire_details[name_count][3]).grid(column=4, row=name_count + 8)
        name_count +=  1
        counters['name_count'] = name_count
        
#Check that inputs are valid
def check_inputs():
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)
    #set error text if name is blank   
    if len(entry_name.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2,row=0)
        input_check = 1
    #set error text if Item hired is blank     
    if len(entry_item.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2,row=1)
        input_check = 1
    #set error text if number of items is blank and not between 1 and 500  
    if entry_hires.get().isdigit(): 
        if int(entry_hires.get()) < 1 or int(entry_hires.get()) > 500:
            Label(main_window, fg="red", text="1-500 only").grid(column=2,row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="1-500 only").grid(column=2,row=2)
        input_check = 1

    if input_check == 0:
        append_name() 

# add the next item to the list
def append_name():
    # append each item to its own part of the list
    hire_details.append([entry_name.get(), entry_item.get(), entry_hires.get(), entry_receipt.get()])
    # clear the boxes
    entry_name.delete(0, 'end')
    entry_item.delete(0, 'end')
    entry_hires.delete(0, 'end')
    entry_receipt.delete(0, 'end')  # clear the receipt entry box as well
    counters['total_entries'] += 1


#delete a row from the list
def delete_row():
    #find row to delete and delete it
    del hire_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0, 'end')
    #clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7) 
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    #print all the items in the list
    PrintHireDetails()

#create the buttons and labels
def setup_buttons():
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid position
    Label(main_window, text="Name").grid(column=0, row=0, sticky=E)
    Label(main_window, text="Item").grid(column=0, row=1, sticky=E)
    Button(main_window, text="Quit", command=quit, width=10).grid(column=4, row=0, sticky=E)
    Button(main_window, text="Append Details", command=check_inputs).grid(column=3, row=1)
    Button(main_window, text="Print Details", command=PrintHireDetails, width=10).grid(column=4, row=1, sticky=E)
    Label(main_window, text="No of Items").grid(column=0, row=2, sticky=E)
    Label(main_window, text="Row #").grid(column=3, row=2, sticky=E)
    Button(main_window, text="Delete Row", command=delete_row, width=10).grid(column=4, row=3, sticky=E)
    Button(main_window, text="Receipt Number", command=generate_receipt_number, width=15).grid(column=2, row=3, sticky=E)

    # create entry box for receipt number
    global entry_receipt
    entry_receipt = Entry(main_window)
    entry_receipt.grid(column=1, row=3)

    Label(main_window, text="               ").grid(column=2, row=0)


#start the program running
def main():
    #Start the GUI it up
    setup_buttons()
    main_window.mainloop()
    
#create empty list for hire details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
hire_details = []    
main_window = Tk()    
entry_name = Entry(main_window)
entry_name.grid(column=1, row=0)
entry_item = Entry(main_window)
entry_item.grid(column=1, row=1)
entry_hires = Entry(main_window)
entry_hires.grid(column=1, row=2)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=3)
main()
