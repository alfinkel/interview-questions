class Person
  attr_accessor :name, :children

  def initialize(name=nil)
    @name = name
    @children = []
  end

  def family_size
    # Recursively count the members in a family by starting from with
    # the person and working down the family tree.
    family_count = 1
    @children.each { |child| family_count += child.family_size }

    return family_count
  end
    
  def family_size_iter_dfs
    # Use a stack to perform a depth first search traversal to count the
    # members in a family starting with the person and working down the
    # family tree.
    stack = [self]
    family_count = 0
    while !stack.empty?
      family_count += 1
      person = stack.pop()
      person.children.each { |child| stack.push(child) }
    end
    return family_count
  end
    
  def family_size_iter_bfs
    # Use a queue to perform a breadth first search traversal to count the
    # members in a family starting with the person and working down the
    # family tree.
    queue = [self]
    family_count = 0
    while !queue.empty?
        family_count += 1
        person = queue.shift
        person.children.each { |child| queue.push(child) }
    end
    return family_count
  end

end

def populate_children(parent, count=10)
  for i in 1..count
    parent.children.push(Person.new("child_#{i.to_s}"))
  end
end

finkel = Person.new("Al")
populate_children(finkel, 10)
finkel.children.each { |person| populate_children(person, 5) }
puts finkel.family_size
puts finkel.family_size_iter_dfs
puts finkel.family_size_iter_bfs
