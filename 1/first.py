with open('input.txt') as fp:
   current = 0
   elves_sum = []
   temp_value = 0
   line = fp.readline()
   while line:
        if line == "\n":
            elves_sum.append(temp_value)
            temp_value = 0
        else:
            temp_value += int(line)
        line = fp.readline()
            
first = max(elves_sum)
elves_sum.remove(max(elves_sum))
second = max(elves_sum)
elves_sum.remove(max(elves_sum))
third = max(elves_sum)

res = first + second + third
print(res)
