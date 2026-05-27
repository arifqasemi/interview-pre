########. List #######
  ### list creation ###
# new_list = list(range(5))
  
# print(new_list)

 ### list access ###

# print(new_list[0])
# print(new_list[-1])
# print(new_list[1:3])
# print(new_list[::-1])

 ### list add/remove ###


# new_list.append(5)
# new_list.pop(0)
# new_list.insert(0,0)
# new_list.remove(2)
# new_list.reverse()
# print(new_list)

  ### list slicing ###
# print(new_list)
# print(new_list[::2])
# print(new_list[1::2])
# print(new_list[:3])
# print(new_list[-1:])
# print(new_list[-1])


  ### list comperhension ###

# doubled_list = [i*2 for i in new_list]
# # print(doubled_list)

# filtered_list = [i for i in new_list if i >=3]
# print(filtered_list)

  ### Dictionaries (Hash Maps) ###

d = dict()
d['3'] = 3
d['d'] = 5
# print(d)
# d.pop('d')
# print(d)

  ### dict iterate ###

# for i in d:
#     print(d[i])

# for key,value in d.items():
#     pass

# for value in d.values():
#     print(value)

  ### Dict operation ###

# print(d.values())
# print(d.keys())
# print(d.items())

 ### Dict Comprehension ###

# d_comp = {key:value*2 for key,value in d.items()}
# print(sorted(d_comp.items(),reverse=True))

  ### useful patterns ###

# from collections import defaultdict

# new_d = defaultdict(int)
# new_d['counter'] +=1
# new_d['counter'] +=3
# print(new_d)

# from collections import defaultdict,Counter
# words = ['the', 'quick', 'brown', 'fox', 'the', 'quick', 'brown', 'fox', 'the']

# # Solution with defaultdict
# word_freq = defaultdict(int)

# for word in words:
#     word_freq[word] += 1  # Simple!

# word_freq_counter = Counter(words)

# print(word_freq)
# print(word_freq_counter.most_common(2))
# # Problem: Group students by their major
# students = [
#     ('Alice', 'Computer Science'),
#     ('Bob', 'Mathematics'),
#     ('Charlie', 'Computer Science'),
#     ('David', 'Physics'),
#     ('Eve', 'Mathematics'),
# ]

# # Solution with defaultdict(list)
# students_by_major = defaultdict(list)

# for name, major in students:
#     students_by_major[major].append(name)

# print(students_by_major)

# 4. Arithmetic operations (unique to Counter!)
# counts1 = Counter(['a', 'b', 'a'])  # Counter({'a': 2, 'b': 1})
# counts2 = Counter(['a', 'c', 'a'])  # Counter({'a': 2, 'c': 1})

# counts1 + counts2  # Counter({'a': 4, 'b': 1, 'c': 1}) - Add counts
# counts1 - counts2  # Counter({'b': 1}) - Subtract counts
# counts1 & counts2  # Counter({'a': 2}) - Intersection (minimum)
# counts1 | counts2  # Counter({'a': 2, 'b': 1, 'c': 1})

# document = "the quick brown fox jumps over the lazy dog the quick brown"
# converted_to_list = document.split()
# converted_back_to_string = ''.join(converted_to_list)
# print(converted_back_to_string)
# print(converted_to_list)

####. Character Frequency in String ###
# from collections import Counter

# word1 = "listen"
# word2 = "silent"

# if Counter(word1) == Counter(word2):
#     print('they are anagrams')


# current_inventory = Counter({'apples': 50, 'bananas': 5, 'oranges': 30})
# new_stock = Counter({'apples': 20, 'bananas': 100, 'oranges': -25})

# new = current_inventory.update(new_stock)
# print(current_inventory)

##Use defaultdict when:
#✅ You're building a dictionary while iterating
#✅ You want to avoid checking if key exists
#✅ You need grouped/related data by key


   ### Sets ###

# new_set = set()
# new_set.add(2)
# new_set.add(2)
# new_set.add(3)
# # print(new_set)

# duplicates = [1, 2, 2, 3, 3, 3]
# removed_dups = set(duplicates)
# print(removed_dups)


  ### String ###

  ## basic operation

# new_string = "hello word"
# # print(new_string[0])
# # print(new_string[::-1])
# # print(new_string[-1])

# new_string.split()           # Split by whitespace: ['hello', 'world']
# new_string.split(',')        # Split by comma
# ''.join(['a', 'b']) # Join list: 'ab'
# new_string.replace('l', 'x') # Replace: 'hexxo worxd'
# new_string.strip()           # Remove whitespace
# new_string.lower()           # Lowercase
# new_string.upper()           # Uppercase
# new_string.startswith('he')  # True
# new_string.endswith('ld')    # True
# new_string.find('o')         # Index of 'o': 4
# new_string.count('l')        # Count occurrences: 3
