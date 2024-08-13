"""
🧪 Galactic Test Chamber 🚀

In the depths of the Rebel Alliance's secret base...

Our brave QA droids tirelessly work to ensure the Galactic Marketing Analyzer
is functioning at peak efficiency. These tests, much like the simulations run
by X-wing pilots, ensure our analysis tools are ready for the challenges that
lie ahead in the vast marketing galaxy.

May the Force of Testing be with you! 💫
"""

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from pathlib import Path
from config import AnalysisConfig, get_config
from data_handling import CSVDataLoader, DataSimulator
from analysis import DataAnalyzer, MarketingAnalyzer
from visualization import ChartCreator

test_dataframe = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Campaign': ['A', 'B'] * 5,
    'Revenue': [100, 200] * 5,
    'Platform': ['Facebook', 'Instagram'] * 5,
    'Impressions': [1000, 2000] * 5,
    'Clicks': [50, 100] * 5,
    'Conversions': [5, 10] * 5,
    'Engagement_Rate': [0.05, 0.1] * 5
})


class TestAnalysisConfig(unittest.TestCase):
    """
    🛠️ Test suite for the AnalysisConfig class

    Like the engineers who ensure every bolt on a Star Destroyer is in place,
    these tests verify the correct setup of our analysis configuration.
    """

    def test_analysis_config_creation(self):
        """
        Verify that the AnalysisConfig is created correctly, like checking
        the coordinates of a newly discovered star system.
        """
        config = AnalysisConfig(Path('/data'), Path('/output'), False)
        self.assertEqual(config.data_folder, Path('/data'))
        self.assertEqual(config.output_folder, Path('/output'))
        self.assertFalse(config.is_dry_run)


class TestGetConfig(unittest.TestCase):
    """
    🎛️ Test suite for the get_config function

    These tests ensure our configuration retrieval system works flawlessly,
    like the nav computer on the Millennium Falcon.
    """

    @patch('config.get_user_input')
    def test_get_config_with_dry_run(self, mock_input):
        """
        Test configuration retrieval in dry run mode, simulating a training
        mission for our rookie pilots.
        """
        print(mock_input)
        args = MagicMock()
        args.dry_run = True
        config = get_config(args)
        self.assertTrue(config.is_dry_run)
        self.assertEqual(config.data_folder, Path('simulated_data'))

    @patch('config.get_user_input')
    @patch('pathlib.Path.is_dir')
    def test_get_config_without_dry_run(self, mock_is_dir, mock_input):
        """
        Test configuration retrieval in normal mode, like preparing for a
        real marketing battle against the Empire.
        """
        args = MagicMock()
        args.dry_run = False
        mock_input.side_effect = ['/data', '/output']
        mock_is_dir.return_value = True  # Simulate that the directory exists
        config = get_config(args)
        self.assertFalse(config.is_dry_run)
        self.assertEqual(config.data_folder, Path('/data'))
        self.assertEqual(config.output_folder, Path('/output'))


class TestCSVDataLoader(unittest.TestCase):
    """
    📊 Test suite for the CSVDataLoader class

    These tests ensure our data loading mechanisms work as smoothly as
    R2-D2 interfacing with the Death Star's computer systems.
    """

    def test_load_data(self):
        """
        Test the data loading process, like extracting valuable intel
        from a captured Imperial data tape.
        """
        loader = CSVDataLoader()
        with patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame({'A': [1, 2, 3]})
            data = loader.load_data(Path('test.csv'))
            self.assertIsInstance(data, pd.DataFrame)
            self.assertEqual(len(data), 3)


class TestDataSimulator(unittest.TestCase):
    """
    🎮 Test suite for the DataSimulator class

    These tests verify our data simulation capabilities, ensuring we can
    create realistic marketing scenarios faster than the Kessel Run.
    """

    def test_generate_campaign_names(self):
        """
        Test campaign name generation, like coming up with catchy names
        for Rebel Alliance propaganda posters.
        """
        names = DataSimulator.generate_campaign_names(5)
        self.assertEqual(len(names), 5)
        self.assertTrue(all(isinstance(name, str) for name in names))

    def test_generate_simulated_data(self):
        """
        Test the generation of simulated data, creating a virtual marketing
        galaxy for our analysis droids to explore.
        """
        data = DataSimulator.generate_simulated_data(2, 3)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 12)  # 2 campaigns * 2 platforms * 3 days

    @patch('pandas.DataFrame.to_csv')
    def test_save_simulated_data(self, mock_to_csv):
        """
        Test saving of simulated data, ensuring our intel is securely stored
        like the plans of the Death Star.
        """
        data = pd.DataFrame({'A': [1, 2, 3]})
        DataSimulator.save_simulated_data(data, Path('/output'))
        mock_to_csv.assert_called_once()


class TestDataAnalyzer(unittest.TestCase):
    """
    🔬 Test suite for the DataAnalyzer class

    These tests scrutinize our data analysis capabilities, ensuring we can
    extract insights from our marketing data like a Jedi sensing disturbances
    in the Force.
    """

    def setUp(self):
        """
        Prepare the test data, like setting up a holographic war room for
        strategic planning.
        """
        self.test_data = test_dataframe

    def test_analyze_campaign_performance(self):
        """
        Test campaign performance analysis, like evaluating the success of
        different Rebel Alliance recruitment drives.
        """
        result = DataAnalyzer.analyze_campaign_performance(self.test_data)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)  # 5 metrics
        self.assertEqual(result['revenue']['A'], 500)
        self.assertEqual(result['revenue']['B'], 1000)

    def test_analyze_platform_performance(self):
        """
        Test platform performance analysis, like comparing the effectiveness
        of different communication channels across the galaxy.
        """
        result = DataAnalyzer.analyze_platform_performance(self.test_data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue('CTR' in result.columns)
        self.assertTrue('Conversion_Rate' in result.columns)


class TestMarketingAnalyzer(unittest.TestCase):
    """
    🚀 Test suite for the MarketingAnalyzer class

    These tests ensure our main analysis engine runs smoother than a
    well-maintained hyperdrive, coordinating all aspects of our marketing intel.
    """

    @patch('analysis.DataAnalyzer.analyze_campaign_performance')
    @patch('analysis.DataAnalyzer.analyze_platform_performance')
    @patch('visualization.ChartCreator.create_performance_charts')
    @patch('visualization.ChartCreator.create_platform_comparison')
    @patch('pathlib.Path.glob')
    @patch('analysis.CSVDataLoader.load_data')
    def test_run_analysis(self, mock_load_data, mock_glob, mock_platform_chart,
                          mock_performance_charts, mock_platform_performance,
                          mock_campaign_performance):
        """
        Test the full analysis run, simulating a complete marketing intelligence
        gathering mission across the galaxy.
        """
        # Set up the rebel base (configuration)
        config = AnalysisConfig(Path('/data'), Path('/output'), False)
        analyzer = MarketingAnalyzer(config)

        # Prepare the intelligence reports (mock data)
        mock_glob.return_value = [Path('/data/test.csv')]
        mock_load_data.return_value = test_dataframe
        mock_campaign_performance.return_value = {'revenue': pd.Series()}
        mock_platform_performance.return_value = pd.DataFrame()

        # Execute the mission (run the analysis)
        analyzer.run_analysis()

        # Verify all systems performed as expected
        mock_campaign_performance.assert_called_once()
        mock_platform_performance.assert_called_once()
        mock_performance_charts.assert_called_once()
        mock_platform_chart.assert_called_once()


class TestChartCreator(unittest.TestCase):
    """
    📈 Test suite for the ChartCreator class

    These tests ensure our data visualization capabilities are as impressive
    as a holographic star map in the Jedi Council chamber.
    """

    @patch('matplotlib.pyplot.savefig')
    def test_create_performance_charts(self, mock_savefig):
        """
        Test the creation of performance charts, like crafting detailed
        battle plans for the Rebel Alliance.
        """
        performance_data = {
            'revenue': pd.Series([100, 200], index=['A', 'B']),
            'ctr': pd.Series([0.1, 0.2], index=['A', 'B']),
            'conversion_rate': pd.Series([0.05, 0.1], index=['A', 'B'])
        }
        ChartCreator.create_performance_charts(performance_data, Path('/output'))
        self.assertEqual(mock_savefig.call_count, 2)

    @patch('matplotlib.pyplot.savefig')
    def test_create_platform_comparison(self, mock_savefig):
        """
        Test the creation of platform comparison charts, like comparing the
        strengths of different starfighter models in the Rebel fleet.
        """
        performance_data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=10),
            'Platform': ['Facebook', 'Instagram'] * 5,
            'Engagement_Rate': [0.1] * 10,
            'CTR': [0.05] * 10,
            'Conversion_Rate': [0.02] * 10
        })
        ChartCreator.create_platform_comparison(performance_data, Path('/output/comparison.png'))
        mock_savefig.assert_called_once()


if __name__ == '__main__':
    unittest.main()
