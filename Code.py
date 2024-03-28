import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('PA3.db')
cur = conn.cursor()
# Function to retrieve the results and display them on the GUI
def get_details_by_name():
    fname = first_name_entry.get()
    lname = last_name_entry.get()
    query = """SELECT B.Train_Number, T.Train_Name FROM Booked B JOIN Train T
                   on B.Train_Number = T.Train_Number where B.Passenger_SSN IN
                   (SELECT SSN FROM Passenger WHERE First_Name=? AND Last_Name=?)"""
    cur.execute(query, (fname, lname))
    results = cur.fetchall()
    for widget in tab1.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for result in results:
        row_label = tk.Label(tab1, text=f"Train Number: {result[0]}\tTrain Name: {result[1]}")
        row_label.pack()


# Function to query traveling passengers
def get_details_by_date():
    train_date = date_entry.get()
    query = """SELECT P.First_Name, P.Last_Name, T.Train_Number, T.Train_Name, B.Ticket_Type
             FROM Train_Status TS
             FULL OUTER JOIN Train T ON T.Train_Name = TS.TrainName
             FULL OUTER JOIN Booked B ON B.Train_Number = T.Train_Number
             FULL OUTER JOIN Passenger P ON P.SSN = B.Passenger_SSN
             WHERE B.Status = 'Booked' AND TS.TrainDate = ?"""
    cur.execute(query, (train_date,))
    rows = cur.fetchall()
    for widget in tab2.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for row in rows:
        row_label = tk.Label(tab2, text=f"First Name: {row[0]}\tLast Name: {row[1]}\tTrain Number: {row[2]}\tTrain Name: {row[3]}\tTicket Type: {row[4]}")
        row_label.pack()
    if not rows:
        tk.messagebox.showinfo("No Results", f"No passengers are booked to travel on {train_date}.")

def get_details_by_age():
    min_age = min_age_entry.get()
    max_age = max_age_entry.get()
    query = """SELECT Train.Train_Number, Train.Train_Name, Train.Source_Station, Train.Destination_Station,
                   Passenger.First_Name, Passenger.Last_Name, Passenger.Address, Passenger.County,
                   Booked.Ticket_Type, Booked.Status
                   FROM Passenger
                   FULL OUTER JOIN Booked ON Passenger.SSN = Booked.Passenger_SSN
                   FULL OUTER JOIN Train ON Booked.Train_Number = Train.Train_Number
                   WHERE substr(Passenger.Birth_Date,7,2) BETWEEN substr(STRFTIME('%Y',date('now', '-'||?||' YEAR')), 3, 2) AND
                   substr(STRFTIME('%Y',date('now', '-'|| ? || ' YEAR')), 3, 2)"""
    cur.execute(query, (max_age, min_age))
    results = cur.fetchall()
    for widget in tab3.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for result in results:
        row_label = tk.Label(tab3, text=f"Train Number: {result[0]}\tTrain Name: {result[1]}\tSource: {result[2]}\tDestination: {result[3]}\tPassenger Name: {result[4]} {result[5]}\tAddress: {result[6]}\tCategory: {result[7]}\tTicket Type: {result[8]}\tTicket Status: {result[9]}")
        row_label.pack()

def get_details_by_ticket_type():
    ticket_type = ticket_type_entry.get()
    query = """SELECT Train.Train_Name, COUNT(*) as PassengerCount, Booked.Status
               FROM Booked
               FULL OUTER JOIN Train ON Booked.Train_Number = Train.Train_Number
               WHERE Booked.Status = ?
               GROUP BY Train.Train_Name"""

    cur.execute(query,(ticket_type,))
    results = cur.fetchall()

    for widget in tab4.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for result in results:
        row_label = tk.Label(tab4, text=f'{result[0]}\t{result[1]}\t\t{result[2]}')
        row_label.pack()

def get_details_by_train_name():
    train_name = train_name_entry.get()

    query = """SELECT Passenger.First_Name, Passenger.Last_Name, Train.Train_Number, Train.Train_Name, Booked.Ticket_Type, Booked.Status
               FROM Passenger
               INNER JOIN Booked ON Passenger.SSN = Booked.Passenger_SSN
               INNER JOIN Train ON Booked.Train_Number = Train.Train_Number
               WHERE TRIM(Train.Train_Name) = ? AND Booked.Status = 'Booked' """
    cur.execute(query,(train_name,))
    results = cur.fetchall()

    for widget in tab5.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for result in results:
        row_label = tk.Label(tab5, text=f"Passenger Name: {result[0]} {result[1]}\tTrain Number: {result[2]}\tTicket Type: {result[4]}")
        row_label.pack()





# Creating the GUI
root = tk.Tk()

root.title("Railway Reservation System")

# Create tabs
tab_parent = ttk.Notebook(root)

# Tab for retrieving booked trains by passenger name
tab1 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Retrieve Booked Trains by Passenger Name")

# Creating the frame to hold the inputs
frame = tk.Frame(tab1)
frame.pack(padx=10, pady=10)

# Creating the input fields for first name and last name
first_name_label = tk.Label(frame, text="First Name:")
first_name_label.grid(row=0, column=0, padx=5, pady=5)
first_name_entry = tk.Entry(frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

last_name_label = tk.Label(frame, text="Last Name:")
last_name_label.grid(row=1, column=0, padx=5, pady=5)
last_name_entry = tk.Entry(frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

# Creating the button to execute the query
query_button = tk.Button(tab1, text="Get Results", command=get_details_by_name)
query_button.pack(padx=10, pady=10)




# Tab for retrieving booked trains by passenger name
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text="Retrieve Train details by date")

# Creating the frame to hold the inputs
frame = tk.Frame(tab2)
frame.pack(padx=10, pady=10)

# Creating the input fields for first name and last name
date_label = tk.Label(frame, text="Enter train date (yyyy-mm-dd):")
date_entry = tk.Entry(frame)

# Creating the button to execute the query
query_button = tk.Button(tab2, text="Get Results", command=get_details_by_date)
query_button.pack(padx=10, pady=10)

# Creating the text box to display the results
date_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
date_entry.grid(row=0, column=1, padx=5, pady=5)
query_button.pack(padx=10, pady=10)




tab3 = ttk.Frame(tab_parent)
tab_parent.add(tab3, text="Retrieve Details by Age range")

frame = tk.Frame(tab3)
frame.pack(padx=10, pady=10)

# Creating the input fields for minimum and maximum age
min_age_label = tk.Label(frame, text="Minimum Age:")
min_age_label.grid(row=0, column=0, padx=5, pady=5)
min_age_entry = tk.Entry(frame)
min_age_entry.grid(row=0, column=1, padx=5, pady=5)

max_age_label = tk.Label(frame, text="Maximum Age:")
max_age_label.grid(row=1, column=0, padx=5, pady=5)
max_age_entry = tk.Entry(frame)
max_age_entry.grid(row=1, column=1, padx=5, pady=5)

# Creating the button to execute the query
query_button = tk.Button(tab3, text="Get Results", command=get_details_by_age)
query_button.pack(padx=10, pady=10)

# Creating the text box to display the results


tab4 = ttk.Frame(tab_parent)
tab_parent.add(tab4, text="Retrieve Train details by Ticket Type")

# Creating the frame to hold the inputs
frame = tk.Frame(tab4)
frame.pack(padx=10, pady=10)

ticket_type_label = tk.Label(frame, text="Ticket Type:")
ticket_type_label.grid(row=0, column=0, padx=5, pady=5)
ticket_type_entry = tk.Entry(frame)
ticket_type_entry.grid(row=0, column=1, padx=5, pady=5)

query_button = tk.Button(tab4, text="Get Results", command=get_details_by_ticket_type)
query_button.pack(padx=10, pady=10)


tab5 = ttk.Frame(tab_parent)
tab_parent.add(tab5, text="Retrieve Train details by Train Name")

# Creating the frame to hold the inputs
frame = tk.Frame(tab5)
frame.pack(padx=10, pady=10)

train_name_label = tk.Label(frame, text="Train Name:")
train_name_label.grid(row=0, column=0, padx=5, pady=5)
train_name_entry = tk.Entry(frame)
train_name_entry.grid(row=0, column=1, padx=5, pady=5)

query_button = tk.Button(tab5, text="Get Results", command=get_details_by_train_name)
query_button.pack(padx=10, pady=10)


# function to delete record from Booked table
def cancel_ticket_and_update_waitlist():
    # get input parameters from entry fields
    ssn = entry1.get()
    train_num = entry2.get()

    # cancel ticket for the passenger by first and last name
    cur.execute("""
    DELETE FROM Booked
    WHERE Passenger_SSN = ? AND Train_Number = ?
    """, (ssn,train_num))

    # update waitlist to book a ticket for the next passenger
    cur.execute("""
    CREATE TRIGGER IF NOT EXISTS update_waiting_list
    AFTER DELETE ON Booked
    BEGIN
        UPDATE Booked SET Status='Booked'
        WHERE Passenger_SSN IN (
            SELECT Passenger_SSN
            FROM Booked
            WHERE Train_Number = old.Train_Number AND Ticket_Type = old.Ticket_Type AND Status = 'WaitL'
            ORDER BY ROWID ASC
            LIMIT 1
        );
    END;
    """)

    # get the next passenger in waitlist to book a ticket
    cur.execute("""
    SELECT Passenger_SSN, Train_Number, Ticket_Type
    FROM Booked
    WHERE Status = 'WaitL'
    ORDER BY ROWID ASC
    LIMIT 1
    """)
    result = cur.fetchone()
    if result:
        # update the first passenger in waitlist to Booked status
        cur.execute("""
        UPDATE Booked SET Status = 'Booked'
        WHERE Passenger_SSN = ?
        """, (result[0],))

        # display the updated booked table after a successful booking
        cur.execute("""
        SELECT SSN, First_Name, Last_Name, Train.Train_Name, Booked.Status
        FROM Passenger
        INNER JOIN Booked ON Passenger.SSN = Booked.Passenger_SSN
        INNER JOIN Train ON Booked.Train_Number = Train.Train_Number
        WHERE Booked.Status = 'Booked'
        """)
        results = cur.fetchall()
        for widget in tab6.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        for result in results:
            row_label = tk.Label(tab6, text=f"SSN: {result[0]}\tPassenger Name: {result[1]} {result[2]}\tTrain Name: {result[3]}\tStatus: {result[4]}")
            row_label.pack()

        # commit changes to database
        conn.commit()


    else:
        # commit changes to database
        conn.commit()

        # display message box to show ticket cancellation success
        messagebox.showinfo("Success", "Ticket Cancelled Successfully")



tab6 = ttk.Frame(tab_parent)
tab_parent.add(tab6, text="Cancel Ticket")

# Creating the frame to hold the inputs
frame = tk.Frame(tab6)
frame.pack(padx=10, pady=10)

entry1_label = tk.Label(frame, text="SSN:")
entry1_label.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2_label = tk.Label(frame, text="Train Number:")
entry2_label.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)


# create cancel button to delete record and update waiting list
cancel_btn = tk.Button(tab6, text="Cancel Ticket", command=cancel_ticket_and_update_waitlist)
cancel_btn.pack( padx=10, pady=10)

tab_parent.pack(expand=1, fill="both")



# Running the GUI
root.mainloop()

# Closing the cursor and the connection
cur.close()
conn.close()
