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

    settings = load_settings()

    # TTS engine
    speaker = Speaker()

    while True:
        try:
            text = input(">> ").strip()

            # empty input skipping
            if not text:
                continue

            # Quit 
            if text.lower() == ":q":
                clean = preprocess("Goodbye. See you soon.")
                speaker.speak(clean, settings["voice"], settings["speed"])
                print("Goodbye.")
                break

            # Settings 
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
