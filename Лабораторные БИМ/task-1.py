numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
no_number_index = 4
numbers[no_number_index]=0

average = sum(numbers)/len(numbers)
numbers[no_number_index] = average

print ("Измененный список:", numbers)

