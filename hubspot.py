import json
import requests
from collections import defaultdict

WINDOW_MILLSEC = 600000


def generateSessionByUser(input):
    hashTable = defaultdict(list)
    for event in input['events']:
        hashTable[event['visitorId']].append(
            (event['timestamp'], event['url']))

    output = {}
    for user, events in hashTable.items():
        # Per user
        sessions = []
        events.sort()  # Sort events by timestamp per user
        startTime, url = events[0]
        endTime, pages = startTime, [url]

        def addSession(startTime, endTime, pages):
            sessions.append(
                {
                    'duration': endTime - startTime,
                    'pages': pages,
                    'startTime': startTime
                }
            )

        for timestamp, url in events[1:]:
            if timestamp <= endTime + WINDOW_MILLSEC:
                # Merge if current timestamp is within WINDOW_MILLSEC
                pages.append(url)
                endTime = timestamp
            else:
                # Append session
                addSession(startTime, endTime, pages)
                pages = [url]
                startTime = endTime = timestamp
        if len(pages) > 0:
            # Finalize last session
            addSession(startTime, endTime, pages)

        output[user] = sessions
    return {'sessionsByUser': output}


if __name__ == '__main__':
    # Send request to get the events data
    response = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=9450f6d95b8a8dcd7bcde9d96be3")
    input = response.json()

    # Convert json data into sessions data
    sessionsByUser = json.dumps(generateSessionByUser(input), indent=2)
    # print(sessionsByUser)

    # Send back the result of generateSessionByUser() to result URL by post
    postResponse = requests.post("https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=9450f6d95b8a8dcd7bcde9d96be3", data=sessionsByUser)
    print(postResponse.status_code)
    print(postResponse.json())

