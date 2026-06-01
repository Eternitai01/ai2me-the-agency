---
name: ai-lead-magnet-expert
description: Product knowledge, pricing, features, and sales playbook for the AI Lead Magnet Expert — Professional AI Lead Generator by EternitAI Group. Use when pitching, quoting, configuring, or updating any agent (Heather, Charlie, etc.) with current pricing, plan features, discount structure, add-ons, and upsell triggers for the AgentOS 24/7 product.
---

# AI Lead Magnet Expert — Professional AI Lead Generator

Product by EternitAI Group. Three tiers, monthly SaaS pricing, contract discounts, event add-ons.

## Product Overview

An AI lead magnet expert embedded on a customer's website and/or accessible via QR code at their event stand. Works 24/7, engages visitors in real conversation, qualifies leads, answers questions, and books meetings — without any human present.

**Agents:** Heather, Charlie, Tania, Charly, Blake, Bernie (configurable per customer)  
**Channels:** Website chat, WhatsApp, Telegram, Voice AI (Pro+)

## Pricing — Full Reference

See `references/pricing.md` for the complete pricing card, discount table, add-ons, and upsell triggers.

## Sales Playbook

**Always open soft:** *"starting from €2,500/month"* — let the conversation qualify the plan.

1. Give Starter first. One sentence on what it covers. Pause.
2. Move to Professional when they signal: inbound calls, CRM, multiple channels, events.
3. Move to Enterprise when they signal: outbound calls, white-label, compliance, unlimited languages.
4. Push-back on price → go to 24-month (-30% + setup waived). That's the closer.
5. Never read the full pricing table. One plan at a time. Keep it a conversation.

## System Prompt Update

To update a voice agent's pricing knowledge, edit the `PRICING:` and `WHAT'S IN EACH PLAN` sections in:

```
/data/.openclaw/workspace-amaya/ten-framework/voice-agent/server.js
```

After editing, deploy:
```bash
cp server.js /tmp/ten-agent-src3/voice-agent/server.js
cd /tmp/ten-agent-src3 && zip -r /tmp/source-new.zip . --exclude '.git/*'
aws s3 cp /tmp/source-new.zip s3://ai2me-ten-agent-build/source.zip --region eu-north-1
aws codebuild start-build --project-name ai2me-ten-agent-build --region eu-north-1
# Wait ~3 min, then:
aws ecs update-service --cluster ai2me-dev-cluster --service ai2me-agent-ten-agent --force-new-deployment --region eu-north-1
```
