class Tree(object):
    x = 0
    l = None
    r = None

def solution(T):
    """
    Return the count for the maximum number of distinct
    nodes in a branch for the tree T.  Given the definition
    of tree as above.
    """
    max_distinct_values = 0
    for path in get_paths(T):
        distinct_values = len(set(path))
        if distinct_values > max_distinct_values:
            max_distinct_values = distinct_values
    return max_distinct_values

def get_paths(root):
    """
    Use stacks to track the traversal of the tree and to
    generate the list of branches from the tree (root).
    """
    # Assign the root to the top of the stack
    tree_nodes = [root]
    paths = [[root.x]]
    branches = []
    while (len(tree_nodes) > 0):
        # Pop the top of the stack
        node = tree_nodes.pop()
        path = paths.pop()
        # If you reached a leaf then add the path (branch)
        # to the branches list, otherwise add nodes to the
        # stack as appropriate
        if node.l is None and node.r is None:
            branches.append(path)
        else:
            if node.r is not None:
                tree_nodes.append(node.r)
                paths.append(path + [node.r.x])
            if node.l is not None:
                tree_nodes.append(node.l)
                paths.append(path + [node.l.x])

    return branches
