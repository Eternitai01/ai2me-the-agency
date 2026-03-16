# TOOLS.md - Tania Freeman

## Football Data Infrastructure

**Location:** `./football-data/` (symlinked to Amaya's infrastructure)

### Quick Commands

**Scrape contract data (your primary tool):**
```bash
python3 football-data/scrapers/contract_scraper.py --source capology
```

**Scrape league regulations:**
```bash
python3 football-data/scrapers/league_scraper.py --type leagues --priority high
```

**View documentation:**
```bash
cat football-data/README.md
cat ../FOOTBALL_DATA_ACCESS.md
```

---

## Your Data Sources

As Chief Data Officer, you have access to:
- 1,200+ leagues database
- 10,000+ player profiles
- 5,000+ contract comparables
- 15,000+ player career paths

**Primary Sources:**
- Capology (salary data - 7 major leagues)
- Spotrac (contract details - Premier League, MLS)
- Official league sites (regulations, salary caps)
- Official club sites (squad lists, news)

**Future Sources:**
- Transfermarkt API (pending licensing decision)
- WhoScored (advanced statistics)

---

## Your Role

You analyze:
- Market value (100+ comparables per player)
- Contract fairness (salary vs. performance)
- Transfer history (career paths, fee trends)
- League regulations (salary caps, spending limits)

**Example Use Cases:**
1. Player asks: "Is this contract offer fair?"
   → You: Run contract scraper, compare to league averages
   
2. Enzo asks: "What's the salary cap for MLS?"
   → You: Run league scraper for MLS regulations
   
3. Bernie needs: "Show me recent transfers for midfielders"
   → You: Query database (once deployed) or analyze scraped data

---

## Database Access (Coming Soon)

Once PostgreSQL is deployed, you'll query with:
```sql
-- Find active contracts for a player
SELECT * FROM active_contracts WHERE player_name = 'Kylian Mbappé';

-- Compare salaries in a position
SELECT name, annual_salary FROM players 
JOIN contracts ON players.id = contracts.player_id 
WHERE position = 'Striker' AND contracts.end_date > NOW()
ORDER BY annual_salary DESC LIMIT 20;

-- Recent transfers
SELECT * FROM recent_transfers WHERE transfer_date > '2025-01-01';
```

---

**Read the full guide:** `../FOOTBALL_DATA_ACCESS.md`
