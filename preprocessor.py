import re


# Common abbreviations and how to speak them
ABBREVIATIONS = {
    "dr."  : "doctor",
    "mr."  : "mister",
    "mrs." : "missus",
    "ms."  : "miss",
    "prof.": "professor",
    "st."  : "street",
    "ave." : "avenue",
    "etc." : "et cetera",
    "e.g." : "for example",
    "i.e." : "that is",
    "vs."  : "versus",
    "approx.": "approximately",
}

# Special characters and how to speak them
SPECIAL_CHARS = {
    "@": " at ",
    "&": " and ",
    "#": " hash ",
    "%": " percent ",
    "+": " plus ",
    "=": " equals ",
    "/": " slash ",
    "\\": " backslash ",
}


def _expand_abbreviations(text: str) -> str:
    """Replace known abbreviations with their spoken form."""
    for abbr, expanded in ABBREVIATIONS.items():
        text = re.sub(re.escape(abbr), expanded, text, flags=re.IGNORECASE)
    return text


def _expand_special_chars(text: str) -> str:
    """Replace special characters with speakable words."""
    for char, word in SPECIAL_CHARS.items():
        text = text.replace(char, word)
    return text


def _fix_caps(text: str) -> str:
    """
    Convert ALL CAPS words to title case so Kokoro
    reads them as words, not letter by letter.
    e.g. ROBOSPEAKER -> Robospeaker
    """
    def fix_word(match):
        word = match.group(0)
        return word.title()

    # Only target words that are fully uppercase and longer than 1 character
    return re.sub(r'\b[A-Z]{2,}\b', fix_word, text)


def _clean_whitespace(text: str) -> str:
    """Remove extra spaces."""
    return re.sub(r' +', ' ', text).strip()


def preprocess(text: str) -> str:
    """
    Full preprocessing pipeline.
    Run this on user input before passing to Kokoro.
    """
    text = _expand_abbreviations(text)
    text = _expand_special_chars(text)
    text = _fix_caps(text)
    text = _clean_whitespace(text)
    return text