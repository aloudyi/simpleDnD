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