import polib, re, argparse

def normalize_apostrophes(po_file_path):
    """
    Normalize apostrophes in a .po file to use ʻ (U+02BB) for o' and g', as well as ʼ (U+02BC) for "tutuq belgisi".
    
    Args:
        po_file_path (str): The path to the .po file.
    """
    # Load the .po file
    po = polib.pofile(po_file_path)
    
    # Define a regex pattern to match different apostrophe characters
    # apostrophe_pattern = re.compile(r"[’‘`]")
    
    
    # Iterate through each entry in the .po file
    for entry in po:
        if entry.msgstr:
            # Replace all variations of apostrophes with the standard single quote
            entry.msgstr = re.sub("O'", "Oʻ", entry.msgstr)
            entry.msgstr = re.sub("o'", "oʻ", entry.msgstr)
            entry.msgstr = re.sub("G'", "Gʻ", entry.msgstr)
            entry.msgstr = re.sub("g'", "gʻ", entry.msgstr)
            entry.msgstr = re.sub("'", "ʼ", entry.msgstr)
            # xozir bu yerga '' gap sifatida kelsa 2 ta tutuq belgi boʻlib qolmasin
            # tayyor roʻyhat boʻlganida soʻzlarni search qilib replace qilardik manimcha
    
    # Save the changes back to the .po file
    po.save(po_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize apostrophes in a .po file.")
    parser.add_argument("--po_file", help="Path to the .po file to normalize.", required=True)
    
    args = parser.parse_args()
    
    normalize_apostrophes(args.po_file)
    print(f"Apostrophes in '{args.po_file}' have been normalized.")
