import praw

reddit = praw.Reddit(client_id='zOTU2L6iq26CSw',
                     client_secret='5KZJM5WZZvZd43cFy_Eg2XTjVi8',
                     username='LIBERTY-PRIME-BOT',
                     password='fuckcommies2298',
                     user_agent='libertyprimemk1')
reddit.validate_on_submit = True

botport = reddit.subreddit('botport')

last_state = "online"


def issue_command(command, message):
    message.mark_read()
    if command == "offline" or command == "stop":
        message.reply("COMMAND ACCEPTED: LIBERTY PRIME - OFFLINE")
        botport.submit(title="LIBERTY PRIME: OFFLINE",
                       selftext="SHUTDOWN COMMAND GIVEN BY USER: " + message.author.name)
        print("Going offline")
        offline()
    elif command == "online" or command == "start":
        message.reply("COMMAND ACCEPTED: LIBERTY PRIME - ONLINE")
        botport.submit(title="LIBERTY PRIME: ONLINE",
                       selftext="START UP COMMAND GIVEN BY USER: " + message.author.name)
        print("Going online")
        online()
    else:
        message.reply("UNRECOGNIZED COMMAND. REFER TO THE USER MANUAL LOCATED IN SUBREDDIT HQ")


def verify_user(username):
    with open('verified_users.lp', 'r') as f:
        for line in f:
            if username == line.rstrip():
                return True
    f.close()
    return False


def online():
    print("Entering online state")  # Used for debugging
    while True:  # while the bot is in the 'online' state
        for message in reddit.inbox.unread(limit=None):  # check all unread messages
            print("Online state: message received")
            verified_user = verify_user(message.author.name)
            message.mark_read()
            if verified_user or message.subject == "Access Code:Pg5a3f":
                issue_command(command=message.body, message=message)
            else:
                message.reply("COMMUNIST DETECTED. USER \'" + message.author.name + "\' NOT RECOGNIZED.")


def offline():
    print("Entering offline state")  # Used for debugging
    while True:  # while the bot is in the 'offline' state
        for message in reddit.inbox.unread(limit=None):
            print("Offline state: message received")
            verified_user = verify_user(message.author.name)
            message.mark_read()
            if (verified_user or message.subject == "Access Code: Pg5a3f") and ("online" in message.body or "start" in message.body):
                issue_command(command=message.body, message=message)
            else:
                message.reply("COMMAND REJECTED: LIBERTY PRIME IS OFFLINE")


def main():
    botport.submit(title="LIBERTY PRIME: ONLINE", selftext="STARTUP PROCEDURE: ACTIVE"
                                                           "\n\nDESIGNATION: LIBERTY-PRIME-BOT MK1"
                                                           "\n\nPRIMARY TARGETS: ANY AND ALL RED CHINESE INVADERS"
                                                           "\n\nMEME CANNONS: HOT"
                                                           "\n\nRICK ROLL RIFLES: HOT"
                                                           "\n\nDESIRE TO TROLL COMMUNISTS: RED. HOT."
                                                           "\n\nAWAITING FURTHER INSTRUCTION")

    print("Going online for the first time")
    online()


if __name__ == "__main__":
    main()
