
# Python JSON Language File Synchronizer

A script to sync key-value pairs across JSON language files with automatic translation.

## Features
- Syncs translations for specific keys across JSON files.
- Requires the base language to be explicitly specified.
- Uses Google Translate for non-base language files.
- Maintains JSON structure and handles missing files gracefully.

## Prerequisites
- Python 3.x
- Install dependencies: `pip install googletrans==4.0.0-rc1`

## Usage
1. **Parameters**:
   - `file_language_pairs`: List of tuples containing file names and language codes (base language in the first tuple).
   - `header_name`: Top-level key in the JSON structure.
   - `key`: Key to update or add.
   - `base_value` (optional): Reference value; extracted from the base file if omitted.

2. **Example**:
   ```python
   file_language_pairs = [
       ('en.json', 'en'),  # Base language file (English)
       ('de.json', 'de'),  # German
       ('fr.json', 'fr'),  # French
   ]

   sync_languages(file_language_pairs, header_name="messages", key="welcome", base_value="Welcome!")
   ```

## How It Works
1. Extracts `base_value` from the first file (`file_language_pairs[0]`) or uses the provided one.
2. Updates JSON files:
   - Base file gets the `base_value`.
   - Other files get translated values.
3. Writes back updated content if changes are made.

## Error Handling
- Skips invalid or missing files.
- Handles JSON decoding and IO errors gracefully.

### Example Outputs

#### Base File (`en.json`):
```json
{
  "messages": {
    "welcome": "Welcome!"
  }
}
```

#### Translated File (`de.json`):
```json
{
  "messages": {
    "welcome": "Willkommen!"
  }
}
```

## License
MIT License.
