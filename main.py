# Import pandas library
import pandas as pd

# Read the hotels.csv file and convert the 'id' column to string
df = pd.read_csv('hotels.csv', dtype={"id": str})

# Read the cards.csv file and convert it to a dictionary
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')

# Read the card_security.csv file
df_cards_security = pd.read_csv('card_security.csv', dtype=str)

# Define a class Hotel
class Hotel:
    # Initialize the Hotel object with hotel_id and hotel_name
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    # Check if the hotel is available
    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == "yes":
            return True
        return False

    # Book the hotel
    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    # Cancel the booking
    def cancel_booking(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'yes'
        df.to_csv('hotels.csv', index=False)

# Define a class SpaHotel that inherits from Hotel
class SpaHotel(Hotel):
    # Book a spa package
    def book_spa_package(self):
        print("Spa package booked.")

# Define a class ReservationTicket
class ReservationTicket:
    # Initialize the ReservationTicket object with customer_name and hotel_object
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    # Generate a reservation ticket
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.hotel_name}
"""
        return content

# Define a class SpaTicket that inherits from ReservationTicket
class SpaTicket(ReservationTicket):
    # Initialize the SpaTicket object with customer_name and hotel_object
    def __init__(self, customer_name, hotel_object):
        super().__init__(customer_name, hotel_object)

    # Generate a spa ticket
    def generate(self):
        content = f"""
                Thank you for your SPA reservation!
                Here are your SPA booking data:
                Name: {self.customer_name}
                Hotel: {self.hotel.hotel_name}
        """
        return content

# Define a class CreditCard
class CreditCard:
    # Initialize the CreditCard object with number
    def __init__(self, number):
        self.number = number

    # Validate the credit card
    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration, 'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        return False

# Define a class SecureCreditCard that inherits from CreditCard
class SecureCreditCard(CreditCard):
    # Authenticate the credit card
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        return False

# Print the dataframe df
print(df)

# Handle multiple bookings
while True:
    hotel_ID = input("Enter the id of the hotel (or 'exit' to quit): ")
    if hotel_ID.lower() == 'exit':
        break
    hotel = SpaHotel(hotel_ID)
    if hotel.available():
        credit_card = SecureCreditCard(number="1234567890123456")
        if credit_card.validate(expiration="12/26", holder="JOHN DOE", cvc="123"):
            if credit_card.authenticate(given_password='mypass'):
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
                print(reservation_ticket.generate())
                spa = input("Do you want to book a spa package? (yes/no): ")
                if spa == "yes":
                    hotel.book_spa_package()
                    spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                    print(spa_ticket.generate())
                cancel = input("Do you want to cancel a booking? (yes/no): ")
                if cancel == "yes":
                    hotel.cancel_booking()
                    print("Booking cancelled.")
            else:
                print('Credit card authentication failed')
        else:
            print("There was a problem with your payment")
    else:
        print("Hotel is not free.")