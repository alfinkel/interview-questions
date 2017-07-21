def most_common(data)
  # Returns the top most often encountered in the data list
  tracker = {}
  top = [data[0]]
  count = 0
  data.each do |element|
    if tracker.has_key?(element)
      tracker[element] += 1
    else
      tracker[element] = 1
    end
    if tracker[element] > count
      count = tracker[element]
      top = [element]
    elsif tracker[element] == count
      top.push(element)
    end
  end
  return top
end