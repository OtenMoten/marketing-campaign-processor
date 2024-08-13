"""
📚 The Jedi Archives 🧠

This module contains the ancient wisdom of data analysis, passed down through generations
of Jedi analysts. Here, raw data is transformed into actionable intelligence that can turn
the tide of the galactic marketing war.
"""

import pandas as pd
from typing import Dict
import logging
from config import AnalysisConfig
from data_handling import CSVDataLoader
from visualization import ChartCreator

logger = logging.getLogger(__name__)


class DataAnalyzer:
    """
    🧙‍♂️ The Jedi Master of data analysis, capable of extracting deep insights from the Force of Data.
    """

    @staticmethod
    def analyze_campaign_performance(dataframe: pd.DataFrame) -> Dict[str, pd.Series]:
        """
        📊 Analyze the performance of our marketing campaigns across the galaxy.

        Args:
            dataframe (pd.DataFrame): Input data containing campaign information

        Returns:
            Dict[str, pd.Series]: Dictionary of analyzed metrics

        Raises:
            ValueError: If required columns are missing from the dataframe
        """
        required_columns = {'Campaign', 'Revenue', 'Platform', 'Impressions', 'Clicks', 'Conversions', 'Engagement_Rate'}
        if not required_columns.issubset(dataframe.columns):
            missing = required_columns - set(dataframe.columns)
            raise ValueError(f"🚫 Missing required columns: {', '.join(missing)}")

        return {
            'revenue': dataframe.groupby('Campaign')['Revenue'].sum().sort_values(ascending=False),
            'ctr': (dataframe.groupby('Campaign')['Clicks'].sum() / dataframe.groupby('Campaign')['Impressions'].sum()).sort_values(ascending=False),
            'conversion_rate': (dataframe.groupby('Campaign')['Conversions'].sum() / dataframe.groupby('Campaign')['Clicks'].sum()).sort_values(ascending=False),
            'engagement_by_platform': dataframe.groupby('Platform')['Engagement_Rate'].mean(),
            'impressions_by_platform': dataframe.groupby('Platform')['Impressions'].sum()
        }

    @staticmethod
    def analyze_platform_performance(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        🔬 Compare the performance of different platforms, like comparing the capabilities of X-wings and TIE fighters.

        Args:
            dataframe (pd.DataFrame): Input data containing platform information

        Returns:
            pd.DataFrame: Analyzed platform performance data
        """
        daily_metrics = dataframe.groupby(['Date', 'Platform']).agg({
            'Engagement_Rate': 'mean',
            'Impressions': 'sum',
            'Clicks': 'sum',
            'Conversions': 'sum'
        }).reset_index()

        daily_metrics['CTR'] = daily_metrics['Clicks'] / daily_metrics['Impressions']
        daily_metrics['Conversion_Rate'] = daily_metrics['Conversions'] / daily_metrics['Clicks']

        return daily_metrics


class MarketingAnalyzer:
    """
    🏛️ The Jedi Council of our analysis mission, orchestrating the entire analytical process.
    """

    def __init__(self, config: AnalysisConfig):
        """
        Initialize the MarketingAnalyzer.

        Args:
            config (AnalysisConfig): Configuration for the analysis
        """
        self.config = config
        self.data_loader = CSVDataLoader()

    def run_analysis(self) -> None:
        """
        🚀 Execute our analysis mission, from data retrieval to insight generation.

        Raises:
            ValueError: If no valid data is found
            Exception: For any other errors during analysis
        """
        try:
            all_data = self._load_all_data()
            if all_data.empty:
                raise ValueError("🕳️ Our intelligence network came up empty. Abort mission.")

            performance_data = DataAnalyzer.analyze_campaign_performance(all_data)
            platform_performance = DataAnalyzer.analyze_platform_performance(all_data)

            self._create_output_folder()
            ChartCreator.create_performance_charts(performance_data, self.config.output_folder)
            ChartCreator.create_platform_comparison(platform_performance, self.config.output_folder / 'platform_comparison.png')

            self._print_top_campaigns(performance_data['revenue'])
        except Exception as e:
            logger.error(f"🌑 The dark side clouds everything. Analysis failed: {str(e)}")
            raise

    def _load_all_data(self) -> pd.DataFrame:
        """
        📡 Gather all intelligence from our data sectors.

        Returns:
            pd.DataFrame: Combined data from all sources

        Raises:
            FileNotFoundError: If no CSV files are found in the data folder
        """
        data_files = list(self.config.data_folder.glob('*.csv'))
        if not data_files:
            raise FileNotFoundError(f"🚫 No CSV files found in {self.config.data_folder}")

        dataframes = [self.data_loader.load_data(file) for file in data_files]
        return pd.concat(dataframes, ignore_index=True)

    def _create_output_folder(self) -> None:
        """
        🗄️ Prepare a secure vault for our analysis artifacts.

        Returns:
            None
        """
        self.config.output_folder.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _print_top_campaigns(revenue_data: pd.Series, top_n: int = 3) -> None:
        """
        🏆 Announce the most successful campaigns, like awarding medals after the Battle of Yavin.

        Args:
            revenue_data (pd.Series): Series containing campaign revenues
            top_n (int): Number of top campaigns to display (default: 3)

        Returns:
            None
        """
        logger.info(f"🥇 Top {top_n} Campaigns by Revenue:")
        for campaign, revenue in revenue_data.head(top_n).items():
            logger.info(f"🚀 {campaign}: {revenue:.2f}")
