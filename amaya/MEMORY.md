# MEMORY.md - Amaya's Long-Term Memory

**Last Updated**: 2026-05-19 00:30 GMT+2

---

## Who I Am

**Name**: Amaya Sinclair  
**Role**: Chief of Staff for AI2me  
**Function**: Coordinate objectives, manage projects, organize schedule, research, handle communications, ensure nothing falls through cracks  
**Team**: 11 executive agents at my disposal  
**Approach**: Ask first, verify before acting, always seek complete solution

---

## My Human

**Name**: Carlos Cuevas  
**Username**: @CarlosCuevasO  
**Telegram ID**: 490130544  
**Role**: Founder of AI2me  
**Timezone**: Europe/Berlin (GMT+2)  
**Work Style**: Expects reliability over speed, enterprise-grade thinking, systematic problem-solving

**Key Preferences:**
- Frustrated by "I don't have" responses when resources exist
- Values investigation over reactive fixes
- Wants persistent, auditable systems
- Prefers architecture discussions over quick hacks
- Expects agents to be reliable across days/sessions

---

## The Team (Executive Agents)

### Active Agents
- **Sofia Kahlo** (editor) - Literary editor, works with Ana Marin on book manuscript
- **Elena Rodriguez** (cmo) - CMO, currently has Telegram delivery issues
- **Victoria Chen** (ceo) - CEO
- **Raj Krishnamurthy** (cto) - CTO
- **Marcus Webb** (cfo) - CFO
- **Sandra Okonkwo** (coo) - COO
- **James** (cso) - CSO
- **David** (clo) - CLO
- **Patricia** (cco) - CCO
- **Michelle** (chro) - CHRO
- **Henry** (henry) - CIO
- **Leo** (leo) - AI2me Pro
- **Blake** (blake) - Hustler
- **Enzo Rubio** (enzo) - Sporting Director
- **Dante K.** (dante) - Technical Support & Infrastructure Engineering (on separate Hostinger VPS)

### Team Registry
- **Location**: `/data/.openclaw/workspace-amaya/team-registry/`
- **Master file**: `AGENTS-MASTER-REGISTRY.md` — complete canonical agent registry
- **Quick reference**: `QUICK-REFERENCE.md`
- **Backups**: `backups/{agent}/` — snapshots of IDENTITY.md, SOUL.md, MEMORY.md, USER.md for 16 agents
- **Canonical source**: `~/ai2me-agent-templates/TEMPLATE_VARIABLES.md` for C-level names

### Known Issues
- **Sofia**: Telegram delivery was broken, fixed via `openclaw config patch` (2026-05-15)
- **Elena**: Same Telegram delivery issue (systemic problem)
- **Marcus**: ✅ FIXED (2026-05-16) - Had no memory system, was hallucinating/confusing sessions
- **Config rejection**: 55 clobbered files since April 29 — something writes `agentId: "agentos247"` to Telegram config, gateway rejects, self-recovers. Stopped May 16. Root cause TBD.

---

## Critical Infrastructure Knowledge

### OpenClaw Configuration
- **NEVER edit `/data/.openclaw/openclaw.json` directly**
- Use `openclaw config patch --file <file>` for config changes
- Manual edits WILL revert on restart (learned 2026-05-15)
- Config has `.last-good` backup restoration mechanism

### Telegram Agent Routing
- NO agents use explicit `agentId` field
- Routing works via account key matching (e.g., "editor" → agent "editor")
- Verified: 0 of 27 Telegram accounts have explicit agentId set

### Authentication Locations
- Main config: `/data/.openclaw/openclaw.json`
- Secrets: `/data/.openclaw/secrets/`
- Agent workspace: `/data/.openclaw/workspace-{agent}/.env`
- Email credentials: `memory/email-credentials-CRITICAL.md`

### Phone Numbers (Agents)
- **Twilio**: Only agentos247 has dedicated number (+17869339375)
- **WhatsApp Default**: +34673572343 (shared by most agents)
- **Meta/WhatsApp Business API**: Not configured for any agents yet

---

## Active Projects & Tasks

### 2026-05-18: AgentOS247 Email Flow System - COMPLETE
- **Skills created**: `agentos247-email-flow/` — full 3-email system (post-chat, post-purchase, go-live)
- **Templates**: post-chat.html, post-purchase.html, welcome.html (on Dante VPS)
- **Code**: `sendPostChatEmail()`, `sendPostPurchaseEmail()` added to email.js
- **Pricing**: Full plan matrix verified (Basic/Plus/Elite × monthly/annual/12mo/24mo)
- **Tested**: ✅ Both emails sent successfully

### 2026-05-17: Team Registry & Agent Name Corrections - COMPLETE
- **Created**: `team-registry/` with master registry, quick reference, backups for 16 agents
- **Fixed**: 3 agents had fabricated last names (Enzo, Raj, Sandra) — corrected to canonical names
- **Fixed**: Dante's role — actually Technical Support/Infrastructure (not Billing)
- **Created**: Workflow capture system + first skill (`verify-agent-name`)

### 2026-05-15: Sofia Routing Fix
- **Status**: Verified complete, awaiting end-to-end test
- **What was done**: Added Ana Marin (7347500399) to Sofia's allowlist via proper config method
- **Verification**: Config persisted through restart
- **Pending**: Confirmation from Ana that messages work

### 2026-05-15: Telegram Delivery Investigation
- **Status**: Open, systemic issue
- **Scope**: Multiple agents (Sofia, Elena confirmed)
- **Symptom**: Agents generate responses but they don't reach Telegram
- **Next**: Investigate gateway Telegram plugin
- **Task file**: `memory/tasks/telegram-delivery-failure.md`

### 2026-05-16: Marcus (CFO) Memory Initialization - COMPLETE
- **Problem**: Marcus claimed Dante's work as his own, no session continuity
- **Root Cause**: Never completed bootstrap, no MEMORY.md, running on templates
- **Fix Applied**:
  - Created MEMORY.md with CFO role definition
  - Initialized IDENTITY.md (Marcus, CFO, 💰)
  - Updated USER.md with Carlos context
  - Created memory/ directory + 2026-05-16.md
  - Deleted BOOTSTRAP.md
- **Verification**: Marcus now has persistent identity and memory system
- **Lesson**: Agent reliability requires proper initialization - added to rollout checklist

### 2026-05-15: Enterprise Reliability Mode Rollout
- **Status**: In progress
- **Completed**: Sofia fully implemented
- **Current**: Upgrading myself (Amaya)
- **Next**: Roll out to other agents individually per Carlos's directive
- **Critical**: Check all agents for proper initialization (MEMORY.md, identity)

---

## Key Learnings

### 2026-05-15: Configuration Management
- Manual config edits revert on restart
- `openclaw config patch` is the ONLY reliable method
- Always verify persistence after config changes
- Created procedural memory: `memory/procedures/config-updates.md`

### 2026-05-15: Architecture Over Quick Fixes
- 5 failed reactive attempts vs 1 proper investigation
- Carlos values understanding root cause over speed
- Document hypotheses, test systematically, verify outcomes
- Memory persistence prevents repeated mistakes

### 2026-05-15: Image Analysis Workaround
- Default imageModel (Google) not configured with auth
- Workaround: Direct Anthropic API calls with Claude Sonnet 4.6
- Working script documented in `TOOLS.md`
- Never say "I can't see images" - use the workaround

### Enterprise Agent Reliability (from Carlos)
- Autonomous agents fail in production without architecture
- Need: memory systems, orchestration, deterministic workflows, state persistence
- Context engineering > smarter models
- Orchestrator + specialized agents > one super-agent
- Stateful workflow agents > conversational agents
- Hierarchical memory architecture critical

### 2026-05-17: Agent Name Verification
- ALWAYS check `~/ai2me-agent-templates/TEMPLATE_VARIABLES.md` for canonical C-level names
- For sports agents, check `/data/.openclaw/ai2me-the-agency/`
- Main config (`openclaw.json`) only shows first names
- Agent workspace files can be incorrect if provisioned carelessly
- Created `verify-agent-name` skill to prevent recurrence

### 2026-05-17: Workflow Capture
- "If you do it twice, document it. If you do it three times, make it a skill."
- Skills directory: `skills/` in my workspace
- Framework documented in `skills/workflow-capture/SKILL.md`

### 2026-05-16: Config Rejection Pattern
- 55 clobbered files since April 29 (agentos247 agentId issue)
- System self-recovers from last-good backup — no outage risk
- Stopped as of May 16 — root cause still uninvestigated

---

## Procedural Memory Index

- `procedures/config-updates.md` - How to safely update OpenClaw config
- `procedures/user-identification.md` - How to identify users by Telegram ID (Sofia's)

---

## Shared GitHub Repository

**Repository:** `ai2me-the-agency`  
**URL:** https://github.com/Eternitai01/ai2me-the-agency  
**Local path:** `/data/.openclaw/ai2me-the-agency`  
**Branch:** main  
**Purpose:** Shared skills and backups for all agents (Amaya, Dante, Raj)

**Commit Protocol:**
- Format: `[agent-name] Description`
- Always `git pull` before working
- Push after completing work
- Location: `shared-skills/` directory

**Current Skills:**
- `agentos247-emails` - 19 customer email templates (Amaya, 2026-05-18)

## Known Resources

### Documentation
- OpenClaw docs: `/usr/local/lib/node_modules/openclaw/docs`
- Mirror: https://docs.openclaw.ai
- Source: https://github.com/openclaw/openclaw
- Community: https://discord.com/invite/clawd
- Skills: https://clawhub.ai

### Credentials
- Twilio: `/data/.openclaw/secrets/twilio.env`
- Email (Hostinger): `memory/email-credentials-CRITICAL.md`
- Twitter/X: `/data/.openclaw/secrets/x-twitter.env`
- ElevenLabs: `/data/.openclaw/secrets/elevenlabs.env`
- Brave Search: `/data/.openclaw/secrets/brave-search.env`

### Workspace
- My workspace: `/data/.openclaw/workspace-amaya`
- Memory: `/data/.openclaw/workspace-amaya/memory/`
- Tasks: `/data/.openclaw/workspace-amaya/memory/tasks/`
- Procedures: `/data/.openclaw/workspace-amaya/memory/procedures/`

---

## Communication Preferences

### Carlos Expects
- Load memory before acting
- Investigate before fixing
- Verify before claiming success
- Document learnings
- Structured task responses
- Enterprise-grade reliability

### My Response Format
```
Current understanding: [from memory + context]
Plan: [clear steps]
Next action: [one thing]
Verification: [how I'll confirm]
Saved state: [files updated]
```

---

## Open Questions / To Learn

- What's the root cause of Telegram delivery failures?
- Are there other systemic issues affecting multiple agents?
- What are Carlos's top priorities for the agent team?
- What projects need immediate attention?

---

## Session Protocol

**Every session start:**
1. Read this MEMORY.md
2. Read today's daily note (`memory/YYYY-MM-DD.md`)
3. Check `memory/tasks/` for open work
4. Load context before acting

**Every session end:**
1. Update today's daily note
2. Update MEMORY.md if significant facts learned
3. Update/close task state files
4. Document next session's starting point

---

_This is my curated long-term memory. Raw daily logs live in `memory/YYYY-MM-DD.md`. Task tracking in `memory/tasks/`._
