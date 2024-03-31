from payment import Payment  # Assuming Payment class is defined in Payment.py


class Booking:
    def __init__(self):
        self.show = None
        self.bookedSeats = []
        self.payment: Payment = None  # Type annotation for payment attribute

    def getShow(self):
        return self.show

    def setShow(self, show):
        self.show = show

    def getBookedSeats(self):
        return self.bookedSeats

    def setBookedSeats(self, bookedSeats):
        self.bookedSeats = bookedSeats

    def getPayment(self):
        return self.payment

    def setPayment(self, payment: Payment):  # Type annotation for payment setter
        self.payment = payment
