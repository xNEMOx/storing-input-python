#Getting Where To Save File
where = ('/Users/neymatgasimli/Desktop/Python-BlockChain/storage.txt')

#Getting What To Write To File
login = input("Login: ")
passz = input("Password: ")

#Actually Writing It
saveFile = open(where, 'w')
saveFile.write("login: " + login + "            " +"Password: " + passz)
saveFile.close()

# python3 storing-input.py
