import os

path = os.path.join(".", "data")
path = ".\\data"

text_path = os.path.join(path, "txt")
text_path = path + '\\txt'

jpg_path = os.path.join(path, "jpg")
jpg_path =  path + '\\jpg'

html_path = os.path.join(path, "html")
html_path =  path + '\\html'

files = os.listdir(path=path)

print(files)

text =[]
jpg = []
html = []

for i in range(len(files)):
    print(files[i])

for filename in files:
    if filename.endswith(".txt"):
        text.append(filename)
    if filename.endswith(".jpg"):
        jpg.append(filename)
    if filename.endswith(".html"):
        html.append(filename)


print()

print(text)
print(jpg)
print(html)
#alexandermodrzewski@gmail.com


for textFile in text:
    os.rename(path+'/'+textFile, text_path+'/'+textFile)

for textFile in jpg:
    os.rename(os.path.join(path, textFile), os.path.join(jpg_path, textFile))

for textFile in html:
    os.rename(os.path.join(path, textFile), os.path.join(html_path, textFile))
