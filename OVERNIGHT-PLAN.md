# Apuesta Esports - Overnight Build Plan
## Mission: Build the most comprehensive esports reference site

### Site Structure (Target)
```
apuestaesports.com/
├── index.html                 # Homepage - Esports hub
├── live/                      # Live odds & map dashboard
│   └── index.html
├── games/                     # Game-specific sections
│   ├── index.html             # All games overview
│   ├── cs2.html               # Counter-Strike 2
│   ├── dota2.html             # Dota 2
│   ├── lol.html               # League of Legends
│   ├── valorant.html          # Valorant
│   └── [more games].html
├── teams/                     # Team profiles
│   ├── index.html             # Team rankings/directory
│   └── [team-slug].html       # Individual team pages
├── players/                   # Player profiles
│   ├── index.html             # Player directory
│   └── [player-slug].html     # Individual player pages
├── countries/                 # Country esports rankings
│   ├── index.html             # Country leaderboard
│   └── [country-code].html    # Individual country pages
├── tournaments/               # Tournament coverage
│   ├── index.html             # Tournament calendar
│   └── [tournament].html      # Individual tournament pages
├── betting/                   # Betting guides
│   ├── index.html             # Betting hub
│   ├── beginners-guide.html   # Getting started
│   └── [game]-betting.html    # Game-specific betting guides
├── sitemap.xml                # SEO sitemap
├── robots.txt                 # SEO robots
├── llms.txt                   # LLM-friendly site description
└── archive/                   # Preserved old pages (not published)
```

### Overnight Schedule (8 Hours)

#### Hour 1 (14:00-15:00 UTC): Foundation & Data Collection
- [ ] Create site skeleton (folders, base templates)
- [ ] Build data scraping scripts for teams/players/tournaments
- [ ] Collect initial data from Liquipedia, HLTV, VLR.gg

#### Hour 2 (15:00-16:00 UTC): Homepage & Navigation
- [ ] Build new homepage with full site navigation
- [ ] Hero section with live stats
- [ ] Featured content sections
- [ ] SEO meta tags & structured data

#### Hour 3 (16:00-17:00 UTC): Game Pages
- [ ] CS2 comprehensive page
- [ ] Dota 2 comprehensive page
- [ ] League of Legends page
- [ ] Valorant page

#### Hour 4 (17:00-18:00 UTC): More Games + Teams Index
- [ ] Additional game pages (CoD, R6, Rocket League, etc.)
- [ ] Teams directory/index page
- [ ] Team ranking algorithm

#### Hour 5 (18:00-19:00 UTC): Team Profile Pages
- [ ] Top 20 CS2 teams
- [ ] Top 20 Dota 2 teams
- [ ] Top 20 LoL teams
- [ ] Team page template with stats, history, roster

#### Hour 6 (19:00-20:00 UTC): Player Profiles
- [ ] Player directory page
- [ ] Top 50 player profiles across games
- [ ] Player stats, achievements, team history

#### Hour 7 (20:00-21:00 UTC): Country Rankings
- [ ] Country index with rankings
- [ ] Individual country pages (top 20 esports countries)
- [ ] Metrics: infrastructure, talent, tournaments hosted, prize money

#### Hour 8 (21:00-22:00 UTC): SEO, Polish & Deploy
- [ ] Sitemap.xml generation
- [ ] robots.txt
- [ ] Update llms.txt with full site description
- [ ] JSON-LD structured data on all pages
- [ ] Final deploy & verification
- [ ] If time: Start on Parier sites

### Data Sources
- **Liquipedia** - Teams, players, tournaments, history
- **HLTV.org** - CS2 rankings, stats
- **VLR.gg** - Valorant rankings
- **OP.GG / Leaguepedia** - LoL data
- **DotaBuff / Stratz** - Dota 2 stats
- **Esports Charts** - Viewership, prize pools
- **Esports Earnings** - Prize money by country/player

### Design Principles
- Dark theme (matches current brand)
- Cloudbet brand colors where appropriate (#FF6B2F, #8D52DA, #DFFD51)
- Fast loading (minimal JS, optimized images)
- Mobile-first responsive
- SEO-optimized (semantic HTML, meta tags, structured data)
- LLM-friendly (clear headings, structured content)

### Cron Jobs for Overnight Work
8 jobs, one per hour, each completing a section.
