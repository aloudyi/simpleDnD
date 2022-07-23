from classes.entity import Entity

class Character(Entity):
    def __init__(self,name,race,user_id,max_hp=10,current_hp=10,spells={},state="normal",
                state_duration=0,modifier=0,description="",picture_url="",level=0,current_xp=0,
                xp_to_next_level=3):
        super().__init__(self,name,race,max_hp,current_hp,state_duration,
                            spells,state, modifier,description,picture_url)
        self.spells = spells
        self.user_id = user_id
        self.level = level
        self.current_xp = current_xp
        self.xp_to_next_level = xp_to_next_level