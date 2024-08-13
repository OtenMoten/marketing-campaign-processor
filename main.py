# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de

"""
🌟 Galactic Marketing Analyzer 🚀

In a data galaxy far, far away...

The Rebel Alliance's Marketing Division seeks to analyze the performance of their
campaigns across the vast reaches of the cosmos. This script, much like the plans
for the Death Star, brings together all the components needed to unveil the secrets
of successful galactic marketing strategies.

May the Force of Data be with you! 💫

Usage:
    python main.py [--dry-run]

Options:
    --dry-run    Run with simulated data (like a training simulation on Dagobah)
"""

import argparse
import sys
from config import get_config
from analysis import MarketingAnalyzer
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def parse_arguments() -> argparse.Namespace:
    """
    Intercept the rebel transmission (command-line arguments).

    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(description="🌌 Galactic Marketing Performance Analyzer")
    parser.add_argument("--dry-run", action="store_true", help="Run with simulated data (like a training simulation on Dagobah)")
    return parser.parse_args()


def main() -> None:
    """
    The main function - our Millennium Falcon that carries us through the analysis journey.

    This function orchestrates the entire analysis process, from gathering intelligence
    to presenting the final results.
    """
    try:
        args = parse_arguments()
        config = get_config(args)
        print("\n🚀 Initiating Hyperdrive to Analysis Galaxy 🌠")
        analyzer = MarketingAnalyzer(config)
        analyzer.run_analysis()
        print("\n🎉 Mission Accomplished: Analysis Complete 🏆")
    except Exception as e:
        logger.error(f"🚨 We've been hit! Unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
