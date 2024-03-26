# Hotel Booking System

This is a simple hotel booking system implemented in Python. It uses pandas to manage data and Object-Oriented Programming (OOP) principles to structure the code. (The card authentication was simplified by providing arguments in the functions)
## Features

- Book a hotel
- Cancel a booking
- Book a spa package
- Handle multiple bookings
- Validate and authenticate a credit card

## Classes

- `Hotel`: Represents a hotel. It has methods to check availability, book a hotel, and cancel a booking.
- `SpaHotel`: Inherits from `Hotel`. It has an additional method to book a spa package.
- `ReservationTicket`: Represents a reservation ticket. It has a method to generate a ticket.
- `SpaTicket`: Inherits from `ReservationTicket`. It has a method to generate a spa ticket.
- `CreditCard`: Represents a credit card. It has a method to validate the card.
- `SecureCreditCard`: Inherits from `CreditCard`. It has an additional method to authenticate the card.

## How to Run

1. Ensure you have Python 3 and pandas installed.
2. Run `main.py` in your Python environment.
3. Follow the prompts in the console to book a hotel, book a spa package, or cancel a booking.

## Data

The system uses three CSV files to manage data:

- `hotels.csv`: Contains data about hotels.
- `cards.csv`: Contains data about credit cards.
- `card_security.csv`: Contains security data for credit cards.

## Future Improvements

- Add more features such as room selection, special requests, etc.
- Improve the user interface.
- Connect to a real database instead of using CSV files.