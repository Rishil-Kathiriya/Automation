wsimport pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart as multipart
from email.mime.text import MIMEText as mtext



df=pd.read_excel("local_data/Testing.xlsx")
emails=list(df['Email'])
sub=list(df['Subject'])
body=list(df['Body'])
print(len(emails),"Emails Found..")



try:
    mail="YourEmail@gmail.com"     #your email
    password="#### #### #### ####"     #your email's app key from google account
    server=sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(mail,password)
    for mail in emails:
        from_="YourEmail@gmail.com"
        to_=mail
        msg=multipart("alternative")
        msg['Subject']="Explore Solutions for Your Business"
        msg['from']="Testing YourEmail@gmail.com"

        text = f"""
            Hi there,

            We hope you're doing well!
            Happy to share this its my first project..
            """
        
        html= """
            <!DOCTYPE html>
            <html>
            <body style="font-family:Arial,sans-serif; background-color:#f9f9f9; padding:20px;">
                <div style="background-color:#ffffff; padding:20px; border-radius:10px; max-width:600px; margin:auto;">
                    <h2 style="color:#333;">Hi there 👋</h2>
                    <p style="color:#555;">
                        We're excited to introduce tailored solutions that can help you streamline your business.
                    </p>
                    <p style="color:#555;">
                        Click below to explore more:
                    </p>
                    <a href="https://www.google.com"
                    style="display:inline-block; background-color:#007bff; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">
                        Visit Our Site
                    </a>
                    <p style="font-size:12px; color:#888; margin-top:30px;">
                        You're receiving this email because you opted in or we thought it might be relevant to you. If not, just ignore it!
                    </p>
                </div>
            </body>
            </html>
            """
        
        msg.attach(mtext(text, "plain"))
        msg.attach(mtext(html, "html"))


        server.sendmail(from_,to_,msg.as_string())
        

        print("Email Sends SuccessFully......")
    server.quit()


except Exception as e:
    print(e)

    





# try:
#     for i in range(len(emails)):
#         my_mail="YourEmail@gmail.com"     #your email
 #        password="#### #### #### ####"     #your email's app key
#         server=sm.SMTP("smtp.gmail.com",587)
#         server.starttls()
#         server.login(my_mail,password)
#         from_="YourEmail@gmail.com"
#         to_=emails[i]
#         msg=multipart("alternarive")
#         msg['Subject']=sub[i]
#         msg['from']="Testing YourEmail@gmail.com"

#         text = body[i]
#         html= """
#             <!DOCTYPE html>
#             <html>
#             <body style="font-family:Arial,sans-serif; background-color:#f9f9f9; padding:20px;">
#                 <div style="background-color:#ffffff; padding:20px; border-radius:10px; max-width:600px; margin:auto;">
#                     <h2 style="color:#333;">Hi there 👋</h2>
#                     <p style="color:#555;">
#                         We're excited to introduce tailored solutions that can help you streamline your business.
#                     </p>
#                     <p style="color:#555;">
#                         Click below to explore more:
#                     </p>
#                     <a href="https://www.google.com"
#                     style="display:inline-block; background-color:#007bff; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">
#                         Visit Our Site
#                     </a>
#                     <p style="font-size:12px; color:#888; margin-top:30px;">
#                         You're receiving this email because you opted in or we thought it might be relevant to you. If not, just ignore it!
#                     </p>
#                 </div>
#             </body>
#             </html>
#             """
        
#         msg.attach(mtext(text, "plain"))
#         # msg.attach(mtext(html, "html"))


#         server.sendmail(from_,to_,msg.as_string())
        

#         server.quit()
#         print("Email Sends SuccessFully......")


# except Exception as e:
#     print(e)
