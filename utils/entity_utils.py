from numpy import maximum

## State Functions
def set_entity_name(custom_name, entity):
    out_msg = entity.name+" has been renamed "+custom_name+"."
    entity.name = custom_name
    return out_msg
def set_entity_state_duration(state_duration, entity):
    entity.state_duration = state_duration
    out_msg = entity.name+" state_duration has been set to "+state_duration+"."
    return out_msg
def set_entity_user_id(user_id, entity):
    entity.user_id = user_id
    out_msg = entity.name+" user_id has been set to "+user_id+"."
    return out_msg
def set_entity_xp_to_next_level(xp_to_next_level, entity):
    entity.xp_to_next_level = xp_to_next_level
    out_msg = entity.name+" XP to next level has been set to "+xp_to_next_level+"."
    return out_msg
def set_entity_current_xp(current_xp, entity):
    entity.current_xp = int(current_xp)
    out_msg = entity.name+" current_xp has been set to "+current_xp+"."
    return out_msg
def set_entity_level(level, entity):
    entity.level = int(level)
    out_msg = entity.name+" level has been set to "+level+"."
    return out_msg
def set_entity_race(race, entity):
    entity.race = race
    out_msg = entity.name+" race has been set to "+race+"."
    return out_msg
def set_entity_current_hp(current_hp, entity):
    entity.current_hp = int(maximum(int(current_hp),entity.max_hp))
    out_msg = entity.name+" current_hp has been set to "+current_hp+"."
    return out_msg
def set_entity_max_hp(max_hp, entity):
    entity.max_hp = int(max_hp)
    out_msg = entity.name+" max_hp has been set to "+max_hp+"."
    return out_msg
def set_entity_state(state, entity):
    entity.state = state
    out_msg = entity.name+" state has been set to "+state+"."
    return out_msg
def set_entity_modifier(modifier, entity):
    entity.modifier = int(modifier)
    out_msg = entity.name+" modifier has been set to "+modifier+"."
    return out_msg
def set_entity_description(description, entity):
    entity.description = description
    out_msg = entity.name+" description has been set to "+description+"."
    return out_msg
def set_entity_picture(picture_url, entity):
    entity.picture_url = picture_url
    out_msg = entity.name+" picture_url has been set to "+picture_url+"."
    return out_msg
def set_entity_class(monster_class, monster_entity):
    monster_entity.monster_class = monster_class
    out_msg = monster_entity.name+" monster_class has been set to "+monster_class+"."
    return out_msg