path = input("path: ")

def fill(text1: str, text2: str) -> list:
    result = []

    print("{}\n(q to quit)".format(text1))
    x = ""
    while x.lower() != "q":
        x = input("{}: ".format(text2))
        if x == "q": break
        result.append(x)
    print()

    return result

hfolder = fill("Hidden folders:", "Hide")
hfiles = fill("Hidden files:", "Hide")
acceptable = fill("Accepts ( filetype example: .lnk )", "Filetype")

meat = {
    "folder": path,
    "hfolders": hfolder,
    "hfiles": hfiles,
    "accepts": acceptable
}

from json import dump
with open("config.json", "w", encoding="UTF-8") as f:
    dump(meat, f)
    f.close()

exit(input("..."))
