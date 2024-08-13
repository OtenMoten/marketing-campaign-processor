"""
🕵️ The Rebel Intelligence Network 📡

This module is responsible for gathering and decoding intelligence from across the galaxy.
Whether intercepting Imperial transmissions or decoding Rebel messages, this is where raw data
becomes valuable information.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
import random
from datetime import datetime, timedelta
import logging
from typing import List

logger = logging.getLogger(__name__)


class DataLoader(ABC):
    """
    🔐 The abstract base class for our data spies. Each spy has their own method of extracting information.
    """

    @abstractmethod
    def load_data(self, file_path: Path) -> pd.DataFrame:
        """
        📥 Load data from the given file path.

        Args:
            file_path (Path): Path to the data file

        Returns:
            pd.DataFrame: Loaded data
        """
        pass


class CSVDataLoader(DataLoader):
    """
    📊 A specialized spy that decodes CSV transmissions.
    """

    def load_data(self, file_path: Path) -> pd.DataFrame:
        """
        📥 Load data from a CSV file.

        Args:
            file_path (Path): Path to the CSV file

        Returns:
            pd.DataFrame: Loaded data

        Raises:
            Exception: If there's an error reading the file
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            logger.error(f"🚨 Transmission interrupted. Error decoding file {file_path}: {str(e)}")
            return pd.DataFrame()


class DataSimulator:
    """
    🎮 The holodeck of our starship, capable of generating simulated campaign data for training purposes.
    """

    @staticmethod
    def generate_campaign_names(num_campaigns: int) -> List[str]:
        """
        🏷️ Generate unique codenames for our marketing campaigns, like call signs for X-wing squadrons.

        Args:
            num_campaigns (int): Number of campaign names to generate

        Returns:
            List[str]: List of generated campaign names
        """
        adjectives = ["Bold", "Smart", "Vibrant", "Sleek", "Dynamic", "Innovative", "Stellar", "Radiant", "Agile", "Zen"]
        nouns = ["Vision", "Quest", "Journey", "Horizon", "Leap", "Spark", "Wave", "Pulse", "Orbit", "Nexus"]
        return [f"{random.choice(adjectives)} {random.choice(nouns)} {i:03d}" for i in range(1, num_campaigns + 1)]

    @staticmethod
    def generate_simulated_data(num_campaigns: int, num_days: int) -> pd.DataFrame:
        """
        🌠 Create a holographic simulation of marketing data across the galaxy.

        Args:
            num_campaigns (int): Number of campaigns to simulate
            num_days (int): Number of days to simulate

        Returns:
            pd.DataFrame: Simulated marketing data
        """
        platforms = ['Facebook', 'Instagram']
        start_date = datetime(2024, 1, 1)
        campaigns = DataSimulator.generate_campaign_names(num_campaigns)

        data = []
        for campaign in campaigns:
            for platform in platforms:
                for day in range(num_days):
                    date = start_date + timedelta(days=day)
                    data.append({
                        "Date": date,
                        "Campaign": campaign,
                        "Platform": platform,
                        "Engagement_Rate": random.uniform(0.01, 0.15),
                        "Impressions": random.randint(10000, 1000000),
                        "Clicks": random.randint(100, 10000),
                        "Conversions": random.randint(10, 1000),
                        "Revenue": random.uniform(1000, 10000)
                    })

        return pd.DataFrame(data)

    @staticmethod
    def save_simulated_data(data: pd.DataFrame, folder: Path) -> None:
        """
        💾 Archive our simulated intelligence for future analysis.

        Args:
            data (pd.DataFrame): Simulated data to save
            folder (Path): Folder to save the data in

        Returns:
            None
        """
        folder.mkdir(parents=True, exist_ok=True)
        file_path = folder / "simulated_data.csv"
        data.to_csv(file_path, index=False)
        logger.info(f"💽 Holographic data archived at {file_path}")
