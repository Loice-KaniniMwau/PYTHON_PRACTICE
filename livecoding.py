#
def divisible(nums):
    sum=0
    
    for num in nums:
        if(num % 2==0):
            sum+=num
        elif (num % 2 !=0):
            print(num *num)
    print(sum)
    

divisible([1,2,3,4,5,6,7,8])
#
def nums(numbers):
    sum=0
    for num in numbers:
        if(num % 2 ==0):
            sum+=num
        elif (num % 2 !=0):
           print( num * num)
    print(sum)
nums([1,2,3,4,5,6,7,8])

def mynumbers(names):
    counted={x: names.count(x) for x in names}
    return counted



print(mynumbers(names=["loice","faith","loice","faith","faith"]))





def square_numbers():
   num=range(1,30)
   for i in num:
      print(i*i)

square_numbers()

def different(a,b,c,d):
#    empty=[]
#    empty.extend([a,b,c,d])
 
#    print(empty)
  empty=[a,b,c,d]
  print(empty)

def findfactorial(n):
  
    factorial=1
   
    if n >= 1:
        for i in range (1,n):
            factorial = factorial * i
        return factorial
#finding median
#classes
class Person:
   def __init__(self,firstname,secondname,age) :
      self.firstname=firstname
      self.secondname=secondname
      self.age=age
      
   

 
person1=Person("loice","mwau",22)
print(f"hello {person1.firstname} {person1.secondname} {person1.age}")

# second largest number
def counting_appearance(names):
    empty={}
    for name in names:
        if name not in empty:
            empty[name]=1
        else:
            empty[name]+=1
    print(empty)
counting_appearance(names=[1,2,2,3,4,2,1])
# appearance of each odd number
def odd_numbers(integers):
    odd_nums={}
    for name in integers:
        if name % 2 !=0:
            if name not in odd_nums:
                odd_nums[name]=1
            else:
                odd_nums[name]+=1
    print(odd_nums)
odd_numbers(integers=[2,4,6,7,9,1,3])
# all names in upper except apple
def skip(allnames):
    for name in allnames:
        if name=="apple":
            continue
        print(name.upper())
skip(allnames=["kanini","apple","faith"])






      

      

            

