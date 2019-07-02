import json
import datetime
import config
import math


class BikeRental(object):
    # missing docstring

    def __init__(self, bikes_rented, start_date, end_date, expiration_date):

        # not validating bikes_rented > 0
        # what about renting 100000000k bikes?
        self.bikes_rented = bikes_rented

        # hardcoded & copy-pasted and datetime formats
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
        self.expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')

        # not validating start_date < expiration_date and start_date < end_date
        self.weeks, self.days, self.hours = self._split_datetime(self.end_date - self.start_date)

    def _split_datetime(self, difference):
        # could be static or function
        # missing docstring

        weeks = int(difference.days / 7)
        days = difference.days - (weeks * 7)
        hours = math.ceil(difference.seconds / 3600)
        return weeks, days, hours

    def get_price(self):
        """Get the price"""

        budget = (
                self.weeks * config.RENT_PER_WEEK +
                self.days * config.RENT_PER_DAY +
                self.hours * config.RENT_PER_HOUR)

        # threshold for family discount is a magic number
        if self.bikes_rented >= 3:
            budget -= budget * config.FAMILY_DISCOUNT_PERCENTAJE / 100

        # not applying any penalty based on end_date - expiration_date > 0
        return budget * self.bikes_rented


class Rental(object):
    # missing docstring

    def __init__(self):
        self.rents = []

    def load_rentals(self):
        """Load the rentals"""

        # hardcoded path and filename
        f = open('in/rentals.json')

        # an invalid json will just raise an exception
        data = json.load(f)

        for r in data:
            self.rents.append(BikeRental(**r))

        # not using context manager. Exceptions before this will leave the resource open
        f.close()

    def get_report(self):
        """Prints a report to the terminal"""
        # method is called get_report but returns nothing
        # instead side effects a print to console instead

        # not open to extension
        lines = ["bikes\ttime rented\t\tprice"]

        for r in self.rents:
            lines.append(f"{r.bikes_rented}\t{r.weeks}w {r.days}d {r.hours}h\t\t{r.get_price()}")

        # printing instead of logging
        print('\n'.join(lines))


def main():
    rental = Rental()
    rental.load_rentals()
    rental.get_report()


if __name__== "__main__":
    main()
