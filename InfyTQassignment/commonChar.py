#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    r = ""
    for i in msg1:
        if i != " ":
            if i in msg2:
                r += i
    if len(r) == 0:
        return -1
    else:
        return r

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)