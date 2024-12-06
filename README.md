# Python JSON Language File Synchronizer with Google Translate

This Python script automates the process of syncing key-value pairs across multiple JSON language files. It translates values using Google Translate for languages other than the base language, ensuring consistent structure and updated translations.

## Features
- Identifies a base language file to extract a reference value for synchronization.
- Updates or adds a specific key-value pair across multiple JSON files.
- Automatically translates values to target languages using Google Translate.
- Supports preserving the structure of JSON files.
- Handles errors such as missing files, JSON decoding issues, and IO errors gracefully.

## Usage

### Prerequisites
- Python 3.x installed on your system.
- `googletrans` library installed:
  ```bash
  pip install googletrans==4.0.0-rc1
  ```

### Script Parameters
1. **`file_language_pairs`**: A list of tuples where:
   - The first element is the file name (e.g., `en.json`, `de.json`).
   - The second element is the language code (e.g., `'en'`, `'de'`). Use `None` for the base language file.
2. **`header_name`**: The top-level key in the JSON structure where updates are applied.
3. **`key`**: The specific key to be updated or added within the `header_name`.
4. **`base_value`** (optional): A reference value for translation. If not provided, the script extracts it from the base file.

### Example Usage

```python
file_language_pairs = [
    ('en.json', 'en'),  # English file as the base language
    ('de.json', 'de'),  # German file
    ('fr.json', 'fr'),  # French file
]

sync_languages(file_language_pairs, header_name="messages", key="welcome", base_value="Welcome!")
```

### How It Works
1. The script identifies the base language file (`base_language`) from `file_language_pairs`.
2. If `base_value` is not provided, it retrieves the value for the specified `key` from the base file.
3. For each target language file:
   - If the language differs from the base language, it translates the `base_value` into the target language using Google Translate.
   - Updates the JSON structure with the translated or base value for the specified `key` under the `header_name`.
4. Writes back the updated JSON content only if changes are detected.

### Error Handling
- Skips processing files that are missing or cannot be read.
- Handles invalid JSON gracefully and prints descriptive error messages.

### Example JSON File Before and After

#### Input (`en.json`):
```json
{
  "messages": {
    "welcome": "Welcome!"
  }
}
```

#### Output (`de.json` the key and value was added by identifying "messages"):
```json
{
  "messages": {
    "welcome": "Willkommen!"
  }
}
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Author
[LeMoiz](https://github.com/LeMoiz)
