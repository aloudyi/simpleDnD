# How to create a spell
A spell hold the following informations :
* `name` : The name of the spell
* `success_condition` : The lowest roll value from which the actions is considered a success.
* `crit_condition` : The lowest roll value from which the actions is considered a critical success.
* `damage` : The damage dealt by the spell.
* `heal` : The HitPoints healed by the spell.
* `cooldown` : The cooldown before casting the spell again.
* `current_cooldown`: The current spell cooldown (0 can be used, >0 no).
* `effect` : The effect of the spell (more on this later.).
* `effect_duration` : The duration of the spell effect.
* `targets` : The maximum number of targets this spell can be used on.
* `description` : The description of the spell.
* `picture_url` : The url of the picture of the spell
* `type` : The type of the spell (more on this later.).
* `add_modifier` : The modifier value added to the character after the spell resolves.

What are the spell parameters `effect` and `type` ?
* The parameter `effect` & `crit_effect`can take the following values :
    * `damage`: The default effect value.
    * `buff` : A buff spell.
    * `stun` : A stun spell.
    * `heal`: A healing spell (spell that heals the `spell_target`).
    * `sustain` : A healing spell (spell that heals the `spell_caster`).  

* The parameter `type` can take the follwoing values :
    * `normal`: The default type value.
    * `double-edge` : When the spell has 2 sides (heal target if **dice_roll > success_condition** else damage target).

Now up to the interesting part.
* The following commands create a spell and links it to your character or monster :
    * Create a spell : !create spell `spell_name`
    * Set spell parameter : !edit spell `spell_name` set spell parameter `parameter_value`
    * Link a spell to a character : !linkspell character `character_name` `spell_name`
    * Link a spell to a monster : ! !linkspell monster `monster_name` `spell_name`