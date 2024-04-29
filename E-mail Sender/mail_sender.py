import smtplib as s

ob = s.SMTP('smtp.gmail.com' ,587)
ob.ehlo()
ob.starttls()
ob.login(username = 'kmonsterboy111@gmail.com' , password= '')

subject = input("Enter Your Subject : - ")
body =  input('Enter your Message here :- ')

message = "subject:{}/n/n".format(subject,body)

listadd = [input('Eneter Recivers mails :- ')]

ob.sendmail('kmonsterboy111@gmail.com' , listadd , message )
print('Sended Mail')
ob.quit()