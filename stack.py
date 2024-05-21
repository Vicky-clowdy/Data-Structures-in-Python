arr=[]
print("STACK OPERATIONS")
print("1.Push\n2.Pop\n3.isempty\n4.Peek\n5.View stack\n6.Min and Max\n7.Exit")
while(1):
  ch=int(input("Enter your choice : "))
  if(ch==1):
    n=int(input("Enter how many elements to append : "))
    for i in range(1,n+1):
        a=input(f"Enter value {i} : ")
        arr.append(a)
    print(arr)
  elif(ch==2):
      try:
          if(len(arr)>0):
            arr.pop()
            print(arr)
          else:
              raise IndexError
      except IndexError:
          print("The stack is empty so it cannot pop")
  elif(ch==3):
       print(len(arr)==0)
  elif(ch==4):
    print("The top value is : ",arr[-1])
  elif(ch==5):
    print(arr)
  elif(ch==6):
    max=arr[0]
    min=arr[0]
    for i in arr:
      if i>max:
        max=i
      elif i<min:
        min=i
    print("The maximum value is : " , max)
    print("The minimum value is : " , min)
  elif(ch==7):
    print("Exiting")
    break
  else:
    print("Invalid choice")