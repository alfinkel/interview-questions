class Person(object):
    def __init__(self, name=None):
        self.name = name
        self.children = []
    
    def family_size(self):
        """
        Recursively count the members in a family by starting from with
        the person and working down the family tree.
        """
        family_count = 1
        for child in self.children:
            family_count += child.family_size()
        return family_count
    
    def family_size_iter_dfs(self):
        """
        Use a stack to perform a depth first search traversal to count the
        members in a family starting with the person and working down the
        family tree.
        """
        stack = [self]
        family_count = 0
        while stack:
            family_count += 1
            person = stack.pop()
            for child in person.children:
                stack.append(child)
        return family_count
    
    def family_size_iter_bfs(self):
        """
        Use a queue to perform a breadth first search traversal to count the
        members in a family starting with the person and working down the
        family tree.
        """
        queue = [self]
        family_count = 0
        while queue:
            family_count += 1
            person = queue.pop(0)
            for child in person.children:
                queue.append(child)
        return family_count

def populate_children(parent, count=10):
  for i in xrange(1, count+1):
    parent.children.append(Person("child_{0}".format(i)))

finkel = Person("Al")
populate_children(finkel, 10)
for person in finkel.children:
  populate_children(person, 5)
print finkel.family_size()
print finkel.family_size_iter_dfs()
print finkel.family_size_iter_bfs()