import os

def GetFilesInDirectory(folderPath):
    filepaths = []
    foundFiles = os.walk(folderPath)

    for path, subdirs, files in foundFiles:
        for name in files:
            filePath = os.path.join(path,name)
            filepaths.append(filePath)
        
    return filepaths