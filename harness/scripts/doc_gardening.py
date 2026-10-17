"""Report document review reminders without changing dates or scheduling work."""
import argparse
from datetime import date
from checks.freshness import check_freshness

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of',type=date.fromisoformat)
    args=parser.parse_args()
    check_freshness(args.as_of)
