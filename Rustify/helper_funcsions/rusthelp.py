from os import listdir

def pluginlerim() -> str:
    pluginler = []

    for fayl in listdir("./Rustify/plugins/"):
        if not fayl.endswith(".py") or fayl.startswith("_"):
            continue
        pluginler.append(fayl.replace('.py',''))

    string = ""
    sehife = [sorted(list(pluginler))[i:i + 5] for i in range(0, len(sorted(list(pluginler))), 5)]
        
    for i in sehife:
        string += '💻 '
        for sira, a in enumerate(i):
            string += "`" + str(a)
            if sira == i.index(i[-1]):
                string += "`"
            else:
                string += "`, "
        string += "\n"
    return string
