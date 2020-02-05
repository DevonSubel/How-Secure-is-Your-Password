def getList(fileName):
   infile = open(fileName,"r")
   ret = []
   for line in infile:
      ret.append(line[:-1])
   return ret
   
def commonWordPermsNumCheck(str):
   if(str[-4:].isdigit()):
       return str[:-4].replace("@","a").replace("$","s").replace("1","l").replace("1","i").replace("0","o").replace("8","o").replace("3","e").replace("4","a").replace("!","l") + str[-4:]
   if(str[:-2].isdigit()):
       return str[:-2].replace("@","a").replace("$","s").replace("1","l").replace("1","i").replace("0","o").replace("8","o").replace("3","e").replace("4","a").replace("!","l") + str[-2:]
   return str.replace("@","a").replace("$","s").replace("1","l").replace("1","i").replace("0","o").replace("8","o").replace("3","e").replace("4","a").replace("!","l")

def checkPermutations(pw,str):
   takeAwayPermsNums = commonWordPermsNumCheck(str) #Takes care of common password permutations
   noNum = ''.join([i for i in str if not i.isdigit()]) #Takes care of simply adding numbers
   noNumPerms  = ''.join([i for i in takeAwayPermsNums if not i.isdigit()]) #Checks the previous 2
   if(pw == takeAwayPermsNums):
      print("Common permutations like replacing e's with 3's doesn't actually increase password protection. Try increasing the length of the password by using a passphrase")
      return True
   if(str[-1].isdigit()): #Checks just adding 1 to the end
      if(int(str[-1]) == 1):
         print("Don't just add a 1 to the end. Find new ways to increase the length")
         return True
   if(str[-4:].isdigit() or str[:-2].isdigit()): #Checks adding 2 or 4 numbers to the end
      if(str[:-4] == pw or str[:-2] == pw):
         print("Adding 2 or 4 numbers to the end (esp. years or a sequence of numbers) doesn't actually help improve passwords that much")
         return True
   if(noNumPerms == pw):
     print("Adding numbers (esp. a year at the end) does not increase password security all that much")
     return True
   if(noNumPerms == pw):
     print("Permutations and adding numbers are nice but can still be detected. Remmeber length is key")
     return True
   return False

def main():
   win = True
   str = raw_input("What is your password: ")
   if(str == 'password'):
     print("Why are you like this? Get a new password then try again")
     exit()
   if(str == "correcthorsebatterystaple"):
     print("We get it you like XKCD. Change your PW.")
     exit()
   passwordList = getList("rockyou.txt")
   for pw in passwordList:
      if str == pw:
         print("Your password is in the rockyou database. Please consider getting a password manager and a new password")
         win = False
         break
      elif checkPermutations(pw,str):
         win = False
         break
   if(win):
      print("You beat this cracker but there are more advanced ones (this one is more a proof-of-concept than anything else). I'd consider getting a password manager")
 
main()
