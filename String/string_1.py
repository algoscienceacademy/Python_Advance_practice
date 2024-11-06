
# check if string is a pangram or not
# shahrear hossain shawon (iiuc)
# 31 EEE, IIUC
#algosciencecademy

from string import ascii_lowercase as lower

def check(s):
    return set(lower) - set(s.lower() ) == set([])
string  = input ("Enter string:")
if (check(string) == True):
    print ("The string is a pangram")
else:
    print ("The string is not a pangram")
