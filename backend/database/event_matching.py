from classes import *

# Function to calculate relevance score based on string-based interests
def calculate_relevance_score(event, interests):
    score = 0
    for interest in interests:
        if interest in event.EventDescription:
            score += 1
        if interest in event.EventTags:
            score += 2
    return score

# Function to sort events by their relevance
def sort_events_by_relevance(events, interests):
    events_with_scores = [(event, calculate_relevance_score(event, interests)) for event in events]
    sorted_events = sorted(events_with_scores, key=lambda x: x[1], reverse=True)
    return [event for event, score in sorted_events]


# Function to calculate relevance score based on string-based interests
def calculate_relevance_score(friend, interests):
    score = 0
    for interest in interests:
        if interest in friend.ExtendedInterestList:
            score += 1
        if interest in friend.InterestList:
            score += 2
    return score

# Function to sort friends by their interest relevance
def sort_events_by_relevance(events, interests):
    friends_with_scores = [(friend, calculate_relevance_score(friend, interests)) for friend in friends]
    sorted_friends = sorted(friends_with_scores, key=lambda x: x[1], reverse=True)
    return [event for event, score in sorted_friends]

# Example usage
if __name__ == "__main__":
    # Create an instance of the application with a user ID
    app = AppInstance(1)
    
    # Mock user interests as a list of strings
    app.MyUser.InterestList = ["programming", "tech", "AI"]
    
    # Mock events
    app.EventList = [
        Event(EventID=1, KAttendeeArr=[]),
        Event(EventID=2, KAttendeeArr=[]),
        Event(EventID=3, KAttendeeArr=[])
    ]
    
    # Adding descriptions and categories to mock events
    app.EventList[0].EventDescription = "A night of music and fun"
    app.EventList[0].EventTags = ["entertainment"]
    
    app.EventList[1].EventDescription = "An exhibition of modern art"
    app.EventList[1].EventTags = ["culture"]
    
    app.EventList[2].EventDescription = "Tech conference with latest advancements in AI"
    app.EventList[2].EventTags = ["science"]
    
    # Sorting events based on relevance
    sorted_events = sort_events_by_relevance(app.EventList, app.MyUser.InterestList)
    
    # Displaying sorted events
    for event in sorted_events:
        print(f"Event ID: {event.EventID}, Description: {event.EventDescription}, Tags: {event.EventTags}")