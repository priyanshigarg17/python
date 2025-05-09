#open bracket must be closed in the correct order
s="[(]"
x=[]
a=0 #indicator
for i in range(0, len(s)):
  char=s[i]
  if(char=='(' or char=="{" or char=="["):
    x.append(char)
  else:
    if((char==")" and "("==x[-1]) or (char=="]" and "["==x[-1]) or (char=="}") and "{"==x[-1]):
      a=1
    else:
      a=0
      break
if(a==1):
  print("valid")
else:
  print("invalid")



s="([]}"
x=[]
a=0 #indicator
for i in range(0, len(s)):
  char=s[i]
  if(char=='(' or char=="{" or char=="["):
    x.append(char)
  else:
    if((char==")" and "("==x[-1]) or (char=="]" and "["==x[-1]) or (char=="}") and "{"==x[-1]):
      a=1
      x.pop()
    else:
      a=0
      break
if(a==1):
  print("valid")
else:
  print("invalid")