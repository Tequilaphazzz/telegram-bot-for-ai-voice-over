import telebot
import config
import io
from voice import get_all_voices, generate_audio

# Bot initialization
API_TOKEN = config.bot_token
bot = telebot.TeleBot(API_TOKEN)

# Get all voices from the voice.py module
voices = get_all_voices()

# Creating a keyboard for voice selection
voice_buttons = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
for voice in voices.voices:
    voice_name = voice.name  # Get the voice name
    button = telebot.types.KeyboardButton(voice_name)
    voice_buttons.add(button)

# Dictionary to store the user's selected voice
selected_voice = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello! I am a bot for creating voice-overs! Select the voice that will be used for the voice-over:",
                 reply_markup=voice_buttons)


@bot.message_handler(func=lambda message: message.text in [voice.name for voice in voices.voices])
def voice_selected(message):
    user_id = message.from_user.id
    selected_voice[user_id] = message.text
    bot.reply_to(message, f"You have selected the voice: {message.text}. Now enter the text for the voice-over:")


@bot.message_handler(func=lambda message: True)
def generate_voice(message):
    user_id = message.from_user.id
    if user_id in selected_voice:
        # Find voice by name
        voice_name = selected_voice[user_id]
        voice = next(voice for voice in voices.voices if voice.name == voice_name)
        voice_id = voice.voice_id

        # Generate audio with the selected voice using the function from voice.py
        audio_generator = generate_audio(message.text, voice_id)

        # Write audio to a byte stream
        audio_bytes = io.BytesIO()
        for chunk in audio_generator:
            audio_bytes.write(chunk)

        # Save audio to a file and send to the user
        audio_bytes.seek(0)  # Return to the start of the stream
        bot.send_audio(user_id, audio_bytes)

    else:
        bot.reply_to(message, "First select a voice using the /start command")


if __name__ == '__main__':
    bot.polling(none_stop=True)