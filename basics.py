# ####################################################################### Clears the screen #######################################################################
#import os
#os.system('cls')



# ####################################################################### Variables #######################################################################
#first_name = 'Adrian'
#print(first_name)


# ####################################################################### Intro To Data Types #######################################################################
#first_name = ("Adrian", "John", "Tina")
#print(first_name[2])

#fav_pizza = {
    #"Adrian": "Pepperoni",
    #"John": "Cheese",
    #"Tina": "Supreme"
#}
#print(fav_pizza["Tina"])



# ####################################################################### String #######################################################################
#talking = "My mom yelled \n\"CLEAN YOUR ROOM!\""
#print(talking)



# ####################################################################### String Manipulation #######################################################################
#my_string = "my name is Adrian Wnek"

#print(my_string.upper())
         #or
#I can also use .lower - makes lower letters.
#I can also use .capitalize - makes capitalized letters.
#I can also use .title - makes titled letters.
#I can also use .swapcase - makes smaller & capitalized letters.
         #or
#print(len(my_string)) - shows how many characters is in the text.
         #or
#print(my_string[0]) - I can choose one specific character with a number inside -> [1]= gives you "y" <- from the text each letter has a number if it's [0] = then you get letter "m".
#print(my_string[3:6]) - choose a range between letters for example [3:6] will read word "nam" from "name" or you can do range to whatever letter depenidng on how many chartacters has a text.
#print(my_string[3:len(my_string)]) - I can choose a range all the way to the end of the text, from 3rd character ->[3:]<- it would display "name is Adrian Wnek".
#print(my_string.split(' ')) - I can split the words between each word and it will look like a list ['my', 'name', 'is', 'Adrian', 'Wnek'].
#print(my_string.split(' ')[3]) - with ->[]<- I can choose a specific word with a number so if I choose [3] it will print "Adrian".
#or you can write ".upper" after [] for example: print(my_string.split(' ')[3].upper) = it will print "ADRIAN" in capitalized letters.

# ####################################################################### Math With Python #######################################################################

#print(2 + 3) -add- "will print 5" 
#print(10 - 3) -subtract- "will print 7"
#print(10 * 3) -multiply- "will print 30"
#print(10 / 2) -devide- "will print 5"
#print(2 ** 2) -to the power of two- "will print 4"
#print(10 % 3) -modules- "will print 1"
#print(3 + 1 * 4) -order of operation- "will print 7"
                     #or
#print((3 + 1) * 4) "will print 16"

#I can also use variables

#num_1 = 3
#num_2 = 2
#print(num_1 + num_2)  "will print 5"

#I can do it also with subtract, multipy, devide, to the power of two, modules, order of operation

# ####################################################################### Floats and Ints #######################################################################

#num_1 = 10
#num_2 = 3
#print (int(num_1 / num_2))  - "will print 3"

#num_1 = 10
#num_2 = 3
#print (round((num_1 / num_2), 2)) - with round function you can round numbers

# ####################################################################### Assignment Operators #######################################################################
# "=" is the assignment operator
#we have alo different math things

#  +=
#  -=
#  *=
#  /=
#  **=
#  %=

#num = 41

#num += 1 #you can add a number to a num that way

#print(num) #proper way to do it

#print(num + 1) #this also can add up a number

# ####################################################################### Lists #######################################################################
#my_name = "Adrian"

#first_names = ['John', "Bob", "Mary", my_name]

#print (first_names[3])



#num = [1, 2, 3, 4, 5]

#first_names = ['John', "Bob", "Mary", num]     #prints 3

#print (first_names[3][2])



#first_names = ['John', "Bob", "Mary"]

#first_names[0] = "Tina"      - we replaced John with Tina

#print(first_names[0])



#first_names = ['John', "Bob", "Mary"]

#del first_names[0] - with this function you can remove one name

#print(first_names)



#first_names = ['John', "Bob", "Mary"]

#first_names.append("Tina")   - append adds additonal name

#print(first_names)



#first_names = ['John', "Bob", "Mary"]

#first_names.append("Tina")  - finds index number, there is 4 numbers as -> 'John', "Bob", "Mary" and "Tina

#print(len(first_names))



#I can always do it easier below:
#first_names = ['John', "Bob", "Mary"]

#print(first_names[len(first_names) - 1])  - This will always give the last item by calling "len" and the subtracting one.

# ####################################################################### Tuples #######################################################################

#tuple_1 = ('John', "Bob", "Mary")
#tuple_2 = ("Tina",)

#tuple_3 = tuple_1 + tuple_2 - that way I added "Tina" to Tuple

#print(tuple_3)



#tuple_1 = ('John', "Bob", "Mary")
#tuple_2 = ("Tina",)

#tuple_3 = tuple_1[0:2] -  up to two "skips first two tuples and removes "Mary"

#print(tuple_3) 



#tuple_1 = ('John', "Bob", "Mary")
#tuple_2 = ("Tina",)

#tuple_3 = tuple_1[0:2] + tuple_2   - Added "Tina" to tuple

#print(tuple_3)

# ####################################################################### Dictionaries #######################################################################

#fav_pizza = {
#   "John": "Pepperoni",
#  "Bob": "Mashroom", 
#  "Tina": "Supreme"
#}

#optional -> del fav_pizza["John"] - deletes "John"

#optional -> fav_pizza["John"] = "Ham" - changes an item

#optional -> fav_pizza.update({"Tim": "Green Peppers"})

#print(fav_pizza["Tim"])

# ####################################################################### Comparison Operators #######################################################################
# "==" - double equal to sign and it's asking a question if does this equal that and could be TRUE or FALSE.
# "!=" - means it's true.
# ">" - greater than.
# "<" - less than.
# ">=" - greater than eual to.
# "<=" - less than equal to.

#first_name = "John"

#print (10 == 10) - it's equal

#print (9 == 10) - it's not equal

#print (9 > 10) - False! it's not greater than 10!

#print (9 < 10) - True! 9 is less than 10!

# I can use comparison operators with strings, I can use them with numbers or any data type

# ####################################################################### Conditional Statements #######################################################################
# If Else Elif


#num = 3  -Not greater

#num = 30
#if (num > 10):
    #print ("Your Number is greater than 10") - number has to be greater than 10.

#elif (num == 3):
    #print ("Youjr Number is 3!!!!!") - if "num" is 3 it will be equal "==" to 3.

#else:
    #print ("Your Number is NOT greater than 10") - any number below 10 will not be greater.

# ####################################################################### Multiple Conditional Statements #######################################################################
# Multiple Conditional Statements
# and, or
#


#num = 110
#if (num > 10) and (num < 100): - Non of them are true.
    #print ("Your Number is greater than 10 but less than 100!")    



#num = 1
#if (num > 10) or (num < 100): - it's greater than 10 but less than 100!
    #print ("Your Number is greater than 10 but less than 100!")



#num = 1
#if (num > 10) or (num == 100):
    #print ("Your Number is greater than 10 but less than 100!")
    
# ####################################################################### While Loops #######################################################################

#counter = 0
#while (counter < 10):
    #print ("The Count is: %s" % counter)
    #counter += 1



#while loop will keep looping until  "10" is no longer true, it stops on number 9 because 9 is less than 10.
#the count is nine and it drops down and it adds one nine plus one is ten, 
#then it loops back around and it says is ten less than ten, Ten is equal to Ten, so it gives False information



# ####################################################################### For Loops #######################################################################

#name = "John"

#for x in name:
    #print(x)

    #I get J o h n, so it's looping through this string and printing out every letter, every "X" that it finds.




#List
#name = ["John", "Bob", "Tina"]

#for x in name:
    #print(x)

    # "X" is each item in the list




#fav_pizza = {
    #"John": "Peperoni",
    #"Bob": "Cheese",
    #"Tina": "Supreme"
#}

#for key, value in fav_pizza.items():    - it gives items information
    #print(value)

    #or

#for x, y in fav_pizza.items():   - it gives name information
    #print(x)


# ####################################################################### Let's Build FizzBuzz! #######################################################################

#count = 0
#while (count < 100):
    #count += 1
    #if (count % 3 == 0) and (count % 5 == 0):
        #print ("%s - FIZZBUZZ!!!" % count)

    #elif (count % 3 == 0):
        #print ("%s - FIZZ!!!" % count)

    #elif (count % 5 == 0):
        #print ("%s - BUZZ!!!" % count)

    #else:
        #print (count)

# ############################################################################## Functions #################################################################################

#def namer(name):
    #print ("Hello %s" % name)

#namer("John")
# It should print out "Hello John"


#def namer(first_name, last_name):
    #print ("Hello %s" % first_name)
    #print ("Hello %s" % last_name)

#namer("Adrian", "Wnek")

# It should print out: 
# "Hello Adrian"
# "Hello Wnek"



#def mather(num1, num2):
    #print (num1 +  num2)
    
#mather(4, 5)
# It should print out 9


########################################################################## Functions Part 2 #################################################################################

#def namer(name):
    #return ("Hello %s" % name)


#my_namer = namer("John")
#for letter in my_namer:
    #print(letter)

########################################################################## Modules ################################################################################# 

#import os
#import namer_module
#os.system('cls')

#print(namer_module.namer("John")




                                                                #PART 2 to Modules is in
                                                      #----------> "namer_module.py"<---------- file.







########################################################################## Intro To Classes ##############################################################


#first_name ="John"

#print(first_name.upper())


########################################################################## Classes ##############################################################


#class Square:
    #def __init__(self, side_length):
        #self.side_length = side_length

        
    #def area(self):
        #return self.side_length * self.side_length


    #def perimeter(self):
        #return self.side_length * 4

    
    #def report(self):
        #print ("Side Length: %s" % self.side_length )
        #print ("Area: %s" % self.area())
        #print ("Perimeter: %s" % self.perimeter())


#my_square = Square(5)
#my_square.report()
