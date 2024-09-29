from classes import *

def calculate_relevance_score(event, interests):
    score = 0
    for interest in interests:
        if interest.keyword in event.description:
            score += 1
        if interest.category == event.category:
            score += 2
    return score

def sort_events_by_relevance(events, interests):
    events_with_scores = [(event, calculate_relevance_score(event, interests)) for event in events]
    sorted_events = sorted(events_with_scores, key=lambda x: x[1], reverse=True)
    return [event for event, score in sorted_events]

# Example usage
if __name__ == "__main__":
    # Assuming you have a list of events and interests
    app = AppInstance(1)
    
    events = app.EventList
    interests = app.MyUser.InterestList + app.MyUser.ExtendedInterestList

    print(events)
    print(interests)

    sorted_events = sort_events_by_relevance(events, interests)
    for event in sorted_events:
        print(event)