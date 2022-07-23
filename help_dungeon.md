# How to create a Dungeon
A dungeon contains the following informations :
* `name` : The name of the dungeon.
* `dict_rooms` : A collection of the rooms contained in the dungeon.
* `picture_url` : The picture of the dungeon.

A room contains the following informations :
* `name` : The name of the room.
* `dict_monsters` : The collection of the monsters contained in the room.
* `picture_url` : The picture of the room.

* You can create a dungeon and edit it's rooms and monsters by using the following commands :
    * Create a dungeon : !create dungeon `dungeon_name`
    * Add a room to the dungeon : !dungeon `dungeon_name` set room name `room_name`
    * Add/Remove monsters to a room in a dungeon : !dungeon `dungeon_name` set room monsters add/remove `room_name` `monster_name` `enemy_name` 
    * Load a dungeon (make it the current dungeon) : !load dungeon `dungeon_name`
    * Load a room from the current dungeon (load monsters from the room into the battle field (stackable)) : !load room `room_name`