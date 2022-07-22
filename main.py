import profile
from re import M
import discord
import numpy as np
import pickle as pkl
import aux_functions
from pyrsistent import field
import copy

class Character:
    def __init__(self, name, race, user_id, max_hp=10, current_hp=10, spells={}, state="normal", state_duration = 0, modifier=0,description="",picture_url="",level=0,current_xp=0,xp_to_next_level=3):
        self.name = name
        self.race = race
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.spells = spells
        self.state = state
        self.modifier = modifier
        self.description = description
        self.picture_url = picture_url
        self.user_id = user_id
        self.level = level
        self.current_xp = current_xp
        self.xp_to_next_level = xp_to_next_level
        self.state_duration = state_duration

    def damage(self,damage):
        self.current_hp=np.maximum(0,self.current_hp-damage)
        if(self.current_hp==0):
            self.state = "unanimated"
    
    def heal(self,heal):
        if(self.current_hp==0):
            self.state = "normal"
        self.current_hp=np.minimum(self.max_hp,self.current_hp+heal)

    def apply_spell(self,spell):
        dice_roll = np.random.randint(1,21)+self.modifier
        modifier = self.modifier
        self.modifier = 0
        if(spell.type=="normal"):
            if(dice_roll>=spell.crit_condition):
                add_heal = spell.crit_heal        
                add_damage = spell.crit_damage
                add_duration = spell.crit_effect_duration
            else:
                add_heal = 0
                add_damage = 0
                add_duration = 0
            if(dice_roll>=spell.success_condition):
                if(spell.effect=="heal"):
                    self.heal(spell.heal+add_heal)
                elif(spell.effect=="buff"):
                    self.modifier = spell.add_modifier
                elif(spell.effect=="drain"):
                    self.heal(spell.heal+add_heal)
                    self.damage(spell.damage+add_damage)
                    
                elif(spell.effect=="damage"):
                    self.damage(spell.damage+add_damage)

                elif(spell.effect=="stun"):
                    print("khbzat")
                    self.damage(spell.damage+add_damage)
                    self.state = "stunned"
                    self.state_duration = spell.effect_duration+add_duration
        elif(spell.type=="double-edge"):
            if(dice_roll<spell.success_condition):
                if(spell.effect=="heal"):
                    self.damage(spell.damage)
                else:
                    self.heal(spell.heal)
            else:
                if(spell.effect=="heal"):
                    self.heal(spell.heal)
                else:
                    self.damage(spell.damage)

        return dice_roll, modifier
class Spell:
    def __init__(self, name, success_condition=10, type="single", crit_condition=17, effect_duration=0, crit_effect_duration=0, crit_damage=0, crit_heal=0, cooldown=0, effect="damage", crit_effect="damage", damage=0, heal=0, add_modifier=0, targets=1, description="", picture_url=""):
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
        #sus
        self.crit_effect = crit_effect
        self.crit_effect_duration = crit_effect_duration
        self.crit_damage = crit_damage
        self.crit_heal = crit_heal
        self.effect_duration = effect_duration
        self.add_modifier = add_modifier
class Monster:
    def __init__(self, name, race, max_hp=10, current_hp=10, state_duration=0, spells={}, state="normal", modifier=0,description="",picture_url=""):
        self.name = name
        self.monster_class = name
        self.race = race
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.spells = spells
        self.state = state
        self.state_duration = state_duration
        self.modifier = modifier
        self.description = description
        self.picture_url = picture_url
    
    def damage(self,damage):
        print("baqbaq")
        self.current_hp=np.maximum(0,self.current_hp-damage)
        if(self.current_hp==0):
            self.state = "unanimated"
    def heal(self,heal):
        if(self.current_hp==0):
            self.state = "normal"
        self.current_hp=np.minimum(self.max_hp,self.current_hp+heal)
        

    def apply_spell(self,spell):
        dice_roll = np.random.randint(1,21)+self.modifier
        modifier = self.modifier
        self.modifier = 0

        if(dice_roll>spell.crit_condition):
            add_heal = spell.crit_heal        
            add_damage = spell.crit_damage
            add_duration = spell.crit_effect_duration
        else:
            add_heal = 0
            add_damage = 0
            add_duration = 0
        if(dice_roll>spell.success_condition):
            if(spell.effect=="heal"):
                self.heal(spell.heal+add_heal)
            elif(spell.effect=="buff"):
                self.modifier = spell.add_modifier
            elif(spell.effect=="drain"):
                self.heal(spell.heal+add_heal)
                self.damage(spell.damage+add_damage)
                
            elif(spell.effect=="damage"):
                self.damage(spell.damage+add_damage)

            elif(spell.effect=="stun"):
                print("khbzat")
                self.damage(spell.damage+add_damage)
                self.state = "stunned"
                self.state_duration = spell.effect_duration+add_duration

        return dice_roll, modifier
class Environment:
    def __init__(self, dict_characters={}, dict_monsters={}, dict_spells={},dict_battle={}):
        self.dict_monsters = dict_monsters # Monster Library
        self.dict_characters = dict_characters # Character Library
        self.dict_spells = dict_spells # Spell Library
        self.dict_battle = dict_battle  # Monsters in battle

    def use_spell(self, caster, spellname, target):
        spell = caster.spells[spellname]
        msg_append = ""

        if(target.name in self.dict_battle.keys()):
            if(target.current_hp==0):
                env.dict_battle.pop(target.name)
                msg_append = "\n**"+caster.name+ " defeated " +target.name+"**."
            
        dice_roll, modifier = target.apply_spell(spell)

        out_msg = "**"+caster.name+"** used `"+spellname+"` on **"+target.name+"**."+msg_append
        return out_msg, dice_roll, modifier

    def add_monster(self,monster):
        self.dict_battle[monster.name] = monster

    def add_character(self,character):
        self.dict_characters[character.user_id] = character

    def add_spell(self,spell):
        self.dict_spells[spell.name] = spell

    def create_monster(self,monster):
        self.dict_monsters[monster.name] = monster

    def save_env(self):
        save = {"monsters":self.dict_monsters,"characters":self.dict_characters,"spells":self.dict_spells,"battle":self.dict_battle}
        output = open(path_to_current+"save_env.pkl","wb")
        pkl.dump(save,output)
        output.close()
        print("Saved env !")
    
    def reload_env(self):
        input = open(path_to_current+"save_env.pkl","rb")
        save = pkl.load(input)
        self.dict_characters = save["characters"]
        self.dict_monsters = save["monsters"]
        self.dict_spells = save["spells"]
        self.dict_battle = save["battle"]
        input.close()


# Initialize the discord client
client = discord.Client()
# Initialize the environment
env = Environment()

path_to_current = "/mnt/c/Users/loudy/Desktop/simpleDnD/"
question_mark_pic = "https://cdn.icon-icons.com/icons2/2367/PNG/512/question_mark_icon_143522.png"
brahim_id = 414778100195393537
game_log_channel_id = 680502901936095425
roll_me_daddy_id = 680495998249730057

# Renvoie un embed
def battle_summary(caster,spellname,target):
    target_old_hp = target.current_hp
    #Use spell
    battle_recap, dice_roll, modifier = env.use_spell(caster,spellname,target)
    embed=discord.Embed(color=0xFF5733)
    # Author name & Author Icon
    embed.set_author(name=caster.name,icon_url=caster.picture_url)
    if(caster.state=="stunned"):
        if(caster.state_duration==0):
            caster.state="normal"
        else:
            caster.state_duration -= 1
            embed.add_field(name="You are **STUNNED**, you can't play this turn.")
            return embed
    # Battle recap
    if(modifier!=0):
        modifier_txt =  "+ "+str(modifier)
    else:
        modifier_txt = ""
    embed.set_thumbnail(url=target.picture_url)
    roll = "You rolled "+str(dice_roll)+modifier_txt+" (**"+str(dice_roll+modifier)+"**)."
    msg = battle_recap+"\n"+roll
    embed.add_field(name="BattleRecap :",value=msg,inline=False)
    if(caster.state=="stunned"):
        duration = "("+str(caster.state_duration)+")"
    else:
        duration = ""
    caster_msg = "**HitPoints** : "+str(caster.current_hp)+"/*"+str(caster.max_hp)+"*\n **State** : *"+caster.state+duration+"*."
    
    if(target.state=="stunned"):
        duration = "("+str(target.state_duration)+")"
    else:
        duration = ""
    target_msg = "**HitPoints** : "+str(target.current_hp)+"("+str(-target_old_hp+target.current_hp)+")/*"+str(target.max_hp)+"*\n **State** : *"+target.state+duration+"*."
    embed.add_field(name=caster.name,value=caster_msg,inline=True)
    embed.add_field(name=target.name,value=target_msg,inline=True)
    return embed

def get_spell_embed(spellname):
    spell = env.dict_spells[spellname]

    embed = discord.Embed(color=0x5733FF)
    
    # Spell Picture
    if(spell.picture_url!=""):
        embed.set_thumbnail(url=spell.picture_url)

    # Spell Summary    
    name = spellname
    effect = spell.effect
    targets = str(spell.targets)
    cooldown = str(spell.cooldown)
    add_modifier = str(spell.add_modifier)
    type = spell.type

    embed.set_author(name="Spell Summary")
    value = "Effect : "+effect+"\nSpell Type : "+type+"\nTargets : "+targets+"\nCooldown : "+cooldown+"\nModifier: "+add_modifier
    embed.add_field(name=name,value=value,inline=False)
    
    # Normal
    title = "Normal Effects"
    success = str(spell.success_condition)
    damage = str(spell.damage)
    heal = str(spell.heal)
    effect_duration = str(spell.effect_duration)
    value = "Success Roll >= "+success+"\nEffect Duration :"+effect_duration+"\nDamage : "+damage+"\nHeal : "+heal
    embed.add_field(name=title,value=value)

    # Crit
    title = "Critical Effects"
    success = str(spell.crit_condition)
    damage = str(spell.crit_damage+spell.damage)
    heal = str(spell.crit_heal+spell.crit_heal)
    effect_duration = str(spell.crit_effect_duration+spell.effect_duration)

    value = "Critical Success Roll >= "+success+"\nCritical Effect Duration :"+effect_duration+"\nCritical Damage : "+damage+"\nCritical Heal : "+heal
    embed.add_field(name=title,value=value)

    return embed
def get_profile_embed(user_id):
    char = env.dict_characters[user_id]
    name = char.name
    level = str(char.level)
    race = char.race
    xp = str(char.current_xp)
    next_level = str(char.xp_to_next_level)
    spellnames = [spell for spell in char.spells.keys()]
    profile_pic = char.picture_url
    hp = str(char.current_hp)
    max_hp = str(char.max_hp)
    embed=discord.Embed(color=0xFF5733)
    embed.set_author(name=name)
    if(profile_pic!=""):
        embed.set_thumbnail(url=profile_pic)
    field_value = "Name : "+name+"\nRace: "+race+"\nLevel : "+level+"\nHitPoints : "+hp+"/"+max_hp+"\nXP : "+xp+"/"+next_level+"\nSpells : "
    for spellname in spellnames:
        field_value = field_value + "\n* "+spellname+"."
    embed.add_field(name="Profile",value=field_value)
    embed.add_field(name="Description",value=char.description,inline=False)
    print(embed)
    return embed

def get_monster_profile_embed(name):
    char = env.dict_monsters[name]
    name = char.name
    race = char.race
    spellnames = [spell for spell in char.spells.keys()]
    profile_pic = char.picture_url
    hp = str(char.current_hp)
    max_hp = str(char.max_hp)
    embed=discord.Embed(color=0xFF5733)
    embed.set_author(name=name)
    if(profile_pic!=""):
        embed.set_thumbnail(url=profile_pic)
    field_value = "Name : "+name+"\nRace: "+race+"\nHitPoints : "+hp+"/"+max_hp+"\nSpells : "
    for spellname in spellnames:
        field_value = field_value + "\n* "+spellname+"."
    embed.add_field(name="Profile",value=field_value)
    embed.add_field(name="Description",value=char.description,inline=False)
    
    print("name",name)
    print("url",profile_pic)
    print("field_value",field_value)
    print("description",char.description)
    print("spellnames",spellnames)
    print("isEmbdedNone ?",embed==None)
    print("type",type(embed))
    return embed

def get_monster_perception_profile_embed(name,user_id):
    perception_roll = np.random.randint(1,21)
    char = env.dict_battle[name]

    name = char.name
    if(perception_roll>=10):
        race = char.race
        monster_class = char.monster_class
    else:
        race = "????"
        monster_class = "????"
    if(perception_roll>10):
        description = char.description
    else:
        description = "?????"
    if(perception_roll>=12):
        profile_pic = char.picture_url
    else:
        profile_pic =question_mark_pic
    if(perception_roll>=14):
        spellnames = [spell for spell in char.spells.keys()]
    else:
        spellnames = []
    if(perception_roll>=15):
        hp = str(char.current_hp)
        max_hp = str(char.max_hp)
    else:
        hp = "??"
        max_hp = "??"
    embed=discord.Embed(color=0xFF5733)
    embed.set_author(name=name)
    if(profile_pic!=""):
        embed.set_thumbnail(url=profile_pic)
    field_value = "Name : "+name+"\nClass: "+monster_class+"\nRace: "+race+"\nHitPoints : "+hp+"/"+max_hp+"\nSpells : "
    for spellname in spellnames:
        field_value = field_value + "\n* "+spellname+"."
    embed.add_field(name="Profile",value=field_value)
    embed.add_field(name="Description",value=description,inline=False)
    text = env.dict_characters[user_id].name+" rolled **"+str(perception_roll)+"** on his perception roll."
    embed.description=text
    print("url",profile_pic)
    print("field_value",field_value)
    print("description",char.description)
    print("spellnames",spellnames)
    print("isEmbdedNone ?",embed==None)
    return embed


## State Functions
def set_entity_name(name,entity):
    entity.name = name
def set_entity_state_duration(state_duration,entity):
    entity.state_duration = state_duration
def set_entity_user_id(user_id,entity):
    entity.user_id = user_id
def set_entity_xp_to_next_level(xp_to_next_level,entity):
    entity.xp_to_next_level = xp_to_next_level
def set_entity_current_xp(current_xp,entity):
    entity.current_xp = int(current_xp)
def set_entity_level(level,entity):
    entity.level = int(level)
def set_entity_race(race,entity):
    entity.race = race
def set_entity_current_hp(current_hp,entity):
    entity.current_hp = int(current_hp)
def set_entity_max_hp(max_hp,entity):
    entity.max_hp = int(max_hp)
def set_entity_state(state,entity):
    entity.state = state
def set_entity_modifier(modifier,entity):
    entity.modifier = int(modifier)
def set_entity_description(description,entity):
    entity.description = description
def set_entity_picture(picture_url,entity):
    entity.picture_url = picture_url

# Spell Management
def create_spell(spellname):
    new_spell = Spell(name=spellname)
    env.add_spell(new_spell) 
def link_spell(entity,spellname,target_dict):
    spell = target_dict[spellname]
    entity.spells[spellname] = spell
def set_spell_success(message,spellname,target_dict):
    msg = message.content
    success_condition = msg.split("set spell success ",1)[1]
    target_dict[spellname].success_condition = int(success_condition)
def set_spell_type(message,spellname,target_dict):
    msg = message.content
    type = msg.split("set spell crit ",1)[1]
    target_dict[spellname].type = type
def set_spell_crit(message,spellname,target_dict):
    msg = message.content
    crit_condition = msg.split("set spell crit ",1)[1]
    target_dict[spellname].crit_condition = int(crit_condition)
def set_spell_damage(message,spellname,target_dict):
    msg = message.content
    damage = msg.split("set spell damage ",1)[1]
    print(damage)
    target_dict[spellname].damage = int(damage)  
def set_spell_heal(message,spellname,target_dict):
    msg = message.content
    heal = msg.split("set spell heal ",1)[1]
    target_dict[spellname].heal = int(heal)
def set_spell_cooldown(message,spellname,target_dict):
    msg = message.content
    cooldown = msg.split("set spell cooldown ",1)[1]       
    target_dict[spellname].cooldown = int(cooldown)
def set_spell_effect(message,spellname,target_dict):
    msg = message.content
    effect = msg.split("set spell effect ",1)[1]
    target_dict[spellname].effect = effect
def set_spell_targets(message,spellname,target_dict):
    msg = message.content
    targets = msg.split("set spell targets ",1)[1]     
    target_dict[spellname].targets = int(targets)
def set_spell_description(message,spellname,target_dict):
    msg = message.content
    description = msg.split("set spell description ",1)[1]
    target_dict[spellname].description = description
def set_spell_picture(message,spellname,target_dict):
    msg = message.content
    picture_url = msg.split("set spell picture ",1)[1]
    target_dict[spellname].picture_url = picture_url
def set_spell_crit_effect(message,spellname,target_dict):
    msg = message.content
    crit_effect = msg.split("set spell crit_effect ",1)[1]
    target_dict[spellname].crit_effect = int(crit_effect)
def set_spell_crit_effect_duration(message,spellname,target_dict):
    msg = message.content
    crit_effect_duration = msg.split("set spell crit_effect_duration ",1)[1]
    target_dict[spellname].crit_effect_duration = int(crit_effect_duration) 
def set_spell_crit_damage(message,spellname,target_dict):
    msg = message.content
    crit_damage = msg.split("set spell crit_damage ",1)[1]
    target_dict[spellname].crit_damage = int(crit_damage)
def set_spell_crit_heal(message,spellname,target_dict):
    msg = message.content
    crit_heal = msg.split("set spell crit_heal ",1)[1]
    target_dict[spellname].crit_heal = int(crit_heal)
def set_spell_effect_duration(message,spellname,target_dict):
    msg = message.content
    effect_duration = msg.split("set spell effect_duration ",1)[1]
    print("sfx_duration",effect_duration)
    target_dict[spellname].effect_duration = int(effect_duration)
def set_spell_modifier(message,spellname,target_dict):
    msg = message.content
    modifier = msg.split("set spell modifier ",1)[1]
    target_dict[spellname].add_modifier = int(modifier)
def remove_spell(message,target_dict):
    content = message.content.split("remove spell ",1)[1]
    content = content.split(" ")
    spellname = content[0]
    target_dict.pop(spellname)

# Monster Management



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    # Reload previous environment
    env.reload_env()

@client.event
async def on_message(message):        
    
    game_log_channel = client.get_channel(id=game_log_channel_id)

    # helper function 
    def fight_summary(caster,target):
        msg = caster.name+" "+str(caster.current_hp)+"/"+str(caster.max_hp)+"   \*\*\*\*\*   "+target.name+" "+str(target.current_hp)+"/"+str(target.max_hp)+"\n"
        return msg
    
    if (message.author == client.user):
        return

    msg = message.content
    # Create a character 
    # create character race name
    if(msg.startswith("!create character ")):
        content = msg.split("!create character ",1)[1]
        content = content.split(" ")
        race = content[0]
        name = content[1]
        
        new_character = Character(name=name,race=race,user_id=message.author.id)
        env.add_character(new_character)

    # Set character parameters
    if(msg.startswith("!set name ")):
        race = msg.split("!set name ",1)[1]
        set_entity_name(name,env.dict_characters[message.author.id])            
    elif(msg.startswith("!set race ")):
        race = msg.split("!set race ",1)[1]
        set_entity_race(race,env.dict_characters[message.author.id])        
    elif(msg.startswith("!set current_hp ")):
        current_hp = msg.split("!set current_hp ",1)[1]
        set_entity_current_hp(current_hp,env.dict_characters[message.author.id])
    elif(msg.startswith("!set max_hp ")):
        max_hp = msg.split("!set max_hp ",1)[1]
        set_entity_max_hp(max_hp,env.dict_characters[message.author.id])  
    elif(msg.startswith("!set state ")):
        state = msg.split("!set state ",1)[1]
        set_entity_state(state,env.dict_characters[message.author.id])
    elif(msg.startswith("!set modifier ")):
        modifier = msg.split("!set modifier ",1)[1]
        set_entity_modifier(modifier,env.dict_characters[message.author.id])
    elif(msg.startswith("!set description ")):
        description = msg.split("!set description ",1)[1]
        set_entity_description(description,env.dict_characters[message.author.id])
    elif(msg.startswith("!set picture ")):
        picture_url = msg.split("!set picture ",1)[1]
        set_entity_picture(picture_url,env.dict_characters[message.author.id])
    elif(msg.startswith("!set level ")):
        level = msg.split("!set level ",1)[1]
        set_entity_level(level,env.dict_characters[message.author.id])
    elif(msg.startswith("!set current_xp ")):
        current_xp = msg.split("!set current_xp ",1)[1]
        set_entity_current_xp(current_xp,env.dict_characters[message.author.id])
    elif(msg.startswith("!set xp_to_next_level ")):
        xp_to_next_level = msg.split("!set xp_to_next_level ",1)[1]
        set_entity_xp_to_next_level(xp_to_next_level,env.dict_characters[message.author.id])
    elif(msg.startswith("!set state_duration ")):
        state_duration = msg.split("!set state_duration ",1)[1]
        set_entity_state_duration(state_duration,env.dict_characters[message.author.id])
    elif(msg.startswith("!set user_id ")):
        user_id = msg.split("!user_id xp_to_next_level ",1)[1]
        set_entity_user_id(user_id,env.dict_characters[message.author.id])    # Create and link spell to character
    elif(msg.startswith("!profile")):
        char = env.dict_characters[message.author.id]
        name = char.name
        level = str(char.level)
        race = char.race
        xp = str(char.current_xp)
        next_level = str(char.xp_to_next_level)
        spellnames = [spell for spell in char.spells.keys()]
        profile_pic = char.picture_url
        hp = str(char.current_hp)
        max_hp = str(char.max_hp)
        
        embed=discord.Embed(color=0xFF5733)
        embed.set_author(name=name)
        if(profile_pic!=""):
            embed.set_thumbnail(url=profile_pic)
        field_value = "Name : "+name+"\nRace: "+race+"\nLevel : "+level+"\nHitPoints : "+hp+"/"+max_hp+"\nXP : "+xp+"/"+next_level+"\nSpells : "
        for spellname in spellnames:
            field_value = field_value + "\n* "+spellname+"."
        embed.add_field(name="Profile",value=field_value)
        embed.add_field(name="Description",value=char.description,inline=False)

        await game_log_channel.send(embed=embed)
    elif(msg.startswith("!spellbook ")):
        spellname = msg.split("!spellbook ",1)[1]
        embed_out = get_spell_embed(spellname)
        await game_log_channel.send(embed=embed_out)
    elif(msg.startswith("!spells")):
        spells = env.dict_spells
        for spellname in spells.keys():
            embed = get_spell_embed(spellname)
            await game_log_channel.send(embed=embed)
    elif(msg.startswith("!monsters")):
        monsters = env.dict_monsters
        for monster_name in monsters.keys():
            embed = get_monster_profile_embed(monster_name)
            await game_log_channel.send(embed=embed)
    
    elif(msg.startswith("!save")):
        env.save_env()
        await game_log_channel.send("Saved the advancement successfully !")
    # Create monster parameters
    elif(msg.startswith("!create monster ")):
        content = msg.split("!create monster ",1)[1]
        content = content.split(" ")
        race = content[0]
        name = content[1]
        new_monster = Monster(name=name,race=race)
        env.create_monster(new_monster)
    # Set monster parameters
    elif(msg.startswith("!monster ")):
        content = msg.split("!monster ",1)[1]
        content = content.split(" ")
        monster_name = content[0]
        msg = " ".join(content[1:])

        if(msg.startswith("set race ")):
            race = msg.split("set race ",1)[1]
            set_entity_race(race,env.dict_monsters[monster_name])
        elif(msg.startswith("set class ")):
            monster_class = msg.split("set class ",1)[1]
            env.dict_monsters[monster_name].monster_class=monster_class
        elif(msg.startswith("set name ")):
            custom_name = msg.split("set name ",1)[1]
            monster = env.dict_monsters[monster_name]
            env.dict_monsters.pop(monster_name)
            monster.name = custom_name
            env.dict_monsters[custom_name] = monster
        elif(msg.startswith("set current_hp ")):
            current_hp = msg.split("set current_hp ",1)[1]
            set_entity_current_hp(current_hp,env.dict_monsters[monster_name])
        elif(msg.startswith("set max_hp ")):
            max_hp = msg.split("set max_hp ",1)[1]
            set_entity_max_hp(max_hp,env.dict_monsters[monster_name])  
        elif(msg.startswith("set state ")):
            state = msg.split("set state ",1)[1]
            set_entity_state(state,env.dict_monsters[monster_name])
        elif(msg.startswith("set modifier ")):
            modifier = msg.split("set modifier ",1)[1]
            set_entity_modifier(modifier,env.dict_monsters[monster_name])
        elif(msg.startswith("set description ")):
            description = msg.split("set description ",1)[1]
            set_entity_description(description,env.dict_monsters[monster_name])
        elif(msg.startswith("set picture ")):
            picture_url = msg.split("set picture ",1)[1]
            set_entity_picture(picture_url,env.dict_monsters[monster_name])
        elif(msg.startswith("join battle ")):
            custom_name = msg.split("join battle ")[1]
            monster = copy.copy(env.dict_monsters[monster_name])
            monster.name = custom_name
            env.add_monster(monster)
            await game_log_channel.send("A monster just joined the battle !")
    # Lists the monsters available in the environment and their basic stats & spells
    elif(msg.startswith("!bestiary ")):
        monster_name = msg.split("!bestiary ",1)[1]
        embed_out = get_monster_profile_embed(monster_name)
        await game_log_channel.send(embed=embed_out)

    # Battle
    # PVM
    # * spellname target
    elif(msg.startswith("*")):
        content = msg.split("*",1)[1]
        content = content.split(" ")
        spellname = content[0]
        target = content[1]
        caster = env.dict_characters[message.author.id]
        print(env.dict_battle)
        target = env.dict_battle[target]
        spell = caster.spells[spellname]
        embed_out = battle_summary(caster,spellname,target)
        await game_log_channel.send(embed=embed_out)
    # & monster_name spell_name target
    elif(msg.startswith("&")):
        content = msg.split("&",1)[1]
        content = content.split(" ")
        caster = content[0]
        spellname = content[1]
        target = content[2]
        print(env.dict_battle)
        caster = env.dict_battle[caster]
        if(target in env.dict_battle.keys()):
            target = env.dict_battle[target]
        else:
            for key in env.dict_characters:
                char = env.dict_characters[key]
                if(char.name==target):
                    target = char
        
        embed_out = battle_summary(caster,spellname,target)
        await game_log_channel.send(embed=embed_out)
    # pvp spellname target
    elif(msg.startswith("pvp")):
        content = msg.split("pvp ",1)[1]
        content = content.split(" ")
        spellname = content[0]
        target = content[1]
        caster = env.dict_characters[message.author.id]
        target = env.dict_characters[target]
        msg_out = env.use_spell(caster=caster,target=target,spellname=spellname)
        await game_log_channel.send(msg_out)
        await game_log_channel.send(fight_summary(caster,target))
    elif(msg.startswith("!create spell ")):
        content = msg.split("!create spell ",1)[1]
        spellname = content.split(" ")[0]
        create_spell(spellname)
    elif(msg.startswith("!linkspell ")):
        content = msg.split("!linkspell ",1)[1]
        if(content.startswith("monster")):
            content = content.split("monster ",1)[1]
            content = content.split(" ")
            name = content[0]
            spellname = content[1]
            entity = env.dict_monsters[name]
            link_spell(entity,spellname,env.dict_spells)
        elif(content.startswith("character")):
            content = content.split("character ",1)[1]
            content = content.split(" ")
            name = content[0]
            spellname = content[1]
            for key in env.dict_characters.keys():
                if(env.dict_characters[key].name==name):
                    entity = env.dict_characters[key]
                    link_spell(entity,spellname,env.dict_spells)    
    elif(msg.startswith("!edit spell ")):
        content = msg.split("!edit spell ",1)[1]
        content = content.split(" ")
        spellname = content[0]
        msg = " ".join(content[1:])
        if(msg.startswith("set spell success ")):
            set_spell_success(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell type ")):
            set_spell_type(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell crit ")):
            set_spell_crit(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell damage ")):
            set_spell_damage(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell cooldown ")):
            set_spell_cooldown(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell effect ")):
            set_spell_effect(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell targets ")):
            set_spell_targets(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell description ")):
            set_spell_description(message,spellname,env.dict_spells)      
        elif(msg.startswith("set spell modifier ")):
            set_spell_modifier(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell crit_damage ")):
            set_spell_crit_damage(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell picture ")):
            set_spell_picture(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell heal ")):
            set_spell_heal(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell crit_effect ")):
            set_spell_crit_effect(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell crit_effect_duration ")):
            set_spell_crit_effect_duration(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell crit_heal ")):
            set_spell_crit_heal(message,spellname,env.dict_spells)
        elif(msg.startswith("set spell effect_duration ")):
            set_spell_effect_duration(message,spellname,env.dict_spells)  
    elif(msg.startswith("!remove spell ")):
        remove_spell(message,env.dict_characters[message.author.id].spells)
    elif(msg.startswith("!battle state")):
        battle = env.dict_battle
        embed = discord.Embed()
        embed.set_author(name="BattleState")
        for mobkey in battle.keys():
            mob_name = mobkey
            mob_hp = str(battle[mobkey].current_hp)
            mob_max_hp = str(battle[mobkey].max_hp)
            value = "HitPoints : "+mob_hp+"/"+mob_max_hp
            embed.add_field(name=mob_name,value=value)
        await game_log_channel.send(embed=embed)
    elif(msg.startswith("!battle clear")):
        env.dict_battle = {}
        await game_log_channel.send(f"Battle Cleared ! requested by <@{message.author.id}>")
    elif(msg.startswith("!battle perception ")):
        battle_monster_name = msg.split("!battle perception ",1)[1]
        embed = get_monster_perception_profile_embed(battle_monster_name,message.author.id)
        await game_log_channel.send(embed=embed)
    elif(msg.startswith("debug")):
#        for key in env.dict_spells.keys():
#            env.dict_spells[key].type="normal"
#        env.dict_spells["Roulette[heal]"].type = "double-edge"
#        env.dict_spells["Roulette[damage]"].type = "double-edge"

        await game_log_channel.send(f"mamak zwina <@{brahim_id}>")
    # Save the environment at the end of each message
    env.save_env()


client.run("OTk5MjY3ODg1Mjc5MTAwOTU4.GeAxaw.nLFYMVT9X-eI21UfBhuJ9LFpyrot9bLAbrj-ho")
