from classes.Entity import Entity

class Monster(Entity):
    def __init__(self,name,race,max_hp=10,current_hp=10,state_duration=0,
                 spells={},state="normal", modifier=0,description="",picture_url=""):
        super().__init__(self,name,race,max_hp,current_hp,state_duration,
                            spells,state, modifier,description,picture_url)
        self.monster_class = name