import toml
import polib


data = toml.load("dictionary.toml")

po = polib.POFile()

for entry in data["translations"]:
    en = entry["en"]
    uz = entry["uz"]
    description = entry["description"]

    po.append(polib.POEntry(comment=description ,msgid=en, msgstr=uz))

po.save("locale/uz.po")

print("------------------------------")
print("Updated locale/uz.po")
print("------------------------------")