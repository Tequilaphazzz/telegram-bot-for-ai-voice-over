from elevenlabs import Voice, VoiceSettings
from elevenlabs.client import ElevenLabs
import config

client = ElevenLabs(api_key=config.elevenlabs_api_key)

# Function to get all voices
def get_all_voices():
    voices = client.voices.get_all()
    return voices

# Function to generate audio
def generate_audio(text: str, voice_id: str):
    audio = client.generate(
        text=text,
        voice=Voice(
            voice_id=voice_id,
            settings=VoiceSettings(stability=0.75, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        ),
        model="eleven_multilingual_v2"
    )
    return audio