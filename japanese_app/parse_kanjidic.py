import json
import xml.etree.ElementTree as ET

XML_FILE_PATH = r"C:\Kanji\kanjidic2.xml"  # Path to your XML file
JSON_FILE_PATH = r"C:\Kanji\kanji-jouyou.json"  # Path to your JSON file
OUTPUT_FILE_PATH = r"C:\Kanji\unified_kanji_with_levels.json"  # Output file for unified kanji data


def load_json(json_path):
    """
    Load JSON file with kanji as keys.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    print(f"Loaded {len(json_data)} kanji from JSON.")
    return json_data


def parse_kanjidic(xml_path, json_kanji):
    """
    Parse the XML file and integrate JLPT levels from JSON.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    kanji_list = []
    for character in root.findall("character"):
        literal = character.find("literal").text  # Kanji character
        misc = character.find("misc")

        # Extract JLPT level from XML
        jlpt_tag = misc.find("jlpt")
        jlpt_level = int(jlpt_tag.text) if jlpt_tag is not None else None

        # Get JLPT level from JSON if available
        json_entry = json_kanji.get(literal)
        jlpt_new = json_entry["jlpt_new"] if json_entry and "jlpt_new" in json_entry else None

        # Final JLPT level: JSON's jlpt_new takes priority if not null
        final_jlpt_level = jlpt_new if jlpt_new is not None else jlpt_level

        # Skip kanji without any JLPT level
        if final_jlpt_level is None:
            continue

        # Extract stroke count
        stroke_count = misc.find("stroke_count").text if misc.find("stroke_count") is not None else None

        # Extract readings
        readings = {"onyomi": [], "kunyomi": []}
        for reading in character.findall('.//reading_meaning/rmgroup/reading'):
            r_type = reading.attrib.get("r_type")
            if r_type == "ja_on":
                readings["onyomi"].append(reading.text)
            elif r_type == "ja_kun":
                readings["kunyomi"].append(reading.text)

        # Extract meanings
        meanings = []
        for meaning in character.findall('.//reading_meaning/rmgroup/meaning'):
            if meaning.attrib.get("m_lang") is None:  # Only include English meanings
                meanings.append(meaning.text)

        kanji_list.append({
            "character": literal,
            "jlpt_level": final_jlpt_level,
            "strokes": int(stroke_count) if stroke_count else None,
            "onyomi": ", ".join(readings["onyomi"]),
            "kunyomi": ", ".join(readings["kunyomi"]),
            "meaning": ", ".join(meanings),
        })

    print(f"Parsed {len(kanji_list)} kanji from XML.")
    return kanji_list


def save_to_json(data, output_path):
    """
    Save data to a JSON file.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Unified kanji data saved to {output_path}")


if __name__ == "__main__":
    # Load JSON data
    json_kanji = load_json(JSON_FILE_PATH)

    # Parse XML and integrate JLPT levels from JSON
    kanji_data = parse_kanjidic(XML_FILE_PATH, json_kanji)

    # Save the result to a unified JSON file
    save_to_json(kanji_data, OUTPUT_FILE_PATH)
