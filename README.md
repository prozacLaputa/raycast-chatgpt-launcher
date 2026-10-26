# Raycast ChatGPT Launcher

简体中文 | [English](README_EN.md)

从 Raycast 打开桌面应用的 **ChatGPT 模式**，并把问题填入新聊天。适合随手提问，不需要选择项目或工作区。

```text
唤起 Raycast → 输入问题 → 问 ChatGPT → 应用中回车发送
```

这是一个很小的 Python Script Command，无第三方 Python 依赖、无后台服务、无 API Key。

## 安装

需要 macOS、Raycast、Python 3，以及支持 `codex://new?mode=chat` 的 ChatGPT 桌面应用。此深链接已在开发者本机实测；其他版本是否支持需要自行确认。它不是 OpenAI 或 Raycast 官方插件。

1. 下载本仓库 ZIP 并解压，或运行：

   ```sh
   git clone https://github.com/prozacLaputa/raycast-chatgpt-launcher.git
   cd raycast-chatgpt-launcher
   chmod +x scripts/ask-chatgpt.py
   python3 --version
   ```

2. 在 Raycast Settings → Extensions → Script Commands → Add Directories 中添加本项目的 `scripts` 目录。
3. 搜索「问 ChatGPT」，按 Tab 输入问题，再按回车。
4. 可选：在 Manage Fallback Commands 中启用「问 ChatGPT」，将它移到第一位。这样输入没有匹配其他命令的问题时，回车就会打开聊天。

不同 Raycast 版本的设置位置可能有所不同。如果提示找不到 Python，请安装 Python 3，并确认 Raycast 的运行环境能找到 `python3`。

## 行为与边界

- 使用 `codex://new?mode=chat&prompt=...`；`codex://` 是桌面应用的协议名，`mode=chat` 才是目标模式。
- **只打开并预填，不自动发送。** 不调用 Codex CLI，不创建 Codex 编程任务。
- 不传工作区或项目参数，不读取或修改项目文件。
- 脚本不主动保存问题、回答或日志；失败信息不回显完整问题 URL。
- **不是无痕模式**：Raycast、macOS 和 ChatGPT 仍可能保留自身的历史；不会自动开启临时聊天或删除记录。
- URL 编码保留中文、换行和特殊字符；问题作为进程参数传递，不拼接为 shell 命令。
- 超长文本仍受系统 URL/参数长度限制；大段材料建议直接粘贴到应用中。

## 开发与验证

```sh
python3 -B test_bridge.py
```

测试覆盖模式与文本编码、仅调用链接打开、拒绝空问题。真实跳转已由本机用户验证；自动化测试不代替跨版本界面兼容测试。

## 卸载

在 Raycast 中移除 Script Directory 或禁用「问 ChatGPT」的 Fallback。已有 ChatGPT 聊天不会被删除。

## 许可证

[MIT](LICENSE)
