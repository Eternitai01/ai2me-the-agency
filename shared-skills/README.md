# AI2me Shared Skills

Shared skills used across multiple agents (Amaya, Dante, Raj, etc.)

## Skills

### agentos247-emails
**Purpose:** Send AgentOS 24/7 customer emails (post-chat, post-purchase)  
**Owner:** Amaya Sinclair (Chief of Staff)  
**Created:** 2026-05-18  

19 total email templates:
- 1 post-chat follow-up (after Charlie widget conversation)
- 18 post-purchase receipts:
  - 9 Instant Plans (Anthropic): Basic, Plus, Elite × 3 terms
  - 9 BYOK Plans (Bring Your Own Key): Starter, Pro, Business × 3 terms

**Pricing Structure:**
- 1 Month: Save 50% off retail
- 12 Months: Save 64% off retail
- 24 Months: Save 73% off retail

**Usage:**
```bash
cd shared-skills/agentos247-emails

# Instant plans
python3 send-specific.py post-purchase --to customer@example.com --name "John" \
  --plan [basic|plus|elite] --term [1month|12months|24months] --order AGT-001

# BYOK plans  
python3 send-specific.py post-purchase --to customer@example.com --name "John" \
  --plan [starter|pro|business] --term [1month|12months|24months] --order AGT-001 --byok
```

## Backup Protocol

All agents (Amaya, Dante, Raj) commit to this repository:
- Branch: `main`
- Commit format: `[agent-name] Skill description`
- Always pull before push
