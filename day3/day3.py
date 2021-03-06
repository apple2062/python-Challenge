def add_to_dict(dict,args=None,definition=None):
  if type(dict) == str:
    print(f"You need to send a dictionary. You sent: {type(dict)}")
  elif definition == None :
    print("You need to send a word and a definition")
  else:
    if args in dict:
      print(f"{args} is already on the dictionary. Won't add")
    else:
      dict[args] = definition
      print(f"{args} has been added")
  
    
def get_from_dict(dict,*args):
  if type(dict) == str:
    print(f"You need to send a dictionary. You sent: {type(dict)}") 
  elif len(args) == 0:
    print("You need to send a word to search for")
  else:
    if args[0] not in dict:
      print(f"{args[0]} was not found in this dict.")
    else:
      print(f"{args[0]}: {dict[args[0]]}")
  

def update_word(dict,word,definition=None):
  if type(dict) == str:
    print(f"You need to send a dictionary. You sent: {type(dict)}") 
  elif definition == None:
    print("You need to send a word and a definition to update.")
  else:
    if word not in dict:
      print(f"{word} is not on the dict. Can't update non-existing word")
    else:
      dict[word] = definition
      print(f"{word} has been updated to: {definition}")
  

def delete_from_dict(dict,word=None):
  if type(dict) == str:
    print(f"You need to send a dictionary. You sent: {type(dict)}")
  elif word==None:
    print("You need to specify a word to delete.")
  else:
    if word in dict:
      del dict[word]
      print(f"{word} has been deleted.")
    else:
      print(f"{word} is not in this dict. Won't delete.")

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\