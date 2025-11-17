# Weather MCP Server

A Model Context Protocol (MCP) server that provides weather information using the National Weather Service API. This server offers real-time weather alerts and forecasts for locations in the United States.

## Features

- **Weather Alerts**: Get active weather alerts for any US state using state codes (e.g., CA, NY, TX)
- **Weather Forecasts**: Get detailed weather forecasts for specific locations using latitude/longitude coordinates
- **Real-time Data**: Fetches live data from the National Weather Service API
- **VS Code Integration**: Seamlessly integrates with VS Code through MCP

## Tools Available

### `get_alerts(state: str)`
Retrieve active weather alerts for a US state.

**Parameters:**
- `state`: Two-letter US state code (e.g., "CA" for California, "NY" for New York)

**Example Usage:**
```
What are the current weather alerts in California?
```

### `get_forecast(latitude: float, longitude: float)`
Get weather forecast for a specific location.

**Parameters:**
- `latitude`: Latitude of the location (decimal degrees)
- `longitude`: Longitude of the location (decimal degrees)

**Example Usage:**
```
What's the weather forecast for San Francisco? (37.7749, -122.4194)
```

## Setup and Installation

### Prerequisites

1. **Python 3.12+** installed on your system
2. **UV package manager** installed (`pip install uv` or follow [UV installation guide](https://docs.astral.sh/uv/getting-started/installation/))
3. **VS Code** with MCP support

### Installation Steps

1. **Clone or navigate to the repository:**
   ```bash
   cd /home/dulanj/cube/git/github/mcp-server/weather
   ```

2. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

3. **Configure VS Code MCP settings:**
   
   The MCP configuration should be set up in `.vscode/mcp.json` in the parent directory. Update the configuration with the correct path:
   ```json
   {
     "servers": {
       "weather-mcp-server": {
         "type": "stdio",
         "command": "uv",
         "args": [
           "--directory",
           "/home/dulanj/cube/git/github/mcp-server/weather",
           "run",
           "weather.py"
         ]
       }
     },
     "inputs": []
   }
   ```

4. **Restart VS Code** to load the MCP server configuration

## Usage in VS Code

Once the server is configured and VS Code is restarted:

1. **Ask for weather alerts:**
   - "What are the weather alerts in Texas?"
   - "Show me current weather alerts for CA"

2. **Request weather forecasts:**
   - "What's the weather forecast for New York City?" (you may need to provide coordinates)
   - "Get weather forecast for latitude 34.0522, longitude -118.2437" (Los Angeles)

3. **The AI assistant will automatically:**
   - Use the appropriate MCP tool
   - Fetch real-time data from the National Weather Service
   - Present the information in a readable format

## Testing the Server

You can test the server manually using UV:

```bash
# Navigate to the weather directory
cd /home/dulanj/cube/git/github/mcp-server/weather

# Run the server directly
uv run weather.py
```

## Configuration File Location

The MCP configuration file should be located at:
```
/home/dulanj/cube/git/github/mcp-server/.vscode/mcp.json
```

Make sure this file contains the correct absolute path to your weather server directory.

## Troubleshooting

### Common Issues

1. **"Server not found" error:**
   - Ensure the path in `mcp.json` matches your actual file system path
   - Verify UV is installed and accessible from the command line
   - Restart VS Code after making configuration changes

2. **"No data available" responses:**
   - Check your internet connection
   - Verify the National Weather Service API is accessible
   - Ensure you're using valid US state codes and coordinates

3. **Dependencies not found:**
   - Run `uv sync` in the weather directory
   - Ensure Python 3.12+ is available

### Updating the Configuration

If you move the project to a different location, update the path in `.vscode/mcp.json`:

```json
"args": [
  "--directory",
  "/your/new/path/to/mcp-server/weather",
  "run",
  "weather.py"
]
```

## API Information

This server uses the National Weather Service API:
- **Base URL**: `https://api.weather.gov`
- **Documentation**: [Weather.gov API Documentation](https://www.weather.gov/documentation/services-web-api)
- **Rate Limits**: Generally generous for personal use
- **Coverage**: United States and territories only

## Development

### Project Structure
```
weather/
├── weather.py          # Main MCP server implementation
├── pyproject.toml      # Project dependencies and metadata
└── README.md          # This file
```

### Dependencies
- `httpx`: For making HTTP requests to the weather API
- `mcp`: Model Context Protocol implementation

### Adding New Features

To add new weather-related tools:

1. Create a new function in `weather.py`
2. Decorate it with `@mcp.tool()`
3. Add proper type hints and docstrings
4. Test the functionality
5. Update this README

## Example Queries

Here are some example queries you can try once the server is running:

- "What's the weather like in California?" (will show alerts)
- "Get weather forecast for San Francisco coordinates"
- "Are there any weather alerts in Florida?"
- "Show me the forecast for latitude 40.7128, longitude -74.0060" (New York City)

## License

This project follows the same license as the parent repository.
