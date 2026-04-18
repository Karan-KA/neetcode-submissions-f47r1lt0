class ListNode:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        dummyhead = ListNode(0,0)
        dummytail = ListNode(0,0)
        self.head = dummyhead
        self.tail = dummytail
        dummyhead.next = dummytail
        dummytail.prev = dummyhead


    def get(self, key: int) -> int:
        
        node = self.cache.get(key, None)

        if node:
            value = node.val

            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node


            prev_tail = self.tail.prev
            prev_tail.next = node
            node.prev = prev_tail
            node.next = self.tail
            self.tail.prev = node

            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            node = ListNode(key, value)
            prev_tail = self.tail.prev
            prev_tail.next = node
            node.prev= prev_tail
            node.next = self.tail
            self.tail.prev = node
            
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                node = self.head.next
                new_node = node.next
                self.head.next = new_node
                new_node.prev = self.head
                self.cache.pop(node.key)

        else:
            node = self.cache[key]
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev

            prev_tail = self.tail.prev
            prev_tail.next = node
            node.prev= prev_tail
            node.next = self.tail
            self.tail.prev = node





            








        
