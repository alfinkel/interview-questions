class MissingElementLocator
  def initialize(input_list)
    #
    # Constructs the object that performs the find operations.
    #
    @input_list = input_list
  end

  def find_missing_order_n
    #
    # Handles locating the missing entries from the list with O(n) efficiency.
    #
    previous_element = @input_list.first
    @input_list.each do |element|
      difference = element - previous_element
      if difference > 1
        start = previous_element + 1
        finish = element - 1
        (start..finish).each { |found| puts found }
      end
      previous_element = element
    end
  end

  def find_missing_divide_conquer
    #
    # Serves as the public interface to the private method that handles
    # locating the missing entries from the list by the divide and conquer
    # approach.
    #
    _find_missing_divide_conquer(@input_list)
  end

  def _find_missing_divide_conquer(input_list)
    #
    # Performs all of the work to locate missing entries from the list by
    # recursively and selectively processing portions of the list.
    #

    # Calculate the difference between the last and first entries in the
    # list and along with the list size use those values to dictate the
    # selective recursion.
    difference = input_list.last - input_list.first
    if input_list.length == 2 and difference > 1
      start = input_list.first + 1
      finish = input_list.last - 1
      (start..finish).each { |found| puts found }
    elsif input_list.length <= difference then
      # Ensure that the last element of the first 1/2 of the input list
      # is the first element of the second 1/2 of the list.
      # Note:  Integer division performs a floor operation on the result.
      _find_missing_divide_conquer(input_list[0, input_list.length / 2 + 1])
      _find_missing_divide_conquer(input_list[input_list.length / 2, input_list.length / 2 + 1])
    end
  end

end

mel = MissingElementLocator.new([2, 3, 5, 6, 9, 11, 13])
puts "O(n)"
mel.find_missing_order_n
puts "Divide and Conquer"
mel.find_missing_divide_conquer
