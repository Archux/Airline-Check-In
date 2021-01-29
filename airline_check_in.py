from random import randint
from collections import OrderedDict
from pprint import pprint
import json
import sys


class Flight:
    def __init__(self, departing, arriving):
        self.departing = departing
        self.arriving = arriving
        self.menu = '''
Pick one of the options:
1. Add a passenger
2. Display all passengers
3. Display Economy
4. Display Business
5. Check Bags
6. Seatmap
7. Delete a passenger
8. Delete a bag
9. Exit

Which option would you like : 
'''
        self.menu_choice = 0
        self.seats = OrderedDict({
            "Business Seats": OrderedDict({
                "1A": False, "1B": False, "1C": False, "1D": False, "1E": False, "1F": False,
                "2A": False, "2B": False, "2C": False, "2D": False, "2E": False, "2F": False,
                "3A": False, "3B": False, "3C": False, "3D": False, "3E": False, "3F": False, }),
            "Economy Seats": OrderedDict({
                "4A": False, "4B": False, "4C": False, "4D": False, "4E": False, "4F": False,
                "5A": False, "5B": False, "5C": False, "5D": False, "5E": False, "5F": False,
                "6A": False, "6B": False, "6C": False, "6D": False, "6E": False, "6F": False,
                "7A": False, "7B": False, "7C": False, "7D": False, "7E": False, "7F": False,
                "8A": False, "8B": False, "8C": False, "8D": False, "8E": False, "8F": False,
                "9A": False, "9B": False, "9C": False, "9D": False, "9E": False, "9F": False,
                "10A": False, "10B": False, "10C": False, "10D": False, "10E": False, "10F": False,
                "11A": False, "11B": False, "11C": False, "11D": False, "11E": False, "11F": False,
                "12A": False, "12B": False, "12C": False, "12D": False, "12E": False, "12F": False,
                "13A": False, "13B": False, "13C": False, "13D": False, "13E": False, "13F": False, })})

    def __repr__(self):
        return(json.dumps(self.seats, indent=4).replace("false", "Empty Seat")
               .replace("{", "",).replace("}", "").replace(",", ""))

    def print_economy(self):
        return (json.dumps(self.seats["Economy Seats"], indent=4).replace("false", "Empty Seat")
                .replace("{", "", ).replace("}", "").replace(",", ""))

    def print_business(self):
        return (json.dumps(self.seats["Business Seats"], indent=4).replace("false", "Empty Seat")
                .replace("{", "", ).replace("}", "").replace(",", ""))


LV7777 = Flight(departing="Riga", arriving="Liepaja")


def random_digits():
    range_start = 10 ** (6 - 1)
    range_end = (10 ** 6) - 1
    return randint(range_start, range_end)


def stars(func):
    def wrapper(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)

    return wrapper


class Passenger:
    num_of_pax = 0
    all_pax = {}
    ticket_type = {"Economy": {}, "Business": {}}
    luggage_list = {}
    total_weight = 0

    def __init__(self, name=None, last_name=None, ticket=None,
                 seat=None, luggage=None, luggage_weight=None, special_req=None):
        self.name = name
        self.last_name = last_name
        self.ticket = ticket
        self.seat = seat
        self.luggage = luggage
        self.luggage_weight = luggage_weight
        self.special_req = special_req
        self.fullname = None

        Passenger.num_of_pax += 1

    def __repr__(self):
        return f"Name: {self.name}\nLast Name: {self.last_name} \n" \
               f"Ticket: {self.ticket}\n" \
               f"Luggage: {self.luggage}\nSpecial: {self.special_req}"

    def add_name(self):
        self.name = input("Name: ")
        self.last_name = input("Last Name: ")
        self.fullname = self.name + " " + self.last_name

    def add_ticket(self):
        while True:
            try:
                self.ticket = input("Type 'E' for Economy\nType 'B' for Business\n").upper()
                if self.ticket == "B":
                    print(f"{self.fullname} added to Business")
                elif self.ticket == "E":
                    print(f"{self.fullname} added to Economy")
                else:
                    print("That's not a valid input")
                    continue
            except ValueError:
                print("Please select either 'E' for Economy or 'B' for Business")
                continue
            else:
                break

    def add_luggage(self):
        question = input("Would you like to add a bag as well? Y/N ")
        if question.lower() == "y":
            self.luggage = f"BB{random_digits()}"
            Passenger.total_weight += 20
        else:
            pass

    def add_seat_business(self):
        if self.ticket.lower() == "e":
            pass
        if self.ticket.lower() == "b":
            print(LV7777.print_business())
            while True:
                self.seat = input("Which seat would you like? ").upper()
                for _ in LV7777.seats:
                    if self.seat in LV7777.seats["Business Seats"].keys():
                        if LV7777.seats["Business Seats"][self.seat] in ["", False]:
                            LV7777.seats["Business Seats"][self.seat] = self.fullname
                            Passenger.ticket_type["Business"][self.seat] = [self]
                            return
                        else:
                            continue
                print("Seat is either occupied or does not exist is this class.")

    def add_seat_economy(self):
        if self.ticket.lower() == "b":
            pass
        if self.ticket.lower() == "e":
            print(LV7777.print_economy())
            while True:
                self.seat = input("Which seat would you like? ").upper()
                for _ in LV7777.seats:
                    if self.seat in LV7777.seats["Economy Seats"].keys():
                        if LV7777.seats["Economy Seats"][self.seat] in ["", False]:
                            LV7777.seats["Economy Seats"][self.seat] = self.fullname
                            Passenger.ticket_type["Economy"][self.seat] = [self]
                            return
                        else:
                            continue
                print("Seat is either occupied or does not exist is this class.")

    def add_special_request(self):
        question = input("Would you like to add a 'Special Request'? Y/N ")
        if question.lower() == "y":
            self.special_req = input("What's the special request?\n")

    def sort_pax(self):
        Passenger.all_pax[self.seat] = self.fullname
        if self.luggage:
            Passenger.luggage_list[self.fullname] = self.luggage

    @classmethod
    @stars
    def display_all_pax(cls):
        print(f"Total Pax: {Passenger.num_of_pax}\n")
        for seat, fullname in Passenger.all_pax.items():
            pprint(f"{seat}: {fullname}")

    @classmethod
    @stars
    def display_economy(cls):
        print("Economy:\n")
        for pax in Passenger.ticket_type['Economy'].items():
            print(f"{pax}\n".replace("(", "").replace(")", "").replace(",", ":").replace("[", "").replace("]", ""))

    @classmethod
    @stars
    def display_business(cls):
        print("Business:\n")
        for pax in Passenger.ticket_type['Business'].items():
            print(f"{pax}\n".replace("(", "").replace(")", "").replace(",", ":").replace("[", "").replace("]", ""))

    @classmethod
    @stars
    def display_luggage(cls):
        print(f"Total bags: {len(Passenger.luggage_list)}\nTotal weight: {Passenger.total_weight}\n")
        for bag in Passenger.luggage_list.items():
            print(f"{bag}\n".replace("(", "").replace(")", "").replace(",", ":").replace("[", "").replace("]", ""))

    def save_(self):
        with open('pax_list.txt', 'a') as f:
            f.write(f"\n\nName: {self.name}\nLast Name: {self.last_name} \n"
                    f"Ticket: {self.ticket}\n"
                    f"Seat: {self.seat}\nLuggage: {self.luggage}\nSpecial: {self.special_req}")
        print("Passenger info also added to Pax_list file.")


def del_pax():
    try:
        del_seat = input("What's the seat number? ").upper()
        del Passenger.all_pax[del_seat]
        if del_seat in Passenger.ticket_type["Economy"]:
            del Passenger.ticket_type["Economy"][del_seat]
        elif del_seat in Passenger.ticket_type["Business"]:
            del Passenger.ticket_type["Business"][del_seat]
        Passenger.num_of_pax -= 1
        if del_seat in LV7777.seats["Economy Seats"] and LV7777.seats["Economy Seats"][del_seat] not in ["", False]:
            LV7777.seats["Economy Seats"][del_seat] = False
        elif del_seat in LV7777.seats["Business Seats"] and LV7777.seats["Business Seats"][del_seat] not in ["", False]:
            LV7777.seats["Business Seats"][del_seat] = False
    except KeyError:
        print("No such seat / passenger available to delete")


def del_bag():
    fullname = input("What's the full name? ")
    if fullname in Passenger.luggage_list:
        del Passenger.luggage_list[fullname]
        Passenger.total_weight -= 20
    else:
        print("No such passenger was found with a bag.")


def add_passenger():
    new = Passenger()
    new.add_name()
    new.add_ticket()
    new.add_luggage()
    new.add_seat_business()
    new.add_seat_economy()
    new.add_special_request()
    new.sort_pax()
    new.save_()
    print("All Done!")


def run_flight_menu():
    while True:
        try:
            LV7777.menu_choice = int(input(LV7777.menu))
            if LV7777.menu_choice == 1:
                add_passenger()
                continue
            elif LV7777.menu_choice == 2:
                Passenger.display_all_pax()
                continue
            elif LV7777.menu_choice == 3:
                Passenger.display_economy()
                continue
            elif LV7777.menu_choice == 4:
                Passenger.display_business()
                continue
            elif LV7777.menu_choice == 5:
                Passenger.display_luggage()
                continue
            elif LV7777.menu_choice == 6:
                print(LV7777)
                continue
            elif LV7777.menu_choice == 7:
                del_pax()
                continue
            elif LV7777.menu_choice == 8:
                del_bag()
                continue
            elif LV7777.menu_choice == 9:
                print('Thanks! Have good day ... ')
                sys.exit(0)
            else:
                print("That's not a valid option.")
        except ValueError:
            print("Enter one of the numbers from 'Menu'.")


if __name__ == '__main__':
    run_flight_menu()
