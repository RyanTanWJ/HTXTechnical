import unittest
from unittest.mock import MagicMock, patch
import whisper_tiny

class TestWhisperTiny(unittest.TestCase):

    def setUp(self) -> None:
        whisper_tiny.model = None
        return super().setUp()
    
    @patch("whisper_tiny.whisper")
    def test_get_model(self, whisper:MagicMock):
        self.assertIsNone(whisper_tiny.model)
        model = whisper_tiny.get_model()
        self.assertIs(model, whisper_tiny.model)
        whisper.load_model.assert_called_once()
    
    @patch("whisper_tiny.whisper")
    def test_transcribe(self, whisper:MagicMock):
        whisper_tiny.transcribe("a.mp3")
        whisper_tiny.model.transcribe.assert_called_once_with("a.mp3")

if __name__ == '__main__':
    unittest.main()