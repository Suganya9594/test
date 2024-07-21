numbers = [2, 3, 5, 3, 7, 2, 5]
no_repeat = None

count_dictionary = {}

for num in numbers:
    if num in count_dictionary:
        count_dictionary[num] += 1
    else:
        count_dictionary[num] = 1

for num in numbers:
    if count_dictionary[num] == 1:
        no_repeat = num
        break

if no_repeat is not None:
    print("First non-repeating element:", no_repeat)
else:
    print("No non-repeating element found in the list.")
