from copy import copy

class Dungeon:
    def __init__(self, name, dict_rooms = {}, picture_url=""):
        self.name = name
        self.dict_rooms = dict_rooms
        self.picture_url = picture_url

    def add_room(self, room):
        room_added = copy(room)
        self.dict_rooms[room_added.name] = room_added

    def remove_room(self,room_name):
        self.dict_rooms.pop(room_name)