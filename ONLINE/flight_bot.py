
def book_ticket():
    print("Hello! Welcome to the AI Travel Chatbot ")

    from_location = input("Enter departure city: ")
    to_location = input("Enter destination city: ")
    date = input("Enter travel date (DD-MM-YYYY): ")
    seats = int(input("How many seats do you want to book? "))

    print(f"\nSearching for trains from {from_location} to {to_location} on {date}...")

    
    trains = [
        {"name": "Express 101", "departure": "10:00 AM", "available_seats": 50},
        {"name": "SuperFast 202", "departure": "3:00 PM", "available_seats": 5},
        {"name": "Night Rider 303", "departure": "9:00 PM", "available_seats": 20},
    ]

    print("\nAvailable trains:")
    for idx, train in enumerate(trains):
        print(f"{idx + 1}. {train['name']} - Departs at {train['departure']} - Seats Available: {train['available_seats']}")

    choice = int(input("\nEnter the number of the train you want to book: ")) - 1

    if trains[choice]['available_seats'] >= seats:
        trains[choice]['available_seats'] -= seats
        print(f"\nBooking Confirmed! {seats} seat(s) on {trains[choice]['name']} from {from_location} to {to_location} on {date}")
    else:
        print(f"\nSorry! Not enough seats available on {trains[choice]['name']}")

book_ticket()
