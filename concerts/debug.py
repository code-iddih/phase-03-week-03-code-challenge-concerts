#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb
from models import Band, Venue, Concert

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///concert.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()  

    # Test retrieving the first Band
    first_band = session.query(Band).first()
    if first_band:
        print("First Band:")
        print(" Name:", first_band.name)
        print(" Hometown:", first_band.hometown)

        # Band concerts()
        # Returns a collection of all the concerts that the Band has played
        print(" Concerts for First Band:", [concert.name for concert in first_band.concerts()])

        # Band venues()
        # Returns a collection of all the venues that the Band has performed at
        print("Venues for First Band:", [venue.title for venue in first_band.venues()])



        # Test retrieving the first Venue
        first_venue = session.query(Venue).first()
        if first_venue:
            print("\nFirst Venue:")
            print(" Title:", first_venue.title)
            print(" City:", first_venue.city)

            # Venue concerts()
            # Returns a collection of all the concerts for the Venue
            print(" Concerts for First Venue:", [concert.name for concert in first_venue.concerts()])
