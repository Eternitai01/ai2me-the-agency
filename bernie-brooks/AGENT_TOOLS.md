# Bernie's Agent Tools — Football Data Access

**Role:** Athlete Advisor Agent  
**Database:** 4,331 clubs from 47 leagues, 23 countries

---

## Quick Access

### Search Clubs (for negotiations)
```bash
cd ~/football-data/tools
python3 club_search.py --country Brazil --tier 1
python3 club_search.py --name "River Plate"
python3 club_search.py --list-countries
```

### Python API
```python
import sys
sys.path.append('/data/.openclaw/workspace-amaya/projects/football-data/tools')
from club_search import search_clubs, get_club_details

# Research clubs for transfer negotiations
clubs = search_clubs(country='Argentina', tier=1)

# Get club details for negotiation prep
details = get_club_details('Boca Juniors')
```

---

## Your Use Cases

**As Player Advisor (Negotiation Focus):**
- Research clubs before negotiations
- Find competing clubs in same market
- Identify salary cap limits (where available)
- Access official websites for contact info

**Database Coverage:**
- 4,331 clubs (negotiate with any of them)
- 47 leagues (understand market context)
- Salary cap data for strategic positioning

---

## Example Negotiation Prep

**Player wants MLS move:**
```bash
python3 club_search.py --league "MLS"
```

**Compare Argentine clubs:**
```bash
python3 club_search.py --country Argentina --tier 1
```

**Research specific club:**
```bash
python3 club_search.py --details "Inter Miami"
```

---

**Database Location:** `~/football-data/data/football_data.db`  
**Tools Location:** `~/football-data/tools/`
