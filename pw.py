import time

def getList(fileName):
   infile = open(fileName,"r")
   ret = []
   for line in infile:
      ret.append(line[:-1])
   return ret
   
def checkPermutations(pw,str):
   takeAwayPerms = str.replace("@","a").replace("$","s").replace("1","l").replace("1","i").replace("0","o").replace("8","o").replace("3","e").replace("4","a").replace("!","l")
   noNum = ''.join([i for i in str if not i.isdigit()])
   noNumPerms  = ''.join([i for i in takeAwayPerms if not i.isdigit()])
   if(str[-4:].isdigit()):
      print("Adding 4 numbers (esp. years) is a very common pw permuation please be aware of this")
      return True
   if(str[-2:].isdigit()):
      print("Adding 2 numbers is a very common pw permuation please be aware of this")
      return True
   if(str.lower() == pw.lower()):
      print("Password crackers can take into accounnt weird capitalizations")
      return True
   if(noNum.lower() in str or noNum.lower() in str or noNumPerms.lower() in str or noNumPerms.lower() in str):
      print("Password crackers are getting better at taking numbers into account everyday")
      return True

def recs():
   print("1) Use a password manager\n2) Prioritize length of pw over ranndom characters (so a long easy to remember PW is better then a short weird one like 1E=(_)!#)")

def main():
   str = raw_input("What is your password: ")
   if(str == 'password'):
     print("Why are you like this?")
     recs()
     exit()
   if(str == "correcthorsebatterystaple"):
     print("We get it you like XKCD. Change your PW.")
     recs()
     exit()
   passwordList = getList("rockyou.txt")
   for pw in passwordList:
      if str == pw:
         print("Your password is in the rockyou database.")
         recs()
         break
      elif checkPermutations(pw,str):
         recs()
         break
main()
