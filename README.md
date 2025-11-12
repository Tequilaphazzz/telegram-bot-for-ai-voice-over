# Telegram Bot for Text Voice-over using ElevenLabs

This project is a Telegram bot that generates voice-over based on text, using the ElevenLabs API platform. The bot allows the user to select a voice, enter text, and receive an audio file with the voice-over. The project is designed to automate tasks related to audio content generation and can be used for podcasts, videos, or other multimedia materials.

## Key Features
- **Audio Generation**:
  - Creating a voice-over of text based on the user-selected voice.
  - Support for high-quality ElevenLabs TTS models.
- **Voice Selection**:
  - The user can select a voice from the list of available ones.
- **Telegram Integration**:
  - Simple interaction through a Telegram bot.
- **File Saving and Sending**:
  - Sending audio files to the user directly in the Telegram chat.

## Technologies Used
- **Python**: Main development language.
- **Telebot (pyTelegramBotAPI)**: Library for working with the Telegram API.
- **ElevenLabs API**: Platform for speech synthesis using AI.

## Installation and Setup
1. **Creating a Telegram Bot**:
   - Find @BotFather on Telegram and create a new bot.
   - Save the API token provided by BotFather.

2. **ElevenLabs Registration**:
   - Register on [ElevenLabs](https://elevenlabs.io/) and obtain an API key.

3. **Project Configuration**:
   - Clone the project repository:
     ```bash
     git clone <Repository URL>
     ```
     
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
     
   - In the `config.py` file, specify the Telegram bot token and the ElevenLabs API key:
   
     ```python
     elevenlabs_api_key = "YOUR_API_KEY"
     bot_token = "YOUR_TELEGRAM_TOKEN"
     ```
   
     Note: Storing the key and token in a `.py` file is unsafe and applicable for demonstration purposes only. For production use, it's better to store them in an `.env` file and call the variables through the corresponding function in your code.
   
4. **Running**:
   
   - Run the bot with the command:
     ```bash
     python main.py
     ```

## How the Bot Works
1. The user starts the bot and enters the `/start` command.
2. The bot suggests selecting a voice from the list using the keyboard.
3. After selecting the voice, the bot requests the text for voice-over.
4. The bot generates an audio file with the text voice-over and sends it to the user.

## Advantages
- Ease of use via Telegram.
- High quality of synthesized speech.
- Flexibility in configuring voices and texts.
- Scalability for multimedia tasks.

## Possible Improvements
- Integration with other platforms (e.g., Discord).
- Support for additional text processing before generation.
- Adding a function to save the user's request history.

## Conclusion
This project demonstrates the practical application of TTS and API technologies in real-world tasks. The Telegram bot provides a convenient interface for generating audio files, making it a useful tool for creative and business purposes.