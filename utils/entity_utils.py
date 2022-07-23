from numpy import maximum
## State Functions
def set_entity_name(name, entity):
    entity.name = name
def set_entity_state_duration(state_duration, entity):
    entity.state_duration = state_duration
def set_entity_user_id(user_id, entity):
    entity.user_id = user_id
def set_entity_xp_to_next_level(xp_to_next_level, entity):
    entity.xp_to_next_level = xp_to_next_level
def set_entity_current_xp(current_xp, entity):
    entity.current_xp = int(current_xp)
def set_entity_level(level, entity):
    entity.level = int(level)
def set_entity_race(race, entity):
    entity.race = race
def set_entity_current_hp(current_hp, entity):
    entity.current_hp = int(maximum(int(current_hp),entity.max_hp))
def set_entity_max_hp(max_hp, entity):
    entity.max_hp = int(max_hp)
def set_entity_state(state, entity):
    entity.state = state
def set_entity_modifier(modifier, entity):
    entity.modifier = int(modifier)
def set_entity_description(description, entity):
    entity.description = description
def set_entity_picture(picture_url, entity):
    entity.picture_url = picture_url