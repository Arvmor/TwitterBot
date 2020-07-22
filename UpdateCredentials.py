#!/usr/bin/env python3
import credentials
from sys import argv


def writeFile(variableName):
    with open("./credentials.py", "+w") as fileHandle:
        for d in variableName:
            fileHandle.write("%s" % d)


# Variables
newAccounts = []

# Append to Variables
for i in range(1, len(argv)):
    if argv[i] != 'EndAccounts':
        newAccounts.append(argv[i])
    else:
        break
if argv[1] != 'EndAccounts':
    credentials.account.append(newAccounts)
i += 1

for i in range(i, len(argv)):
    if argv[i] != 'EndRetweet':
        credentials.retweetSource.append(argv[i][20:])
    else:
        break
i += 1

for i in range(i, len(argv)):
    if argv[i] != 'EndFollow':
        credentials.followIdList.append(argv[i][20:])
    else:
        break
i += 1

for i in range(i, len(argv)):
    if argv[i] != 'EndError':
        credentials.errorText.append(argv[i])
    else:
        break
i += 1

# Write to file
newText = f"""account = {credentials.account}
retweetSource = {credentials.retweetSource}
followIdList = {credentials.followIdList}
errorText = {credentials.errorText}"""
writeFile(newText)
