# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 





letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050"))


# name = input("Enter your name: ")
# date = input("Enter selection date: ")

# letter = f"""Dear {name},
# You are selected!
# {date}"""

# print(letter)
