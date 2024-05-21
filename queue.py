arr=[]
print("QUEUE OPERATIONS")
print("1.Enqueue\n2.Dequeue\n3.isempty\n4.Peek\n5.View Queue\n6.Size\n7.Exit")
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
            arr.pop(0)
            print(arr)
          else:
              raise IndexError
      except IndexError:
          print("The queue is empty so it cannot pop")
  elif(ch==3):
       print(len(arr)==0)
  elif(ch==4):
    print("First value is : ",arr[0])
  elif(ch==5):
    print(arr)
  elif(ch==6):
    print("Size : ",len(arr))
  elif(ch==7):
    print("Exiting")
    break
  else:
    print("Invalid choice")