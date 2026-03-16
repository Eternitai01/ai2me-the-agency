# TOOLS.md - Bernie Brooks

## Football Data Infrastructure

**Location:** `./football-data/` (symlinked to Amaya's infrastructure)

### Quick Commands

**Scrape transfer news & squad data:**
```bash
python3 football-data/scrapers/league_scraper.py --type clubs
```

**Scrape contract data:**
```bash
python3 football-data/scrapers/contract_scraper.py --source capology
```

**View documentation:**
```bash
cat football-data/README.md
cat ../FOOTBALL_DATA_ACCESS.md
```

---

## Your Data Sources

As transfer market intelligence specialist, you have access to:
- 10 top clubs (squad lists, news, contract announcements)
- 15 major leagues (transfer windows, regulations)
- Contract comparables (salary benchmarks)
- Transfer history (15,000+ career paths target)

**Current Sources:**
- Official club websites (Real Madrid, Barcelona, Man City, etc.)
- Official league websites (Premier League, La Liga, etc.)
- Capology (salary data)
- Spotrac (contract details)

**Future Sources:**
- Transfermarkt API (transfer history, market values)
- Media aggregation (Goal, Marca, ESPN)

---

## Your Role

You handle:
- Transfer negotiations (market intelligence, timing)
- Contract structuring (performance bonuses, release clauses)
- Legal compliance (FIFA regulations, work permits)
- Relationship management (clubs, agents, leagues)

**Example Use Cases:**
1. Player wants to transfer to Premier League
   → You: Scrape Premier League clubs for squad needs, check work permit rules
   
2. Contract negotiation needs benchmarks
   → You: Run contract scraper for position/league comparables
   
3. Transfer window closing, need urgent intel
   → You: Scrape club news pages for last-minute announcements

---

## Database Access (Coming Soon)

Once PostgreSQL is deployed, you'll query with:
```sql
-- Find clubs needing a specific position
SELECT c.name, l.name as league 
FROM clubs c 
JOIN leagues l ON c.league_id = l.id 
WHERE c.id IN (
  SELECT club_id FROM contracts 
  WHERE end_date < '2026-06-30' AND position = 'Center Back'
);

-- Transfer window dates
SELECT name, country, transfer_window_summer_start, transfer_window_summer_end
FROM leagues WHERE tier = 1;

-- Recent transfers by club
SELECT * FROM recent_transfers WHERE to_club_id = 123;
```

---

**Read the full guide:** `../FOOTBALL_DATA_ACCESS.md`
