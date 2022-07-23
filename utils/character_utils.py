from classes.Character import Character

def create_character(content, user_id, env):
    content = content.split(" ")
    race = content[0]
    name = content[1] 
    new_character = Character(name=name,race=race,user_id=user_id)
    env.add_character(new_character)
