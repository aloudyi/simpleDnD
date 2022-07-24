class Spell:
    def __init__(self,
                 name,success_condition=10,type="normal",crit_condition=17,effect_duration=0,
                 crit_effect_duration=0,crit_damage=0,crit_heal=0,cooldown=0,current_cooldown=0,
                 effect="damage",crit_effect="damage",damage=0,heal=0,add_modifier=0,targets=1,
                 description="",picture_url=""):
        self.name = name
        self.success_condition = success_condition
        self.crit_condition = crit_condition
        self.damage = damage
        self.heal = heal
        self.cooldown = cooldown
        self.effect = effect
        self.targets = targets
        self.description = description
        self.picture_url = picture_url
        self.type = type
        self.crit_effect = crit_effect
        self.crit_effect_duration = crit_effect_duration
        self.crit_damage = crit_damage
        self.crit_heal = crit_heal
        self.effect_duration = effect_duration
        self.add_modifier = add_modifier
        self.current_cooldown = current_cooldown