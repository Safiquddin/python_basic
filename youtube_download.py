from pytube import YouTube
link = input("Enter the youtube Link- ")
print("Downloading...")
YouTube(link).streams.first().download()
print("Video download successsfully")