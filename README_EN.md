# Raycast ChatGPT Launcher

[简体中文](README.md) | English

Open the desktop app in **ChatGPT mode** with a question prefilled in a new chat. A lightweight entry point for everyday questions, without selecting a project or workspace.

```text
Open Raycast → type a question → Ask ChatGPT → press Enter in the app to send
```

A small Python Script Command with no third-party Python dependencies, background service, or API key.

## Install

Requires macOS, Raycast, Python 3, and a ChatGPT desktop app supporting `codex://new?mode=chat`. The link was tested on the developer’s machine; compatibility with other versions is not guaranteed. This is not an official OpenAI or Raycast extension.

1. Download and extract this repository’s ZIP, or run:

   ```sh
   git clone https://github.com/prozacLaputa/raycast-chatgpt-launcher.git
   cd raycast-chatgpt-launcher
   chmod +x scripts/ask-chatgpt.py
   python3 --version
   ```

2. In Raycast Settings → Extensions → Script Commands → Add Directories, select this project’s `scripts` folder.
3. Search for the command **问 ChatGPT**, press Tab to enter your question, then Enter.
4. Optionally enable it in Manage Fallback Commands and move it to the top. Queries that do not match another command can then open the chat with Enter.

Settings locations vary by Raycast version. If Python is missing, install Python 3 and ensure `python3` is available in Raycast’s execution environment.

## Behavior and limits

- Opens `codex://new?mode=chat&prompt=...`. The scheme belongs to the desktop app; `mode=chat` selects ChatGPT.
- **Prefills only; does not send automatically.** No Codex CLI invocation or Codex coding task creation.
- Does not pass workspace/project parameters or read/write project files.
- Does not explicitly save prompts, answers, or logs. Errors do not echo the full prompt URL.
- **Not an incognito mode.** Raycast, macOS, and ChatGPT may retain their own history. The script does not enable temporary chats or delete history.
- URL encoding preserves Unicode, newlines, and special characters. Input is passed as data, never interpolated into shell code.
- Very long text remains subject to OS URL/argument limits; paste large documents directly into the app.

## Development

```sh
python3 -B test_bridge.py
```

Tests cover mode/text encoding, opening only the deep link, and empty-input rejection. A local user verified the real app transition; unit tests do not establish compatibility across app versions.

## Uninstall

Remove the Script Directory or disable its fallback in Raycast. Existing ChatGPT conversations are not deleted.

## License

[MIT](LICENSE)
