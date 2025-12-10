# Tesseract OCR MCP

Tools:
- `ocr_image`: base64-encoded image input
- `ocr_image_from_url`: fetches an image from HTTP/HTTPS

Base64 input:
```json
{
  "method": "call_tool",
  "params": {
    "name": "ocr_image",
    "arguments": {
      "base64_image": "<base64-contents>",
      "language": "eng"
    }
  },
  "jsonrpc": "2.0",
  "id": 1
}
```

URL input:
```json
{
  "method": "call_tool",
  "params": {
    "name": "ocr_image_from_url",
    "arguments": {
      "image_url": "https://example.com/image.png",
      "language": "eng"
    }
  },
  "jsonrpc": "2.0",
  "id": 1
}
```