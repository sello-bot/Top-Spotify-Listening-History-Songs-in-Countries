"""
🎵 Spotify Knowledge Map - Discover Your Musical Patterns

A comprehensive toolkit for analyzing Spotify listening history and uncovering
surprising patterns in your musical behavior.

Main modules:
- data_loader: Load and preprocess Spotify data
- pattern_analyzer: Core pattern analysis algorithms  
- visualizer: Create interactive visualizations
- insights_generator: Generate personalized insights

Example usage:
    from src import SpotifyAnalyzer
    
    analyzer = SpotifyAnalyzer('path/to/spotify_data.csv')
    patterns = analyzer.analyze_all_patterns()
    analyzer.create_knowledge_map()
"""

__version__ = "1.0.0"
__author__ = "Spotify Knowledge Map Contributors"
__email__ = "contact@example.com"

from .data_loader import SpotifyDataLoader
from .pattern_analyzer import PatternAnalyzer
from .visualizer import SpotifyVisualizer
from .insights_generator import InsightsGenerator

class SpotifyAnalyzer:
    """Main class for Spotify listening analysis."""
    
    def __init__(self, data_path: str):
        """Initialize analyzer with data file path."""
        self.loader = SpotifyDataLoader(data_path)
        self.analyzer = PatternAnalyzer()
        self.visualizer = SpotifyVisualizer()
        self.insights = InsightsGenerator()
        
    def analyze_all_patterns(self):
        """Run complete analysis pipeline."""
        df = self.loader.load_and_preprocess()
        patterns = self.analyzer.analyze_all(df)
        return patterns
        
    def create_knowledge_map(self):
        """Generate complete knowledge map with visualizations."""
        patterns = self.analyze_all_patterns()
        figures = self.visualizer.create_all_plots(patterns)
        insights = self.insights.generate_personal_profile(patterns)
        return {
            'patterns': patterns,
            'visualizations': figures,
            'insights': insights
        }

__all__ = [
    'SpotifyAnalyzer',
    'SpotifyDataLoader', 
    'PatternAnalyzer',
    'SpotifyVisualizer',
    'InsightsGenerator'
]
