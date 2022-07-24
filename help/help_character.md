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

* The `state` parameter can only be one of the following :
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
