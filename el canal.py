def determine_reading_status(n, a, q, notifications):
    online_subscribers = a  

    for notification in notifications:
        if notification == '+':
            online_subscribers += 1
        else:
            online_subscribers = max(0, online_subscribers - 1)

    if online_subscribers == n:
        return "YES"
    elif online_subscribers >= a:
        return "MAYBE"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n, a, q = map(int, input().split())
    notifications = input()

    result = determine_reading_status(n, a, q, notifications)
    print(result)
