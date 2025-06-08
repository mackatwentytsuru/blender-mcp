# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

BlenderMCP is a Model Context Protocol (MCP) server that enables Claude to control Blender 3D software through a socket-based communication system. The project consists of an MCP server that Claude connects to and a Blender addon that receives and executes commands.

## Development Commands

### Standard Installation
```bash
# Install dependencies (requires uv package manager)
uv pip install -e .

# Run the MCP server
blender-mcp

# The server runs on stdio by default for MCP communication
```

### Docker Installation (Recommended for Multi-Client Setup)
```bash
# Build and start the Docker container
docker-compose up -d

# View logs
docker logs -f blender-mcp-server

# Stop the container
docker-compose down

# Test the connection
docker exec -i blender-mcp-server blender-mcp
```

## Docker Configuration

When running in Docker, the server uses environment variables for Blender connection:
- `BLENDER_HOST`: Host address where Blender is running (default: localhost)
- `BLENDER_PORT`: Port for Blender socket connection (default: 9876)

For WSL2/Windows setup, use the Windows host IP (typically 172.31.32.1) to connect from Docker to Blender running on Windows.

## Multi-Client Configuration

BlenderMCP supports multiple Claude clients simultaneously:

### Claude Desktop (Windows/macOS)
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

### Claude Code (WSL2)
Due to a known issue with global settings, use project-specific configuration:
```bash
# Add to current project
claude mcp add blender-mcp docker exec -i blender-mcp-server blender-mcp

# Or use the helper script
~/mcp設定ツール/add-blender-mcp.sh
```

### Cursor
Add to MCP Servers settings in Cursor preferences.

## Architecture

### Three-Layer System with Docker:
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

### Two-Component System:
1. **MCP Server** (`src/blender_mcp/server.py`): Handles Claude's requests via MCP protocol
2. **Blender Addon** (`addon.py`): Runs inside Blender, receives commands via TCP socket (port 9876)

### Communication Flow:
- Claude → MCP Server (stdio/MCP protocol)
- MCP Server → Blender Addon (TCP socket with JSON messages)
- Commands are executed in Blender's main thread for thread safety

### Key Patterns:
- Tools are registered using `@mcp.tool()` decorator in server.py
- Global connection state managed via `_blender_connection` variable
- All Blender operations go through `send_command_to_blender()` function
- Blender addon uses timer-based execution to ensure thread safety
- Docker container handles multi-client connections seamlessly

## Important Implementation Details

### Adding New Tools:
1. Add tool method in `server.py` with `@mcp.tool()` decorator
2. Implement corresponding command handler in `addon.py`'s `execute_command()` function
3. Tools should return structured data (dicts/lists) that serialize to JSON

### Error Handling:
- Connection errors should be caught and return user-friendly messages
- Blender exceptions are caught in addon and returned as error responses
- Use `ConnectionError` for connection issues, generic exceptions for other errors

### Testing Changes:
1. Reload the Blender addon after changes to `addon.py`
2. Restart the MCP server after changes to `server.py`
3. Test socket connection using the "Test Connection" button in Blender's UI panel

## Testing and Debugging

### Docker Environment Testing:
```bash
# Check if container is running
docker ps | grep blender-mcp

# Test direct execution
docker exec -i blender-mcp-server blender-mcp

# View real-time logs
docker logs -f blender-mcp-server

# Check environment variables
docker exec blender-mcp-server env | grep BLENDER

# Restart container after changes
docker-compose restart
```

### Common Issues:
1. **Connection Refused**: Ensure Blender addon is set to listen on 0.0.0.0 instead of localhost
2. **WSL2 IP Changes**: The Windows host IP may change; check with `ip route | grep default`
3. **Multiple Clients**: Docker handles concurrent connections automatically

## External Integrations

The project supports optional integrations with:
- **PolyHaven**: Environment maps and materials (free, no API key needed)
- **Sketchfab**: 3D model downloads (requires API key)
- **Hyper3D**: AI model generation (requires API key)

API keys are stored in environment variables and passed through the MCP server configuration.

## Running Commands

When running BlenderMCP in Docker, always ensure:
1. The Docker container is running: `docker ps`
2. Blender is open with the addon enabled and auto-started
3. Test connection using: `docker exec -i blender-mcp-server blender-mcp`

For development, you can run these commands to verify the setup:
```bash
# Lint and type checking (if available)
# npm run lint
# npm run typecheck

# Docker health check
docker-compose ps
```