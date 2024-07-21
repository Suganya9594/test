total_number_of_mangoes = [3, 7, 2, 9, 1]
students = 3


# Sort the list of total_number_of_mangoes 
total_number_of_mangoes.sort()  

 #  minimum difference to infinity
mininmum_difference = float('inf') 
beginning = 0
end = students - 1

while end < len(total_number_of_mangoes):
    difference = total_number_of_mangoes[end] - total_number_of_mangoes[beginning]  # Calculate the difference
    if difference < mininmum_difference:
        mininmum_difference = difference
    beginning += 1
    end += 1

print("Minimum difference between bags given to students:", mininmum_difference)
