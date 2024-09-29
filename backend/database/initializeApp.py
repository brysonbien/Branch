from classes import *
from db_reader import *

def init(instance):


    MyUser = instance.MyUser
    MyUserID = MyUser.UserID

    MyUser.fill_user()
    MyUser.fill_user_friends()
    

    for friendID in MyUser.UserFriendsList:
        user = User(friendID)
        user.fill_user()
        instance.FriendUserList.append(user)

    FriendsEventsArr = CustomHashSet()

    for friendUser in instance.FriendUserList:
        db_reader.fill_user(friendUser)  #API call from database returns EventIDs in an array
        for event in friendUser.myEventIDArr:
            FriendsEventsArr.add(event, friendID)

    print(MyUser.myEventIDArr, 'my horse cock')
    for eventID in MyUser.myEventIDArr:
        FriendsEventsArr.add(eventID[1:-1], MyUserID)
        

    for eventID in FriendsEventsArr.set:
        newEvent = Event(FriendsEventsArr.get_data(eventID), eventID)
        newEvent.fill_event()
        instance.EventList.append(newEvent)
        return


        