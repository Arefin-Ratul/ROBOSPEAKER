from speaker import Speaker
from preprocessor import preprocess
from settings import load_settings, configure_settings


COMMANDS = """
Commands:
  :settings  - change voice and speed
  :q         - quit
"""


def main():
    print("=" * 60)
    print("        ROBOSPEAKER by Arefin Ratul")
    print("        Giving a voice to those who need one.")
    print("=" * 60)
    print(COMMANDS)

    # Load saved settings (or defaults if first run)
    settings = load_settings()

    # Initialize the TTS engine
    speaker = Speaker()

    while True:
        try:
            text = input(">> ").strip()

            # Skip empty input
            if not text:
                continue

            # Quit command
            if text.lower() == ":q":
                clean = preprocess("Goodbye. See you soon.")
                speaker.speak(clean, settings["voice"], settings["speed"])
                print("Goodbye.")
                break

            # Settings command
            elif text.lower() == ":settings":
                settings = configure_settings(settings)

            # Normal speech
            else:
                clean = preprocess(text)
                speaker.speak(clean, settings["voice"], settings["speed"])

        except KeyboardInterrupt:
            print("\nExiting ROBOSPEAKER.")
            break


if __name__ == "__main__":
    main()