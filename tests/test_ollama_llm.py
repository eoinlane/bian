import unittest
from unittest.mock import patch
import requests
from ollama_llm import OllamaLLM  # Assuming the Ollama LLM class is in ollama_llm.py

class TestOllamaLLM(unittest.TestCase):

    @patch('requests.post')
    def test_generate_response(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"text": "Sample response text"}

        llm = OllamaLLM(model="llama3")
        response = llm.generate("What is the meaning of life?")
        
        self.assertEqual(response, "Sample response text")
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
