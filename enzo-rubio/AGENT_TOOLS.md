# Enzo's Agent Tools — Football Data Access

**Role:** AI Sporting Director  
**Database:** 4,331 clubs from 47 leagues, 23 countries

---

## Quick Access

### Search Clubs
```bash
cd ~/football-data/tools
python3 club_search.py --country Spain --tier 1
python3 club_search.py --name Barcelona
python3 club_search.py --list-countries
```

### Python API
```python
import sys
sys.path.append('/data/.openclaw/workspace-amaya/projects/football-data/tools')
from club_search import search_clubs, get_club_details

# Find all clubs in La Liga
clubs = search_clubs(country='Spain', tier=1, league='La Liga')
for name, league, country, tier, website in clubs:
    print(f"{name} - {website}")

# Get details for specific club
details = get_club_details('Real Madrid')
```

---

## Your Use Cases

**As Club Scout:**
- Search clubs by country/league to find scouting targets
- Filter by tier to focus on specific divisions
- Access official websites for contact info

**Database Coverage:**
- 4,331 clubs across 47 leagues
- Covers: Europe (major + minor), Americas (full), Asia (partial)
- Tiers 1-4 (Spain has all 4 divisions)

---

## Example Queries

**Find Portuguese clubs:**
```bash
python3 club_search.py --country Portugal
```

**Find all Tier 2 clubs:**
```bash
python3 club_search.py --tier 2
```

**Search by name:**
```bash
python3 club_search.py --name "Atletico"
```

---

**Database Location:** `~/football-data/data/football_data.db`  
**Tools Location:** `~/football-data/tools/`
