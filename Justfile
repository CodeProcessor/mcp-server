[private]
default:
    @echo "Available commands:"
    @just --list


# Run the weather MCP server (port 8008)
run-weather:
    cd weather && uv run fastmcp run weather.py:mcp --transport http --port 8008 --host 0.0.0.0

# Run the Tesseract OCR MCP server (port 8010)
run-ocr:
    cd tesseract-ocr && uv run fastmcp run ocr.py:mcp --transport http --port 8010 --host 0.0.0.0