from datetime import datetime, timedelta
import random
import json

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class BikeRental(object):

    def __init__(self, bikes_rented:int, start_date:datetime, end_date:datetime, expiration_date:datetime):
        self. bikes_rented = bikes_rented
        self.start_date = datetime.strftime(start_date, DATE_FORMAT)
        self.end_date = datetime.strftime(end_date, DATE_FORMAT)
        self.expiration_date = datetime.strftime(expiration_date, DATE_FORMAT)


class BikeRentalBuilder(object):

    def build(self, bikes_rented, start_date, duration, expired):

        expiration_date = start_date + duration
        end_date = start_date + duration

        if expired:
            end_date += expired

        return BikeRental(bikes_rented, start_date, end_date, expiration_date)


def main():

    with open('in/rentals.json', mode='w+') as file:

        builder = BikeRentalBuilder()

        latest_rental = datetime.now()

        bikes = list()

        for i in range(10):

            bikes_rented = random.randrange(1, 6)

            duration = timedelta(
                days=random.randrange(0,30),
                hours=random.randrange(0,24),
                minutes=random.randrange(0, 59))

            expired = timedelta(
                days=random.randrange(0,30),
                hours=random.randrange(0,24),
                minutes=random.randrange(0, 59))

            has_expired = [True]*3+[False]

            bikes.append(builder.build(bikes_rented, latest_rental, duration, expired if random.choice(has_expired) else None))

            latest_rental += timedelta(hours=random.randrange(0,12), minutes=random.randrange(0, 59))

        file.write(json.dumps(list(map(lambda x: x.__dict__, bikes)), indent=4))


if __name__== "__main__":
    main()
