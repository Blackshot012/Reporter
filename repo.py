
from telethon import TelegramClient
from telethon import functions, types, errors
from os import system
from colorama import Fore as Coloresh
import asyncio#, logging
from requests import get
from colorama import Fore,init

banner=(
    """
__________                             __                
\______   \ ____ ______   ____________/  |_   
 |       _// __ \\____ \ /  _ \_  __ \   __\
 |    |   \  ___/|  |_> >  <_> )  | \/|  | 
 |____|_  /\___  >   __/ \____/|__|   |__| 
    
    edit=blackshot.v1
    """
    
)
        

async def main():
    api_ids=input("Send your api_id: => :)")
    api_hashs=input("Send your apihash: => :) ")
    print(Fore.MAGENTA+banner)
    global client
    api_id = api_ids
    api_hash = f"{api_hashs}"
    client = TelegramClient("data", api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
    	q = True
    	phone = input("[?] Enter  YOUR  Phone  Number => ")
    	send = await client.send_code_request(phone)
    	code = input("[?]Please Enter The Code => ")
    	
    	try:
    	    await client.sign_in(phone, code)
    	except errors.SessionPasswordNeededError:
    	    passwd = input("[?] Enter Your Account Password => ")
    	    await client.sign_in(password = passwd)
    	except:
    	    pass

    a = client.is_connected()
    if a == True:
        print ("\n[☆] SuCceSsfuLy Connected :)")
    elif a == False:
        print("\n [!!] Not Connected ! Please Check  Your Connection And Retry ♡")
    try:
    	feshar = int(input("[?] Enter Number Of Report --> "))
    except:
    	print("[!]eshtebah edad vard konid :))")
    	exit()
    if feshar == "" or feshar == " ":
    	print("[!] Eshteba zadi dash")
    	exit()
    if feshar < 5:
    	print("[!] dash fesharesh kheili kame dardesh nemiad")
    	exit()
    username = input("[?] Send Target Channel / Group UserName (Without @) => ")
    if username == "" or username == " " or " " in username:
    	print("[!] dash eshteba zadi :)")
    	exit()
    try:
    	username = username.replace('@', '')
    except:
    	pass
    r = get("https://t.me/"+username)
    if not "Preview channel" in r.text:
        if not "online" in r.text:
            print("[!] channel is invalid !")
            exit()
    message_id = input("[?] Send Target Channel / Group Post Id => ")
    try:
        rsn = int(input("[?] choose reason for report :\n1.porn\n2.spam\n3.Copyright => "))
    except:
        print("[!] dash fagat bayad addad bezani  !")
        exit()
    msg = input("[?]Enter a Message to report the channel / group => ")
    if rsn == 1:
        rsn = types.InputReportReasonPornography()
    elif rsn == 2:
        rsn = types.InputReportReasonSpam()
    elif rsn == 3:
        rsn = types.InputReportReasonCopyright()
    else:
        print("[!]dash fagat as list entekhab kon !")
        exit()
    i = 0
    print("[☆]Starting Please wait....")
    while True:
        if i == feshar:
            print("[✅] SuCcEssfulLy Finished Sending Requests Sended ")

            break
        
        a = await client(functions.messages.ReportRequest(
            peer='@'+username,
            id=[int(message_id)],
            reason=rsn,
            message = msg
        ))
        b = await client(functions.account.ReportPeerRequest(
            peer='@'+username,
            reason=rsn,
            message = msg
        ))
        if a == True:
            print("[?] SuCcEssfulLy Send Request Sended  ")
            i += 1
        if i == feshar:

            print("[✅] SuCcEssfulLy Finished Sending Requests Sended  ")

            break
        if b == True:
            print("[?] SuCcEssfulLy Send Request Sended")
            i += 1
        if i == feshar:
            print("[✅] SuCcEssfulLy Finished Sending Requests Sended   ")
            break



asyncio.run(main())

