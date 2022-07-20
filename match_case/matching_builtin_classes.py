actions = [
    {"text": "1", "color": "blue", "sleep": 96.2},
    {"sound": "www.daje.com", "format": "ogg"},
    {"sleep": 25.3},
]

for action in actions:
    match action:
        case {"text": str(message), "color": str(c)}:
            print(c)
            print(message)
        case {"sleep": float(duration)}:
            print(duration)
        case {"sound": str(url), "format": "ogg"}:
            print(url)
        case {"sound": _, "format": _}:
            print("Unsupported audio format")
