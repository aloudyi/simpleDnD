
def create_character(new_character, user_id, env):
    env.add_character(new_character)
    out_msg = "The character "+new_character.name+" has been created, use **!profile** command to see it's information profile."
    return out_msg