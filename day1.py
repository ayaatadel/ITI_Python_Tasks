# 1-Write a program that counts up the number of vowels [a, e, i, o,
# u] contained in the string.
count=0
sentence="sancbbebbIoUmAnE"
vowels="aeiouAEIOU"

for char in sentence :
    if char in vowels :
         count+=1
print("Vowels Count :",count)
print("******************************************************")
# 2-Fill an array of 5 elements from the user, Sort it in descending
# and ascending orders then display the output.

arrElements=[]
for i  in range(5):
    eleInteger=int(input("Enter Your Element :"))
    arrElements.append(eleInteger)
arrElements.sort()
print(arrElements)
print("Elements Sorted Descending :",sorted(arrElements))
print("Elements Sorted Ascending :",sorted(arrElements,reverse=True))

print("******************************************************")

# 3-Write a program that prints the number of times the string 'iti'
# occurs in anystring.

string="iti welcomed iti students this is iti smnhc iti jshjcsa iti "
print("Count of iti word is : ",string.count("iti"))

print("***************************************************************")

# 4-Write a program that remove all vowels from the input word and
# generate a brief version of it.
count=0
sentence="sancbbebbIoUmAnE"
vowels="aeiouAEIOU"
for char in sentence:
    if char in vowels:
        sentence=sentence.replace(char,"")  
print("Sentence with out Vowels :",sentence)

print("********************************************************")

# 5-Write a program that prints the locations of "i" character in any
# string you added.

sentence="dcnbhdicmmidmmcnmdisnmsi"
ch="i"
location=[]
for i in range(len(sentence)):
    if  sentence[i]==ch:
        location.append(i)

print(location)
print("*********************************************************")
    
# 6-Write a program that generate a multiplication table from 1 to the
# number passed.

num=int(input("Enter Number of tables:")) 

for i in range(1, num+1):
    for j in range(1, i+1):
      print(i*j, end="\t") 
      
    print()
print("********************************************")
    
# 7-   Write a program that build a Mario pyramid like below:
#                 *
#               * *
#             * * *  
#           * * * * 
 
 
height=int(input("Enter Number of height:")) 
 
for i in range( 1, height+1):
     print(" "*(height-i) + "*"*(i)  )
   
        
