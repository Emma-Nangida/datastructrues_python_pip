#1. Write a Python program to get a single string from 
#two given strings, separated by a space, and swap the first 
#two characters of each string
def swap_first_two_chars(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + ' ' + new_str2

string1 = 'Emma'
string2 = 'school'
print(swap_first_two_chars(string1, string2))

#2.  Write a Python function that takes a list
# of words and returns the longest word and the length of the longest one

def longest_word(words):
    
    long_word = ""
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            long_word = word
            longest_word = len(word)
    return long_word, longest_word
names=["Winner","Hello"]
print(longest_word(names))

#3. Write a Python program that accepts a comma-separated 
#sequence of words as input and prints the distinct words in sorted 
#form (alphanumerically).
# def distinct_words(names):
#      names='joyce, banana, apple, mango, berry, kiwi'
#      words_list = names.split(',')
#      words_list = [word.strip() for word in words_list]
#      words_set = set(words_list)
#      sorted_word_list = sorted(list(words_set))

# sorted_words_list = sorted(list(words_set))


#4.. Write a Python function that takes two lists and returns 
#True if they have at least one common member.
# def check_common_member(list1,list2):
#    for items in list1:
#         if items in list2:
#            return True
#    list1 = [1, 2, 3, 4, 5]
#    list2 = [5, 6, 7, 8, 9]

# print(check_common_member())
    

#5. Write a Python program to convert a list to a list of dictionaries.
#Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", 
#"#800000", "#FFFF00"]
def list_to_dict(keys, values):
  
    return [dict(zip(keys, values[i:i+len(keys)])) for i in range(0, len(values), len(keys))]
keys = ["Black", "Red", "Maroon", "Yellow"]
values = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = list_to_dict(keys, values)

print(result)

#6. Write a Python program to check whether all dictionaries 
#in a list are empty or not
def check_empty_dictionary(lst):
    for d in lst:
        if bool(d):
            return False
    return True
my_list = [{}, {}, {}]
print(check_empty_dictionary(my_list)) 

my_list = [{}, {'a': 1}, {}]
print(check_empty_dictionary(my_list))
#7. Given a list of numbers, use list comprehension to 
#remove all odd numbers from the list:
#numbers = [3,5,45,97,32,22,10,19,39,43]
# def remove_odds(numbers):
     
#  [num for num in numbers if num % 2 == 0]
#  numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
# print(remove_odds())
        


#8. Find the common numbers in two lists (without using a tuple or set) 
#list_a = 1, 2, 3, 4, 
#list_b = 2, 3, 4, 5
list_x = [1, 2, 3, 4]
list_z = [2, 3, 4, 5]

common_numbers = []

for number in list_x:
    if number in list_z and number not in common_numbers:
        common_numbers.append(number)

print(common_numbers)

#9. Use a nested list comprehension to find all of the 
#numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# divisible_numbers = [num for num in range(1, 1001) 
#                      if any(num % digit == 0 for digit in range(2, 10))]

# print(divisible_numbers(2,10))
#10. Wrivite a Python function to remove all vowels in a string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string
my_string = "Hey Emmamai"
new_string = remove_vowels(my_string)
print(new_string) 