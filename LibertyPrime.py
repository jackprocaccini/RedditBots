import praw


def online():
    online_bool = True
    print("Entering online state")
    while online_bool:
        for message in reddit.inbox.unread(limit=None):
            if message.subject == "Access Code:Pg5a3f" and ("offline" or "stop") in message.body:
                print("Online state: message received")
                message.reply("COMMAND ACCEPTED: LIBERTY PRIME - OFFLINE")
                message.mark_read()
                botport.submit(title="LIBERTY PRIME: OFFLINE",
                               selftext="SHUTDOWN PROCEDURE GIVEN BY USER: " + str(message.author))
                online_bool = False
            else:
                message.mark_read()
                message.reply("COMMAND REJECTED: PLEASE REFER TO USER MANUAL AT SUBREDDIT HQ")
    print("Going offline")
    offline()


def offline():
    offline_bool = True
    print("Entering offline state")
    while offline_bool:
        for message in reddit.inbox.unread(limit=None):
            if message.subject == "Access Code:Pg5a3f" and ("online" or "start") in message.body:
                print("Offline state: message received")
                message.reply("COMMAND ACCEPTED: LIBERTY PRIME - ONLINE")
                message.mark_read()
                botport.submit(title="LIBERTY PRIME: ONLINE",
                               selftext="START UP PROCEDURE GIVEN BY USER: " + str(message.author))
                offline_bool = False
            else:
                message.mark_read()
                message.reply("COMMAND REJECTED: LIBERTY PRIME IS OFFLINE")
    print("Going online")
    online()


reddit = praw.Reddit(client_id='zOTU2L6iq26CSw',
                     client_secret='5KZJM5WZZvZd43cFy_Eg2XTjVi8',
                     username='LIBERTY-PRIME-BOT',
                     password='fuckcommies2298',
                     user_agent='libertyprimemk1')
reddit.validate_on_submit = True

botport = reddit.subreddit('botport')

botport.submit(title="LIBERTY PRIME: ONLINE", selftext="STARTUP PROCEDURE: ACTIVE"
                                                       "\n\nDESIGNATION: LIBERTY-PRIME-BOT MK1"
                                                       "\n\nPRIMARY TARGETS: ANY AND ALL RED CHINESE INVADERS"
                                                       "\n\nMEME CANNONS: HOT"
                                                       "\n\nAWAITING FURTHER INSTRUCTION")

print("Going online for the first time")
online()
