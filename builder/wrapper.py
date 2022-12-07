import builder.download as download
import builder.pagewriter as pagewriter

download.load("storage.json")
download.download()
pagewriter.write("manhera")