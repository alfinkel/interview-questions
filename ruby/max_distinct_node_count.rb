require 'set'
class Tree
  attr_accessor :x, :l, :r

  def initialize
    @x = 0
    @l = nil
    @r = nil
  end

end

def solution(T)
  # Return the count for the maximum number of distinct
  # nodes in a branch for the tree T.  Given the definition
  # of tree as above.

  max_distinct_values = 0
  get_paths(T).each do |path|
    distinct_values = path.to_set.count
    if distinct_values > max_distinct_values
      max_distinct_values = distinct_values
    end
  end
  return max_distinct_values
end

def get_paths(root):
  # Use stacks to track the traversal of the tree and to
  # generate the list of branches from the tree (root).

  # Assign the root to the top of the stack
  tree_nodes = [root]
  paths = [[root.x]]
  branches = []
  while !tree_nodes.empty?
    # Pop the top of the stack
    node = tree_nodes.pop()
    path = paths.pop()
    # If you reached a leaf then add the path (branch)
    # to the branches list, otherwise add nodes to the
    # stack as appropriate
    if node.l.nil? and node.r.nil?
      branches.push(path)
    else
      if !node.r.nil?
        tree_nodes.push(node.r)
        paths.push(path + [node.r.x])
      end
      if node.l.nil?
        tree_nodes.push(node.l)
        paths.append(path + [node.l.x])
      end
    end
  end

  return branches
end