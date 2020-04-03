from Sorting.Sorting import bubble_sort


def closestPairSum(list1,list2,x):
    list1_sorted = bubble_sort([int(item.split(' ')[1]) for item in list1])
    list2_sorted = bubble_sort([int(item.split(' ')[1]) for item in list2])
    matrix = []
    for item1 in list1_sorted:
        sublist = [item1+item2 for item2 in list2_sorted]
        matrix.append(sublist)
    max_value = matrix[0][0]
    current_topping = 0
    if max_value >= x:
        return max_value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1,-1,-1):
            if max_value <= matrix[i][j] <= x:
                max_value = matrix[i][j]
                current_topping = j

    if max_value == x:
        return max_value
    else:
        list2_sorted.pop(current_topping)
        for i in range(len(list2_sorted)-1,-1,-1):
            if max_value + list2_sorted[i] <= x:
                max_value += list2_sorted[i]
        return max_value


flavors = ['githeri 900','chapo 500', 'mandazi 700']
toppings = ['sukuma 350','kienjenji 400','meat 300']

print(closestPairSum(flavors,toppings,1500))