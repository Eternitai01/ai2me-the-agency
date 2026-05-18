# AgentOS 24/7 Email Inventory

## 10 Total Emails

### 1 Post-Chat Follow-Up
**File:** `templates/post-chat.html`  
**When:** After customer chats with Charlie widget  
**Variables:** `{{NAME}}`

---

### 9 Post-Purchase Receipts

#### Basic Plan (500 conversations, Telegram)

| File | Price | Term | Discount |
|------|-------|------|----------|
| `post-purchase-basic-monthly.html` | €180/mo | 1 Month | — |
| `post-purchase-basic-12months.html` | €65/mo | 12 Months | Save 64% |
| `post-purchase-basic-24months.html` | €49/mo | 24 Months | Save 73% |

**Features:**
- 500 conversations/month
- Telegram agent
- 80+ professional AI roles
- Persistent memory & knowledge base
- AI agent initiation guide
- Constant OpenClaw updates & improvements
- 24/7 technical support

---

#### Plus Plan (800 conversations, WhatsApp)

| File | Price | Term | Discount |
|------|-------|------|----------|
| `post-purchase-plus-monthly.html` | €219/mo | 1 Month | — |
| `post-purchase-plus-12months.html` | €79/mo | 12 Months | Save 64% |
| `post-purchase-plus-24months.html` | €59/mo | 24 Months | Save 73% |

**Features:**
- 800 conversations/month
- Dedicated WhatsApp number
- Telegram agent
- 80+ professional AI roles
- Persistent memory & knowledge base
- Priority email + chat support
- AI agent initiation guide
- Constant OpenClaw updates & improvements

---

#### Elite Plan (1500 conversations, Telegram + WhatsApp + Voice)

| File | Price | Term | Discount |
|------|-------|------|----------|
| `post-purchase-elite-monthly.html` | €552/mo | 1 Month | — |
| `post-purchase-elite-12months.html` | €199/mo | 12 Months | Save 64% |
| `post-purchase-elite-24months.html` | €149/mo | 24 Months | Save 73% |

**Features:**
- 1500 conversations/month
- Dedicated WhatsApp number
- Telegram agent
- Voice calls included
- Dante Guardian personal monitoring
- 80+ professional AI roles
- Persistent memory & knowledge base
- Priority 24/7 support
- AI agent initiation guide
- Constant OpenClaw updates & improvements

---

## Quick Reference

```bash
# Post-chat
python3 send-specific.py post-chat --to EMAIL --name "NAME"

# Post-purchase
python3 send-specific.py post-purchase --to EMAIL --name "NAME" --plan PLAN --term TERM --order ORDER

# Plans: basic, plus, elite
# Terms: monthly, 12months, 24months
```

## Status

✅ All 10 emails generated and tested (2026-05-18)
