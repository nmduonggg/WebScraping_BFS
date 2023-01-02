class Node:
    '''
    Standardization by Node(move, value, link)
    '''
    def __init__(self, move, value, link):
        self.move = move
        self.value = value
        self.link = link
    def __str__(self):
        return f"({self.move}, {self.value}, {self.link})"