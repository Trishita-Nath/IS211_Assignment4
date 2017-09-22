import random
import time

def sequential_search(a_list, item):
	start_time = time.time()
	pos = 0
	found = False
	while pos < len(a_list) and not found:
		if a_list[pos] == item:
			found = True
		else:
			pos = pos+1
	
	time_taken = (time.time() - start_time)
	return (found, time_taken)
	



def ordered_sequential_search(a_list, item):
	start_time = time.time()			
	pos = 0
	found = False
	stop = False
	while pos < len(a_list) and not found and not stop:
		if a_list[pos] == item:
			found = True
		else:
			if a_list[pos] > item:
				stop = True
			else:
				pos = pos+1
	time_taken = (time.time() - start_time)
	return (found, time_taken)


def binary_search_iterative(a_list, item):
	start_time = time.time()			
	first = 0
	last = len(a_list) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if a_list[midpoint] == item:
			found = True
		else:
			if item < a_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	
	time_taken = (time.time() - start_time)
	
	return (found, time_taken)


def binary_search_recursive(a_list, item):
	start_time = time.time()	
	if len(a_list) == 0:
		time_taken = (time.time() - start_time)
		return (False, time_taken)
	else:
		midpoint = len(a_list) // 2
		if a_list[midpoint] == item:		
			time_taken = (time.time() - start_time)
			return (True, time_taken)
		else:
			if item < a_list[midpoint]:
				return binary_search_recursive(a_list[:midpoint], item)
			else:
				return binary_search_recursive(a_list[midpoint + 1:], item)




def main():
	# Parameters used for searching
	MAX_INTEGER = 100000
	SIZES = [500, 1000, 10000]
	NUM_LISTS = 100
	TEST_ITEM = -1

	# Calculating average searching time for 100 seperate lists of SIZE 500, 1000, 10000
	print "Searching item = {}\n".format(TEST_ITEM)
	for SIZE in SIZES:
		print "~~~ 100 lists of SIZE = {} ~~~".format(SIZE)
		total_time = [0, 0, 0, 0]
		for i in range(0, NUM_LISTS):
			test_list = random.sample(range(1, MAX_INTEGER), SIZE)
			
			#sequential
			(result, time_taken) = sequential_search(test_list, TEST_ITEM)
			total_time[0] = total_time[0] + time_taken
			
			#sort the list
			test_list.sort()
			
			#ordered_sequential
			(result, time_taken) = ordered_sequential_search(test_list, TEST_ITEM)
			total_time[1] = total_time[1] + time_taken
			
			#binary_search_interative
			(result, time_taken) = binary_search_iterative(test_list, TEST_ITEM)
			total_time[2] = total_time[2] + time_taken
			
			#binary_search_recursive
			(result, time_taken) = binary_search_recursive(test_list, TEST_ITEM)
			total_time[3] = total_time[3] + time_taken
			
		average_time = []
		for t in total_time:
			average_time.append(t / NUM_LISTS)

		print "Sequential Search took {:10.7f} seconds to run, on average".format(average_time[0])
		print "Ordered Sequential Search took {:10.7f} seconds to run, on average".format(average_time[1])
		print "Iterative Binary Search took {:10.7f} seconds to run, on average".format(average_time[2])
		print "Recursive Binary Search took {:10.7f} seconds to run, on average\n".format(average_time[3])


if __name__ == "__main__":
	main()
