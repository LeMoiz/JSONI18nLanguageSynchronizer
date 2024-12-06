import json
from googletrans import Translator

def sync_languages(file_language_pairs, header_name, key, base_value=None):
    translator = Translator()
    base_language = None

    for file_name, language in file_language_pairs:
        if language:
            try:
                with open(file_name, 'r', encoding='utf-8') as base_file:
                    base_data = json.load(base_file)
                if header_name in base_data and isinstance(base_data[header_name], dict):
                    if base_value is None:
                        base_value = base_data[header_name].get(key)
                    base_language = language
                    break
            except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
                print(f"Error processing base file {file_name}: {e}")
                return

    if not base_value:
        print("No base value found or provided.")
        return

    # Process each file, translating if necessary
    for file_name, language in file_language_pairs:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                original_content = file.read()
                data = json.loads(original_content)

            if header_name in data and isinstance(data[header_name], dict):
                if language and language != base_language:
                    # Translate base value to the target language
                    translated_value = translator.translate(base_value, src=base_language, dest=language).text
                    data[header_name][key] = translated_value
                else:
                    # Use base value as it is
                    data[header_name][key] = base_value

            # Write back the updated content, preserving structure 
            # NOTE: alter indentation if needed
            updated_content = json.dumps(data, indent=2, ensure_ascii=False)
            if updated_content != original_content:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(updated_content)

            print(f"Updated {file_name} successfully.")
        except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
            print(f"Error processing {file_name}: {e}")

# EXAMPLE USAGE
file_language_pairs = [
    ('en.json', None),
    ('de.json', 'de'),
    ('fr.json', 'fr'),
]

sync_languages(file_language_pairs, "HEADER", "KEY", base_value="VALUE")
