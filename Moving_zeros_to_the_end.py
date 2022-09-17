# Kyu 5
def move_zeros(array):
	new_array = [x for x in array if x != 0]
	zero_count = array.count(0)
	while zero_count > 0:
		new_array.append(0)
		zero_count -= 1
	return new_array


"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
