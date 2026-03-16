# Tania's Agent Tools — Football Data Access

**Role:** Athlete Advisor Agent  
**Database:** 4,331 clubs from 47 leagues, 23 countries

---

## Quick Access

### Search Clubs (for player advising)
```bash
cd ~/football-data/tools
python3 club_search.py --country Spain --tier 1
python3 club_search.py --name Barcelona
python3 club_search.py --list-leagues --country England
```

### Python API
```python
import sys
sys.path.append('/data/.openclaw/workspace-amaya/projects/football-data/tools')
from club_search import search_clubs, list_leagues

# Help player find clubs in their target country
clubs = search_clubs(country='Spain', tier=1)

# Show all leagues in a country
leagues = list_leagues(country='England')
for name, country, tier, club_count in leagues:
    print(f"{name} (Tier {tier}): {club_count} clubs")
```

---

## Your Use Cases

**As Player Advisor:**
- Research clubs when player asks "Should I join X?"
- Find alternative clubs in same league/country
- Identify tier/competition level for career planning
- Access club websites for research

**Database Coverage:**
- 4,331 clubs (can advise on moves to any of them)
- 47 leagues (know the competition landscape)
- Salary cap data (where available) for contract advice

---

## Example Player Questions

**"Should I move to Spain or England?"**
```bash
python3 club_search.py --country Spain --tier 1
python3 club_search.py --country England --tier 1
```

**"What clubs are in La Liga?"**
```bash
python3 club_search.py --league "La Liga"
```

**"Tell me about Barcelona"**
```bash
python3 club_search.py --details "Barcelona"
```

---

**Database Location:** `~/football-data/data/football_data.db`  
**Tools Location:** `~/football-data/tools/`
