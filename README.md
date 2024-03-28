# Railway-Reservation-System

This report consists of three sections:
1.	Honor Code
2.	Query Implementation in the UI
3.	Team Contributions

QUERY IMPLEMENTATION IN THE UI
Query-1: User input the passenger’s last name and first name and retrieve all trains they are booked on.
 
We enter the first name and last name of the passenger we get the list of trains they’re booked on. We see the train name and train number.
Query-2: User input the Date and list of passengers travelling on entered day with ‘Booked’ tickets displays on UI.
 
Upon entering the date of journey, we get the details of the passengers traveling on that day along with the train details like train name and number , and finally the ticket category.

Query-3: User input the age of the passenger (50 to 60) and UI display the train information (Train Number, Train Name, Source and Destination) and passenger information (Name, Address, Category, ticket status) of passengers who are between the ages of 50 to 60.
 
Our database contains the date of birth of passengers. We use that to retrieve the list of passengers aged between 50 and 60 along with the details of the passengers and the respective trains.
Query-4: List all the train name along with count of passengers it is carrying
 
 
In this query, we are having user input of Ticket Type. We are displaying an entire list of all the trains along with the passengers it’s carrying of that ticket type. Although we have five trains, this shows only three of them because only these are booked with passengers.

Query-5: Enter a train name and retrieve all the passengers with confirmed status travelling in that train.
 
When the user enters the name of the train, it returns the details of the passenger traveling in it, along with the train details.

Query-6: User Cancel a ticket (delete a record) and show that passenger in waiting list get ticket
confirmed.
Case - 1:  When there are No WaitL tickets. Then we just cancel the booked ticket and don’t update any other ticket from Booked to WaitL.
 
Case - 2: When there are WaitL tickets. Then we cancel the booked ticket and update a WaitL ticket to Booked status. We will also display all the Booked tickets.
