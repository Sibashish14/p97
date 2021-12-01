chance=1;
number=39;
num=0;
while chance<=5:
    if(chance==1):
        num=input("The number is lesser than 100 and greater than 0:");
        if(num==number):
          print("You guessed it");
          break;
    elif(chance==2):
        num=input("The number is multiple of thirteen:");
        print(num);
        if(num==number):
         print("You guessed it");
         break;
    elif(chance==3):
        num=input("The number is also the multiple of a number less than 10:");
        if(num==number):
         print("You guessed it");
         break;
    elif(chance==4):
        num=input("It is less than 50:");
        if(num==number):
         print("You guessed it");
    elif(chance==5):
        num=input("Tt\'s first digit is equal to the digit common in its factors:");
        if(num==number):
             print("You guessed it");
        else:
             print("You're a fool");
    chance+=1;