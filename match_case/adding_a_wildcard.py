# command = "daje roma forza loba"
# match command.split():
#     case "daje":
#         print("daje")
#     case ("daje",*args, last) if last == "loba":
#         print("daje", *args, last)
#     case ("daje",*args, _):
#         print("daje", *args)
#     case ("daje", _,*args):
#         print("daje", *args)


command = "go east"
valid_actions = ("go", "head", "move", "run", "walk")
match command.split():
    case [
        action,
        ("north" | "south" | "east" | "west") as direction,
    ] if action in valid_actions:
        print(action, direction)
