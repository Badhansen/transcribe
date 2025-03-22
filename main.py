import ffmpeg
import whisper
import torch

def extract_audio(video_path, audio_path):
    try:
        ffmpeg.input(video_path).output(audio_path).run()
    except Exception as e:
        print("Error extracting audio: {e}")

def transcribe_audio(audio_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = whisper.load_model("base").to(device)
    result = model.transcribe(audio_path)
    with open("transcript.txt", "w") as f:
        f.write(result["text"])

if __name__ == "__main__":
    video_path = "Eminem 'Guinness World Record' _100 Words in 16 Seconds_ Rap God Live YouTube Awards.mp4"
    audio_path = "audio.wav"
    extract_audio(video_path, audio_path)
    transcribe_audio(audio_path)
