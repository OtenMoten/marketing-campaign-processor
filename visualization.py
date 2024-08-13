"""
🌌 The Hologram Projector 📽️

This module is our hologram projector, capable of creating visual representations of our data
that even a Hutt could understand. These visualizations are our secret weapon in communicating
the results of our analysis to the Rebel high command.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pandas as pd
from typing import Dict
import logging

logger = logging.getLogger(__name__)


class ChartCreator:
    """
    🎨 Our master hologram technician, capable of creating stunning visual representations of our data.
    """

    @staticmethod
    def set_style():
        """
        🖌️ Set the visual style of our holograms, ensuring they're worthy of a presentation to the Rebel Alliance.

        Returns:
            None
        """
        sns.set_theme(style="whitegrid")
        plt.rcParams['font.sans-serif'] = ['Arial']
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['xtick.labelsize'] = 10
        plt.rcParams['ytick.labelsize'] = 10

    @staticmethod
    def create_performance_charts(performance_data: Dict[str, pd.Series], output_folder: Path) -> None:
        """
        📊 Create a series of performance charts, like tactical displays in the Rebel war room.

        Args:
            performance_data (Dict[str, pd.Series]): Dictionary containing performance metrics
            output_folder (Path): Folder to save the output charts

        Returns:
            None
        """
        ChartCreator.set_style()
        ChartCreator._create_revenue_bar_chart(performance_data['revenue'], output_folder / 'revenue_performance.png')
        ChartCreator._create_ctr_conversion_scatter(performance_data['ctr'], performance_data['conversion_rate'], output_folder / 'ctr_vs_conversion.png')

    @staticmethod
    def _create_revenue_bar_chart(revenue_data: pd.Series, output_path: Path) -> None:
        """
        💰 Create a bar chart of campaign revenues, like comparing the size of Imperial Star Destroyers.

        Args:
            revenue_data (pd.Series): Series containing revenue data for each campaign
            output_path (Path): Path to save the output chart

        Returns:
            None
        """
        plt.figure(figsize=(20, 10))
        ax = sns.barplot(x=revenue_data.index, y=revenue_data.values)
        plt.title('Campaign Revenue Performance', fontweight='bold')
        plt.xlabel('Campaigns')
        plt.ylabel('Total Revenue ($)')
        plt.xticks(rotation=90, ha='right')
        for i, v in enumerate(revenue_data.values):
            ax.text(i, v, f'${v:.0f}', ha='center', va='bottom', rotation=90, fontsize=8)
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        logger.info(f"💾 Revenue chart saved as {output_path}")
        plt.close()

    @staticmethod
    def _create_ctr_conversion_scatter(ctr_data: pd.Series, conversion_rate_data: pd.Series, output_path: Path) -> None:
        """
        🎯 Create a scatter plot of CTR vs Conversion Rate, like mapping the positions of starships in a space battle.

        Args:
            ctr_data (pd.Series): Series containing Click-Through Rate data for each campaign
            conversion_rate_data (pd.Series): Series containing Conversion Rate data for each campaign
            output_path (Path): Path to save the output chart

        Returns:
            None
        """
        fig, ax = plt.subplots(figsize=(16, 12))
        sns.scatterplot(x=ctr_data, y=conversion_rate_data, s=100, ax=ax)

        top_campaigns = ctr_data.nlargest(10)
        for campaign, ctr in top_campaigns.items():
            conversion_rate = conversion_rate_data[campaign]
            ax.annotate(str(campaign),
                        (ctr, conversion_rate),
                        xytext=(5, 5),
                        textcoords='offset points',
                        fontsize=8,
                        alpha=0.7,
                        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

        ax.set_title('Click-Through Rate vs Conversion Rate by Campaign', fontweight='bold')
        ax.set_xlabel('Click-Through Rate')
        ax.set_ylabel('Conversion Rate')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        logger.info(f"💾 CTR vs Conversion chart saved as {output_path}")
        plt.close(fig)

    @staticmethod
    def create_platform_comparison(performance_data: pd.DataFrame, output_path: Path) -> None:
        """
        🚀 Create a comparison chart of different platforms, like comparing the capabilities of different starfighter models.

        Args:
            performance_data (pd.DataFrame): DataFrame containing performance data for different platforms
            output_path (Path): Path to save the output chart

        Returns:
            None
        """
        performance_data['Date'] = pd.to_datetime(performance_data['Date'])
        plt.figure(figsize=(16, 10))
        metrics = ['Engagement_Rate', 'CTR', 'Conversion_Rate']
        colors = ['blue', 'green', 'red']

        for i, metric in enumerate(metrics):
            plt.subplot(3, 1, i + 1)
            for platform in performance_data['Platform'].unique():
                platform_data = performance_data[performance_data['Platform'] == platform]
                plt.plot(platform_data['Date'], platform_data[metric],
                         label=f"{platform} {metric}", color=colors[i],
                         linestyle='-' if platform == 'Facebook' else '--')

            plt.title(f"{metric} Over Time", fontweight='bold')
            plt.xlabel('Date')
            plt.ylabel(metric)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        logger.info(f"💾 Platform comparison chart saved as {output_path}")
        plt.close()
