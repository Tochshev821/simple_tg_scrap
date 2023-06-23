from telethon.sync import TelegramClient
 
import csv
 
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from telethon import functions, types


api_id = 
api_hash = ''
phone = '+'
 
client = TelegramClient(phone, api_id, api_hash)
client.start()

chats = []
last_date = None
size_chats = 200
groups=[]


if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=size_chats,
            hash = 0
        ))
chats.extend(result.chats)


for chat in chats:
    try:
        groups.append(chat)
    except:
        continue

print('num of group ')
i=0
for g in groups:
   print(str(i) + '- ') # + g.title)
   i+=1

g_index = input("write num that u want  ")
target_group=groups[int(g_index)]

all_participants = []
all_participants = client.get_participants(target_group)
#print(all_participants)

with open("members111.csv","w",encoding='utf-8') as f:
   writer = csv.writer(f,delimiter=",",lineterminator="\n")
   writer.writerow(['username','name','group'])
   for user in all_participants:
       if user.username:
           username= user.username
       else:
           username= ""
       if user.first_name:
           first_name= user.first_name
       else:
           first_name= ""
       if user.last_name:
           last_name= user.last_name
       else:
           last_name= ""
       name= (first_name + ' ' + last_name).strip()
       writer.writerow([username,name,target_group.title])

print('DONE')

#parse messages from chat
offset_id = 0
limit = 100
all_messages = []
total_messages = 0
total_count_limit = 0
 
while True:
   history = client(GetHistoryRequest(
       peer=target_group,
       offset_id=offset_id,
       offset_date=None,
       add_offset=0,
       limit=limit,
       max_id=0,
       min_id=0,
       hash=0
   ))
   if not history.messages:
       break
   messages = history.messages
   for message in messages:
       all_messages.append(message.message)
   offset_id = messages[len(messages) - 1].id
   if total_count_limit != 0 and total_messages >= total_count_limit:
       break
  
with open("chats.csv", "w", encoding="UTF-8") as f:
   writer = csv.writer(f, delimiter=",", lineterminator="\n")
   for message in all_messages:
       writer.writerow([message])  
print('DONE mess saving')
#channel_username='extremecode' # your channel
#channel_entity=client.get_entity(channel_username)
#posts = client(GetHistoryRequest(
#    peer=channel_entity,
#    limit=100,
#    offset_date=None,
#    offset_id=0,
#    max_id=0,
#    min_id=0,
#    add_offset=0,
#    hash=0))
#print(posts.messages)
