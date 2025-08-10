import re


with open("baby2008.html", "r", encoding="utf-8") as file:
    html_content = file.read()

pattern = r"<tr align=\"right\"><td>\d+</td><td>(\w+)</td><td>(\w+)</td>"


matches = re.findall(pattern, html_content)


male_names = [m[0] for m in matches]
female_names = [m[1] for m in matches]


all_names = list(set(male_names + female_names))

def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

sorted_names = bubble_sort(all_names.copy())

def binary_search(names, target):
    low = 0
    high = len(names) - 1
    while low <= high:
        mid = (low + high) // 2
        if names[mid] == target:
            return mid  
        elif names[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

name_to_search = input("Enter name: ")
index = binary_search(sorted_names, name_to_search)

if index != -1:
    print(f"{name_to_search} found at index {index} in the sorted list.")
else:
    print(f"{name_to_search} not found.")
