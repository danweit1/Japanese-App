import xml.etree.ElementTree as ET

def map_jlpt_level(old_level):
    """
    Convert old JLPT levels to the modern N5–N1 system.
    """
    mapping = {
        4: 5,  # JLPT 4 → N5
        3: 4,  # JLPT 3 → N4
        2: 3,  # JLPT 2 → N3/N2 (approximate)
        1: 1,  # JLPT 1 → N1
    }
    return mapping.get(old_level, None)


def parse_kanjidic(xml_file):
    kanji_list = []
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for character in root.findall('character'):
        literal = character.find('literal').text  # Kanji character
        misc = character.find('misc')

        # Get JLPT level (remapped)
        jlpt_tag = misc.find('jlpt')
        if jlpt_tag is not None:
            old_jlpt_level = int(jlpt_tag.text)
            jlpt_level = map_jlpt_level(old_jlpt_level)
        else:
            jlpt_level = None

        # Skip kanji without a JLPT level
        if jlpt_level is None:
            continue

        # Get stroke count
        stroke_count = misc.find('stroke_count').text if misc.find('stroke_count') is not None else None

        # Extract readings
        readings = {"onyomi": [], "kunyomi": []}
        for reading in character.findall('.//reading_meaning/rmgroup/reading'):
            r_type = reading.attrib.get('r_type')
            if r_type == 'ja_on':
                readings["onyomi"].append(reading.text)
            elif r_type == 'ja_kun':
                readings["kunyomi"].append(reading.text)

        # Extract meanings
        meanings = []
        for meaning in character.findall('.//reading_meaning/rmgroup/meaning'):
            if meaning.attrib.get('m_lang') is None:  # Only include English meanings
                meanings.append(meaning.text)

        kanji_list.append({
            "character": literal,
            "onyomi": ", ".join(readings["onyomi"]),
            "kunyomi": ", ".join(readings["kunyomi"]),
            "stroke_count": int(stroke_count) if stroke_count else None,
            "jlpt_level": jlpt_level,
            "meanings": ", ".join(meanings),
        })

    return kanji_list


# Example usage
if __name__ == "__main__":
    # Provide the path to your decompressed kanjidic2.xml file
    xml_file = 'C:/Kanji/kanjidic2.xml'  # Replace with the actual path to your XML file

    # Parse the XML file
    kanji_data = parse_kanjidic(xml_file)

    # Print the total number of JLPT kanji parsed and a sample of the data
    print(f"Total JLPT Kanji Parsed: {len(kanji_data)}")
    for kanji in kanji_data[:5]:  # Display the first 5 kanji
        print(kanji)
