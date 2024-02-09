DiverseBeats = ["Tusa", "Rockstar", "Tangerine"]

DiverseBeats.append("Seasons")  # add seasons
DiverseBeats.remove("Rockstar")  # remove
DiverseBeats.insert(1, "Telepatia")  # insert Telepatia into the second slot

size = len(DiverseBeats)  # total number of songs
print(size)

HarryStyles = "Watermelon Sugar"

if HarryStyles in DiverseBeats:  # look for harry styles
    print("True")
else:
    print("False")

print(DiverseBeats)  # for testing
