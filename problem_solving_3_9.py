def find_triplet_with_sum(arr, target_sum):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return arr[i], arr[j], arr[k]
    return None

arr = [10, 20, 30, 9]
target_sum = 59
result = find_triplet_with_sum(arr, target_sum)

if result:
    print("Triplet found:", result)
else:
    print("No triplet found with the given sum.")

    