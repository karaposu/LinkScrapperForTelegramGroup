
import  re
import telethon
from telethon import TelegramClient
import asyncio
from telegram_connection import telegram_connection
from telethon.tl.types import MessageEntityUrl
import datetime
import pandas as pd

# pd.set_option('display.width', 300)
# pd.set_option('display.max_columns', 10)


# Checks if the message includes "File uploaded"
# and returns 1 if it does.
def checkIfMessageisRelevant(x):

    search_result = re.search("File uploaded", x)


    if   search_result== None:
        return 0
    else:
        return 1

# uses the information that lesson name is between
# "File uploaded" and "2022" to extract lesson name.
def extractLessonName(x):


    x = re.split("File uploaded:", x)
    search_result = re.search("202", x[1])
    last_indx_after_name = search_result.span()[0]
    name = x[1][0:last_indx_after_name]

    return name


async def getMessages(t_con):


    data=[]

    client = TelegramClient(t_con.get_username(), t_con.get_api_id(), t_con.get_api_hash())
    await client.start()

    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f'{dialog.id}:{dialog.title}')

    GROUPID= 1001432993223



    async with  client:


         channel = await client.get_entity(GROUPID)
         messages =  client.iter_messages(channel, reverse=True)
         async for x in messages:
              if x.message != None:
                  # x_id = str(x.id)
                  d_truncated = datetime.date(x.date.year, x.date.month, x.date.day)
                  x_date=str(d_truncated)
                  if checkIfMessageisRelevant(x.text)==1:
                     name= str(extractLessonName(x.text))

                     for _, target in x.get_entities_text(MessageEntityUrl):

                        x_link= str(target)
                  # print(x_id, name, x_link, x_date)
                  data.append([ name, x_link, x_date])


         data.append([' Final Defence ', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', '2022-06-23'])
         df = pd.DataFrame(data, columns=[ 'title', 'link', 'msg_date'])
         # print(df.head(5))
         all_names = df['title'].tolist()
         print(set(all_names))




    changes_list= []
    changes_list.append([ ' MOR - Methods of Operations Research ' ,' MOR ' ])
    changes_list.append([' Programming Language Python Friday ' , ' Python ' ])
    changes_list.append([  ' Technological Entrepreneurship1 ' ,  ' TE '])
    changes_list.append([ ' Technological Entrepreneurship2 '  , ' TE '])
    changes_list.append([ ' Technological Entrepreneurship '  , ' TE '])
    changes_list.append([' BA - Business Analysis ' , ' BA '])
    changes_list.append([' NLP - Natural Language Processing ' ,' NLP ' ])
    changes_list.append([ ' QML - Quantum Machine Learning ', ' QML '])
    changes_list.append([ ' PMP - Project Management Practice ' , ' PMP '])
    changes_list.append([ ' PMP1 ' , ' PMP '])
    changes_list.append([ ' Sys ' , ' System Analysis '])
    changes_list.append([' NLP 25-09-' ,' NLP ' ])
    changes_list.append([' Python 26-09-' ,' Python ' ])
    changes_list.append([' TE1 ' ,' TE ' ])
    changes_list.append([' TE - Technological Entrepreneurship ' ,' TE ' ])
    changes_list.append([' IT- Information theory ' ,' IT ' ])
    changes_list.append([' IT - Information theory ' ,' IT ' ])
    changes_list.append([' ImP - Image processing ' ,' ImP ' ])
    changes_list.append(['ImP' ,' ImP ' ])
    changes_list.append([ ' Image processing ' ,'ImP' ])
    changes_list.append([ ' Academic Seminar1 ' ,' Academic Seminar ' ])
    changes_list.append([  ' DL            ' ,' DL ' ])
    changes_list.append([  ' Deep Learning ' ,' DL ' ])
    changes_list.append([   ' DCS - Distributed Computing Systems ' ,' Distributed Computing Systems ' ])
    changes_list.append([  ' DCS  ' ,' Distributed Computing Systems ' ])
    changes_list.append([  ' ST ' ,' Storage Technologies ' ])
    changes_list.append([  ' DP - Application aspects of social data processing ' ,' DP ' ])
    changes_list.append([   ' DCS - course ' ,' Distributed Computing Systems ' ])
    changes_list.append([   ' Ap. Stat - Applied statistics ' ,' Applied Statistics ' ])
    changes_list.append([    ' Ap. Stat ',' Applied Statistics ' ])
    changes_list.append([    ' Applied Statistics. Stat ',' Applied Statistics ' ])
    changes_list.append([    ' ML - Machine Learning ',' ML ' ])
    changes_list.append([    ' Predefence - bachelor ','   Predefence - bachelor ' ])
    changes_list.append([    ' Predefence ','   Predefence ' ])
    changes_list.append([    ' Predefence - master ','   Predefence - master ' ])
    changes_list.append([    ' Final Defence ','   Final Defence ' ])


    for x in range (len(df)):

        for xx in changes_list:

             if  df.at[x, 'title'] == xx[0]:

                 df.loc[x, 'title'] = xx[1]


    # print(df.head(5))

    df= df.sort_values(['title','msg_date'])
    zed=df['title'].tolist()
    print(zed)
    df=df.reset_index()
    print(df.columns)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    print(df.columns)
    df.to_csv('BDA_Master_all_lesson_links.csv')



def main():

    t_con = telegram_connection()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getMessages(t_con))

if __name__ == "__main__":

     main()


