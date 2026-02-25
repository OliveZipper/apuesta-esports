# Self-Hosted Images

This folder contains locally-hosted images for reliability.

## Current Status

### Game Logos (Working)
- `games/cs2.svg` - Counter-Strike 2 (from Steam CDN)
- `games/dota2.png` - Dota 2 (from Steam CDN)
- `games/valorant.svg` - Valorant (from Wikipedia)

### Team Logos (Placeholders)
Team logos in `teams/` are placeholders. To get real logos:

1. Visit https://liquipedia.net/counterstrike/Team_Liquid (or other team)
2. Right-click the logo → Save Image As
3. Save to this folder as `liquid.png`

Repeat for: g2, spirit, navi, faze, sentinels, cloud9, falcons, og

### Why Placeholders?
Liquipedia and HLTV block automated downloads (Cloudflare protection).
The production site uses CDN URLs directly which work in browsers.

## Usage

Update HTML to use local images:
```html
<!-- Instead of -->
<img src="https://external-cdn.com/team.png">

<!-- Use -->
<img src="/images/teams/liquid.png" onerror="this.src='/images/teams/placeholder.svg'">
```
