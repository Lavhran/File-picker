path = input("path: ")

hfolder = []
print("hidden folders: (q to quit)")
x = ""
while x.lower() != "q":
    x = input("Hide: ")
    if x == "q": break
    hfolder.append(x)

acceptable = []
print("Accepts ( filetype example: .lnk ): (q to quit)")
x = ""
while x.lower() != "q":
    x = input("filetype: ")
    if x == "q": break
    acceptable.append(x)

meat = {
    "folder": path,
    "hfolders": hfolder,
    "accepts": acceptable
}

from json import dump
with open("config.json", "w", encoding="UTF-8") as f:
    dump(meat, f)
    f.close()

exit(input("..."))
