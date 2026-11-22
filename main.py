import os

PLAN = (
    "Sell missed-call text-back to US mobile detailers. "
    "Day 1: pull 300 in Texas off Google Maps; text owners: "
    "$149 setup + $29/mo, live in a day \u2014 a missed call is a lost job, "
    "so they buy same-day. $100: Twilio + domain. "
    "Demo it on your number, close 4 by day 14 ($596, +$29/mo each)."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
