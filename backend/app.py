
import sqlite_db
import tempfile
import whisper_tiny
from flask import Flask, request, Response

app = Flask(__name__)

@app.get("/health")
def health():
    return {
        "whisper_tiny":"FAIL" if not whisper_tiny.get_model() else "OK",
        "sqlite_db":"FAIL" if not sqlite_db.get_engine() else "OK"
    }, {'Access-Control-Allow-Origin':'*'}

@app.post("/transcribe")
def transcribe():
    resp = dict()
    for key, file in request.files.items():
        with tempfile.NamedTemporaryFile() as fp:
            file.save(fp)
            transc_res = whisper_tiny.transcribe(fp.name)
            if not transc_res:
                resp[key] = "FAIL"
                continue
            resp[key] = sqlite_db.write(file.filename, transc_res["text"])
    return resp, {'Access-Control-Allow-Origin':'*'}

@app.get("/transcriptions")
def transcriptions():
    return [{"audio_filename":res[1],"transcription":res[2]}for res in sqlite_db.get_all()], {'Access-Control-Allow-Origin':'*'}

@app.get("/search")
def search():
    return [{"audio_filename":res[1],"transcription":res[2]}for res in sqlite_db.search(request.args.get('search'))], {'Access-Control-Allow-Origin':'*'}
