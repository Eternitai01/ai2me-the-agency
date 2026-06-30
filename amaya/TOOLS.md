# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Image Analysis

**Primary Method:** Qwen 3.7 Max supports vision natively via the `image` tool.

**Usage:**
```bash
image tool with model=qwen/qwen3.7-max
```

**Fallback Method:** Direct Anthropic API calls with Claude Sonnet 4-6 when needed.

**Working Python script for image analysis:**

```python
import base64
import json
import subprocess
import urllib.request

# Read image
with open('/path/to/image.jpg', 'rb') as f:
    image_data = base64.standard_b64encode(f.read()).decode('utf-8')

# Get API key from config
result = subprocess.run(['grep', '-A', '5', '"anthropic"', '/data/.openclaw/openclaw.json'], 
                       capture_output=True, text=True)
api_key = [line for line in result.stdout.split('\n') if 'apiKey' in line][0].split('"')[3]

payload = {
    "model": "claude-sonnet-4-6",
    "max_tokens": 2000,
    "messages": [{
        "role": "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": image_data
            }
        }, {
            "type": "text",
            "text": "Extract ALL text visible in this image. Include every word, number, heading, and piece of text exactly as shown."
        }]
    }]
}

req = urllib.request.Request(
    'https://api.anthropic.com/v1/messages',
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'x-api-key': api_key,
        'anthropic-version': '2023-06-01'
    }
)

with urllib.request.urlopen(req, timeout=30) as response:
    result = json.loads(response.read().decode('utf-8'))
    print(result['content'][0]['text'])
```

**Available Anthropic Vision Models:**
- claude-sonnet-4-6 ✅ (supports image_input + pdf_input)
- claude-opus-4-6 ✅ (supports image_input + pdf_input)
- claude-opus-4-7 ✅ (supports image_input + pdf_input)
- claude-sonnet-4-5-20250929 ✅ (supports image_input + pdf_input)
- claude-haiku-4-5-20251001 ✅ (supports image_input + pdf_input)

**Never say "I can't see images" again.** Use this Python script method when the `image` tool fails due to auth issues.

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)
