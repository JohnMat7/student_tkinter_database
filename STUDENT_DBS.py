from tkinter import *
import tkinter.font as font
import csv

root = Tk()
root.title("STUDENT DATABASE SYSTEM")
root.geometry("850x600")
root.configure(bg="light sky blue")


# def write_to_file():
#     with open("stu_database.txt", "a+") as file:
#         file.write(f"{stu_name},{father_name},{mother_name},{add_no}")


l1 = Label(root, text="Name:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=0, column=0)
stu_name = Entry(root, width=20, font=('Consolas', 16))
stu_name.grid(row=0, column=1)


l1 = Label(root, text="Father's Name:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=1, column=0)
father_name = Entry(root, width=20, font=('Consolas', 16))
father_name.grid(row=1, column=1)


l1 = Label(root, text="Mother's Name:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=2, column=0)
mother_name = Entry(root, width=20, font=('Consolas', 16))
mother_name.grid(row=2, column=1)


l1 = Label(root, text="Admission no.:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=3, column=0)
add_no = Entry(root, width=20, font=('Consolas', 16))
add_no.grid(row=3, column=1)


l1 = Label(root, text="Class:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=0, column=2)
add_no = Entry(root, width=20, font=('Consolas', 16))
add_no.grid(row=0, column=3)


l1 = Label(root, text="Phone No:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=1, column=2)
stu_class = Entry(root, width=20, font=('Consolas', 16))
stu_class.grid(row=1, column=3)


l1 = Label(root, text="Date of Birth:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=2, column=2)
add_no = Entry(root, width=20, font=('Consolas', 16))
add_no.grid(row=2, column=3)


l1 = Label(root, text="Address:", font=(
    'Consolas', 16), bg="light sky blue")
l1.grid(row=3, column=2)
add_no = Entry(root, width=20, font=('Consolas', 16))
add_no.grid(row=3, column=3)

seperator = Label(root, text="\n", bg="light sky blue")
seperator.grid(row=4, column=0)
submit_button = Button(root, text="Submit", padx=30, pady=10)
submit_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
