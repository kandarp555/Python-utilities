#Grade Generator
name = str(input("Enter the student name:\n"))
sub1 = int(input("\nEnter the marks of sub1:\n"))
sub2 = int(input("Enter the marks of sub2:\n"))
sub3 = int(input("Enter the marks of sub3:\n"))
sub4 = int(input("Enter the marks of sub4:\n"))
percentage = int((sub1+sub2+sub3+sub4)/4)

while (sub1<0 or sub1>100) or (sub2<0 or sub2>100) or (sub3<0 or sub3>100) or (sub4<0 or sub4>100) :
    sub1 = int(input("Enter the marks of sub1:\n"))
    sub2 = int(input("Enter the marks of sub2:\n"))
    sub3 = int(input("Enter the marks of sub3:\n"))
    sub4 = int(input("Enter the marks of sub4:\n"))
    percentage = int((sub1+sub2+sub3+sub4)/4)

print("Hello,", name ,"you got", percentage,"%")
if percentage<33:
    print("You have achieved grade E")
elif percentage>=33 and percentage<50:
    print("You have achieved grade D")
elif percentage>= 50 and percentage<75:
    print("You have achieved grade C")
elif percentage>= 75 and percentage<90:
    print("You have achieved grade B")
elif percentage>=90:
    print("You have achieved grade A")

