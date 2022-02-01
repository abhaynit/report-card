# importing pafy
import pafy

# url of video
url = "https://youtu.be/YyVI46K8q9E+0"

# instant created
video = pafy.new(url)

# getting number of likes
count = video.viewcount

# showing likes
print("View Count : " + str(count))
