# AgentOS 24/7 Customer Emails

**10 ready-to-send customer email templates** for the AgentOS 24/7 sales and onboarding flow.

## Email Inventory

### 1. Post-Chat Follow-Up (1 email)
Sent after customer chats with Charlie on agentos247.com

### 2. Post-Purchase Receipts (9 emails)
Sent after Stripe payment confirmation — one for each plan+term combination:

| Plan | 1 Month | 12 Months (Save 64%) | 24 Months (Save 73%) |
|------|---------|----------------------|----------------------|
| **Basic** (€180) | €180/mo | €65/mo | €49/mo |
| **Plus** (€219) | €219/mo | €79/mo | €59/mo |
| **Elite** (€552) | €552/mo | €199/mo | €149/mo |

## Quick Send

```bash
cd /data/.openclaw/workspace-amaya/skills/agentos247-emails

# Post-chat
python3 send-specific.py post-chat --to customer@example.com --name "John"

# Post-purchase (pick one)
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan basic --term monthly --order AGT-001
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan plus --term 12months --order AGT-002
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan elite --term 24months --order AGT-003
```

## Plan Features

### Basic (500 conversations, Telegram)
- 500 conversations/month
- Telegram agent
- 80+ professional AI roles
- Persistent memory & knowledge base
- 24/7 technical support

### Plus (800 conversations, Telegram + WhatsApp)
All Basic features, plus:
- Dedicated WhatsApp number
- Priority support

### Elite (1500 conversations, All channels)
All Plus features, plus:
- Voice calls included
- Dante Guardian monitoring

## Template Generation

Templates are pre-generated with correct pricing and features:

```bash
python3 generate-all.py  # Regenerates all 9 post-purchase templates
```

Output: `templates/generated/post-purchase-{plan}-{term}.html`

## Design

- **Logo:** 140px width, white background
- **Colors:** Purple gradient CTAs (#667eea → #764ba2)
- **Discount badges:** Shown for 12-month and 24-month terms
- **Mobile responsive:** Max 600px width

## Files

```
10 total emails:
├── 1 post-chat (templates/post-chat.html)
└── 9 post-purchase (templates/generated/*.html)
    ├── 3 Basic (monthly, 12months, 24months)
    ├── 3 Plus (monthly, 12months, 24months)
    └── 3 Elite (monthly, 12months, 24months)
```

## Testing

All 10 emails tested and sent to cc@eternitaigroup.com on 2026-05-18.

## Integration

These templates mirror the production system on Dante's VPS (172.62.26.150).

See `SKILL.md` for full documentation.
