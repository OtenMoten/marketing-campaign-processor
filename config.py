"""
🧠 The Jedi Council's Wisdom 📜

This module contains the sacred texts of configuration, guiding our journey
through the stars of data analysis. Like the Force, it binds our galaxy of code together.
"""

import argparse
from dataclasses import dataclass
from pathlib import Path
import logging
from time import sleep

from data_handling import DataSimulator

logger = logging.getLogger(__name__)


@dataclass
class AnalysisConfig:
    """
    📊 The sacred texts of our analysis mission.

    Attributes:
        data_folder (Path): The coordinates of our data sector
        output_folder (Path): The destination for our analysis artifacts
        is_dry_run (bool): Whether we're running a holographic simulation
    """
    data_folder: Path
    output_folder: Path
    is_dry_run: bool


def get_user_input(prompt: str) -> str:
    """
    💬 Use the Force to receive guidance from the user.

    Args:
        prompt (str): The question to ask the user

    Returns:
        str: The user's response
    """
    sleep(0.5)
    print(prompt, end='')
    return input().strip()


def get_config(args: argparse.Namespace) -> AnalysisConfig:
    """
    🛠️ Assemble the sacred texts of configuration, like a Jedi constructing their lightsaber.

    Args:
        args (argparse.Namespace): Command-line arguments

    Returns:
        AnalysisConfig: The assembled configuration

    Raises:
        ValueError: If an invalid directory path is provided
    """
    logger.info("🌌 Gathering Intelligence from Across the Galaxy 🔭")
    if args.dry_run:
        logger.info("🎭 Initiating holographic simulation with data for 100 campaigns across 30 star systems")
        data_folder = Path('simulated_data')
        simulated_data = DataSimulator.generate_simulated_data(num_campaigns=100, num_days=30)
        DataSimulator.save_simulated_data(simulated_data, data_folder)
        logger.info("🏁 Holographic data generation complete.")
    else:
        logger.info("🗺️ Please provide the coordinates for our mission:")
        data_folder = Path(get_user_input("Enter the path to your marketing intelligence files: "))
        if not data_folder.is_dir():
            raise ValueError(f"🚫 Invalid sector coordinates: {data_folder}")

    output_folder = Path(get_user_input("Enter the coordinates for the mission report destination: "))
    return AnalysisConfig(data_folder, output_folder, args.dry_run)
