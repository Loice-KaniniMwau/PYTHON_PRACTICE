def divisible_by():
    emmpty=[]
    x=range(100,200)
    for i in x:
        if (i % 7 ==0):
         emmpty.append(i)
    return emmpty
         
         
        
print(divisible_by())
#
def divisible():
   empty=[]
   x=range(100,200)
   empty=[i for i in x if i % 7 ==0 ]
   return empty
print(divisible())

def sumof_nums(a,b):
   sum=a+b
   if(sum > 10):
      print(f"{sum} is greater than 10")
   elif(sum< 10):
      print(f"{sum} is less than 10")
   elif(sum ==10):
      print(f"{sum} is equal to 10")
   else:
      print(f"sum not greater,less than or equal to 10")

sumof_nums(1,2)

#membership check
def check_num(mylist):
   if(4 in mylist):
      return True
   else:
      return False
print(check_num([1,2,3,5,6,7,8]))
#counting number of occcurrences
def counting_occurrence():
   list_days=["Monday","Tuesday","Friday","Monday"]
   count=0
   find_day="Monday"
   for i in list_days:
      if(find_day in i):
         count+=1
   print(count)
   

counting_occurrence()
#remove second last item and returns the whole list without the removed item
def remove_second():
   lista=[2,4,6,8]
   theindex=lista[-2]
   lista.remove(theindex)
   print(lista)
         
remove_second()
#removing last item
def remove_last():
   fruits=['apples',"grapes","pineapple"]
   fruits.pop()
   print(fruits)
remove_last()

#while loop to iterate and break when the item is equal to the fourth index
def breaking_loop(mylist):
   starting=0
   while starting <=len(mylist):
      starting+=1
      if(starting <=4):
         break
      print(starting)

# list comprehension
# to get numbers who average is greater than 


   
   




                        
         

      
      
   
   

   