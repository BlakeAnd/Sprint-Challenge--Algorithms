#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
i checked the number of loops at n avlues 2,4,8 and found them to be 2,4,8
assuming this pattern holds, the run time should be o(n)

b)
the outer loop will repeat from repeat n number of times as it is a +1 increment

the inner while loop is incremented by multiplication, and scales linearly when n is doubled (n at 2,4,8 gives runs 1,2,3) this suggest a logn(n) time for that loop

combining these the runtime seems to be o(n * log(n))

c)
i evaluated this code by putting a print statement inside it and counting the number of prints to see how many times the function ran
 here is the code 

 count = 0
def bunnyEars(bunnies):
      global count
      count = count +1
      print(count)
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)


print(bunnyEars(2))
#print(bunnyEars(4)) uncomment these one at a time to see pattern
#print(bunnyEars(8))
#print(bunnyEars(16))

it appears to run about n number of times without really scaling up or down as numbers double

so complexity is o(n)

## Exercise II
begin on floor 1 (ground), throw an egg
if the egg breaks stop throwing
if the egg does not break proceed to the next floor
repeat this until an egg breaks
remember the number of the floor that the egg broke at

i believe the runtime complexity is o(n) because you will only need to ascend the the floors once until your reach floor f and stop throwing eggs
