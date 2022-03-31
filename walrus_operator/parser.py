import parse
from reader import feed
import statistics

# feed.get_titles()

pattern = parse.compile(
    "The Real Python Podcast – Episode #{num:d}: {name}"
)

# print(pattern.parse(
#     "The Real Python Podcast – Episode #63: "
#     "Create Web Applications Using Anvil"
# ))

podcasts = [
    podcast["name"]
    for title in feed.get_titles()
    if (podcast := pattern.parse(title))
]

# print(podcasts)
# The generator expression uses an assignment expression to avoid calculating the length of each episode title twice.
print(statistics.mean(
    title_length
    for title in podcasts
    if (title_length := len(title)) > 50
))