import json
from googletrans import Translator

def sync_languages(file_language_pairs, header_name, key, base_value=None):
    translator = Translator()
    
    if not base_value:
        first_file, _ = file_language_pairs[0]
        try:
            with open(first_file, 'r', encoding='utf-8') as base_file:
                base_value = json.load(base_file).get(header_name, {}).get(key)
        except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
            print(f"Error processing {first_file}: {e}")
            return

    if not base_value:
        print("No base value found or provided.")
        return

    for file_name, language in file_language_pairs:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)

            if header_name in data and isinstance(data[header_name], dict):
                data[header_name][key] = translator.translate(base_value, dest=language).text if language else base_value

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(json.dumps(data, indent=2, ensure_ascii=False))

            print(f"Updated {file_name} successfully.")
        except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
            print(f"Error processing {file_name}: {e}")

# EXAMPLE USAGE
file_language_pairs = [
    ('en.json', 'en'),
    ('de.json', 'de'),
    ('fr.json', 'fr'),
]

sync_languages(file_language_pairs, "HEADER", "KEY", base_value="VALUE")
