# How to create your character
First thing in order to understand how a character is designed.
A character hold the following informations : 

* `name` : The name of your character.
* `race` : The race of your character.
* `current_hp` : The current HitPoints of your character.
* `max_hp` : The maximum HitPoints of your character.
* `spells` : The spells your character can use (more on this later.).
* `state` : The state of your character (more on this later).
* `state_duration` : The duration left until your state returns to normal.
* `modifier` : The current dice modifier of your character.
* `description` : The description of your character.
* `picture_url` : The url to the picture of your character.
* `user_id` : The userID linked to your character
* `level` : The current level of your character.
* `current_xp` : The current XP of your character.
* `xp_to_next_level` : The XP needed to reach the next level (not how much you have but how much u need to from Level n (0XP) to Level n+1 (0XP)).

The `state` parameter can only be one of the following :
    * `normal` : everything is good, the default state
    * `stunned` : you are stunned, and you can't play this turn
    * `unanimated` : your HitPoints reached 0.

Now moving forward to how to actually create your character.
* Run the following commands to :
    * Create your character : !create character `race` `name`
    * Set his description : !set description `description_text`
    * Set his picture : !set picture `picture_url`
    * Attack a monster (pvm) : *`spell_name` `monster_custom_name`
    * Attack a player (pvp) : pvp `spell_name` `character_target_name`
The other information is filled by default.

# How to create a spell
A spell hold the following informations :
* `name` : The name of the spell
* `success_condition` : The lowest roll value from which the actions is considered a success.
* `crit_condition` : The lowest roll value from which the actions is considered a critical success.
* `damage` : The damage dealt by the spell.
* `heal` : The HitPoints healed by the spell.
* `cooldown` : The cooldown before casting the spell again.
* `effect` : The effect of the spell (more on this later.).
* `effect_duration` : The duration of the spell effect.
* `targets` : The maximum number of targets this spell can be used on.
* `description` : The description of the spell.
* `picture_url` : The url of the picture of the spell
* `type` : The type of the spell (more on this later.).
* `crit_effect` : The effect of the spell if it crits.
* `crit_effect_duration` : The duration of the crit effect of the spell.
* `crit_damage` : The extra damage dealt by the spell if it crits.
* `crit_heal` : The extra HitPoints dealt by the spell if it crits.
* `add_modifier` : The modifier value added to the character after the spell resolves.

What are the spell parameters `effect` and `type` ?
* The parameter `effect` can take the following values :
    * `damage`: The default effect value.
    * `buff` : A buff spell.
    * `stun` : A stun spell.
    * `heal`: A healing spell.

* The parameter `type` can take the follwoing values :
    * `normal`: The default type value.
    * `double-edge` : When the spell has 2 sides (heal target if **dice_roll > success_condition** else damage target).

Now up to the interesting part.
* The following commands create a spell and links it to your character or monster :
    * Create a spell : !create spell `spell_name`
    * Set spell parameter : !edit spell `spell_name` set spell parameter `parameter_value`
    * Link a spell to a character : !linkspell character `charactername` `spell_name`
    * Link a spell to a monster : ! !linkspell monster `monstername` `spell_name`

# How to create a monster
A monster holds informations similar to the character, except a few.
* `name` : The name of the monster.
* `monster_class` : The class of the monster (same as the name, don't ask why).
* `race` : The race of the monster.
* `current_hp` : The current HitPoints of the monster.
* `max_hp` : The maximum HitPoints of the monster.
* `spells` : The spells the monster can use.
* `state` : The state of the monster (similar to the character).
* `state_duration` : The duration of the state the monster is in.
* `modifier` : The dice modifier the monster has for his next roll.
* `description` : The description of the monster.
* `picture_url` : The url of the monster's picture.

* You can create a monster and edit his parameters by using the following commands :
    * Create a monster : !create monster `monster_race` `monster_name`
    * Set a monster's prameters : !monster `monster_name` set parameter `parameter_value`
    * Make a monster join the battle : !monster `monster_name` join battle `custom_name` (mob#1 for example).
    * Make a monster attack (only if he already joined the battle) : &`monster_custom_name` `spell_name` `target`

# Miscellaneous commands
* Battle related commands :
    * See the current monsters in battle : !battle state
    * Clear the monsters in battle (GM use only) : !battle clear
    * Perception roll on monsters that are showing in battle : !battle perception `monster_name`
* General Information related commands :
    * See the character profile : !profile
    * See a specific spell informations : !spellbook `spell_name`
    * See a specific monster informations : !bestiary `monster_name`
    * See all spells available (GM use only) : !spells

And finally the most important command, to remind Brahim how beautiful his mom is : debug
