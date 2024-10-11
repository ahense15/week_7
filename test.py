newphrase = "rainstorm"
# create a new variable called shortphrase
# and assign it a value by slicing 
# the newphrase variable by removing 
# the first 3 characters 
# and the last 3 characters
# the first 3 characters are "rai"
# the last 3 characters are "orm"
# substring(str, start, length end)
shortphrase = newphrase[3:len(newphrase)-3]
# shortphrase = newphrase[4:len(newphrase)-6]  ----- college board
print(shortphrase)
# explain len(newphrase)-3 = 9 - 3 = 6
# why does it end with 6 
# because the last index is not included

