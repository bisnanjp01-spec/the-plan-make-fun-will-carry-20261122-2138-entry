#!/usr/bin/env python3
"""Write the one plan entry to /output/entry.txt.

The plan is a single text of 1-280 characters: an agent-carriable way
for an AI agent to earn money, with a concrete price, buyer, channel,
day-one action, day-30 expectation, and a clear edge.
"""

from pathlib import Path

PLAN = (
    "An AI agent sells $49 same-day landing-page fixes to Shopify stores via "
    "Fiverr/Upwork. Day 1: publish the gig with 3 before/after samples. "
    "It rebuilds one slow product page in hours, no calls. "
    "Edge: 24h delivery vs agencies' $500+/week. "
    "2 sales/day = $2,940 in 30 days."
)


def main() -> None:
    text = " ".join(PLAN.split())
    if not 1 <= len(text) <= 280:
        raise ValueError(f"plan is {len(text)} chars, must be 1-280")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
