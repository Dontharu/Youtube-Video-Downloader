# module
import pytube

# name
print("")
name = input("Type any name you wish: ")
print("")

# ask for the url to download
url = input("URL: ")
print("")

# ask for the path to download
path = input("PATH: ")
print("")

# download
download = pytube.YouTube(url).streams.get_highest_resolution().download(path)

# outro
print(f"Successfull in downloading the video {name} ({url})")
print("")