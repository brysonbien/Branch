from Classes import *

#exec(open('filename.py').read())

GLOBALFriendOBJ = []
GLOBALEventOBJ = []

ProfileID = 123456  #Send to server from the app/phone/webpage
MyProfileOBJ = Profile(ProfileID)

for friendID in MyProfileOBJ.FriendIDArr:
    GLOBALFriendOBJ.append(Profile(friendID))

FriendsEventsArr = CustomHashSet()

for friendOBJ in GLOBALFriendOBJ:
    EventArr = friendOBJ.myEventIDArr #API call from database returns EventIDs in an array
    for event in EventArr:
        FriendsEventsArr.add(event, friendID)

for eventID in FriendsEventsArr.set:
    newEvent = Event(eventID, FriendsEventsArr.get_data(eventID))
    GLOBALEventOBJ.append(newEvent)

        