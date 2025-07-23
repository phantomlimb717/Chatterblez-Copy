# Chatterblez 🗣️📖✨

## 🚀 Transform Your PDFs & EPUBS into Engaging Audiobooks! 🎧

Ever wished your favorite books could talk to you? 🤩 Chatterblez is here to make that dream a reality! 🪄 We leverage the cutting-edge **Next-gen AI Chatterbox-tts from Resemble-AI** ([check them out!](https://github.com/resemble-ai/chatterbox)) to generate high-quality audiobooks directly from your PDF or EPUB files. 📚➡️🔊

Inspired by the awesome work of [audiblez](https://github.com/santinic/audiblez), Chatterblez takes text-to-speech to the next level, offering a seamless and delightful listening experience. 💖

---

### 💻 Compatibility 🧑‍💻

Tested and running smoothly on:

* Windows 11 🪟
* Python 3.12 🐍
* **NVIDIA CUDA 12.4:** Required for GPU acceleration and optimal performance. Please ensure you have a compatible NVIDIA graphics card and the necessary CUDA drivers installed. 🚀

---

### 🛠️ Installation & Setup 🚀

Ready to dive in? Here's how to get Chatterblez up and running on your machine:

#### 1. Clone the Repository 📥

```bash
git clone https://github.com/cpttripzz/Chatterblez
```

#### 2. Install CUDA (NVIDIA Graphics Cards Only!) ⚡️

If you have an NVIDIA GPU, install CUDA for optimal performance. This significantly speeds up the AI processing!

* Download CUDA 12.4:
  [https://developer.nvidia.com/cuda-12-4-0-download-archive?target\_os=Windows\&target\_arch=x86\_64\&target\_version=11\&target\_type=exe\_local](https://developer.nvidia.com/cuda-12-4-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)
* Follow the installation instructions provided by NVIDIA. 🧑‍💻

#### 3. Install Python Dependencies 📦

Navigate into the cloned directory and install the required Python packages:

```bash
cd Chatterblez
uv venv --python 3.12  # or however you prefer to create the venv
.venv\Scripts\activate
uv pip install --index-strategy unsafe-best-match -r requirements.txt
```

This might take a moment, so grab a coffee! ☕

#### 4. Install FFMPEG 🔊

FFmpeg is required for audio processing. Here's how to install it:

**🔵 Windows:**

1. Download a static build from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Extract the `.zip` to a location like `C:\ffmpeg`
3. Add the `C:\ffmpeg\bin` path to your **System Environment Variables**:

   * Search *"Edit the system environment variables"* from the Start Menu
   * Click "Environment Variables..."
   * Under "System Variables", find `Path`, click **Edit...**, then **New**, and paste the `bin` folder path
4. Open a new Command Prompt and run:

   ```bash
   ffmpeg -version
   ```

   You should see FFmpeg version info.

**🟢 Linux (Ubuntu):**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg -y
ffmpeg -version
```

**🟣 macOS (with Homebrew):**

```bash
brew install ffmpeg
ffmpeg -version
```

---

### 🚀 Usage

Here's how to use Chatterblez from the command line:

**Basic Conversion (Single File):**

To convert a single EPUB or PDF file, use the `-f` or `--file` argument:

```bash
python cli.py -f "path/to/your/book.epub"
```

The output audiobook will be saved in the current directory.

**Specifying an Output Folder:**

You can specify a different output folder using the `-o` or `--output` argument:

```bash
python cli.py -f "path/to/your/book.pdf" -o "path/to/output/folder"
```

**Batch Processing:**

To convert all supported files in a directory, use the `-b` or `--batch` argument:

```bash
python cli.py -b "path/to/your/books_folder"
```

**Advanced Options:**

*   **`--filterlist`**: A comma-separated list of chapter names to ignore (case-insensitive).
    ```bash
    python cli.py -f "book.epub" --filterlist "Contents,Preface"
    ```
*   **`--wav`**: Path to a WAV file for voice conditioning (audio prompt).
    ```bash
    python cli.py -f "book.epub" --wav "path/to/your/voice.wav"
    ```
*   **`--speed`**: Speech speed (default: 1.0).
    ```bash
    python cli.py -f "book.epub" --speed 1.2
    ```
*   **`--cuda`**: Use GPU for faster processing (if available).
    ```bash
    python cli.py -f "book.epub" --cuda
    ```

---

### 🖼️ GUI Usage

Chatterblez also includes a graphical user interface (GUI) for a more interactive experience.

**Launching the GUI:**

To launch the GUI, run the `pyside.py` script:

```bash
python pyside.py
```

**Features:**

*   **File -> Open**: Load a single EPUB or PDF file.
*   **File -> Batch Mode**: Process all supported files in a selected directory.
*   **Chapter List**: View and select which chapters to include in the audiobook.
*   **Text Preview**: See the extracted text from the selected chapter.
*   **Voice Selection**: Choose a custom WAV file for voice conditioning.
*   **Output Folder**: Specify where to save the generated audiobook.
*   **Real-time Progress**: Monitor the progress of the audiobook creation process.

---

### 🙏 Acknowledgements

* **Resemble-AI** for their incredible [Chatterbox-tts](https://github.com/resemble-ai/chatterbox) project. They're making AI voices sound truly human! 🗣️
* **santinic** for the inspiration from [audiblez](https://github.com/santinic/audiblez). Great minds think alike! 💡

---

### 💌 Contributing

Got ideas? Found a bug? Want to make Chatterblez even better? We'd love your contributions! Please feel free to open an issue or submit a pull request. Let's build something amazing together! 🤝

---

### 📜 License

\[Add your license information here, e.g., MIT License]

---

Made with ❤️ by cpttripzz ✨
Happy listening! 🎧📖💖

---

Let me know if you’d like to add demo commands, screenshots, or a `chatterblez.py` usage example next.
