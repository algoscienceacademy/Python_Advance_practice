#check program to remove odd indexed charcters in a string
# shahrear hossain shawon (iiuc)
# 31 EEE, IIUC
#algosciencecademy
# 11/6/2024

def modify(string):
    final = ""
    for i in range(len(string)):
        if i % 2 == 0:
            final = final + string[i]
    return final
string = input("Enter string:")
print("Modified string is:")
print(modify(string))



