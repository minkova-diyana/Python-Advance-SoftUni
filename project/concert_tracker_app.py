from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician: Singer, Drummer, Guitarist] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type != 'Guitarist' and musician_type != 'Drummer' and musician_type != 'Singer':
            raise ValueError('Invalid musician type!')
        if any([m for m in self.musicians if m.name == name]):
            raise Exception(f'{name} is already a musician!')
        musician = eval(f'{musician_type}(name, age)')
        self.musicians.append(musician)
        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if any([b for b in self.bands if b.name == name]):
            raise Exception(f'{name} band is already created!')
        band = Band(name)
        self.bands.append(band)
        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_check = [c for c in self.concerts if c.place == place]
        if any(concert_check):
            raise Exception(f'{place} is already registered for {concert_check[0].genre} concert!')  # genre ?
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f'{musician_name} isn\'t a musician!')
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f'{band_name} isn\'t a band!')
        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f'{band_name} isn\'t a band!')
        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f'{musician_name} isn\'t a member of {band_name}!')
        band.members.remove(musician)
        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        guitarist = []
        singers = []
        drummer = []
        musicians = guitarist + singers + drummer
        mandatory_skills = {'Rock': {'Guitarist': ['play rock'], 'Singer': ['sing high pitch notes'],
                                     'Drummer': ['play the drums with drumsticks']},
                            'Metal': {'Guitarist': ['play metal'], 'Singer': ['sing low pitch notes'],
                                      'Drummer': ['play the drums with drumsticks']},
                            'Jazz': {'Guitarist': ['play jazz'],
                                     'Singer': ['sing low pitch notes', 'sing high pitch notes'],
                                     'Drummer': ['play the drums with drum brushes']}}

        for musician in band.members:
            type_musician = musician.__class__.__name__
            if type_musician == 'Guitarist':
                guitarist.append(musician)
            elif type_musician == 'Singer':
                singers.append(musician)
            else:
                drummer.append(musician)
        if len(guitarist) == 0 or len(singers) == 0 or len(drummer) == 0:
            raise Exception(f'{band_name} can\'t start the concert because it doesn\'t have enough members!')
        musicians = guitarist + singers + drummer
        for m in musicians:
            for skill in mandatory_skills[concert.genre][m.__class__.__name__]:
                if skill not in m.skills:
                    raise Exception(f'The {band_name} band is not ready to play at the concert!')
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'
