# Airline-Check-In

Tried to make a simple version on an airline check-in system, where passengers can be added, assigned to seats of a given flight, luggage can be added etc.
Once code runs, you have a menu of options to select from:

1. Add a passenger:

  Asks to input a name, last name, Economy or Business class, asks if luggage should also be included, 
  displays seats according to the class and let's you choose one of the available seats and also asks if some special request is needed to add for the passenger.
  Once all information in given, passenger gets saved in additional file "pax_list.txt" where they can be seen and added back with same info, 
  in case someone gets deleted by mistake or just to trace back who was origionally added to the flight.
  
2. Display all passengers:

  Shows total number and list of all current passengers for the flight by seat number and full name, for quick overview.
  
3. Display Economy:

  Shows all details for each passenger currently in the Economy class.
  
4. Display Business:

  Shows all details for each passenger currently in the Business class.
  
5. Check Bags:

  Displays total weight of all checked in bags (each 20 kg), total amount of bags and a list with full name of the passenger and the bag "tag number". 
  
6. Seatmap:

  Shows all the seats on the airplane (rows 1 to 13 in this case) by splitting "Business" and "Economy" classes and shows either seat is empty or assigned to someone.
  
7. Delete a passenger:

  Lets you delete a passenger by giving the seat number of the person you want to remove.
  
8. Delete a bag:

  Lets you delete a bag by giving the full name of the passenger whos bag you want to remove.
  
9. Exit
