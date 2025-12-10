from __future__ import annotations

import base64
import tempfile
from pathlib import Path

import httpx
import pytesseract
from fastmcp import FastMCP
from PIL import Image

mcp = FastMCP("tesseract-ocr")

def _write_temp_image(data: bytes, suffix: str = ".img") -> Path:
    """Persist raw image bytes to a temp file and return the path."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    tmp.write(data)
    tmp.flush()
    tmp.close()
    return Path(tmp.name)


def decode_image(base64_image: str) -> Path:
    """Decode base64 image bytes into a temp file and return its path."""
    data = base64.b64decode(base64_image, validate=True)
    return _write_temp_image(data)


async def download_image(image_url: str) -> Path:
    """Download an image from a URL into a temp file and return its path."""
    async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
        response = await client.get(image_url)
        response.raise_for_status()
        data = response.content

    suffix = Path(image_url).suffix or ".img"
    return _write_temp_image(data, suffix=suffix)

@mcp.tool()
async def ocr_image_from_base64(base64_image: str, language: str = "eng") -> str:
    """Run OCR on a base64-encoded image using Tesseract.
    
    Args:
        base64_image: Base64-encoded image
        language: Language code for Tesseract (default: "eng")

    Returns:
        Text extracted from the image
    """
    img_path = decode_image(base64_image)
    try:
        with Image.open(img_path) as img:
            text = pytesseract.image_to_string(img, lang=language)
            return text.strip() or "No text detected."
    except (OSError, pytesseract.TesseractError) as exc:
        return f"OCR failed: {exc}"
    finally:
        try:
            img_path.unlink(missing_ok=True)
        except OSError:
            pass


@mcp.tool()
async def ocr_image_from_url(image_url: str, language: str = "eng") -> str:
    """Run OCR on an image fetched from a URL using Tesseract.
    
    Args:
        image_url: HTTP/HTTPS URL pointing to an image.
        language: Language code for Tesseract (default: "eng")

    Returns:
        Text extracted from the image
    """
    try:
        img_path = await download_image(image_url)
    except httpx.HTTPError as exc:
        return f"Image download failed: {exc}"

    try:
        with Image.open(img_path) as img:
            text = pytesseract.image_to_string(img, lang=language)
            return text.strip() or "No text detected."
    except (OSError, pytesseract.TesseractError) as exc:
        return f"OCR failed: {exc}"
    finally:
        try:
            img_path.unlink(missing_ok=True)
        except OSError:
            pass


def main():
    mcp.run()

if __name__ == "__main__":
    main()