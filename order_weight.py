def order_weight(strng):
    # for input string with numbers return sorted string with numbers based 
    # on the sum of the digits

    # strip the string of trailing spaces and separate numbers
    nums = strng.strip(' ').split(' ')
    strng_out = []
    sum_list = []
    for i in nums:
        # sum each number character values
        sum_i = sum(map(int,list(i)))
        
        if strng_out == []:
            strng_out.append(i)
            sum_list.append(sum_i)
        else:
            # for each number, check where it is in the sorted list
            # starting from the biggest numbers 
            for j in range(len(strng_out)-1,-1,-1):

                # if the sum of digits is greater, just append
                if sum_i > sum_list[j]:
                    where_to_insert = j+1
                    break
                
                # if the sum is lower check if its lower than the next one
                elif sum_i < sum_list[j]:
                    where_to_insert = j
                    
                # if the sum is equal, sort by order
                elif sum_i == sum_list[j]:
                    unsorted = [strng_out[j],i]
                    to_sort = [strng_out[j],i]
                    to_sort.sort()
                    if unsorted == to_sort:
                        where_to_insert = j+1
                        break
                    else:
                        where_to_insert = j
                
            # insert to appropriate place
            strng_out.insert(where_to_insert,i)
            sum_list.insert(where_to_insert,sum_i)
    # return string                               
    return ' '.join(strng_out)

print(order_weight("56 65 74 100 99 68 86 180 90   "))
print(order_weight('2000 103 123 4444 99'))
print(order_weight(''))


# other solutions
##
# def order_weight(_str):
#     return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


##
# def sum_string(s):
#     sum = 0
#     for digit in s:
#         sum += int(digit)
#     return sum

# def order_weight(strng):
#     # your code
#     initial_list = sorted(strng.split())
#     result = " ".join(sorted(initial_list, key=sum_string))
    
#     return result