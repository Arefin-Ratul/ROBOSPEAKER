# ROBOSPEAKER 🔊
### Giving a voice to those who need one.
**Developed by Arefin Ratul**

---

ROBOSPEAKER is a text-to-speech assistive tool designed for people who cannot speak. You type — it speaks. The voice is human-like, fully offline after the first setup, and customizable.

---

## Requirements

Before you start, make sure you have the following:

- **Windows 10 or 11** (64-bit)
- **Python 3.11** — download from [python.org](https://www.python.org/downloads/release/python-3110/)
  - During installation, check **"Add Python to PATH"**
- **Internet connection** for first-time setup only (downloads ~350MB of model files)

---

## Installation — Step by Step

### Step 1 — Download the project

Click the green **Code** button on this GitHub page → **Download ZIP** → Extract it somewhere on your computer.

Or if you have Git installed:
```
git clone https://github.com/YOUR_USERNAME/ROBOSPEAKER.git
```

---

### Step 2 — Open the project folder in cmd

Open Command Prompt and navigate to the folder where you extracted ROBOSPEAKER:

```
cd path\to\ROBOSPEAKER
```

Example:
```
cd E:\CODING\Python\ROBOSPEAKER
```

---

### Step 3 — Create a virtual environment

```
python -m venv venv
```

This creates an isolated Python environment for ROBOSPEAKER so it doesn't interfere with anything else on your computer.

---

### Step 4 — Activate the virtual environment

```
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your cmd line. This means the environment is active.

---

### Step 5 — Install dependencies

```
pip install -r requirements.txt
```

This will install Kokoro, PyTorch, and all other required packages. **This may take several minutes** depending on your internet speed. PyTorch alone is about 2GB.

> ⚠️ If the installation times out, run this instead:
> ```
> pip install --timeout 300 -r requirements.txt
> ```

---

### Step 6 — Run ROBOSPEAKER

```
python main.py
```

**The first time you run it**, ROBOSPEAKER will download the voice model (~327MB) from the internet. This only happens once. After that, everything works fully offline.

---

## How to Use

Once running, you will see:

```
============================================================
        ROBOSPEAKER by Arefin Ratul
        Giving a voice to those who need one.
============================================================
Commands:
  :settings  - change voice and speed
  :q         - quit

>>
```

- **Type anything** after `>>` and press Enter — ROBOSPEAKER will speak it aloud
- **Type `:settings`** to change your voice (Male/Female, Deep/Light) and speaking speed
- **Type `:q`** to exit

Your voice and speed preferences are **saved automatically** and remembered next time you run the program.

---

## Every Time You Want to Run ROBOSPEAKER

You only need to do the full installation once. After that, just:

```
venv\Scripts\activate
python main.py
```

---

## Troubleshooting

**"No module named 'speaker'"**
Make sure you activated the venv first (`venv\Scripts\activate`) and that all files are in the same folder.

**"pip install" times out**
Run `pip install --timeout 300 -r requirements.txt` to give it more time.

**Voice sounds noisy or distorted**
Make sure your audio output device is set correctly in Windows sound settings.

**First run is slow**
This is normal — the voice model is being downloaded. Subsequent runs start instantly.

**Program crashes on startup**
Make sure you are using Python 3.11, not 3.12, 3.13, or 3.14. Other versions may have compatibility issues with some dependencies.

---

## Project Structure

```
ROBOSPEAKER/
│
├── main.py            # Entry point — run this to start
├── speaker.py         # Kokoro TTS engine wrapper
├── preprocessor.py    # Text cleaning and normalization
├── settings.py        # Voice and speed config
└── requirements.txt   # All dependencies
```

---

## License

This project is open source and free to use.

---

*ROBOSPEAKER — Because everyone deserves a voice.*
