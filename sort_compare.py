import random
import time

def insertion_sort(a_list):
	start_time = time.time()
	for index in range(1, len(a_list)):
		current_value = a_list[index]
		position = index
		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position = position - 1
		a_list[position] = current_value
	
	time_taken = time.time() - start_time
	return time_taken

def shell_sort(a_list):
	start_time = time.time()
	sublist_count = len(a_list) // 2
	while sublist_count > 0:
		for start_position in range(sublist_count):
			gap_insertion_sort(a_list, start_position, sublist_count)
		sublist_count = sublist_count // 2
	
	time_taken = time.time() - start_time
	return time_taken
	
	
def gap_insertion_sort(a_list, start, gap):
	for i in range(start + gap, len(a_list), gap):
		current_value = a_list[i]
		position = i
		while position >= gap and a_list[position - gap] > current_value:
			a_list[position] = a_list[position - gap]
			position = position - gap
		a_list[position] = current_value


def python_sort(a_list):
	start_time = time.time()
	a_list.sort()
	time_taken = time.time() - start_time
	return time_taken
	
	



def main():
	# Parameters used for sorting
	MAX_INTEGER = 100000
	SIZES = [500, 1000, 10000]
	NUM_LISTS = 100
	

	# Calculating average sorting time for 100 seperate lists of SIZE 500, 1000, 10000
	for SIZE in SIZES:
		print "~~~ 100 lists of SIZE = {} ~~~".format(SIZE)
		total_time = [0, 0, 0]
		for i in range(0, NUM_LISTS):
			test_list = random.sample(range(1, MAX_INTEGER), SIZE)
			
			list1 = list(test_list)
			list2 = list(test_list)
			list3 = list(test_list)
			
			total_time[0] = total_time[0] + insertion_sort(list1)
			total_time[1] = total_time[1] + shell_sort(list2)
			total_time[2] = total_time[2] + python_sort(list3)
		
		average_time = []
		for t in total_time:
			average_time.append(t / NUM_LISTS)

		print "Insertion Sort took {:10.7f} seconds to run, on average".format(average_time[0])
		print "Shell Sort took {:10.7f} seconds to run, on average".format(average_time[1])
		print "Python Sort took {:10.7f} seconds to run, on average\n".format(average_time[2])

if __name__ == "__main__":
	main()
