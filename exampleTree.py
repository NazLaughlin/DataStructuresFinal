class BST:
    class Node:
        def __init__(self, data): # On creation of new Node Object
            self.data = data
            self.left = None
            self.right = None

    def __init__(self): # On creation of new BST object
        # Set our root to None
        self.root = None

    def insert(self, data): # When trying to add data to our tree
        if self.root is None: # If we have no root...
            self.root = BST.Node(data) # Make a new node with the data and set it as our root.
        else: # Otherwise...
            # Start at the root and look for where to put it.
            self._insert(data, self.root)

    def _insert(self, data, node): # When trying to add new data to a not empty tree...
        if data < node.data: # If the data is smaller than ours...
            # The data belongs on the left side.
            if node.left is None: # If there's nothing to our left...
                # We found an empty spot
                node.left = BST.Node(data) # Make a new Node with our data and put it on our left.
            else: # Otherwise...
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data: # If the data is bigger than ours...
            # The data belongs on the right side.
            if node.right is None: # If there's nothing to our right...
                # We found an empty spot
                # Make a new node with the data and put it on our right.
                node.right = BST.Node(data)
            else: # Otherwise... 
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
        else:
            # If the data isn't greater or less than our data, it's the same
            # and we should just return to avoid duplicates.
            return

    def __contains__(self, data): # When trying to see if something is in our tree
        return self._contains(data, self.root)  # Start at the root and recursively look.

    def _contains(self, data, node): # Recursive function for searching the tree.
        if data == node.data: # If the data matches ours...
            return True # We found it, it's here.
        else: # Otherwise...
            if node.left is not None and self._contains(data, node.left):
                # If there's something to our left, search down that branch,
                # And if they find it anywhere down there, we'll pass along
                # back up that it's been found.
                return True
            elif node.right is not None and self._contains(data, node.right):
                # Same for the right.
                return True
            else: # Otherwise...
                # It's not on our left or right, so pass back up to keep searching.
                # If we get here on the root, it's not in our tree, so pass back
                # false.
                return False

    def __iter__(self): # To get each element from the tree one at a time, 
        # Like in a foreach loop.
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node): # To iterate through lowest to biggest.
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self): # Get each element from the tree largest to smallest.
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node): # Recursive function to get each element one
        # At a time largest to smallest.
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
    
    def display(self):
        for item in self:
            print("    " + item)
    
    def has(self, item):
        return item in self

def prompt(question):
    return input(question)

def promptChoice():
    choice = "a"
    while(True):
        choice = input("What will you choose?")
        if choice.isnumeric():
            if int(choice) < 1 or int(choice) > 4:
                print("Invalid choice, out of range.")
            else:
                return choice
        else:
            print("invalid choice, not a number")

def main():
    pass
    
main()