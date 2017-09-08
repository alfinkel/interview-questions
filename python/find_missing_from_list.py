#! /usr/bin/env python

import sys
import time

class MissingElementLocator(object):
    def __init__(self, input_list):
        """
        Constructs the object that performs the find operations.
        """
        self.input_list = input_list
        self.input_size = len(self.input_list)
        full_size = self.input_list[-1] - self.input_list[0] + 1
        self.output_size = full_size - self.input_size

    def find_missing_order_n(self):
        """
        Handles locating the missing entries from the list with O(n) efficiency.
        """
        previous_element = self.input_list[0]
        for element in self.input_list:
            difference = element - previous_element
            if difference > 1:
                start = previous_element + 1
                end = previous_element + difference
                for found in xrange(start, end):
                    print found
            previous_element = element

    def find_missing_divide_conquer(self):
        """
        Serves as the public interface to the private method that handles
        locating the missing entries from the list by the divide and conquer
        approach.
        """
        self._find_missing_divide_conquer(self.input_list)

    def _find_missing_divide_conquer(self, input_list):
        """
        Performs all of the work to locate missing entries from the list by
        recursively and selectively processing portions of the list.
        """
        # Calculate the difference between the last and first entries in the
        # list and along with the list size use those values to dictate the
        # selective recursion.
        difference = input_list[-1] - input_list[0]
        size = len(input_list)
        if size == 2 and difference > 1:
            start = input_list[0] + 1
            end = input_list[-1]
            for found in xrange(start, end):
                print found
        elif size <= difference:
            # Ensure that the last element of the first 1/2 of the input list
            # is the first element of the second 1/2 of the list.
            # Note:  Integer division performs a floor operation on the result.
            self._find_missing_divide_conquer(input_list[:size / 2 + 1])
            self._find_missing_divide_conquer(input_list[size / 2:])

def main():
    # An anonymous function to calculate the time in milliseconds
    time_in_ms = lambda: int(round(time.clock() * 1000))

    # Standup a MissingElementLocator object and read in a list from STDIN
    locator = MissingElementLocator([int(line) for line in sys.stdin])

    print "O(n)"
    order_n_start = time_in_ms()
    locator.find_missing_order_n()
    order_n_runtime = time_in_ms() - order_n_start
    print '--------------'
    print 'n = {0}'.format(locator.input_size)
    print 'm = {0}'.format(locator.output_size)
    print 'runtime = {0}ms\n'.format(order_n_runtime)

    print "Divide and conquer"
    div_conq_start = time_in_ms()
    locator.find_missing_divide_conquer()
    div_conq_runtime = time_in_ms() - div_conq_start
    print '--------------'
    print 'n = {0}'.format(locator.input_size)
    print 'm = {0}'.format(locator.output_size)
    print 'runtime = {0}ms\n'.format(div_conq_runtime)

if __name__ == '__main__':
    main()
