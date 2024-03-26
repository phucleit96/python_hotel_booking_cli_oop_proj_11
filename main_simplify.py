import pandas as pd
from abc import ABC, abstractmethod
df = pd.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == "yes":
            return True
        return False

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        return False


class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel.hotel_name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip().title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        return "Hello, this is your digital ticket"

    def download(self):
        pass


hotel1 = Hotel("188")
hotel2 = Hotel("134")
print(hotel1.hotel_name)
print(hotel2.watermark)
print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket('john doe', hotel1)
print(ticket.generate())
converted = ReservationTicket.convert(10)
print(converted)
