import sys
sys.setrecursionlimit(10**6)

foldersTotal = {}
class Folder:
    def __init__(self):
        self.folders = {}
        self.files = []

    def addFolder(self, folderName):
        if foldersTotal.get(folderName, -1) == -1:
            foldersTotal[folderName] = Folder()

        self.folders[folderName] = foldersTotal[folderName]

    def addFile(self, fileName):
        self.files.append(fileName)

    def countFiles(self):
        children = self.folders.keys()
        if len(children) == 0:
            return [set(self.files), len(self.files)]

        resultSet = set(self.files)
        resultCount = len(self.files)
        for childName in children:
            fileSet, count = foldersTotal[childName].countFiles()
            resultSet = resultSet.union(fileSet)
            resultCount += count
        return [resultSet, resultCount]


N, M = map(int, sys.stdin.readline().split())

for _ in range(N + M):
    parentName, childName, isFolder = sys.stdin.readline().strip().split()

    if foldersTotal.get(parentName, -1) == -1:
        foldersTotal[parentName] = Folder()

    if isFolder == '1':
        foldersTotal[parentName].addFolder(childName)
    else:
        foldersTotal[parentName].addFile(childName)

Q = int(sys.stdin.readline())

for _ in range(Q):
    query = sys.stdin.readline().strip()
    targetFileName = query.split('/')
    fileSet, count = foldersTotal[targetFileName[-1]].countFiles()
    print(len(fileSet), count)