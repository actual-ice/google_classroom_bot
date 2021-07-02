# ---IMPORT MODULES---
import lol_email
from lol_email import valid_email
from lol_email import new_email
from bot_client import send_message
import time

valid_emails = {
    '"Divina Gracia Gabute (Classroom)" <no-reply+85708bec@classroom.google.com>':'ESP',
    '"Irene Joy Miranda (Classroom)" <no-reply+52a8659b@classroom.google.com> ':'Science/Homeroom',
    '"Donnabelle Banzon (Classroom)" <no-reply+7e62e0db@classroom.google.com>':'Scientific Writing',
    '"Joel Viana (Classroom)" <no-reply+3a969b59@classroom.google.com>':'MAPEH',
    '"Rolly Bitancor (Classroom)" <no-reply+025c46dc@classroom.google.com>':'MATH',
    '"Mina Lucero (Classroom)" <no-reply+b1609455@classroom.google.com>':'AP',
    '"Eden Paras (Classroom)" <no-reply+986a176c@classroom.google.com>':'AP',
    '"Jayson Zabala (Classroom)" <no-reply+2bc79fdd@classroom.google.com>':'English',
    '"Edna Macauyag (Classroom)" <no-reply+bcf4ffe5@classroom.google.com>':'ICT',
    '"Christine Joy Navidad (Classroom)" <no-reply+6403eff3@classroom.google.com>':'Filipino',
    '"Oliveth Sasha Gliponeo (Classroom)" <no-reply+e715f598@classroom.google.com>':'Research',
    '"Freezing Ice (Classroom)" <no-reply+47717a9e@classroom.google.com>':'Ice'
    }


while True:
    my_new_email = ''
    my_new_email = new_email()
    #new_email = (email message, where the email is from, link)
    if my_new_email:
        email_address = my_new_email[1]
        
        e_status = valid_email(email_address, valid_emails)
        if e_status:
            link = my_new_email[2]
            message = e_status + '\n' + '\n' + link
            send_message(message)

    #check the email after every second
    time.sleep(1)