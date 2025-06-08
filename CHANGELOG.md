# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CI/CD pipeline with GitHub Actions (lint, test, Docker build)
- Basic unit tests for server components
- NOTICE file with proper attribution
- Security considerations in .env.example
- Detailed comments in configuration files

### Changed
- Enhanced .env.example with detailed API key descriptions

### Removed
- .DS_Store file from repository

### Security
- Added placeholder for authentication token (implementation pending)
- Documented security risks in NOTICE file

## [0.2.0] - 2025-01-09

### Added
- Docker support with Dockerfile and docker-compose.yml
- Multi-client connectivity (Claude Desktop, Claude Code, Cursor)
- Auto-start functionality for Blender addon
- Helper scripts for Claude Code configuration
- Comprehensive documentation (CLAUDE.md, DOCKER_SETUP_JP.md)
- Screenshot capture capability
- PolyHaven, Sketchfab, and Hyper3D integrations

### Changed
- Server now listens on 0.0.0.0 instead of localhost
- Use environment variables for host/port configuration
- Complete README rewrite with badges and emojis

### Fixed
- Connection issues in multi-client setup
- WSL2 to Windows host connectivity

## [0.1.0] - 2024-12-XX (Original Fork)

### Added
- Initial fork from BlenderGPT
- Model Context Protocol (MCP) integration
- Basic Blender control via Claude AI

[Unreleased]: https://github.com/mackatwentytsuru/blender-mcp/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/mackatwentytsuru/blender-mcp/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/mackatwentytsuru/blender-mcp/releases/tag/v0.1.0