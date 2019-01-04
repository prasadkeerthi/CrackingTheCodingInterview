#!/usr/bin/env python
# coding: utf-8

# In[183]:


#Cracking the coding interview in python
#String and arrays


# In[192]:


#Question 1
#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures?
#Hints: #44, #7 7 7, #732 
def isUnique(string1):
    dict={}

    flag=True

    for i,c  in enumerate(string1):

        if c in dict:

            dict[c]=dict[c]+1
        else:
            dict[c]=1 
    for key,value in dict.items():

        if value>1:
            flag=False
    print(flag)


string1='qqwertyuiop'
isUnique(string1)


# In[194]:


#Question 2
#Check Permutation: Given two strings, write a method to decide if one is a permutation of the
#other.
#Hints: #7, #84, #722, #737

def isPermutation(string1,string2):

    dic={}
    if(len(string1)==len(string2)):


        for i in string1:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1

        for i in string2:
             if i in dic:
                dic[i]=dic[i]-1
             else:
                dic[i]=1
        sum=0 
        for key,value in dic.items():
            sum+=value


        if sum==0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
    
string1='qwertyuiop'
string2='rpoiuyewqt'
isPermutation(string1,string2)
    


# In[195]:


#Question 3
#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string. (Note: If implementing in Java, please use a character array so that you can
#perform this operation in place.)
#EXAMPLE
#Input: "Mr John Smith ", 13
#Output: "Mr%20John%20Smith"
#Hints: #53, # 118

def URLify(string1):
    

    for i,c in enumerate(string1):
        if string1[i]==' ':

            string1=string1[0:i]+'%20'+string1[i+1:]
    print(string1)
string1="Mr  John Smith    "
URLify(string1)


# In[198]:



#Question 4
#  Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
#A palindrome is a word or phrase that is the same forwards and backwards. A permutation  is a rearrangement of letters
#The palindrome does not need to be limited to just dictionary words. 
#EXAMPLE
#Input: Tact Coa
#Output: True (permutations: "taco cat", "atco cta", etc.)
#Hints: #106, #121, #134, #136 

def haspalindrome(string1):

    string1=string1.lower()

    dic={}
    for i in string1:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]=dic[i]+1
    even=0
    odd=0

    for key, value in dic.items():
        if value%2==0:
            even+=1
        elif value%2==1 and key!=' ' :
            odd+=1

    if(odd>1):
        print('False')
    else:
        print('True')

string1="Tacocat"

haspalindrome(string1)
        


# In[188]:


#Question 5
#One Away: There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false
#Hints:#23, #97, #130 

string1="ple"
string2='pale'

dic={}
for i in string1:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
for i in string2:
    if i in dic:
        dic[i]=dic[i]-1
    else:
        dic[i]=1
sum=0
for key,value in dic.items():
    sum=sum+value
print(sum)

if sum<=2 and sum>=-2:
    print('true')
else:
    print('false')
    

    


# In[200]:


#Question 6
#String Compression: Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
#"compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#Hints:#92, #110
def stringCompression(string1):

    result=''
    dic={}
    for i,c in enumerate(string1):

        if i!=0 and string1[i]!=string1[i-1]:
              if string1[i-1]  in dic:

                result=result+string1[i-1]+str(dic[string1[i-1]])

              dic[string1[i-1]]=0


        if string1[i] in dic:
            dic[string1[i]]=dic[string1[i]]+1

           # print(dic[c])
        else:
            dic[string1[i]]=1
    result=result+string1[-1:]+str(dic[string1[-1:]])
    #for key, value in dic.items():
       # print(key,value)
    print(result)

string1="aaaabbdfghjkbbccaa"
stringCompression(string1)
    
    
        


# In[190]:


#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
#Hints: #51, # 100 


# In[204]:


#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#column are set to 0.
#Hints:#17, #74, #702 

def ZeroMatrix(Matrix):
    row={}
    col={}
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix[0])):
            if Matrix[i][j]==0:
                row[i]=0
                col[j]=0
   
    for key,value in row.items():
        row_no=key
       
        for i in range(0,len(Matrix[0])):
            Matrix[row_no][i]=0 

    for key,value in col.items():
        col_no=key
        for i in range(0,len(Matrix)):
            Matrix[i][col_no]=0 
    return Matrix
        
        

w, h = 8, 5;
Matrix = [[1 for x in range(w)] for y in range(h)] 


Matrix[0][0]=0
Matrix[2][3]=0
        
Matrix=ZeroMatrix(Matrix)
Matrix


        


# In[ ]:





# In[ ]:





# In[ ]:




