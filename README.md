# BlenderMCP

[![CI](https://github.com/mackatwentytsuru/blender-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/mackatwentytsuru/blender-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Blender 3.0+](https://img.shields.io/badge/blender-3.0+-orange.svg)](https://www.blender.org/)
[![Security Policy](https://img.shields.io/badge/security-policy-red.svg)](SECURITY.md)

Model Context Protocol server for controlling Blender 3D via AI assistants (Claude Desktop, Claude Code, Cursor).

⚠️ **Security Warning**: This software executes arbitrary Python code. See [SECURITY.md](SECURITY.md) for details.

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Claude    │     │   Claude    │     │   Cursor    │
│   Desktop   │     │    Code     │     │             │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                     │
       └───────────────────┴─────────────────────┘
                           │
                    ┌──────▼──────┐
                    │ MCP Server  │ (Port: stdio)
                    │   (Docker)  │
                    └──────┬──────┘
                           │ TCP Socket
                    ┌──────▼──────┐
                    │   Blender   │ (Port: 9876)
                    │    Addon    │
                    └─────────────┘
```

## Quick Start

### Prerequisites

- Blender 3.0+
- Python 3.10-3.12
- Docker (optional, recommended)
- One of: Claude Desktop, Claude Code, or Cursor

### Installation

#### Option 1: Docker (Recommended)

```bash
git clone https://github.com/mackatwentytsuru/blender-mcp.git
cd blender-mcp
docker-compose up -d
```

#### Option 2: Local Installation

```bash
git clone https://github.com/mackatwentytsuru/blender-mcp.git
cd blender-mcp
pip install -e .  # or use uv: uv pip install -e .
```

### Blender Addon Setup

1. Install addon:
   - Edit → Preferences → Add-ons → Install
   - Select `addon.py`
   - Enable "BlenderMCP" addon
2. Server auto-starts on Blender launch (port 9876)

### Client Configuration

#### Claude Desktop (Windows)

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

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

#### Claude Code (WSL2)

Per-project configuration:
```bash
claude mcp add blender-mcp docker exec -i blender-mcp-server blender-mcp
```

#### Cursor

Add to MCP settings:
```json
{
  "blender-mcp": {
    "command": "docker",
    "args": ["exec", "-i", "blender-mcp-server", "blender-mcp"]
  }
}
```

## API Reference

### Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `execute_blender_code` | Execute Python code in Blender | `code: str` |
| `get_scene_info` | Get current scene information | None |
| `get_object_info` | Get object details | `object_name: str` |
| `get_viewport_screenshot` | Capture viewport | `width: int, height: int` |

### Environment Variables

```bash
# Connection settings
BLENDER_HOST=localhost    # Host where Blender is running
BLENDER_PORT=9876        # Port for socket connection

# API keys (optional)
POLYHAVEN_API_KEY=       # For asset downloads
SKETCHFAB_API_KEY=       # For model search
HYPER3D_API_KEY=         # For AI generation

# Security (not yet implemented)
MCP_AUTH_TOKEN=          # Authentication token
```

## Security Considerations

**Current security issues:**
1. No authentication on socket connection
2. Arbitrary code execution without sandboxing
3. Listens on all interfaces (0.0.0.0)

**Mitigations:**
- Use firewall to restrict access
- Run in isolated environment
- Only use with trusted AI clients
- See [SECURITY.md](SECURITY.md) for details

## Development

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"  # or: uv pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run linting
ruff check src/
mypy src/
```

### Docker Development

```bash
# Build image
docker build -t blender-mcp:dev .

# Run with live code reload
docker run -v $(pwd)/src:/app/src blender-mcp:dev

# View logs
docker logs -f blender-mcp-server
```

## Troubleshooting

### Connection Refused

1. Check Blender addon is enabled and running
2. Verify port 9876 is not blocked by firewall
3. For Docker: ensure container can reach host

### WSL2 Issues

- Windows host IP may change on restart
- Check with: `ip route | grep default | awk '{print $3}'`
- Update `BLENDER_HOST` environment variable

### Performance

- Large operations block other clients
- Viewport screenshots are base64 encoded (size overhead)
- Complex scenes may timeout

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Add tests for new functionality
4. Ensure CI passes
5. Submit Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) file.

Based on [BlenderGPT](https://github.com/gd3kr/BlenderGPT) by gd3kr.
See [NOTICE](NOTICE) for third-party attributions.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Support

- Issues: [GitHub Issues](https://github.com/mackatwentytsuru/blender-mcp/issues)
- Security: See [SECURITY.md](SECURITY.md)
- Documentation: [Wiki](https://github.com/mackatwentytsuru/blender-mcp/wiki)