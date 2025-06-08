# 🎨 BlenderMCP - AI-Powered 3D Creation Assistant

<div align="center">

![BlenderMCP](assets/hammer-icon.png)

**🤖 Claude × 🎮 Blender = ∞ Creative Possibilities**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Blender](https://img.shields.io/badge/Blender-3.0%2B-orange.svg)](https://www.blender.org/)
[![MCP](https://img.shields.io/badge/MCP-Protocol-green.svg)](https://modelcontextprotocol.io/)

[English](#english) | [日本語](#japanese)

</div>

---

<a name="english"></a>
## 🌟 What is BlenderMCP?

BlenderMCP is a revolutionary bridge that connects Claude AI (Desktop, Code, Cursor) with Blender 3D software through the Model Context Protocol (MCP). Create, modify, and manipulate 3D scenes using natural language! 🚀

### ✨ Key Features

- 🎯 **Multi-Client Support**: Works with Claude Desktop, Claude Code, and Cursor
- 🐳 **Docker Support**: Easy deployment and consistent environment
- 🌐 **Cross-Platform**: Windows, macOS, Linux (with WSL2 support)
- 🔄 **Auto-Start**: Server starts automatically when Blender launches
- 🎨 **Asset Integration**: PolyHaven, Sketchfab, and Hyper3D support
- 📸 **Viewport Screenshots**: Capture and share your 3D views
- 🔧 **Full Python Access**: Execute any Blender Python code

### 🎬 Quick Demo

<details>
<summary>📹 Watch Video Demos</summary>

- [Basic Usage](https://github.com/user-attachments/assets/example1.mp4)
- [Advanced Features](https://github.com/user-attachments/assets/example2.mp4)
- [Docker Setup](https://github.com/user-attachments/assets/example3.mp4)

</details>

## 🚀 Getting Started

### Prerequisites

- 🎮 Blender 3.0 or newer
- 🐍 Python 3.10+
- 🐳 Docker (for Docker setup)
- 🤖 Claude Desktop/Code/Cursor

### 🎯 Quick Install

#### Option 1: Standard Installation

```bash
# Clone the repository
git clone https://github.com/your-username/blender-mcp.git
cd blender-mcp

# Install dependencies
pip install -e .
```

#### Option 2: Docker Installation (Recommended) 🐳

```bash
# Clone and navigate
git clone https://github.com/your-username/blender-mcp.git
cd blender-mcp

# Start with Docker Compose
docker-compose up -d
```

### 📦 Blender Addon Installation

1. Download `addon.py` from this repository
2. In Blender: Edit → Preferences → Add-ons → Install
3. Select the downloaded `addon.py` file
4. Enable "BlenderMCP" addon ✅
5. The server now auto-starts with Blender! 🎉

## 🔧 Configuration

### 🖥️ Claude Desktop

<details>
<summary>Windows Configuration</summary>

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "blender-mcp": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

For Docker setup:
```json
{
  "mcpServers": {
    "blender-mcp": {
      "command": "wsl",
      "args": ["-e", "docker", "exec", "-i", "blender-mcp-server", "blender-mcp"]
    }
  }
}
```

</details>

<details>
<summary>macOS Configuration</summary>

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "blender-mcp": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

</details>

### 💻 Claude Code

For global configuration, add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "blender-mcp": {
      "type": "stdio",
      "command": "docker",
      "args": ["exec", "-i", "blender-mcp-server", "blender-mcp"]
    }
  }
}
```

Or use the helper script:
```bash
~/mcp設定ツール/add-blender-mcp.sh
```

### 🎯 Cursor

Add to Cursor settings → MCP Servers:

```json
{
  "blender-mcp": {
    "command": "uvx",
    "args": ["blender-mcp"]
  }
}
```

## 🎨 Usage Examples

### Basic Commands

```
👤: Create a red cube
🤖: I'll create a red cube for you...

👤: Add lighting to the scene
🤖: Adding three-point lighting setup...

👤: Take a screenshot
🤖: Here's the current viewport...
```

### Advanced Examples

```python
# Create animated scene
👤: Create a spinning galaxy of cubes

# Import assets
👤: Download and add a tree model from PolyHaven

# Complex operations
👤: Create a procedural material with noise texture
```

## 🌟 Enhanced Features

### 🌍 PolyHaven Integration
- Search and download HDRIs, textures, and models
- Automatic material setup
- One-command asset import

### 🎭 Sketchfab Support
- Search millions of 3D models
- Direct import with materials
- API key management

### 🤖 Hyper3D AI Generation
- Text-to-3D model generation
- Image-to-3D conversion
- Real-time preview

## 🐳 Docker Deployment

### Multi-Client Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Claude    │     │   Claude    │     │   Cursor    │
│   Desktop   │     │    Code     │     │             │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                     │
       └───────────────────┴─────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   Docker    │
                    │ MCP Server  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Blender   │
                    │   (0.0.0.0) │
                    └─────────────┘
```

### 🚀 Quick Docker Setup

1. **Start the container**:
   ```bash
   docker-compose up -d
   ```

2. **Configure your client** (see configuration section above)

3. **Start creating!** 🎨

## 🛠️ Troubleshooting

<details>
<summary>Connection Issues</summary>

- Ensure Blender addon is enabled and server is running
- Check firewall settings for port 9876
- For Docker: verify container is running with `docker ps`

</details>

<details>
<summary>WSL2 Specific</summary>

- Use the provided scripts in `~/mcp設定ツール/`
- Check Windows firewall allows WSL2 connections
- Verify Docker Desktop WSL2 integration is enabled

</details>

## 🤝 Contributing

We love contributions! Whether you're fixing bugs, adding features, or improving documentation, your help is welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original [BlenderGPT](https://github.com/gd3kr/BlenderGPT) by gd3kr
- [Model Context Protocol](https://modelcontextprotocol.io/) team
- The amazing Blender community 🎨

## 📞 Support

- 📧 Issues: [GitHub Issues](https://github.com/your-username/blender-mcp/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-username/blender-mcp/discussions)
- 📖 Documentation: [Wiki](https://github.com/your-username/blender-mcp/wiki)

---

<a name="japanese"></a>
## 🌟 BlenderMCPとは？

BlenderMCPは、Model Context Protocol (MCP)を通じてClaude AI（Desktop、Code、Cursor）とBlender 3Dソフトウェアを接続する革新的なブリッジです。自然言語で3Dシーンを作成、修正、操作できます！🚀

### ✨ 主な機能

- 🎯 **マルチクライアント対応**: Claude Desktop、Claude Code、Cursor対応
- 🐳 **Docker対応**: 簡単なデプロイと一貫した環境
- 🌐 **クロスプラットフォーム**: Windows、macOS、Linux（WSL2対応）
- 🔄 **自動起動**: Blender起動時にサーバーが自動的に開始
- 🎨 **アセット統合**: PolyHaven、Sketchfab、Hyper3D対応
- 📸 **ビューポートスクリーンショット**: 3Dビューのキャプチャと共有
- 🔧 **完全なPythonアクセス**: あらゆるBlender Pythonコードを実行

### 使い方の例

```
👤: 赤い立方体を作って
🤖: 赤い立方体を作成します...

👤: シーンに照明を追加して
🤖: 3点照明のセットアップを追加します...

👤: スクリーンショットを撮って
🤖: 現在のビューポートです...
```

詳細な日本語のセットアップガイドは[DOCKER_SETUP_JP.md](DOCKER_SETUP_JP.md)をご覧ください。

---

<div align="center">

**Made with ❤️ by the Creative Community**

🎨 Happy Blending! 🚀

</div>