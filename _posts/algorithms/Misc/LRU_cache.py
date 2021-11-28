
from collections import OrderedDict

class LRUCache(OrderedDict):
    # Here once the object is created it will be of type OrderedDict.
    '''
    Algo:
    For Get:
        1. If the key not in self, then return -1.
        2. Get the keys value
        3. Move it to the last using move_to_end function of OrderedDict.
    For Put:
        1. If Key exists
            move_to_end and update
            return
        2. Add key
            check if number of key or len(self) more than capacity
             if yes, then self.popitem(Last=False)


    '''
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lru_ca p =capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1

        va l =self[key]
        self.move_to_end(key)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self:
            self[key ] =value
            self.move_to_end(key)
            return

        self[key ] =value
        if len(self) > self.lru_cap:
            self.popitem(last=False)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)