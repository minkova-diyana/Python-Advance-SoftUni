from project.band_members.musician import Musician


class Guitarist(Musician):
    AVAILABLE_SKILLS_MUSICIAN_CAN_LEARN = ['play metal', 'play rock', 'play jazz']

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
