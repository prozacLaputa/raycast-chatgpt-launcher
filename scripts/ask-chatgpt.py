#!/usr/bin/env python3
# @raycast.schemaVersion 1
# @raycast.title 问 ChatGPT
# @raycast.mode silent
# @raycast.packageName ChatGPT
# @raycast.icon 💬
# @raycast.argument1 {"type":"text","placeholder":"输入问题，打开 ChatGPT"}
# @raycast.description 打开 ChatGPT 模式并填入问题；目前需要在应用中回车发送。

"""Open the ChatGPT composer without invoking the Codex inference backend."""
import subprocess
import sys
from urllib.parse import urlencode, quote


def chat_url(prompt):
    if not prompt.strip():
        raise ValueError('请输入问题。')
    return 'codex://new?' + urlencode({'mode': 'chat', 'prompt': prompt}, quote_via=quote)


def run(prompt, opener=None):
    url = chat_url(prompt)
    if opener is None:
        subprocess.run(['/usr/bin/open', url], check=True, stderr=subprocess.DEVNULL)
    else:
        opener(url)
    return url


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('请输入一个问题。')
        run(sys.argv[1])
    except ValueError as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
    except (OSError, subprocess.CalledProcessError):
        print('未能打开 ChatGPT，请确认桌面应用已安装。', file=sys.stderr)
        sys.exit(1)
