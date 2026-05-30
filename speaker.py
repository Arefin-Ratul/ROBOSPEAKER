import sounddevice as sd
from kokoro import KPipeline


SAMPLE_RATE = 24000

# Available voices mapped to simple categories
VOICES = {
    "female_warm":   "af_heart",
    "female_clear":  "af_bella",
    "male_deep":     "bm_lewis",
    "male_neutral":  "am_adam",
}


class Speaker:
    def __init__(self):
        self.pipeline = None

    def _load_pipeline(self):
        """Load Kokoro pipeline only once."""
        if self.pipeline is None:
            print("Loading ROBOSPEAKER engine...")
            self.pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')
            print("Engine ready.\n")

    def speak(self, text: str, voice: str = "female_warm", speed: float = 1.0):
        """
        Speak the given text using Kokoro TTS.

        Args:
            text  : the text to speak
            voice : one of the VOICES keys (e.g. "female_warm", "male_deep")
            speed : speaking speed, 0.5 (slow) to 2.0 (fast), default 1.0
        """
        self._load_pipeline()

        voice_id = VOICES.get(voice, "af_heart")

        # Loop through all chunks so long sentences play fully
        for gs, ps, samples in self.pipeline(text, voice=voice_id, speed=speed):
            if samples is not None and len(samples) > 0:
                sd.play(samples, SAMPLE_RATE)
                sd.wait()