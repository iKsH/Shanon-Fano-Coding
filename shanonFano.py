# Shanon Fano Coding technique in Python
# Team 4 - Ikram Shah (ECE15124) | Hemanth Kumaar (ECE15123) | Sainath (ECE15113) | Vikranth Narayan (ECE15160)
# For 'Information Theory and Coding Techniques' Term Project

import collections
message = "aaaabbbccd!!!"
code_book = {}

def create_list(message):
    # Create a list of letters with frequency
    list = dict(collections.Counter(message))
    print(list)

    # Sort the list in descending order based on the value instead of character
    list_sorted = sorted(list.iteritems(), key = lambda (k,v):(v,k),reverse=True)

    # Format the final list as - [letter,frequency,code]
    final_list = []
    for key,value in list_sorted:
        final_list.append([key,value,''])

    # Returns the final list
    return final_list

# It divides the list into 2 parts 
def divide_list(list):
    if len(list) == 2:
        return [list[0]],[list[1]]
    else:
        n = 0
        for i in list:
            n+= i[1]
        x = 0
        distance = abs(2*x - n)
        j = 0
        for i in xrange(len(list)):
            x += list[i][1]
            if distance < abs(2*x - n):
                j = i
    return list[0:j+1], list[j+1:]

# Assigns '0' to higher probability & '1' to lower probability
def label_list(list):
    l1,l2 = divide_list(list)
    for i in l1:
        i[2] += '0'
        code_book[i[0]] = i[2]
    for i in l2:
        i[2] += '1'
        code_book[i[0]] = i[2]
    print "Label Iter - ",code_book
    if len(l1)==1 and len(l2)==1:
        return
    label_list(l2)
    return code_book

# Codewords are assigned to the corresponding symbol
cb = label_list(create_list(message))
print "Final Codebook - ",cb