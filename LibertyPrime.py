import praw
import random

reddit = praw.Reddit(client_id='zOTU2L6iq26CSw',
                     client_secret='5KZJM5WZZvZd43cFy_Eg2XTjVi8',
                     username='LIBERTY-PRIME-BOT',
                     password='fuckcommies2298',
                     user_agent='libertyprimemk1')
reddit.validate_on_submit = True

botport = reddit.subreddit('botport')

last_state = "ONLINE"


def issue_command(command, message):
    global last_state
    message.mark_read()
    print(command)
    if command == "offline":
        message.reply("COMMAND ACCEPTED: LIBERTY PRIME - OFFLINE")
        botport.submit(title="LIBERTY PRIME: OFFLINE",
                       selftext="SHUTDOWN COMMAND GIVEN BY USER: " + message.author.name)
        print("Going offline")
        last_state = "OFFLINE"
        offline()
    elif command == "online":
        message.reply("COMMAND ACCEPTED: LIBERTY PRIME - ONLINE")
        botport.submit(title="LIBERTY PRIME: ONLINE",
                       selftext="START UP COMMAND GIVEN BY USER: " + message.author.name)
        print("Going online")
        last_state = "ONLINE"
        online()
    elif command == "status":
        print("Status query")
        message.reply("COMMAND ACCEPTED: CURRENT STATUS - " + last_state.upper())
    else:
        print("Unrecognized command: \'" + command + "\' not found")
        message.reply("COMMAND: \'" + command + "\' UNKNOWN.")


def verify_user(username):
    with open('verified_users.lp', 'r') as f:
        for line in f:
            if username == line.rstrip():  # necessary to remove new line character
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
            if (verified_user or message.subject == "Access Code:Pg5a3f") and (message.body == "offline" or message.body == "online" or message.body == "status"):
                issue_command(command=message.body, message=message)
            else:
                print("Summon detected. Responding with random line")
                with open('responses.lp', 'r') as f:
                    lines = f.read().splitlines()
                    rand_line = str(random.choice(lines)).upper()
                message.reply(rand_line)


def offline():
    print("Entering offline state")  # Used for debugging
    while True:  # while the bot is in the 'offline' state
        for message in reddit.inbox.unread(limit=None):
            print("Offline state: message received")
            verified_user = verify_user(message.author.name)
            message.mark_read()
            if (verified_user or message.subject == "Access Code: Pg5a3f") and (message.body == "offline" or message.body == "online" or message.body == "status"):
                print("Verified user detected. Processing command")
                issue_command(command=message.body, message=message)


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
