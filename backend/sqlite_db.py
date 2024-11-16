import logging
import os
from time import time
from uuid import UUID, uuid4
from sqlalchemy import Engine, create_engine, insert, or_, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine: Engine | None = None
log = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass

class Transcription(Base):
    __tablename__ = "transcriptions"
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    audio_file_name: Mapped[str]
    transcribed_text: Mapped[str]
    created_timestamp: Mapped[int]

def get_engine():
    global engine
    if not engine:
        try:
            engine = create_engine(f'sqlite:///{os.getenv("SQLITE_FILEPATH", "default.db")}')
        except Exception as e:
            log.error("whisper load model error: %s", e)
    return engine

def write(audio_file_name, transcribed_text):
    engine = get_engine()
    if not engine:
        return "FAIL"
    with engine.connect() as connection:
        connection.execute(insert(Transcription),[{
            "uuid" : uuid4(),
            "audio_file_name":audio_file_name,
            "transcribed_text":transcribed_text,
            "created_timestamp":int(time())
        }])
        connection.commit()
    return "OK"

def get_all():
    engine = get_engine()
    with engine.connect() as connection:
        return connection.execute(select(Transcription)).all()

def search(fts_text:str):
    engine = get_engine()
    with engine.connect() as connection:
        return connection.execute(
            select(Transcription).where(
                or_(
                    Transcription.audio_file_name.match(fts_text), 
                    Transcription.transcribed_text.match(fts_text)
                )
            )
        ).all()
    