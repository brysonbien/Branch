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
        db_reader.fill_user_event(friendUser)  #API call from database returns EventIDs in an array
        for event in friendUser.myEventIDArr:
            FriendsEventsArr.add(event, friendID)

    for eventID in FriendsEventsArr.set:
        newEvent = Event(eventID, FriendsEventsArr.get_data(eventID))
        newEvent.fill_event()
        instance.EventList.append(newEvent)
        return

        