'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0
def count_th(word):
    global count
    # print(word[0])
    if(len(word) <= 1):
      return_num = count
      print(count, return_num)
      count = 0
      return return_num
    elif(word[0] == "t" and word[1] == "h"):
      count = count + 1
    # TBC
    return count_th(word[1:])
    

print(count_th("mathematical"))
print(count_th("thoth"))
print(count_th("recreation"))