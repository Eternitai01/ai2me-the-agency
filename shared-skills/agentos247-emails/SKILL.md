---
name: agentos247-emails
description: Send AgentOS 24/7 customer emails (post-chat follow-up, post-purchase receipt) with proper branding and templates. 19 total emails: 1 post-chat + 18 post-purchase (6 plans × 3 time terms: 3 Instant + 3 BYOK).
---

## When to Use This Skill

- Customer chatted with Charlie on agentos247.com → send post-chat follow-up
- Customer completed Stripe payment → send post-purchase receipt
- Agent deployment is complete → send welcome/go-live email
- Testing email templates for AgentOS 24/7

## Quick Start

**19 emails total:**
- 1 post-chat follow-up
- 18 post-purchase emails:
  - 9 Instant Plans (Anthropic): Basic, Plus, Elite
  - 9 BYOK Plans (Bring Your Own Key): Starter, Pro, Business

All templates are pre-generated in `templates/generated/` with the AgentOS logo embedded inline.

### Post-Chat Follow-Up (1 email)
```bash
cd /data/.openclaw/workspace-amaya/skills/agentos247-emails
python3 send-specific.py post-chat \
  --to customer@example.com \
  --name "John"
```

### Post-Purchase Receipts (18 emails)

#### Instant Plans (9 emails) - We provide AI
```bash
# Basic plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan basic --term 1month --order AGT-001
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan basic --term 12months --order AGT-002
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan basic --term 24months --order AGT-003

# Plus plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan plus --term 1month --order AGT-004
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan plus --term 12months --order AGT-005
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan plus --term 24months --order AGT-006

# Elite plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan elite --term 1month --order AGT-007
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan elite --term 12months --order AGT-008
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan elite --term 24months --order AGT-009
```

#### BYOK Plans (9 emails) - Customer provides their own API keys
```bash
# Starter BYOK plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan starter --term 1month --order AGT-010 --byok
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan starter --term 12months --order AGT-011 --byok
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan starter --term 24months --order AGT-012 --byok

# Pro BYOK plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan pro --term 1month --order AGT-013 --byok
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan pro --term 12months --order AGT-014 --byok
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan pro --term 24months --order AGT-015 --byok

# Business BYOK plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan business --term 1month --order AGT-016 --byok
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan business --term 12months --order AGT-017 --byok
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan business --term 24months --order AGT-018 --byok
```

## Email Flow Overview

```
Customer visits agentos247.com
         ↓
   Chats with Charlie
         ↓
[Email 1: Post-Chat] ← Gentle nudge toward purchase
         ↓
Customer purchases via Stripe
         ↓
[Email 2: Post-Purchase] ← Receipt + "deploying your agents"
         ↓
  24h later: Agents deployed
         ↓
[Email 3: Welcome/Go-Live] ← "Your agents are ready!"
```

## Template Variables

### Post-Chat (`templates/post-chat.html`)
- `{{NAME}}` — Customer first name

### Post-Purchase (`templates/post-purchase.html`)
- `{{NAME}}` — Customer first name
- `{{PLAN_NAME}}` — "Basic", "Plus", or "Elite"
- `{{PRICE}}` — Price number (e.g., "90", "109", "276")
- `{{BILLING_PERIOD}}` — "Monthly", "Annual", "12 months", "24 months"
- `{{CONVERSATIONS}}` — "500", "800", "1500"
- `{{CHANNEL}}` — "Telegram", "WhatsApp", or "Telegram + WhatsApp"
- `{{ORDER_NUM}}` — Order receipt number
- `{{PLAN_FEATURES}}` — HTML `<li>` items with plan features
- `{{EXTRA_MESSAGE}}` — Optional extra HTML (leave empty for none)

### Welcome/Go-Live (`templates/welcome.html`)
- `{{CUSTOMER_NAME}}` — Customer first name
- `{{PLAN_NAME}}` — Plan display name (e.g., "Professional Plan")
- `{{CUSTOMER_NUM}}` — Customer number/ID

## Pricing Reference

### Instant Plans (Anthropic)

| Plan | 1 Month | 12-Month (Save 28%) | 24-Month (Save 46%) |
|------|---------|---------------------|---------------------|
| Basic | €90/mo | €65/mo | €49/mo |
| Plus | €110/mo | €79/mo | €59/mo |
| Elite | €276/mo | €199/mo | €149/mo |

### BYOK Plans (Bring Your Own Key)

| Plan | 1 Month | 12-Month (Save 28%) | 24-Month (Save 46%) |
|----------|---------|---------------------|---------------------|
| Starter | €54/mo | €39/mo | €29/mo |
| Pro | €91/mo | €65/mo | €49/mo |
| Business | €184/mo | €132/mo | €99/mo |

## Plan Features

### Basic (500 conversations, Telegram)
- 500 conversations/month
- Telegram agent
- 80+ professional AI roles
- Persistent memory & knowledge base
- AI agent initiation guide
- Constant OpenClaw updates
- 24/7 technical support

### Plus (800 conversations, Telegram + WhatsApp)
All Basic features, plus:
- Dedicated WhatsApp number
- Priority email + chat support

### Elite (1500 conversations, All channels)
All Plus features, plus:
- Voice calls included
- Dante Guardian personal monitoring

## Design Specs

- **Logo:** 140px width, white background header
- **Colors:** Purple gradient CTAs (#667eea → #764ba2)
- **Typography:** System fonts (-apple-system, Roboto, etc.)
- **Layout:** Max 600px width, mobile responsive
- **Logo source:** https://agentos247.com/assets/agentos247-logo-DgB4oMWh.png (embedded inline)

## Files

```
agentos247-emails/
├── SKILL.md              # This file
├── send-specific.py      # CLI for sending specific plan+term emails
├── generate-all.py       # Generate all 9 post-purchase templates
├── templates/
│   ├── post-chat.html    # Base post-chat template
│   ├── post-purchase.html # Base post-purchase template
│   └── generated/        # 9 pre-generated plan+term templates
│       ├── post-purchase-basic-monthly.html
│       ├── post-purchase-basic-12months.html
│       ├── post-purchase-basic-24months.html
│       ├── post-purchase-plus-monthly.html
│       ├── post-purchase-plus-12months.html
│       ├── post-purchase-plus-24months.html
│       ├── post-purchase-elite-monthly.html
│       ├── post-purchase-elite-12months.html
│       └── post-purchase-elite-24months.html
└── assets/
    └── logo.png          # AgentOS 24/7 logo (156KB)
```

## Integration with Dante's System

These templates mirror the production system on Dante's VPS:
- **Server:** 172.62.26.150 (srv1465134)
- **Live templates:** `/opt/clawolution-api/email-templates/`
- **Email code:** `/opt/clawolution-api/agentos247-email.js`
- **Functions:** `sendPostChatEmail()`, `sendPostPurchaseEmail()`, `sendWelcomeEmail()`

## Error Handling

The send script will:
- ✅ Validate required variables before sending
- ✅ Embed logo inline (CID method)
- ✅ Provide clear error messages
- ✅ Exit with proper status codes

## Testing

```bash
# Test all three emails to yourself
cd /data/.openclaw/workspace-amaya/skills/agentos247-emails

python3 send.py post-chat --to cc@eternitaigroup.com --name "Carlos"

python3 send.py post-purchase \
  --to cc@eternitaigroup.com \
  --name "Carlos" \
  --plan "Basic" \
  --price "90" \
  --billing "Annual" \
  --conversations "500" \
  --channel "Telegram" \
  --order "TEST-001"

python3 send.py welcome \
  --to cc@eternitaigroup.com \
  --name "Carlos" \
  --plan "Professional Plan" \
  --customer-num "TEST-001"
```

## Related Skills

- `email-sender` — Base email sending infrastructure (Hostinger SMTP)
- `agentos247-email-flow` — Documentation of email flow + pricing

## Notes

- Credentials loaded from `/data/.openclaw/secrets/hostinger-mail-amaya.env`
- Default sender: `team@agentos247.com` (CC: team@eternitaigroup.com)
- Logo embedded inline to avoid external dependencies
- Templates use simple `{{ variable }}` substitution (Jinja2-style)
