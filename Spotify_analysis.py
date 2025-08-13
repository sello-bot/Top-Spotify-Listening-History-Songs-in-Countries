#!/usr/bin/env python3
"""
🎵 Spotify Personal Knowledge Map - Main Analysis Script
========================================================

Discover surprising patterns in your Spotify listening behavior!
This script analyzes your listening history and creates an interactive knowledge map.

Usage:
    python spotify_analysis.py --data path/to/spotify_history.csv
    python spotify_analysis.py --kaggle  # For Kaggle environment

Author: Your Name
Version: 1.0.0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import argparse
import sys
import warnings
warnings.filterwarnings('ignore')


class SpotifyKnowledgeMapper:
    """Main class for analyzing Spotify listening patterns."""
    
    def __init__(self, data_path=None, kaggle_mode=False):
        """Initialize the analyzer with data path or Kaggle mode."""
        self.kaggle_mode = kaggle_mode
        self.data_path = data_path
        self.df = None
        self.insights = []
        
    def load_data(self):
        """Load Spotify data from file or Kaggle input."""
        print("🎵 Loading Spotify data...")
        
        if self.kaggle_mode:
            # Kaggle paths
            try:
                self.df = pd.read_csv('/kaggle/input/top-spotify-songs-in-countries/spotify_history.csv')
                print(f"✅ Loaded {len(self.df):,} listening records from Kaggle")
            except FileNotFoundError:
                print("❌ Kaggle input file not found. Please upload your Spotify data.")
                return False
        else:
            # Local file path
            try:
                self.df = pd.read_csv(self.data_path)
                print(f"✅ Loaded {len(self.df):,} listening records")
            except FileNotFoundError:
                print(f"❌ File not found: {self.data_path}")
                return False
                
        print(f"📊 Available columns: {list(self.df.columns)}")
        return True
        
    def preprocess_data(self):
        """Clean and prepare data for analysis."""
        print("🔧 Preprocessing data...")
        
        # Find and convert datetime column
        datetime_cols = [col for col in self.df.columns 
                        if any(term in col.lower() for term in ['time', 'date', 'ts'])]
        
        if datetime_cols:
            time_col = datetime_cols[0]
            self.df['timestamp'] = pd.to_datetime(self.df[time_col])
            
            # Extract time features
            self.df['hour'] = self.df['timestamp'].dt.hour
            self.df['day_of_week'] = self.df['timestamp'].dt.day_name()
            self.df['month'] = self.df['timestamp'].dt.month_name()
            self.df['year'] = self.df['timestamp'].dt.year
            self.df['date'] = self.df['timestamp'].dt.date
            
            print(f"⏰ Date range: {self.df['timestamp'].min()} to {self.df['timestamp'].max()}")
        else:
            print("⚠️ No timestamp column found - temporal analysis will be limited")
            
        # Standardize column names
        column_mapping = {
            'master_metadata_track_name': 'trackName',
            'master_metadata_album_artist_name': 'artistName',
            'master_metadata_album_album_name': 'albumName'
        }
        
        for old_name, new_name in column_mapping.items():
            if old_name in self.df.columns:
                self.df[new_name] = self.df[old_name]
                
        print("✅ Data preprocessing complete!")
        
    def analyze_temporal_patterns(self):
        """Analyze when you listen to music most."""
        print("\n🕐 ANALYZING TEMPORAL PATTERNS")
        print("="*50)
        
        if 'timestamp' not in self.df.columns:
            print("⚠️ No timestamp data available for temporal analysis")
            return {}
            
        patterns = {}
        
        # Peak listening hour
        if 'hour' in self.df.columns:
            hourly_counts = self.df['hour'].value_counts().sort_index()
            peak_hour = hourly_counts.idxmax()
            patterns['peak_hour'] = peak_hour
            
            # Classify listening personality
            if 5 <= peak_hour < 12:
                patterns['temporal_personality'] = "Morning music person"
                patterns['personality_emoji'] = "🌅"
            elif 12 <= peak_hour < 17:
                patterns['temporal_personality'] = "Afternoon listener"
                patterns['personality_emoji'] = "☀️"
            elif 17 <= peak_hour < 22:
                patterns['temporal_personality'] = "Evening music lover"
                patterns['personality_emoji'] = "🌆"
            else:
                patterns['temporal_personality'] = "Night owl listener"
                patterns['personality_emoji'] = "🌙"
                
            print(f"{patterns['personality_emoji']} You're a {patterns['temporal_personality']} (peak at {peak_hour}:00)")
            self.insights.append(f"{patterns['personality_emoji']} You're a {patterns['temporal_personality']} (peak at {peak_hour}:00)")
            
        # Peak listening day
        if 'day_of_week' in self.df.columns:
            daily_counts = self.df['day_of_week'].value_counts()
            peak_day = daily_counts.idxmax()
            patterns['peak_day'] = peak_day
            print(f"📅 {peak_day} is your biggest music day")
            self.insights.append(f"📅 {peak_day} is your biggest music day")
            
        return patterns
        
    def analyze_music_preferences(self):
        """Analyze your music taste and preferences."""
        print("\n🎵 ANALYZING MUSIC PREFERENCES")
        print("="*50)
        
        preferences = {}
        
        # Top artists analysis
        if 'artistName' in self.df.columns:
            artist_counts = self.df['artistName'].value_counts()
            top_artist = artist_counts.index[0]
            top_artist_plays = artist_counts.iloc[0]
            artist_percentage = (top_artist_plays / len(self.df)) * 100
            
            preferences['top_artist'] = top_artist
            preferences['top_artist_percentage'] = artist_percentage
            
            print(f"⭐ Your #1 artist: {top_artist} ({top_artist_plays} plays, {artist_percentage:.1f}%)")
            self.insights.append(f"⭐ {top_artist} dominates your playlist ({artist_percentage:.1f}% of all listening)")
            
            # Music diversity analysis
            total_artists = self.df['artistName'].nunique()
            total_plays = len(self.df)
            
            # Calculate concentration ratio (top 10% of artists)
            top_10_percent = max(1, int(len(artist_counts) * 0.1))
            top_artists_plays = artist_counts.head(top_10_percent).sum()
            concentration_ratio = (top_artists_plays / total_plays) * 100
            
            preferences['diversity_score'] = 100 - concentration_ratio
            preferences['total_artists'] = total_artists
            
            # Classify music exploration behavior
            if concentration_ratio > 80:
                exploration_type = "Comfort Zone listener - you love your favorites!"
                exploration_emoji = "🏠"
            elif concentration_ratio > 60:
                exploration_type = "Balanced listener - mix of favorites and exploration!"
                exploration_emoji = "⚖️"
            else:
                exploration_type = "Explorer - always discovering new music!"
                exploration_emoji = "🗺️"
                
            preferences['exploration_type'] = exploration_type
            print(f"{exploration_emoji} You're a {exploration_type}")
            self.insights.append(f"📊 You're an '{exploration_type.split(' -')[0]}' - {exploration_type.split('- ')[1]}")
            
        return preferences
        
    def analyze_listening_intensity(self):
        """Analyze how much and how intensively you listen."""
        print("\n🎧 ANALYZING LISTENING INTENSITY")
        print("="*50)
        
        intensity = {}
        
        if 'timestamp' in self.df.columns:
            # Calculate daily averages
            daily_counts = self.df.groupby('date').size()
            avg_daily_plays = daily_counts.mean()
            max_daily_plays = daily_counts.max()
            
            intensity['avg_daily_plays'] = avg_daily_plays
            intensity['max_daily_plays'] = max_daily_plays
            
            # Classify listening intensity
            if avg_daily_plays > 50:
                intensity_type = "heavy listener"
                intensity_emoji = "🎧"
            elif avg_daily_plays > 20:
                intensity_type = "moderate listener"
                intensity_emoji = "🎵"
            else:
                intensity_type = "selective listener"
                intensity_emoji = "🎶"
                
            intensity['intensity_type'] = intensity_type
            print(f"{intensity_emoji} You're a {intensity_type} ({avg_daily_plays:.0f} songs/day average)")
            self.insights.append(f"{intensity_emoji} You're a {intensity_type} ({avg_daily_plays:.0f} songs/day average)")
            
            # Calculate total listening time (rough estimate)
            total_days = (self.df['timestamp'].max() - self.df['timestamp'].min()).days
            if total_days > 0:
                intensity['total_days'] = total_days
                intensity['total_plays'] = len(self.df)
                
        return intensity
        
    def analyze_skip_behavior(self):
        """Analyze skip patterns if available."""
        print("\n🚫 ANALYZING SKIP BEHAVIOR")
        print("="*50)
        
        skip_cols = ['skipped', 'skip', 'reason_end', 'reason_start']
        skip_col = None
        
        for col in skip_cols:
            if col in self.df.columns:
                skip_col = col
                break
                
        if not skip_col:
            print("⚠️ No skip data available")
            return {}
            
        skip_analysis = {}
        
        # Overall skip rate
        if self.df[skip_col].dtype == bool:
            skip_rate = (self.df[skip_col].sum() / len(self.df)) * 100
        else:
            # Handle different skip indicators
            skip_indicators = ['SKIP', 'skip', True, 'skipped']
            skip_count = self.df[skip_col].isin(skip_indicators).sum()
            skip_rate = (skip_count / len(self.df)) * 100
            
        skip_analysis['overall_skip_rate'] = skip_rate
        print(f"📊 Overall skip rate: {skip_rate:.1f}%")
        
        # Artist-specific skip analysis
        if 'artistName' in self.df.columns and skip_rate > 0:
            artist_skip_stats = self.df.groupby('artistName').agg({
                skip_col: lambda x: (x == True).sum() if x.dtype == bool else x.isin(['SKIP', 'skip', True, 'skipped']).sum(),
                'artistName': 'count'
            }).rename(columns={'artistName': 'total_plays'})
            
            artist_skip_stats['skip_rate'] = (artist_skip_stats[skip_col] / artist_skip_stats['total_plays'] * 100)
            
            # Filter artists with at least 10 plays
            frequent_artists = artist_skip_stats[artist_skip_stats['total_plays'] >= 10]
            
            if len(frequent_artists) > 0:
                most_skipped = frequent_artists.nlargest(5, 'skip_rate')
                least_skipped = frequent_artists.nsmallest(5, 'skip_rate')
                
                skip_analysis['most_skipped_artists'] = most_skipped
                skip_analysis['least_skipped_artists'] = least_skipped
                
        return skip_analysis
        
    def create_temporal_visualization(self, patterns):
        """Create temporal pattern visualizations."""
        if 'hour' not in self.df.columns:
            return None
            
        # Create subplots for temporal patterns
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('🕐 Listening by Hour', '📅 Listening by Day', 
                           '📆 Monthly Patterns', '📈 Listening Trend'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "scatter"}]]
        )
        
        # Hourly pattern
        hourly_counts = self.df['hour'].value_counts().sort_index()
        fig.add_trace(go.Bar(
            x=hourly_counts.index, 
            y=hourly_counts.values,
            name='Hourly',
            marker_color='#1DB954'
        ), row=1, col=1)
        
        # Daily pattern
        if 'day_of_week' in self.df.columns:
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            daily_counts = self.df['day_of_week'].value_counts().reindex(day_order, fill_value=0)
            fig.add_trace(go.Bar(
                x=daily_counts.index,
                y=daily_counts.values,
                name='Daily',
                marker_color='#1ED760'
            ), row=1, col=2)
            
        # Monthly pattern
        if 'month' in self.df.columns:
            month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December']
            monthly_counts = self.df['month'].value_counts().reindex(month_order, fill_value=0)
            fig.add_trace(go.Bar(
                x=monthly_counts.index,
                y=monthly_counts.values,
                name='Monthly',
                marker_color='#1ED760'
            ), row=2, col=1)
            
        # Daily trend over time
        if 'date' in self.df.columns:
            daily_trend = self.df.groupby('date').size().reset_index()
            daily_trend.columns = ['date', 'plays']
            fig.add_trace(go.Scatter(
                x=daily_trend['date'],
                y=daily_trend['plays'],
                mode='lines',
                name='Daily Trend',
                line=dict(color='#1DB954', width=2)
            ), row=2, col=2)
            
        fig.update_layout(
            height=800,
            title_text="⏰ Your Music Listening Patterns",
            showlegend=False,
            template='plotly_white'
        )
        
        return fig
        
    def generate_knowledge_map(self):
        """Generate the complete personal music knowledge map."""
        print("\n🗺️ GENERATING YOUR PERSONAL MUSIC KNOWLEDGE MAP")
        print("="*60)
        
        # Print all insights
        print("\n🎵 YOUR MUSICAL PERSONALITY PROFILE:")
        for i, insight in enumerate(self.insights, 1):
            print(f"{i:2}. {insight}")
            
        # Summary statistics
        print(f"\n📊 SUMMARY STATISTICS:")
        print(f"   🎵 Total tracks played: {len(self.df):,}")
        
        if 'artistName' in self.df.columns:
            print(f"   🎤 Unique artists discovered: {self.df['artistName'].nunique():,}")
            
        if 'timestamp' in self.df.columns:
            days_span = (self.df['timestamp'].max() - self.df['timestamp'].min()).days
            print(f"   📅 Days of listening data: {days_span:,}")
            if days_span > 0:
                print(f"   📈 Average daily plays: {len(self.df)/days_span:.1f}")
                
        if 'trackName' in self.df.columns:
            unique_tracks = self.df['trackName'].nunique()
            repeat_ratio = (len(self.df) - unique_tracks) / len(self.df) * 100
            print(f"   🔄 Repeat listening rate: {repeat_ratio:.1f}%")
            
        print(f"\n🎉 Your music tells a unique story - these patterns make you who you are!")
        print(f"🎵 Thanks for exploring your musical personality! 🎵")
        
    def run_full_analysis(self):
        """Run the complete analysis pipeline."""
        print("🎵 SPOTIFY PERSONAL KNOWLEDGE MAP ANALYSIS")
        print("="*60)
        print("Discovering the patterns that make your music taste unique...")
        
        # Load and preprocess data
        if not self.load_data():
            return False
            
        self.preprocess_data()
        
        # Run all analyses
        temporal_patterns = self.analyze_temporal_patterns()
        music_preferences = self.analyze_music_preferences()
        listening_intensity = self.analyze_listening_intensity()
        skip_behavior = self.analyze_skip_behavior()
        
        # Create visualizations
        if temporal_patterns:
            fig = self.create_temporal_visualization(temporal_patterns)
            if fig:
                fig.show()
                
        # Generate final knowledge map
        self.generate_knowledge_map()
        
        return True


def main():
    """Main function to run the analysis."""
    parser = argparse.ArgumentParser(description='🎵 Spotify Personal Knowledge Map')
    parser.add_argument('--data', type=str, help='Path to Spotify data CSV file')
    parser.add_argument('--kaggle', action='store_true', help='Run in Kaggle mode')
    
    args = parser.parse_args()
    
    if not args.data and not args.kaggle:
        print("❌ Please provide either --data path/to/file.csv or --kaggle")
        parser.print_help()
        sys.exit(1)
        
    # Initialize and run analysis
    analyzer = SpotifyKnowledgeMapper(
        data_path=args.data, 
        kaggle_mode=args.kaggle
    )
    
    success = analyzer.run_full_analysis()
    
    if success:
        print("\n✅ Analysis complete! Check your visualizations above.")
    else:
        print("\n❌ Analysis failed. Please check your data file.")
        sys.exit(1)


if __name__ == "__main__":
    main()
