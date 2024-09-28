

from typing import Any, List, Tuple

class Profile:
    def __init__(self, ProfileID):
        self.ProfileID = ProfileID
        #API Call for the rest of the relavent information
        self.FriendIDArr = []
        self.myEventIDArr = []

class Event:
    def __init__(self, EventID, KAttendeeArr):
        self.EventID = EventID
        self.KAttendeeArr = KAttendeeArr
        #API Call for the rest of the relavent information
        self.UKAttendeeArr = []

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class CustomHashSet:
    def __init__(self):
        self.set = set()
        self.heads = {}

    def add(self, key, data):
        if key not in self.set:
            # New unique key
            self.set.add(key)
            self.heads[key] = Node(key, data)
            return 1
        else:
            # Duplicate key, add to linked list
            new_node = Node(key, data)
            new_node.next = self.heads[key]
            self.heads[key] = new_node
            return self._count_nodes(key)
    
    def get_keys(self):
        return self.set
    
    def get_data(self, key):
        if key not in self.set:
            return None
        return [node.data for node in self._iterate_nodes(key)]
    
    def get_count(self, key):
        if key not in self.set:
            return 0
        return self._count_nodes(key)
    
    def remove(self, key):
        if key not in self.set:
            return 0

        node = self.heads[key]
        if node.next is None:
            # Only one node, remove from set and heads
            self.set.remove(key)
            del self.heads[key]
            return 0
        else:
            # Remove the head, keep the rest of the list
            self.heads[key] = node.next
            return self._count_nodes(key)


    def _count_nodes(self, key):
        return sum(1 for _ in self._iterate_nodes(key))

    def _iterate_nodes(self, key):
        node = self.heads[key]
        while node:
            yield node
            node = node.next

    def __contains__(self, key):
        return key in self.set

    def __len__(self):
        return len(self.set)

