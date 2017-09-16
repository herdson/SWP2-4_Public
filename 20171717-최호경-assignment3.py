import pickle

dbfilename = '20171717-최호경-assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
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
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
        elif parse[0] == 'del':
            tram = 0
            while tram < len(scdb):
                if scdb[tram]['Name'] == parse[1]:
                    scdb.remove(scdb[tram])
                else:
                    tram += 1
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                print("Cant find Key name")
        elif parse[0] == 'find':
            for i in scdb:
                if parse[1] == i["Name"]:
                    print(i)
        elif parse[0] == 'inc':
            for k in scdb:
                try:
                    if parse[1] == k["Name"]:
                        k["Score"] = str(int(k['Score'])+int(parse[2]))
                    else:
                        print("No name here")
                        break
                except:
                    print('Plz type integer')
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            if attr == 'Name':
                print(attr + "=" + p[attr], end=' ')
            else:
                print(attr + "=", int(p[attr]), end= ' ')
        print()




scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

