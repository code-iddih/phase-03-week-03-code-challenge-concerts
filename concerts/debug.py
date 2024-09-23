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
        print(" Venues for First Band:", [venue.title for venue in first_band.venues()])

        # Band play_in_venue(venue, date)
        # Creates a new concert for the band in the specified venue on the given date
        if session.query(Venue).count() > 0:  # Ensuring there are venues available
            venue = session.query(Venue).first()  # Getting the first venue
            new_concert = first_band.play_in_venue(venue, "2024-10-11")
            session.add(new_concert)
            session.commit()
            print("A new concert has been created Successfully:")
            print("Name:", new_concert.name)
            print("Date:", new_concert.date)
        
        # Band all_introductions()
        # Returns an array of strings representing all the introductions for this band
        example_introduction = print("Introductions for First Band:", first_band.all_introductions())

        # Band most_performances()
        # Returns the Band instance for the band that has played the most concerts
        most_performed_band = Band.most_performances(session)
        print("\nBand with the most performances:")
        print("Name:", most_performed_band.name)
        print("Hometown:", most_performed_band.hometown)
        print("Total Concerts:", len(most_performed_band.concerts()))  




    # Test retrieving the first Venue
    first_venue = session.query(Venue).first()
    if first_venue:
        print("\nFirst Venue:")
        print(" Title:", first_venue.title)
        print(" City:", first_venue.city)

        # Venue concerts()
        # Returns a collection of all the concerts for the Venue
        print(" Concerts for First Venue:", [concert.name for concert in first_venue.concerts()])

        # Venue bands()
        # Returns a collection of all the bands who performed at the Venue
        print(" Bands for First Venue:", [band.name for band in first_venue.bands()])

        # Venue concert_on(date)
        # Finds and returns the first concert on that date at that venue
        concert_date = "2024-10-01"  
        concert = first_venue.concert_on(concert_date)
        if concert:
            print(f"\nConcert on {concert_date} at {first_venue.title}:")
            print("Name:", concert.name)
            print("Date:", concert.date)
        else:
            print(f"No concert found on {concert_date} at {first_venue.title}.")

        # Venue most_frequent_band()
        # Returns the band with the most concerts at the venue
        the_most_frequent_band, concert_counts = first_venue.most_frequent_band()
        if the_most_frequent_band:
            print(f"\nMost Frequent Band at {first_venue.title}:")
            print("Name:", the_most_frequent_band.name)
            print("Hometown:", the_most_frequent_band.hometown)
            print("Number of Concerts:", concert_counts)
        else:
            print(f"No concerts found at {first_venue.title}.")


    # Test retrieving the first Concert
    first_concert = session.query(Concert).first()
    if first_concert:
        print("\nFirst Concert:")
        print(" Name:", first_concert.name)
        print(" Date:", first_concert.date)

        # Concert band()
        # Returns the Band instance for this Concert
        print(" Band for First Concert:", first_concert.band().name)

        # Concert venue()
        # Returns the Venue instance for this Concert
        print(" Venue for First Concert:", first_concert.venue().title)

        # Concert hometown_show()
        # Returns True if the concert is in the band's hometown, False if it is not
        print(first_concert.hometown_show())

        # Concert introduction()
        # Returns a string with the band's introduction for this concert
        print(first_concert.introduction())


