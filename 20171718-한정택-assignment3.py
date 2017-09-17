import pickle

dbfilename = 'test3_4.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []

    try:
        scdb = pickle.load(fH)
        for p in scdb:
            p['Age'] = int(p['Age'])
            p['Score'] = int(p['Score'])
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
            except:
                print("Invalid Input")

        elif parse[0] == 'del':
            try:
                for i in range(len(scdb)).__reversed__():
                    if scdb[i]['Name'] == parse[1]:
                        scdb.remove(scdb[i])
            except:
                print("Invalid Input")

        elif parse[0] == 'show':
            try:
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                print("Invalid Input")

        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':
            try:
                for i in range(len(scdb)):
                    if scdb[i]["Name"] == parse[1]:
                        print(scdb[i])
            except:
                print("Invalid Input")

        elif parse[0] == 'inc':
            try:
                for i in range(len(scdb)):
                    if scdb[i]['Name'] == parse[1]:
                        scdb[i]['Score'] = int(scdb[i]['Score']) + int(parse[2])
            except:
                print("Invalid Input")


        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
