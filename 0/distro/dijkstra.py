class Node():
    def __init__(self, value, priority, action):

        # Number of node on graph
        self.value = value

        # Priority in the search
        self.priority = priority

        # The node used to get to this node in the search
        self.action = action

class PrioQueue():
    def __init__(self):
        
        # Nodes yet to be explored
        self.frontier = set()

        # Nodes we've already looked at
        self.explored = set()

    def add_node(self, new_node):
        """
        Maybe adds a new node to the Queue
        """
        # Loop through nodes in our frontier
        for node in self.frontier:

            # If the new node is already in the frontier, replace
            # the old one if the old one is no better
            if node.value == new_node.value:
                if node.priority >= new_node.priority:
                    self.frontier.remove(node)
                    self.frontier.add(new_node)
                return
        
        # If we haven't explored it yet, add to the frontier
        if new_node.value not in self.explored:
            self.frontier.add(new_node)

    def pop_node(self):
        """
        Returns the lowest priority node from the frontier
        """
        # Returns none if we're done exploring
        if self.is_empty():
            return None

        # Finds minimum node based on priority
        min_node = min(self.frontier, key=lambda node: node.priority)

        # Remove from frontier, adds to explored
        self.frontier.remove(min_node)
        self.explored.add(min_node.value)

        # Return value
        return min_node

    def is_empty(self):
        """
        Checks if the frontier is empty
        """
        return len(self.frontier) == 0


# Our graph, where each key is a node, and the value is a list
# of nodes it could lead to in the form (value, weight)
graph = {
    1: [(5, 20), (6, 5), (7, 15), (4, 20), (2, 10)],
    2: [(4, 10), (3, 5)],
    3: [(2, 15), (4, 5)],
    4: [(5, 10)],
    5: [(6, 5)],
    6: [],
    7: [(6, 10)],
    8: [(1, 5), (7, 5)],
    9: [(8, 20), (2, 15), (10, 10)],
    10: [(2, 5), (3, 15)]
}

        
        
