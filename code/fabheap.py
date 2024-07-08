class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            self._merge_with_root_list(self.min_node, node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1
        return node

    def find_min(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                children = [x for x in self._iterate_node(z.child)]
                for x in children:
                    self._merge_with_root_list(self.min_node, x)
                    x.parent = None
            self._remove_from_root_list(z)
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.total_nodes -= 1
        return z.key if z else None

    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("new key is greater than current key")
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    def delete(self, x):
        self.decrease_key(x, float('-inf'))
        self.extract_min()

    def _merge_with_root_list(self, min_node, node):
        node.left = min_node
        node.right = min_node.right
        min_node.right = node
        node.right.left = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _iterate_node(self, node):
        if not node:
            return
        start = node
        while True:
            yield node
            node = node.right
            if node == start:
                break

    def _link(self, y, x):
        self._remove_from_root_list(y)
        y.parent = x
        if x.child is None:
            x.child = y
            y.right = y
            y.left = y
        else:
            self._merge_with_root_list(x.child, y)
        x.degree += 1
        y.mark = False

    def _consolidate(self):
        max_degree = int(self.total_nodes ** 0.5) + 1
        A = [None] * max_degree
        nodes = [x for x in self._iterate_node(self.min_node)]
        for w in nodes:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min_node = None
        for i in range(max_degree):
            if A[i] is not None:
                if self.min_node is None:
                    self.min_node = A[i]
                else:
                    self._merge_with_root_list(self.min_node, A[i])
                    if A[i].key < self.min_node.key:
                        self.min_node = A[i]

    def _cut(self, x, y):
        self._remove_from_child_list(y, x)
        y.degree -= 1
        self._merge_with_root_list(self.min_node, x)
        x.parent = None
        x.mark = False

    def _remove_from_child_list(self, parent, node):
        if parent.child == node:
            if node.right != node:
                parent.child = node.right
            else:
                parent.child = None
        node.left.right = node.right
        node.right.left = node.left

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

# Example usage
fib_heap = FibonacciHeap()
node1 = fib_heap.insert(10)
node2 = fib_heap.insert(20)
node3 = fib_heap.insert(30)
print("Minimum key:", fib_heap.find_min())  # Output: 10
print("Extracted minimum key:", fib_heap.extract_min())  # Output: 10
print("Minimum key after extraction:", fib_heap.find_min())  # Output: 20
fib_heap.decrease_key(node3, 5)
print("Minimum key after decreasing key:", fib_heap.find_min())  # Output: 5
