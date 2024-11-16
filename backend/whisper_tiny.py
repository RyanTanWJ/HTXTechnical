import logging
import whisper

model: whisper.Whisper | None = None
log = logging.getLogger(__name__)

def get_model():
    global model
    if not model:
        try:
            model = whisper.load_model("tiny")
        except Exception as e:
            log.error("whisper load model error: %s", e)
    return model

def transcribe(audio_file:str):
    model = get_model()
    if not model:
        return None
    result = model.transcribe(audio_file)
    return result #["text"]