import pafy
  
url = 'https://youtu.be/YyVI46K8q9E'

v = pafy.new(url)
s = v.getbest()
#print("Size is %s" % s.get_filesize())
fc = s.get_filesize()
print(fc)
#filename = s.download()  # starts download