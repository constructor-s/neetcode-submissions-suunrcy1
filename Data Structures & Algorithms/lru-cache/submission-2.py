class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = {"prev": None, "next": None} # dummy
        self.tail = {"prev": None, "next": None} # dummy
        self.head["next"] = self.tail
        self.tail["prev"] = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            if len(self.d) >= 2:
                node = self.d[key]

                # Remove the node
                prev_ = node["prev"]
                next_ = node["next"]
                prev_["next"] = next_
                next_["prev"] = prev_

                # Insert the node between the dummy head and the first node
                prev_ = self.head
                next_ = self.head["next"]
                prev_["next"] = node
                node["prev"] = prev_
                node["next"] = next_
                next_["prev"] = node

            return self.d[key]["value"]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node["value"] = value

            # Take the node out
            prev_ = node["prev"]
            next_ = node["next"]
            prev_["next"] = next_
            next_["prev"] = prev_
            
        else:
            node = {"key": key, "value": value, "prev": None, "next": None}

            if len(self.d) == self.capacity:
                # Remove the tail node
                n = self.tail["prev"]
                prev_ = n["prev"]
                next_ = self.tail
                prev_["next"] = next_
                next_["prev"] = prev_
                del self.d[n["key"]]

        self.d[key] = node
        # Insert the node between the dummy head and the first node
        prev_ = self.head
        next_ = self.head["next"]
        prev_["next"] = node
        node["prev"] = prev_
        node["next"] = next_
        next_["prev"] = node

