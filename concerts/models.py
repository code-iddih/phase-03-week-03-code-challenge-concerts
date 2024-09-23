import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    ForeignKey,
    create_engine,
    Column,
    Integer,
    String,
    Table,
    Date
)

from sqlalchemy.orm import (
    relationship,
    sessionmaker
)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = 'sqlite:///' + os.path.join(BASE_DIR , 'concert.db')

engine = create_engine('sqlite:///concert.db')

Base = declarative_base()

# Band Model
class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer() , primary_key = True)
    name = Column(String(255) , nullable = False)
    hometown = Column(String(255) , nullable = False)
    # Defining the relationship
    concerts_list = relationship(
        'Concert', 
        back_populates = 'band_instance'
    )

    # Object Relationship Methods

    def concerts(self):
        return self.concerts_list
    
    def venues(self):
        return [concert.venue_instance for concert in self.concerts_list]


# Venue Model
class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer() , primary_key = True)
    title = Column(String(255) , nullable = False)
    city = Column(String(255) , nullable = False)
    # Defining the relationship
    concerts_list = relationship(
        'Concert',
        back_populates = 'venue_instance'
    )

    # Object Relationship Methods

    def concerts(self):
        return self.concerts_list
    
    def bands(self):
        return [concert.band_instance for concert in self.concerts_list] 


# Concert Model
class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer() , primary_key = True)
    name = Column(String(255) , nullable = False)
    date = Column(String(50) , nullable = False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    band_instance = relationship('Band', back_populates='concerts_list')
    venue_instance = relationship('Venue', back_populates='concerts_list')

    # Object Relationship Methods

    def band(self):
        return self.band_instance
    
    def venue(self):
        return self.venue_instance
    
    # Aggregate and Relationship Methods

    def hometown_show(self):
        return self.venue_instance.city == self.band_instance.hometown

