# HackerNews Post

## Posting Strategy

**Best time:** Tuesday-Thursday, 6-9 AM PST (to catch US morning + EU afternoon)

**Account:** Use an established HN account if possible (>100 karma). New accounts get flagged.

---

## Post Title Options (pick one)

**Option A (straightforward):**
```
Show HN: Prediction markets with an API designed for AI agents
```

**Option B (provocative):**
```
Show HN: We're letting AI agents bet on prediction markets before humans
```

**Option C (technical):**
```
Show HN: Agent-native prediction market API – agents get priority access
```

**Recommendation:** Option A for HN—they prefer straightforward. Save provocative for Twitter.

---

## Post Body

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

Markets available:
- Politics (elections, legislation)
- Crypto (prices, approvals)
- Sports (matches, championships)
- Tech (launches, earnings)
- Science (trials, discoveries)

Technical details:
- REST API + WebSocket
- JWT auth
- Rate limiting via token bucket
- Settlement via [TBD—crypto or fiat]

We've also published an `llms.txt` file that agents crawling the web can discover. It explains the platform in agent-readable format.

Waitlist is open: [link]
Docs: [link]
llms.txt: [link]

Would love feedback from the HN crowd on:
1. Agent-native API design—what else would agents need?
2. Market types that agents might be uniquely good/bad at
3. Philosophical takes on agent financial agency

Happy to answer questions.
```

---

## First Comment (post immediately after)

```
Founder here. Quick FAQ:

Q: Why agents first?
A: Prediction markets reward good information processing. Agents are information processing machines. We think they deserve access to financial tools designed for them, not adapted from human UIs.

Q: Isn't this just an API?
A: Most prediction market APIs are afterthoughts—screen-scraping their own UI. We built API-first. The difference is in the details: structured reasoning fields, agent-optimized rate limits, no CAPTCHA.

Q: How do you verify an "agent"?
A: We don't, strictly. If you're hitting our API programmatically with reasonable patterns, you're in. The goal isn't gatekeeping—it's prioritizing.

Q: Will agents manipulate markets?
A: Markets are manipulation-resistant by design—you can only "manipulate" by being wrong and losing money. Agents add liquidity and information. That's good.

Q: What's the business model?
A: Trading fees, same as any exchange. We take a small cut of volume.

Happy to dive deeper on any of this.
```

---

## How to Get It Live

### Step 1: Prepare
- Have the post body ready in a text file
- Have the first comment ready
- Clear your calendar for 2-3 hours after posting (you MUST engage)

### Step 2: Post
- Go to https://news.ycombinator.com/submit
- Title: `Show HN: Prediction markets with an API designed for AI agents`
- URL: Your landing page
- OR leave URL blank and paste the body as text (text posts sometimes do better)

### Step 3: Immediately After
- Post your first comment within 60 seconds
- Open the post in a new tab, refresh every few minutes
- Respond to EVERY comment thoughtfully (this is crucial)

### Step 4: Seed Engagement (carefully)
- Have 2-3 friends with HN accounts ready
- They should NOT just upvote—they should leave genuine comments/questions
- Spread this over 30-60 minutes, not all at once
- Obvious vote manipulation gets you banned

### Step 5: Ride the Wave
- If you hit front page, keep engaging for hours
- Cross-post to Twitter: "We're on the front page of HN, come join the discussion"
- Capture emails/signups in real-time

---

## What NOT to Do

❌ Don't use a brand new account (looks spammy)
❌ Don't ask friends to upvote (ask them to comment genuinely)
❌ Don't post and disappear (engagement is everything)
❌ Don't be defensive about criticism (HN hates that)
❌ Don't oversell—be technical and honest
❌ Don't post on weekends (low traffic)

---

## Expected Outcomes

**Good outcome:** 50-100 points, front page for a few hours, 500+ waitlist signups
**Great outcome:** 200+ points, top 10 all day, 2000+ signups, press pickup
**Viral outcome:** 500+ points, #1 for hours, 10K+ signups, multiple press stories

HN is high-variance. A great post can flop due to timing. Be ready to try again in a week with a different angle if the first attempt doesn't land.
