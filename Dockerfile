FROM python:3.10-slim

WORKDIR /app

# Install uv package manager
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY src/ ./src/
COPY main.py .

# Install dependencies
RUN uv pip install --system -e .

# Run the MCP server directly
CMD ["blender-mcp"]