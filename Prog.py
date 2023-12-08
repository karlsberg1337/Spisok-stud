f = open('12.txt', 'r', encoding="utf-8")

students = []

for student_str in f:
	s = student_str.split(";")
	students.append({'id': int(s[0]), 'name': s[1], 'pol': s[2], 'var': int(s[3])})

f.close

def bubble_sort(dictionary, key, reverse):
    n = len(dictionary)
    for i in range(n-1):
        for j in range(n-i-1):
            if reverse:
                if dictionary[j][key] < dictionary[j+1][key]:
                    dictionary[j], dictionary[j+1] = dictionary[j+1], dictionary[j]
            else:
                if dictionary[j][key] > dictionary[j+1][key]:
                    dictionary[j], dictionary[j+1] = dictionary[j+1], dictionary[j]
    return dictionary


students = bubble_sort(students, 'name', True)

for student in students:
	print(student)


def bubble_sort(nums):  
 
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
 
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
 
                swapped = True
