import email
import smtplib
from email.message import EmailMessage


EMAIL="swapswapy123@gmail.com"
PASS="4851Abce" 

def send_email(email,Nischay):
   with open("static/CSS/s.css","r") as f:
      data=f.read()

   msg=EmailMessage()
   msg["Subject"]="Verifcation"
   msg["from"]=EMAIL
   msg["to"]=email
   msg.set_content(f"""

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
         
         {data}
      </style>
   </head>
   <body>
      <div class="main">
      <h2 class="main-head">AGROMATE</h2>
      <div class="content">
         <h2>Hi there, {Nischay}!</h2>
         <p>Someone (hopefully you) has signed up with this email at Agromate. If it was you thank you for registring with us. Please click the button below to verify your ownership of this email for the account.</p>
         <p>Agromate - a simple and easy platform to connect farmers and landlords with each other.</p>
         <button><a href="/">Verify Now</a></button>
         <p>You have to confirm your account before this link expires.</p>
         <P>Agromate- farming made easy.</P>
      </div>
   </div>
   </body>
   </html>
   """,subtype="html")


   with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
      
      smtp.login(EMAIL,PASS)
      smtp.send_message(msg)