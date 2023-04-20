## TorrentContentCategoryFileSorter

This utility allows to handle your torrent downloads in a semi-automatised way.

The optimal way of use is run it every a certain amount of time in the server you are running the torrent client. There are 2 methods you can use (see main.py):

 ### ProcessTorrentFiles (from TorrentProcessor)
 
 This parses the contents of the directory (and subdirectories) located in its first parameter path, registers them and sends the correponding torrent file to the folder being monitored by the torrent client. For example, if you will paste file for 'TypeA' files in the folder WatchTypeA:

 _torrproc.ProcessTorrentFiles("WatchTypeA", "TypeA", "WatchTorrent")_

 This will look for torrent files in the WatchTypeA folder, parse the, registers the contained video files and their type (in this case, TypeA) in the sqlite3 DB and then move them to the WatchTorrentFolder (the folder being monitored by the torrent client).

 Supported video files are: _'.avi', '.mp4', '.mkv'_ but you can add new ones in the TorrentProcessor.py file if you wish

 ### ProcessDownloadedFiles (from DownloadedProcessor)

 This takes the files already downloaded (by 'downloaded' I mean the ones in the folder passed as the first - and only - parameter)- Then queries the sqlite3 DB to get the corresponding Type and moves it to the corresponding folder (this is the) their parameter in the ProcessTorrentFiles call.

 _downproc.ProcessDownloadedFiles("TorrentDownloads")_

 ## Example:

 Imagine I call the following lines of code (main.py)_:

 ```python
import TorrentProcessor as torrproc
import DownloadedProcessor as downproc

torrproc.ProcessTorrentFiles("WatchTypeA", "TypeA", "WatchTorrent") #line 1
torrproc.ProcessTorrentFiles("WatchTypeB", "TypeB", "WatchTorrent") #line 2

downproc.ProcessDownloadedFiles("TorrentDownloads")                 # line 3
```

This means:

 * Line 1 processes the torrent files inside the folder _WatchTypeA_, registers their (supported) video files (the ones that will be downloaded) and moves it to the _WatchTorrent_ folder (monitored by the torrent client, so download starts automatically). Imagine that type 'A' are summer videos, then the tool says: OK, from WatchTypeA I will take all the video files referenced by the torrent files in it, will register them and will start the download via the monitored folder.

 * Line 2 does exactly the same but for the 'B' folder and type. Let's say it's for winter videos.

 * Line 3 looks for the supported video files already downloaded (the client downloads them in the "TorrentDownloads" folder) and queries de DB: _Which folder (type) should I target for the file xxxxxxxxxxxxx?_ This way, the video is moved to the corresponding folder (the one passed in the second parameter in the ProcessTorrentFiles folder).
