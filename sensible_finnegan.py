import markovify
import time


with open("body.txt") as bolus:
    undigested = bolus.read()

gizzard = markovify.Text(undigested)

print "Standby! Ten lines of easy-to-digest James Joyce coming right up!\n\n"
# Dramatic pause..

time.sleep(1)
for i in range(10):
    print(gizzard.make_short_sentence(140))
