class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind): # Wrong
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind-left_size-1) # Adjust index
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key): # Correct
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''


    def insert(self, key): # Too slow
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1 # Adjust size of node
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1 # Adjust size of node
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Your code goes here
        if child_side == "R":
            temp1 = self.right
            if direction == "L":
                self.right = self.right.right
                temp2 = self.right.left
                self.right.left = temp1
                self.right.left.right = temp2
                self.right.left.size -= self.right.size
                if self.right.left.right is not None: self.right.left.size += self.right.left.right.size
                self.right.size += 1
                if temp1.left is not None: self.right.size += temp1.left.size
            elif direction == "R":
                self.right = self.right.left
                temp2 = self.right.right
                self.right.right = temp1
                self.right.right.left = temp2
                self.right.right.size -= self.right.size
                if self.right.right.left is not None: self.right.right.size += self.right.right.left.size
                self.right.size += 1
                if temp1.right is not None: self.right.size += temp1.right.size
        elif child_side == "L":
            temp1 = self.left
            if direction == "L":
                self.left = self.left.right
                temp2 = self.left.left
                self.left.left = temp1
                self.left.left.right = temp2
                self.left.left.size -= self.left.size
                if self.left.left.right is not None: self.left.left.size += self.left.left.right.size
                self.left.size += 1
                if temp1.left is not None: self.left.size += temp1.left.size
            elif direction == "R":
                self.left = self.left.left
                temp2 = self.left.right
                self.left.right = temp1
                self.left.right.left = temp2
                self.left.right.size -= self.left.size
                if self.left.right.left is not None: self.left.right.size += self.left.right.left.size
                self.left.size += 1
                if temp1.right is not None: self.left.size += temp1.right.size

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self
