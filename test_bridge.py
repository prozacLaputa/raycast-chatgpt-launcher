import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit, parse_qs

spec = importlib.util.spec_from_file_location('bridge', Path(__file__).parent/'scripts/ask-chatgpt.py')
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)

class BridgeTests(unittest.TestCase):
    def test_chat_mode_and_exact_prompt(self):
        prompt = '中文 & "引号"\n$(touch /tmp/should-not-exist) # ?'
        query = parse_qs(urlsplit(bridge.chat_url(prompt)).query)
        self.assertEqual(query, {'mode': ['chat'], 'prompt': [prompt]})
    def test_only_opens_link_without_cli_inference(self):
        with patch.object(bridge.subprocess, 'run') as run:
            bridge.run('你好')
        run.assert_called_once_with(['/usr/bin/open', bridge.chat_url('你好')], check=True, stderr=bridge.subprocess.DEVNULL)
    def test_empty_prompt(self):
        with self.assertRaises(ValueError): bridge.run('  ')

if __name__ == '__main__': unittest.main()
