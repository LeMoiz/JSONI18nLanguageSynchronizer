import json
from googletrans import Translator

def sync_languages(file_language_pairs, header_name, key, base_value=None):
    translator = Translator()
    base_file, base_language = file_language_pairs[0]

    if not base_language or not base_file:
        print("Base language must be specified in the first tuple.")
        return

    if not base_value:
        try:
            with open(base_file, 'r', encoding='utf-8') as bf:
                base_value = json.load(bf).get(header_name, {}).get(key)
        except:
            print(f"Error reading {base_file}")
            return

    for file_name, language in file_language_pairs:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
            if header_name in data and isinstance(data[header_name], dict):
                data[header_name][key] = (
                    translator.translate(base_value, dest=language).text if language else base_value
                )
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except:
            print(f"Error processing {file_name}")

# EXAMPLE USAGE
file_language_pairs = [
    ('en.json', 'en'),
    ('de.json', 'de'),
    ('fr.json', 'fr'),
]

sync_languages(file_language_pairs, "HEADER", "KEY", base_value="VALUE")
