from tkinter import *

root = Tk()

def getvals():
    print("It works! Button clicked")
    print(f"Name: {namevalue.get()}")
    print(f"Phone: {phonevalue.get()}")
    print(f"Gender: {gendervalue.get()}")
    print(f"Emergency Contact: {emergencyvalue.get()}")
    print(f"Payment Method: {paymentmethodvalue.get()}")
    print(f"Prebook Meals: {'Yes' if foodservicevalue.get() else 'No'}")

    # Write data to file AFTER user submits
    with open('out.txt', 'a', encoding='utf-8') as f:
        f.write(f"Name: {namevalue.get()}\n")
        f.write(f"Phone: {phonevalue.get()}\n")
        f.write(f"Gender: {gendervalue.get()}\n")
        f.write(f"Emergency Contact: {emergencyvalue.get()}\n")
        f.write(f"Payment Method: {paymentmethodvalue.get()}\n")
        f.write(f"Prebook Meals: {'Yes' if foodservicevalue.get() else 'No'}\n\n")

root.geometry("644x566")

# Heading
Label(root, text="Welcome to Neha Travels", font="arial 12 bold", pady=15, fg="blue").grid(row=0, column=3, columnspan=2)

# Text labels for the form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmethod = Label(root, text="Payment Method")

# Grid positioning for labels
name.grid(row=1, column=2, padx=10, pady=5, sticky="E")
phone.grid(row=2, column=2, padx=10, pady=5, sticky="E")
gender.grid(row=3, column=2, padx=10, pady=5, sticky="E")
emergency.grid(row=4, column=2, padx=10, pady=5, sticky="E")
paymentmethod.grid(row=5, column=2, padx=10, pady=5, sticky="E")

# Tkinter variables for storing form data
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmethodvalue = StringVar()
foodservicevalue = IntVar()

# Entry fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmethodentry = Entry(root, textvariable=paymentmethodvalue)

# Grid positioning for entries
nameentry.grid(row=1, column=3, pady=5)
phoneentry.grid(row=2, column=3, pady=5)
genderentry.grid(row=3, column=3, pady=5)
emergencyentry.grid(row=4, column=3, pady=5)
paymentmethodentry.grid(row=5, column=3, pady=5)

# Checkbox for meal prebooking
foodservice = Checkbutton(root, text="Want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3, pady=10)

# Submit button
submit = Button(root, text="Submit to Harry Travels", bg="blue", fg="white", command=getvals)
submit.grid(row=7, column=3, pady=10)

root.mainloop()
