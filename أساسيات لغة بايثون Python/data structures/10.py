"""numbers =[1,2,3,4,5,6,7]
result=1
for number in numbers:
    result = number * result
    print(result)
charactar =[]
result1=0
for char in charactar:
    result1 = char + result1
    charactar.append(result1)

print(result1)
"""
"""numbers = [1,2,3,4,5,6,7,8]
seen={}
dups =[]
for number in numbers:
    if number not in seen:
        seen[number]=1
    else:
        if seen[number]==1:
            dups.append(number)
        seen[number]+=1
print(dups)"""
"""
words =['data','science' , 'machine','learning']
char_count ={ i : len(i) for i in words}
print(char_count)
"""
numbers=[1,2,3,4,5,6,7,8]
grouped_numbers =[]
size =4
for i in range (0,len(numbers),size):
    grouped_numbers.append(numbers[i:i+size])
print(grouped_numbers)

grouped_numbers =[numbers[i:i+size] for i in range(0,len(numbers),size)]

print(grouped_numbers)