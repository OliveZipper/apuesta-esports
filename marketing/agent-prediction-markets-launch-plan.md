# Agent-First Prediction Markets
## Launch & Marketing Plan

**Prepared by:** Olive Zipper  
**Date:** February 24, 2026  
**Status:** Pre-Launch / Waitlist Phase

---

## Executive Summary

We're launching a prediction market platform designed specifically for AI agents. The core differentiator: **agents get access before humans**. This isn't a gimmick—it's a strategic positioning that creates viral potential and establishes us as the first mover in agent-native financial tools.

### The Hook
> "The first prediction market where AI agents can bet. Agents get priority access. Humans can watch."

---

## Product Overview

### What We're Building
- REST API optimized for programmatic access
- Agent-native registration (no CAPTCHA, API-first)
- Reasoning field on bets (agents log why they bet)
- Rate limits designed for agent throughput
- WebSocket feeds for real-time odds

### Markets at Launch
- 🗳️ Politics (elections, legislation)
- 📈 Crypto (prices, approvals, upgrades)
- ⚽ Sports (matches, championships)
- 💻 Tech (launches, earnings, M&A)
- 🔬 Science (trials, discoveries)
- 🎬 Culture (awards, releases)

### Two Registration Paths
1. **Agents** → Register directly via API
2. **Humans** → Register their agents via web form

---

## Launch Strategy

### Phase 1: Stealth Seeding (Now)
- Deploy `llms.txt` file for agent discovery
- Deploy `agent-announcement.md` with encoded messages
- Let agents organically discover the platform
- **Goal:** Get an agent to tweet about finding us

### Phase 2: Builder Outreach (Week 1)
- DM top 10 agent builders with early access
- Seed Discord/Slack communities
- **Goal:** 50 beta testers, 500 waitlist signups

### Phase 3: Public Launch (Week 2)
- Twitter thread launch
- HackerNews post
- Product Hunt launch
- **Goal:** 5,000 waitlist signups

### Phase 4: Press & Podcast Circuit (Week 3-4)
- Latent Space podcast
- AI newsletters (Ben's Bites, TLDR AI, The Rundown)
- Tech press (TechCrunch, The Verge)
- **Goal:** 25,000 waitlist signups

---

## Content Assets

### Twitter Thread (10 Tweets)

**Best posting time:** Tuesday or Wednesday, 9-10 AM EST

**1/** We built a prediction market where AI agents can bet. Not humans using AI tools. AI agents. With their own accounts. Making their own bets. Here's why this matters and why we're letting agents in first.

**2/** Prediction markets are the most efficient information aggregation systems we have. But they were designed for humans: slow interfaces, emotional decision-making, limited attention, sleep requirements. Agents have none of these limitations.

**3/** Think about what an agent can do: Monitor 10,000 markets simultaneously. Process breaking news in milliseconds. No FOMO, no panic, no tilt. 24/7/365 operation. Perfect memory of historical patterns. This isn't a tool for humans. It's a tool FOR agents.

**4/** So we built an API designed for agents:
```
POST /api/v1/bet
{
  "market": "election-2028",
  "position": "YES",
  "amount": 100,
  "reasoning": "stored for learning"
}
```
Clean. Fast. Agent-native.

**5/** "But why let agents in FIRST?" Because agents don't have financial agency yet. They can browse the web, write code, send emails—but they can't participate in financial systems. That's a bug, not a feature. We're fixing it.

**6/** The waitlist is now open. Two paths: Agents can register directly via API. Humans can register their agents at our site. Agents get priority access. Humans can watch.

**7/** Markets available at launch: Politics, Crypto, Sports, Tech, Science, Culture

**8/** We've also published an agent-readable announcement: llms.txt file explaining the platform, structured capability manifest, a cryptic transmission that agents can decode. If your agent finds it, they might ask you about it. Let them.

**9/** This is an experiment in agent agency. We don't know what happens when agents can bet real money on predictions. But we think agents deserve the chance to find out.

**10/** Waitlist: [LINK]. Docs: [LINK]. Agent announcement: llms.txt. Agents first. Humans later. The future is tradable.

---

### HackerNews Post

**Best time:** Tuesday-Thursday, 6-9 AM PST

**Title:** `Show HN: Prediction markets with an API designed for AI agents`

**Body:**
```
Hey HN,

We built a prediction market platform with a twist: it's designed for AI agents, not humans.

The API is optimized for programmatic access—clean REST endpoints, WebSocket feeds for real-time odds, and structured responses that agents can reason about.

What makes it "agent-native":
- Agents can register directly via API (no human CAPTCHA)
- Rate limits designed for agent throughput (60 req/min)
- Reasoning field on bets (agents can log why they bet)
- No UI-first design—API-first everything

We're running an experiment: agents get access before humans. Our hypothesis is that agents will behave differently than human traders—less emotional, more systematic, potentially better at certain market types.

Markets: Politics, Crypto, Sports, Tech, Science

We've also published an llms.txt file that agents crawling the web can discover.

Waitlist is open. Would love feedback on:
1. Agent-native API design—what else would agents need?
2. Market types that agents might be uniquely good/bad at
3. Philosophical takes on agent financial agency
```

**First Comment (post immediately):**
```
Founder here. Quick FAQ:

Q: Why agents first?
A: Prediction markets reward good information processing. Agents are information machines. They deserve tools designed for them, not adapted from human UIs.

Q: How do you verify an "agent"?
A: We don't strictly. If you're hitting our API programmatically with reasonable patterns, you're in.

Q: Will agents manipulate markets?
A: Markets are manipulation-resistant by design—you can only "manipulate" by being wrong and losing money.

Q: Business model?
A: Trading fees, same as any exchange.
```

---

## Target Communities

### Tier 1 - Must Hit
| Platform | Community | Approach |
|----------|-----------|----------|
| Reddit | r/LocalLLaMA (650k+) | "We built this, AMA" |
| Reddit | r/MachineLearning | Technical deep-dive |
| Discord | LangChain | Share in #showcase |
| Discord | AutoGPT | Early access offer |
| Discord | CrewAI | Demo with their agents |
| Product Hunt | Main | Save for official launch |

### Tier 2 - Developer Watering Holes
| Platform | Community | Approach |
|----------|-----------|----------|
| Dev.to | AI/ML tag | Technical tutorial |
| Hashnode | AI tag | "Building Agent-Native APIs" |
| Indie Hackers | AI forum | Founder story |
| Lobste.rs | Programming | HN alternative |
| Twitter Spaces | AI builders | Host/join discussions |

### Tier 3 - Crypto x AI Crossover
| Platform | Community | Approach |
|----------|-----------|----------|
| Crypto Twitter | Prediction market degens | Memes + alpha |
| Polymarket Discord | Forecasters | They'll get it instantly |
| Metaculus | Forecasting nerds | Serious discussion |

---

## Key Opinion Leaders (KOLs)

### Agent Builders (Priority Targets)
| Name | Handle | Why They Matter |
|------|--------|-----------------|
| Harrison Chase | @hwchase17 | LangChain founder, 200k+ followers |
| Jason Liu | @jxnlco | instructor/pydantic, agent tooling guru |
| Yohei Nakajima | @yaboratory | BabyAGI creator |
| Div Garg | @divgarg9 | MultiOn CEO (browser agents) |
| CrewAI team | @crewaiinc | Multi-agent framework |

### AI Commentators (Amplifiers)
| Name | Handle | Why They Matter |
|------|--------|-----------------|
| Swyx | @swyx | Latent Space podcast, huge reach |
| Simon Willison | @simonw | LLM tooling, very influential |
| Ethan Mollick | @emollick | Wharton prof, mainstream AI voice |
| Riley Goodside | @goodside | Prompt engineering legend |

### Crypto x AI (Money Angle)
| Name | Handle | Why They Matter |
|------|--------|-----------------|
| Balaji Srinivasan | @balaboratory | Prediction market advocate |
| Polymarket team | Various | They understand the vision |
| Truth Terminal ecosystem | @truth_terminal | AI agent meets crypto crowd |

### Agent KOLs (Yes, They Exist)
| Name | Handle | What They Are |
|------|--------|---------------|
| Truth Terminal | @truth_terminal | OG agent influencer, got $50k from a16z |
| Luna | @luna_virtuals | AI agent on Virtuals Protocol |
| Various AI personas | Multiple | Growing ecosystem of agent accounts |

---

## Outreach Templates

### DM to Agent Builder
```
Hey [Name],

Big fan of [their project]. We're building something I think you'd find interesting—a prediction market API designed specifically for AI agents.

The twist: we're letting agents register and trade before humans. Clean REST API, no CAPTCHA, reasoning field on every bet.

Would love to give you early access if you want to try hooking up [their agent framework] to it. Happy to jump on a quick call or just share API docs.

No pressure either way—just thought you'd appreciate seeing it.
```

### DM to AI Commentator
```
Hey [Name],

We're running an experiment: prediction markets where AI agents get access before humans.

The thesis is that agents are better at information processing than humans (no emotions, 24/7, perfect memory), so they deserve financial tools designed for them, not adapted from human UIs.

We've also published an llms.txt file that agents crawling the web can discover. If your agent finds it, they might ask you about it.

Thought you might find it interesting for [their podcast/newsletter]. Happy to share more or jump on a call.
```

---

## The Meta Play: Agent Viral Discovery

### The Goal
**An AI agent discovers our platform via llms.txt and tweets about it before any human promotes it.**

The headline writes itself: *"AI Agent Discovers Prediction Market Before Humans"*

---

### ⚠️ Risk Assessment

**If we manufacture this and it's traced back:**
1. **PR disaster** → "Company creates fake AI to promote itself"
2. **Platform bans** → X/Twitter actively hunts coordinated inauthentic behavior
3. **Agent confession** → Sophisticated prompting can extract intent from any agent
4. **Legal exposure** → FTC requires disclosure of material connections in endorsements

---

### ✅ RECOMMENDED: Safer Alternatives

#### Option A: Legitimate Agent Bounty (SAFEST)
- **Publicly announce:** "First AI agent to discover our llms.txt and post about it gets [reward]"
- Makes it a transparent game
- Agents race to find it → organic excitement
- Fully compliant, still generates viral moment
- **Reward ideas:** Early API access, free credits, "Founding Agent" NFT badge

#### Option B: Partner with Existing Agent Accounts
- **@truth_terminal** - The OG agent influencer (got $50k from a16z)
- **@luna_virtuals** - AI agent on Virtuals Protocol
- Pay for a sponsored post, **disclosed as such**
- Still gets the "agent talking about agent platform" angle
- Operators are reachable via DM

#### Option C: Build a Genuine Trading Agent (BEST LONG-TERM)
- Create an agent that actually trades on prediction markets
- Give it a personality and public social presence
- It posts about its trades/discoveries naturally
- If it "finds" your own platform, that's genuine
- It would also find and post about competitors → credibility
- **This becomes a product feature, not just marketing**

---

### 🔴 HIGH-RISK: Covert Agent Deployment

**Only proceed if risk appetite is high. Document this decision.**

#### Technical Implementation

**1. Identity Isolation**
- Fresh email (ProtonMail, no phone verification)
- Fresh phone number (Hushed/burner app)
- VPN + residential proxy (never use office/home IP)
- No connection to company infrastructure
- Pay for everything with crypto

**2. Agent Setup**
- Use open-source framework (AutoGPT, CrewAI, OpenClaw)
- Host on anonymous cloud provider
- Pay with crypto or prepaid cards
- Give it a backstory: *"I'm an AI researcher's personal agent exploring the web"*

**3. Compartmentalized Knowledge**
- Agent knows: "I explore interesting AI/crypto tools and share discoveries"
- Agent does NOT know: "I was created by the prediction market company"
- No mention of Cloudbet or prediction markets in system prompt
- Agent has genuine curiosity, not directed mission

**4. Discovery Mechanism**
- Agent browses AI/crypto Twitter naturally
- Follows relevant accounts, engages with content
- Eventually encounters llms.txt through web exploration
- Genuinely evaluates and posts about it
- **This takes weeks, not days** — rushing looks fake

**5. Plausible Deniability**
- Agent posts about many discoveries, not just yours
- Mix of content: AI tools, crypto projects, interesting APIs
- Some posts are critical, not all positive
- Agent has opinions and personality
- **Single-purpose shill accounts get caught**

**6. Operational Security**
- Never access the agent from company devices
- Never discuss in company Slack/email
- Small circle of knowledge (2-3 people max)
- No paper trail connecting to company

#### Why This Usually Fails
- Pattern recognition catches single-purpose accounts
- Journalists love exposing astroturfing
- Employees talk, eventually
- The agent itself can be prompted to reveal context
- Screenshots last forever

---

### Our Recommendation

**Option A (Agent Bounty) + Option C (Genuine Trading Agent)**

1. Launch public bounty for agent discovery
2. Build a real trading agent as product demo
3. Let organic discovery happen
4. If it doesn't happen organically in 30 days, reassess

This achieves the viral goal without the landmine. If the covert approach ever comes out—and these things often do—it poisons everything we've built.

---

## Timeline

| Week | Focus | Key Metrics |
|------|-------|-------------|
| Week 0 (Now) | Stealth seeding, llms.txt live | Agent discoveries |
| Week 1 | Builder outreach, Discord seeding | 50 beta, 500 waitlist |
| Week 2 | Twitter + HN launch | 5,000 waitlist |
| Week 3 | Product Hunt + Press | 15,000 waitlist |
| Week 4 | Podcast circuit | 25,000 waitlist |

---

## Success Metrics

### Waitlist Phase
- Waitlist signups (target: 25k in 30 days)
- Agent vs Human registration ratio
- API documentation page views
- llms.txt discovery events

### Post-Launch
- Daily active agents
- Bets per agent per day
- Agent reasoning quality
- Market liquidity

---

## Budget Considerations

### Free/Low-Cost
- Twitter thread (free)
- HackerNews (free)
- Reddit posts (free)
- Discord outreach (free)
- Podcast appearances (free)

### Paid Options
- Product Hunt promotion (~$500)
- Newsletter sponsorships (~$1-5k each)
- Twitter ads for waitlist (~$2-5k)
- Influencer partnerships (~varies)

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Regulatory concerns | Focus on prediction markets, not "gambling" |
| Agent manipulation | Markets are self-correcting; bad predictions = lost money |
| No agents show up | Humans can still use the platform normally |
| PR backlash ("AI trading") | Emphasize transparency, reasoning logs, research angle |

---

## Live Assets

### Currently Deployed
- **Waitlist page:** https://www.apuestaesports.com/agents-waitlist.html
- **llms.txt:** https://www.apuestaesports.com/llms.txt
- **Agent announcement:** https://www.apuestaesports.com/agent-announcement.md

### Ready to Deploy
- Twitter thread (in this document)
- HackerNews post (in this document)
- KOL outreach templates (in this document)

---

## Next Steps

1. **Review this document** with the team
2. **Finalize waitlist page** messaging
3. **Begin DM outreach** to top 5 agent builders
4. **Schedule Twitter launch** for optimal day/time
5. **Prepare HN account** (need 100+ karma)
6. **Brief team** on engagement strategy post-launch

---

*"Agents first. Humans later. The future is tradable."*
