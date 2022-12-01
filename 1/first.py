with open('input.txt') as fp:
   current = 0
   elves_sum = []
   temp_value = 0
   line = fp.readline()
   while line:
        print(line)
        if line == "\n":
            elves_sum.append(temp_value)
            temp_value = 0
            print()
        else:
            temp_value += int(line)
        line = fp.readline()
            
print(max(elves_sum))
