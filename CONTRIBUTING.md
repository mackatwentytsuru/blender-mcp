# Contributing to BlenderMCP

Thank you for your interest in contributing to BlenderMCP! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive criticism

## How to Contribute

### Reporting Issues

1. Check existing issues first
2. Use issue templates
3. Include:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details

### Submitting Changes

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR-USERNAME/blender-mcp.git
   cd blender-mcp
   ```

2. **Create Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Setup Development Environment**
   ```bash
   # Using uv (recommended)
   uv pip install -e ".[dev]"
   
   # Or using pip
   pip install -e ".[dev]"
   ```

4. **Make Changes**
   - Follow existing code style
   - Add tests for new features
   - Update documentation

5. **Run Tests**
   ```bash
   # Lint
   ruff check src/ tests/
   ruff format src/ tests/
   
   # Type check
   mypy src/
   
   # Unit tests
   pytest tests/ -v
   ```

6. **Commit**
   ```bash
   git add .
   git commit -m "feat: describe your changes"
   ```
   
   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation
   - `test:` Tests
   - `refactor:` Code refactoring
   - `chore:` Maintenance

7. **Push & PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create Pull Request on GitHub.

## Development Guidelines

### Code Style

- Use `ruff` for linting and formatting
- Follow PEP 8
- Type hints are encouraged
- Docstrings for public functions

### Testing

- Write tests for new features
- Maintain test coverage
- Test edge cases
- Mock external dependencies

### Documentation

- Update README if needed
- Add docstrings
- Update CHANGELOG.md
- Include examples

### Security

- Never commit secrets
- Validate user input
- Follow security guidelines in SECURITY.md
- Report vulnerabilities privately

## Pull Request Process

1. Update documentation
2. Add tests
3. Ensure CI passes
4. Request review
5. Address feedback
6. Maintainer merges

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create git tag
4. GitHub Actions builds release

## Questions?

- Open an issue
- Discuss in PR
- Check wiki

Thank you for contributing! 🎉