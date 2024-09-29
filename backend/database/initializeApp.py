from classes import *
from db_reader import *

def init(instance):


    MyUser = instance.MyUser
    MyUserID = MyUser.UserID

    MyUser.fill_user()
    MyUser.fill_user_friends()
    

    for friendID in MyUser.FriendIDArr:
        user = User(friendID)
        user.fill_user
        instance.FriendUserList.append(user)

    FriendsEventsArr = CustomHashSet()

    for friendUser in instance.FriendUserList:
        EventArr = db_reader.fill_user_reader(friendUser)  #API call from database returns EventIDs in an array
        for event in EventArr:
            FriendsEventsArr.add(event, friendID)

    for eventID in FriendsEventsArr.set:
        newEvent = Event(eventID, FriendsEventsArr.get_data(eventID))
        newEvent.fill_event()
        instance.EventList.append(newEvent)
        return

        