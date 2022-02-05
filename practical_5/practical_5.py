def change_case(str):
    output=''
    for character in str:
        if(character.isupper()==True):
            output+=(character.lower())
        elif(character.islower()==True):
            output+=(character.upper())
        else:
            output+=character
    return output

str=input()
result=change_case(str)
print(result)