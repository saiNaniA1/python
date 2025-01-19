from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database1

# Function to handle selection from the Treeview
def selection(event):
    global selected_row_data
    selected_item = tree.selection()
    if selected_item:
        selected_row_data = tree.item(selected_item)['values']
        idEntry.delete(0, END)
        NameEntry.delete(0, END)
        PhoneEntry.delete(0, END)
        SalaryEntry.delete(0, END)

        idEntry.insert(0, selected_row_data[0])
        NameEntry.insert(0, selected_row_data[1])
        PhoneEntry.insert(0, selected_row_data[2])
        roleBox.set(selected_row_data[3])
        GenderBox.set(selected_row_data[4])
        SalaryEntry.insert(0, selected_row_data[5])

# Function to clear input fields
def clear_fields():
    idEntry.delete(0, END)
    NameEntry.delete(0, END)
    PhoneEntry.delete(0, END)
    SalaryEntry.delete(0, END)
    roleBox.set("Web Developer")
    GenderBox.set("Male")

# Function to load data into the Treeview
def treeview_data():
    employees = database1.fetch_employee()
    tree.delete(*tree.get_children())  # Clear existing data
    for employee in employees:
        # Correct mapping of columns
        tree.insert('', 'end', text="", values=(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

# Function to add an employee
def add_employee():
    if idEntry.get() == "" or PhoneEntry.get() == "" or NameEntry.get() == "" or SalaryEntry.get() == "":
        messagebox.showerror("Error", "All fields must be filled.")
    elif not SalaryEntry.get().isdigit() or float(SalaryEntry.get()) <= 0:
        messagebox.showerror("Error", "Salary must be a positive number.")
    elif database1.id_exists(idEntry.get()):
        messagebox.showerror("Error", "Employee ID already exists.")
    else:
        database1.insert(
            idEntry.get(),
            NameEntry.get(),
            PhoneEntry.get(),
            roleBox.get(),
            GenderBox.get(),
            float(SalaryEntry.get())
        )
        treeview_data()
        messagebox.showinfo("Success", "Employee added successfully!")
        clear_fields()

# Function to update an employee's details
def update_employee():
    if not tree.selection():
        messagebox.showerror("Error", "Please select an employee to update.")
    else:
        database1.update(
            idEntry.get(),
            NameEntry.get(),
            PhoneEntry.get(),
            roleBox.get(),
            GenderBox.get(),
            float(SalaryEntry.get())
        )
        treeview_data()
        messagebox.showinfo("Success", "Employee updated successfully!")
        clear_fields()

# Function to delete a selected employee
def delete_employee():
    if not tree.selection():
        messagebox.showerror("Error", "Please select an employee to delete.")
    else:
        selected_item = tree.selection()[0]
        employee_id = tree.item(selected_item)['values'][0]
        database1.delete(employee_id)
        treeview_data()
        messagebox.showinfo("Success", "Employee deleted successfully!")
        clear_fields()

# Function to delete all employees
def delete_all_employees():
    if messagebox.askyesno("Confirmation", "Are you sure you want to delete all employees?"):
        database1.delete_all()
        treeview_data()
        messagebox.showinfo("Success", "All employees deleted successfully!")

# Function to search for employees
def search_employee():
    query = searchEntry.get()
    if not query:
        messagebox.showerror("Error", "Please enter a value to search.")
    else:
        employees = database1.search_employee(searchBox.get(), query)
        tree.delete(*tree.get_children())
        for employee in employees:
            tree.insert('', 'end', text="", values=(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
        if not employees:
            messagebox.showinfo("No Results", "No matching employees found.")

# Main Window Configuration
window = CTk()
window.geometry("950x630")
window.title("Employee Management System")
window.configure(fg_color='#4C585B')
window.resizable(False, False)

# Load Logo Image
Logo = CTkImage(Image.open("cover.jpg"), size=(930, 150))
LogoLabel = CTkLabel(window, image=Logo, text="")
LogoLabel.grid(row=0, column=0, columnspan=2)

# Left Frame
LeftFrame = CTkFrame(window, fg_color='#4C585B')
LeftFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Left Frame Widgets
CTkLabel(LeftFrame, text="Id", font=("Times New Roman", 18, "bold"), text_color='White').grid(row=0, column=0, padx=20, pady=15, sticky='w')
idEntry = CTkEntry(LeftFrame, font=("Times New Roman", 15, "bold"), width=180)
idEntry.grid(row=0, column=1)

CTkLabel(LeftFrame, text="Name", font=("Times New Roman", 18, "bold"), text_color='White').grid(row=1, column=0, padx=20, pady=15, sticky='w')
NameEntry = CTkEntry(LeftFrame, font=("Times New Roman", 15, "bold"), width=180)
NameEntry.grid(row=1, column=1)

CTkLabel(LeftFrame, text="Phone Number", font=("Times New Roman", 18, "bold"), text_color='White').grid(row=2, column=0, padx=20, pady=15, sticky='w')
PhoneEntry = CTkEntry(LeftFrame, font=("Times New Roman", 15, "bold"), width=180)
PhoneEntry.grid(row=2, column=1)

CTkLabel(LeftFrame, text="Role", font=("Times New Roman", 18, "bold"), text_color='White').grid(row=3, column=0, padx=20, pady=15, sticky='w')
role_options = ['Web Development', 'Cloud Architect', 'Technical Writer', 'Network Engineer', 'DevOps Engineer',
                'Data Scientist', 'Business Analyst', 'IT Consultant', 'UI/UX Design']
roleBox = CTkComboBox(LeftFrame, values=role_options, width=180, font=("Times New Roman", 18, "bold"), state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

CTkLabel(LeftFrame, text="Gender", font=("Times New Roman", 18, "bold"), text_color='White').grid(row=4, column=0, padx=20, pady=15, sticky='w')
Gender_options = ['Male', 'Female']
GenderBox = CTkComboBox(LeftFrame, values=Gender_options, width=180, font=("Times New Roman", 18, "bold"))
GenderBox.grid(row=4, column=1)
GenderBox.set('Male')

CTkLabel(LeftFrame, text="Salary", font=("Times New Roman", 18, "bold"), text_color='White').grid(row=5, column=0, padx=20, pady=15, sticky='w')
SalaryEntry = CTkEntry(LeftFrame, font=("Times New Roman", 15, "bold"), width=180)
SalaryEntry.grid(row=5, column=1)

# Right Frame
RightFrame = CTkFrame(window)
RightFrame.grid(row=1, column=1, padx=10, pady=10)

search_options = ['ID', 'Name', 'Phone Number', 'Role', 'Salary']
searchBox = CTkComboBox(RightFrame, values=search_options, state='readonly', width=150)
searchBox.grid(row=0, column=0, padx=5, pady=5)
searchBox.set('Search By')

searchEntry = CTkEntry(RightFrame, width=150)
searchEntry.grid(row=0, column=1, padx=5, pady=5)

searchButton = CTkButton(RightFrame, text='Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2, padx=5, pady=5)

showAllButton = CTkButton(RightFrame, text='Show All', width=100, command=treeview_data)
showAllButton.grid(row=0, column=3, padx=5, pady=5)

# Treeview for Employee Data
tree = ttk.Treeview(RightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

tree['columns'] = ('Id', 'Name', 'Phone Number', 'Role', 'Gender', 'Salary')
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.config(show='headings')

# Scrollbar
scrollbar = ttk.Scrollbar(RightFrame, orient=VERTICAL, command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')
tree.config(yscrollcommand=scrollbar.set)

# Button Frame
buttonFrame = CTkFrame(window)
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

CTkButton(buttonFrame, text='New Employee', font=("Times New Roman", 15, "bold"), width=160, corner_radius=15, command=clear_fields).grid(row=0, column=0, padx=5, pady=5)
CTkButton(buttonFrame, text='Add Employee', font=("Times New Roman", 15, "bold"), width=160, corner_radius=15, command=add_employee).grid(row=0, column=1, padx=5, pady=5)
CTkButton(buttonFrame, text='Update Employee', font=("Times New Roman", 15, "bold"), width=160, corner_radius=15, command=update_employee).grid(row=0, column=2, padx=5, pady=5)
CTkButton(buttonFrame, text='Delete Employee', font=("Times New Roman", 15, "bold"), width=160, corner_radius=15, command=delete_employee).grid(row=0, column=3, padx=5, pady=5)
CTkButton(buttonFrame, text='Delete All', font=("Times New Roman", 15, "bold"), width=160, corner_radius=15, command=delete_all_employees).grid(row=0, column=4, padx=5, pady=5)

# Bind Treeview Selection Event
tree.bind('<ButtonRelease-1>', selection)

# Load initial data
treeview_data()

# Run the app
window.mainloop()



