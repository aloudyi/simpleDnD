from classes.Monster import Monster

def create_monster(content, env):
    content = content.split(" ")
    race = content[0]
    name = content[1]
    new_monster = Monster(name=name, race=race)
    env.create_monster(new_monster)