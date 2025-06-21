You're right\! My apologies. The CUDA version should be clearly stated as `12.4` in the compatibility section to match the installation instructions.

Here's the corrected `README.md` content:

-----

# Chatterblez 🗣️📖✨

## 🚀 Transform Your PDFs & EPUBS into Engaging Audiobooks\! 🎧

Ever wished your favorite books could talk to you? 🤩 Chatterblez is here to make that dream a reality\! 🪄 We leverage the cutting-edge **Next-gen AI Chatterbox-tts from Resemble-AI** ([check them out\!](https://github.com/resemble-ai/chatterbox)) to generate high-quality audiobooks directly from your PDF or EPUB files. 📚➡️🔊

Inspired by the awesome work of [audiblez](https://github.com/santinic/audiblez), Chatterblez takes text-to-speech to the next level, offering a seamless and delightful listening experience. 💖

-----

### 💻 Compatibility 🧑‍💻

Tested and running smoothly on:

  * Windows 11 🪟
  * Python 3.12 🐍
  * **NVIDIA CUDA 12.4:** Required for GPU acceleration and optimal performance. Please ensure you have a compatible NVIDIA graphics card and the necessary CUDA drivers installed. 🚀

-----

### 🛠️ Installation & Setup 🚀

Ready to dive in? Here's how to get Chatterblez up and running on your machine:

1.  **Clone the Repository** 📥

    ```bash
    git clone https://github.com/cpttripzz/Chatterblez
    ```

2.  **Install CUDA (NVIDIA Graphics Cards Only\!)** ⚡️
    If you have an NVIDIA GPU, you'll want to install CUDA for optimal performance. This significantly speeds up the AI processing\!

      * Download CUDA 12.4: [https://developer.nvidia.com/cuda-12-4-0-download-archive?target\_os=Windows\&target\_arch=x86\_64\&target\_version=11\&target\_type=exe\_local](https://developer.nvidia.com/cuda-12-4-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)
      * *Follow the installation instructions provided by NVIDIA.* 🧑‍💻

3.  **Install Python Dependencies** 📦
    Navigate into the cloned directory and install the required Python packages:

    ```bash
    cd Chatterblez
    pip install -r requirements.txt
    ```

    This might take a moment, so grab a coffee\! ☕

-----

### 🚀 Usage (Coming Soon\!)

Detailed usage instructions, including how to convert your first PDF or EPUB, will be added here shortly\! Stay tuned\! ⏳

-----

### 🙏 Acknowledgements

  * **Resemble-AI** for their incredible [Chatterbox-tts](https://github.com/resemble-ai/chatterbox) project. They're making AI voices sound truly human\! 🗣️
  * **santinic** for the inspiration from [audiblez](https://github.com/santinic/audiblez). Great minds think alike\! 💡

-----

### 💌 Contributing

Got ideas? Found a bug? Want to make Chatterblez even better? We'd love your contributions\! Please feel free to open an issue or submit a pull request. Let's build something amazing together\! 🤝

-----

### 📜 License

[Add your license information here, e.g., MIT License]

-----

Made with ❤️ by cpttripzz ✨
Happy listening\! 🎧📖💖

-----

To update your `README.md` file, simply copy the entire content above and paste it into your `README.md` file, replacing the old content, then save it.