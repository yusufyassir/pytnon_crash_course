def send_messages(messages, moved_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        moved_messages.append(current_message)

list = ['hello', 'i am iron man', 'get help', 'im batman']
messagess = []
send_messages(list[:], messagess)

print(list)
print(messagess)