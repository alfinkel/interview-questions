def validate_closure(seq)
  # Check that a string sequence is valid when using {}, [], ().
  # 
  # For example:
  #   > validate_closure('al{fi[nk]el}(st{e}in)') will return true
  #   > validate_closure('()') will return true
  #   > validate_closure('al{fi[nkel}](st{e}in)') will return false
  #   > validate_closure('(') will return false
  #   > validate_closure(']') will return false

  match = {'(' => ')', '{' => '}', '[' => ']'}
  stack = []
  seq.chars.each do |character|
    if match.has_key?(character)
      stack.push(character)
    end
    if match.has_value?(character)
      if stack.empty?
        return false
      end
      last = stack.pop
      if match[last] != character
        return false
      end
    end
  end
  if !stack.empty?
    return false
  end
  return true
end

tests = ['al{fi[nk]el}(st{e}in)', '()', 'al{fi[nkel}](st{e}in)', '(', ']']

tests.each do |test|
  puts "#{test} -> #{validate_closure(test).to_s}"
end
