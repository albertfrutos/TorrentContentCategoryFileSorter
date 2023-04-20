import os
import sqlite3

import Common as cm

def ProcessDownloadedFiles(downloadsSource):
    downloadedFiles = cm.GetFilesInDirectory(downloadsSource)
    ClassifyDownloadedFiles(downloadedFiles)

def ClassifyDownloadedFiles(downloadedFiles):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        for file in downloadedFiles:
            fileName = os.path.basename(file).split('/')[-1]
            cursor.execute("SELECT ID, Type FROM files WHERE Filename=?", (fileName,))
            for ID, Type in cursor.fetchall():
                os.replace(file,os.path.join(Type,fileName))
                cursor.execute("DELETE FROM files WHERE ID=?", (ID,))
                connection.commit()

