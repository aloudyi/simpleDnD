def create_monster(new_monster, env):
    env.create_monster(new_monster)
    out_msg = "The entity "+new_monster.name+" have been added to monsters, use the command **!bestiary** `monster_name` to see it's information profile."
    return out_msg