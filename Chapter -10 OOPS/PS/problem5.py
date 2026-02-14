class Train:
    def __init__(self, train_name, total_seats, fare_per_ticket):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_ticket = fare_per_ticket

    # Method to book ticket
    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= self.available_seats:
            self.available_seats -= number_of_tickets
            total_fare = number_of_tickets * self.fare_per_ticket
            print(f"{number_of_tickets} ticket(s) booked successfully!")
            print(f"Total fare: ₹{total_fare}")
        else:
            print("Sorry, not enough seats available.")

    # Method to get seat status
    def get_status(self):
        print(f"Train: {self.train_name}")
        print(f"Available Seats: {self.available_seats}/{self.total_seats}")

    # Method to get fare information
    def get_fare_info(self):
        print(f"Train: {self.train_name}")
        print(f"Fare per ticket: ₹{self.fare_per_ticket}")
