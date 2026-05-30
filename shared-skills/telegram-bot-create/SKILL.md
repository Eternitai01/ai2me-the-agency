---
name: telegram-bot-create
description: Create a new Telegram bot via BotFather programmatically — no human interaction needed. Uses Dante's VPS (72.62.26.150) Pyrogram user session to automate the BotFather conversation. Use when asked to create a Telegram bot for a new agent, customer, or feature without Carlos doing anything manually.
---

# Telegram Bot Create

Creates a new Telegram bot via BotFather using a Pyrogram MTProto user session on Dante's VPS. No manual steps required.

## How It Works

`scripts/create-bot.py` runs on Dante's VPS using a pre-authorized Pyrogram session string. It messages BotFather, handles the `/newbot` flow, and returns the token as JSON.

## Prerequisites

- SSH access to Dante's VPS: `ssh -i ~/.ssh/dante_vps root@72.62.26.150`
- Credentials already set on VPS — see `references/credentials.md`

## Workflow

### 1. Run the script on Dante's VPS

```bash
ssh -i ~/.ssh/dante_vps -o StrictHostKeyChecking=no root@72.62.26.150 "
cd /root/.openclaw/workspace-dante
TELEGRAM_API_ID=30969438 \
TELEGRAM_API_HASH=1d6085f2ca1d4a38ddef470b70682eea \
TELEGRAM_SESSION='<session_string>' \
python3 create-bot.py 'Bot Display Name' 'bot_username_bot'
"
```

Returns:
```json
{"success": true, "token": "1234567890:AAB...", "username": "bot_username_bot", "display_name": "Bot Display Name"}
```

If `success: false`, check `error` field — common issues: flood wait, username taken, session expired.

### 2. Configure the bot

```bash
TOKEN="<token from above>"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/setMyDescription" -d "description=<desc>"
curl -s -X POST "https://api.telegram.org/bot$TOKEN/setMyShortDescription" -d "short_description=<short>"
curl -s -X POST "https://api.telegram.org/bot$TOKEN/setMyCommands" \
  -H "Content-Type: application/json" \
  -d '{"commands":[{"command":"start","description":"Start"},{"command":"help","description":"Help"}]}'
```

### 3. Wire to OpenClaw

```bash
echo '{
  "channels": {
    "telegram": {
      "accounts": {
        "<account-key>": {
          "name": "<Display Name>",
          "enabled": true,
          "dmPolicy": "open",
          "botToken": "<token>",
          "allowFrom": ["*"],
          "groupPolicy": "allowlist"
        }
      }
    }
  }
}' > /tmp/patch.json && openclaw config patch --file /tmp/patch.json
```

Then restart: gateway restart.

### 4. Wire to agent (if needed)

In `openclaw.json` agents array, set `accountId` on the agent to match the account key above.

## Error Handling

- **Flood wait**: BotFather is rate-limiting — wait the indicated seconds, retry
- **Username taken**: Script auto-retries with a randomized suffix
- **Session expired**: See `references/credentials.md` for how to regenerate
- **SSH timeout**: Verify VPS is up at `72.62.26.150`; key is `~/.ssh/dante_vps`

## Notes

- Username must end in `bot` — script enforces this
- Session credentials: see `references/credentials.md`
- Script lives on VPS at `/root/.openclaw/workspace-dante/create-bot.py`
- Copy in `scripts/create-bot.py` is the reference copy — sync to VPS if updated
