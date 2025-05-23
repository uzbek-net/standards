import polib


po = polib.pofile("FILE_LOCATION")

for entry in po.fuzzy_entries():
    entry.flags.remove('fuzzy')
po.save()