#creat a dict
my_dict = {
"Itachi" : "I'll protect village", 
"Naruto" : "I'll be Hokage", 
"Shikamaru" : "What a drag!", 
"Pain" : "I want you to feel pain", 
"Hinata Hyuga" : "Byakugan!"
}

write_ninja = input("Write your favrite ninja : ").title()
ninja_quote = my_dict.get(write_ninja)

if ninja_quote:
    print(ninja_quote)
else:
    print("Try again !")   