import json
import os


SETTINGS_FILE = "robospeaker_settings.json"

DEFAULT_SETTINGS = {
    "voice": "female_warm",
    "speed": 1.0,
}

# Voice menu shown to user
VOICE_OPTIONS = {
    "1": ("female_warm",   "Female - Warm"),
    "2": ("female_clear",  "Female - Clear"),
    "3": ("male_deep",     "Male - Deep"),
    "4": ("male_neutral",  "Male - Neutral"),
}


def load_settings() -> dict:
    """Load settings from file. If no file exists, return defaults."""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                data = json.load(f)
                # Fill in any missing keys with defaults
                for key, val in DEFAULT_SETTINGS.items():
                    if key not in data:
                        data[key] = val
                return data
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read settings file. Using defaults.")
    return DEFAULT_SETTINGS.copy()


def save_settings(settings: dict):
    """Save current settings to file."""
    try:
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=4)
    except IOError:
        print("Warning: Could not save settings.")


def configure_voice(settings: dict) -> dict:
    """Interactive voice selection menu."""
    print("\n--- Voice Selection ---")
    for key, (_, label) in VOICE_OPTIONS.items():
        print(f"  {key}. {label}")

    while True:
        choice = input("Choose a voice (1-4): ").strip()
        if choice in VOICE_OPTIONS:
            settings["voice"] = VOICE_OPTIONS[choice][0]
            print(f"Voice set to: {VOICE_OPTIONS[choice][1]}")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 4.")

    return settings


def configure_speed(settings: dict) -> dict:
    """Interactive speed selection."""
    print("\n--- Speed Selection ---")
    print("  Enter a value between 0.5 (slow) and 2.0 (fast)")
    print("  Default is 1.0 (normal)")

    while True:
        choice = input("Enter speed: ").strip()
        try:
            speed = float(choice)
            if 0.5 <= speed <= 2.0:
                settings["speed"] = speed
                print(f"Speed set to: {speed}")
                break
            else:
                print("Out of range. Enter a value between 0.5 and 2.0.")
        except ValueError:
            print("Invalid input. Enter a number like 1.0 or 1.5.")

    return settings


def configure_settings(settings: dict) -> dict:
    """Run full settings configuration and save."""
    settings = configure_voice(settings)
    settings = configure_speed(settings)
    save_settings(settings)
    print("Settings saved.\n")
    return settings