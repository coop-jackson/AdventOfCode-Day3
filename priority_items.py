#part 1 Day 3
priorities_sum  = 0
#splits rucksack into two compartments
compartments = [''] * 2

with open('rucksack_items.txt') as file:
    #reads in each line of data as rucksack
    for rucksack in file.readlines():
        rucksack = rucksack.strip()
        num_items = len(rucksack)
        #splits the rucksack items.
        compartments[0], compartments[1] = rucksack[0:num_items//2], rucksack[num_items//2:num_items]
        #nested loop to find matching character
        for items_one in compartments[0]:
            found_identical = False

            for items_two in compartments[1]:
                if items_one == items_two:  
                    found_identical = True
                    #changes value to priority value and adds it to sum
                    if ord(items_one) > 90:
                        priorities_sum += ord(items_one) - 96
                    else:
                        priorities_sum += ord(items_one) - 38
                    break
            if found_identical:
                break

file.close()
print(f'sum of priorities of item types: {priorities_sum}')  

#part 2 day 3
#groups of three -badge: only item carried by all three elves

#reads in data to large list rucksack.
with open('rucksack_items.txt') as file:
    rucksack = file.readlines()
file.close()


badge_priority = 0
#iterates through rucksack list index in iterations of three (group size)
for i in range(0, len(rucksack), 3):
    found_identical = False
    #assigns rucksack to group members
    elf_one = rucksack[i].strip()
    elf_two = rucksack[i + 1].strip()
    elf_three = rucksack[i + 2].strip()
    #triple nested for loop to find 'badge'
    for items_one in elf_one:

        for items_two in elf_two:

            for items_three in elf_three:

                if items_one == items_two == items_three:
                    found_identical = True
                    if ord(items_one) > 90:
                        badge_priority += ord(items_one) - 96
                    else:
                        badge_priority += ord(items_one) - 38
                    break
            if found_identical:
                break
        if found_identical:
            break
print(f'Sum of badge priorities: {badge_priority}')

