import torrent_parser as tp
import os
import sqlite3

import Common as cm

videoExtensions = ['.avi', '.mp4', '.mkv']


def ProcessTorrentFiles(directoryTorrentFiles, type, torrentListenerFolder):
    torrentFiles = cm.GetFilesInDirectory(directoryTorrentFiles)
    videoFiles, torrentFilesToLoad = GetFilteredFilesInTorrentByExtension(torrentFiles, videoExtensions)
    RegisterNewFilesToDB(videoFiles, type)
    MoveFiles(torrentFilesToLoad, torrentListenerFolder)


def MoveFiles(sources, targetFolder):
    for source in sources:
        fileName = os.path.basename(source).split('/')[-1]
        target = os.path.join(targetFolder,fileName)
        os.replace(source, target)


def GetFilteredFilesInTorrentByExtension(torrentFiles, extensions):
    torrentFilesToLoad = []
    videoFiles = []
    for torrentFile in torrentFiles:
            files = tp.parse_torrent_file(torrentFile)
            for file in files['info']['files']:
                filename = file['path'][0]
                fileExtension = os.path.splitext(filename)[1]
                if(fileExtension in extensions):
                    videoFiles.append(filename)
                    if not (torrentFile in torrentFilesToLoad):
                        torrentFilesToLoad.append(torrentFile)

    return videoFiles, torrentFilesToLoad

def RegisterNewFilesToDB(files, type):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        for file in files:
            cursor.execute("INSERT INTO files (Filename, Type) VALUES(?, ?)", (file, type))
        connection.commit()

