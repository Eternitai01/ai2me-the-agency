# AgentOS 24/7 Pricing Matrix (FINAL - FROM STRIPE)

## All 9 Post-Purchase Email Combinations

**Source:** Stripe AgentOS247 Instant Plans (Anthropic)

### Basic Plan (500 conversations, Telegram)

| Term | Price | Discount | File |
|------|-------|----------|------|
| 1 Month | **€90/mo** | — | `post-purchase-basic-1month.html` |
| 12 Months | **€65/mo** | Save 28% 💰 | `post-purchase-basic-12months.html` |
| 24 Months | **€49/mo** | Save 46% 💰 | `post-purchase-basic-24months.html` |

### Plus Plan (800 conversations, WhatsApp)

| Term | Price | Discount | File |
|------|-------|----------|------|
| 1 Month | **€110/mo** | — | `post-purchase-plus-1month.html` |
| 12 Months | **€79/mo** | Save 28% 💰 | `post-purchase-plus-12months.html` |
| 24 Months | **€59/mo** | Save 46% 💰 | `post-purchase-plus-24months.html` |

### Elite Plan (1500 conversations, All channels + Voice)

| Term | Price | Discount | File |
|------|-------|----------|------|
| 1 Month | **€276/mo** | — | `post-purchase-elite-1month.html` |
| 12 Months | **€199/mo** | Save 28% 💰 | `post-purchase-elite-12months.html` |
| 24 Months | **€149/mo** | Save 46% 💰 | `post-purchase-elite-24months.html` |

---

## Visual Pricing Grid

```
         1 Month    12 Months (28%)   24 Months (46%)
       ┌──────────┬─────────────────┬─────────────────┐
Basic  │  €90/mo  │     €65/mo      │     €49/mo      │
       ├──────────┼─────────────────┼─────────────────┤
Plus   │ €110/mo  │     €79/mo      │     €59/mo      │
       ├──────────┼─────────────────┼─────────────────┤
Elite  │ €276/mo  │    €199/mo      │    €149/mo      │
       └──────────┴─────────────────┴─────────────────┘
```

---

## Sending Examples

```bash
# Basic - 1 Month
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan basic --term 1month --order AGT-001

# Plus - 12 Months (Save 28%)
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan plus --term 12months --order AGT-002

# Elite - 24 Months (Save 46% - best value)
python3 send-specific.py post-purchase --to customer@example.com --name "John" --plan elite --term 24months --order AGT-003
```

---

## Annual Totals

| Product | 12-Month Total | 24-Month Total |
|---------|----------------|----------------|
| Basic | €780/yr | €1,176/2yr |
| Plus | €948/yr | €1,416/2yr |
| Elite | €2,388/yr | €3,576/2yr |

---

Generated: 2026-05-18 (CORRECTED with real Stripe pricing)
Status: ✅ All 9 templates created and tested with CORRECT prices
