import TorrentProcessor as torrproc
import DownloadedProcessor as downproc

torrproc.ProcessTorrentFiles("WatchTypeA", "TypeA", "WatchTorrent")
torrproc.ProcessTorrentFiles("WatchTypeB", "TypeB", "WatchTorrent")

downproc.ProcessDownloadedFiles("TorrentDownloads")