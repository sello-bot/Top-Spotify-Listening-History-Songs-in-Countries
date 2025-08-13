# 🎵 Spotify Personal Knowledge Map
About Dataset This dataset contains detailed Spotify listening history of a user. Each record captures information about a specific track played on Spotify, including metadata about the track, playback behavior, and the user's interaction with the platform. It spans multiple years and provides insights into user behavior.

> Discover surprising patterns in your music listening behavior and uncover what your Spotify data reveals about you!

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Kaggle](https://img.shields.io/badge/Kaggle-Ready-20BEFF.svg)](https://kaggle.com)

## 🚀 What This Does

Transform your raw Spotify listening history into fascinating insights about your musical personality! This project analyzes your listening patterns to reveal:

- 🌅 **Temporal Patterns**: When do you listen to music most?
- 🎭 **Musical Moods**: How your music taste changes throughout the day
- 🚫 **Skip Behavior**: Which artists make you hit that skip button?
- 🎯 **Explorer vs Comfort Zone**: Are you discovering new music or sticking to favorites?
- ⚡ **Energy Cycles**: How your music energy matches your daily rhythm
- 📊 **Personal Music DNA**: A complete profile of your unique listening patterns


## 📁 Project Structure

```
spotify-knowledge-map/
├── 📓 spotify_analysis.ipynb          # Main analysis notebook
├── 🐍 src/
│   ├── __init__.py
│   ├── data_loader.py                 # Data loading utilities
│   ├── pattern_analyzer.py            # Core pattern analysis
│   ├── visualizer.py                  # Plotting and visualization
│   └── insights_generator.py          # Insight text generation
├── 📊 sample_data/
│   ├── sample_spotify_history.csv     # Sample data for testing
│   └── data_dictionary.csv            # Column descriptions
├── 🖼️ assets/
│   ├── screenshot_1.png               # Example outputs
│   ├── screenshot_2.png
│   └── knowledge_map_example.png
├── 📋 requirements.txt                # Python dependencies
├── 🛠️ setup.py                       # Package setup
├── ⚖️ LICENSE                         # MIT License
├── 📖 README.md                       # This file
├── 🔧 .gitignore                      # Git ignore rules
└── 📝 CONTRIBUTING.md                 # Contribution guidelines
```

## 🎨 Example Outputs

### Your Musical Personality Map
```
🗺️  YOUR MUSIC PERSONALITY MAP:
1. 🌙 You're a night owl listener (peak at 23:00)
2. 📅 Friday is your biggest music day
3. 🎧 You're a heavy listener (47 songs/day average)
4. ⭐ Taylor Swift dominates your playlist (12.3% of all listening)
5. 📊 You're an 'Explorer' - always discovering new music!
```

### Temporal Patterns Dashboard
![Knowledge Map Example](assets/knowledge_map_example.png)

## 📊 Required Data Format

Your Spotify data should include these columns (the script auto-detects available columns):

| Column | Description | Required |
|--------|-------------|----------|
| `ts` / `endTime` | Timestamp of play | ✅ Yes |
| `artistName` | Artist name | ✅ Yes |
| `trackName` | Track name | ✅ Yes |
| `skipped` | Whether track was skipped | ⚪ Optional |
| `platform` | Listening platform | ⚪ Optional |
| Audio features | `energy`, `danceability`, etc. | ⚪ Optional |

## 🔍 Key Features

### 🕐 Temporal Analysis
- **Peak listening hours**: When you're most active musically
- **Day-of-week patterns**: Your musical weekly rhythm  
- **Monthly trends**: How your listening evolves over time
- **Seasonal patterns**: Music preferences by season

### 🎵 Musical Behavior
- **Skip rate analysis**: Which artists/genres you skip most
- **Repeat listening**: Songs and artists you can't get enough of
- **Discovery patterns**: How often you explore new music
- **Playlist diversity**: Your musical exploration vs comfort zone ratio

### 🎭 Mood & Energy
- **Daily energy cycles**: How your music energy changes throughout the day
- **Weekend vs weekday listening**: Different musical moods for different times
- **Context awareness**: Platform and device usage patterns

### 📈 Insights Generation
- **Personality profiling**: "Night owl", "Explorer", "Comfort zone" classifications
- **Surprising connections**: Unexpected patterns in your data
- **Comparative analysis**: How your patterns compare to typical listeners

## 🛠️ Technical Details

### Dependencies
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing  
- **matplotlib** - Static plotting
- **seaborn** - Statistical visualization
- **plotly** - Interactive visualizations
- **jupyter** - Notebook environment

### Performance
- Handles datasets with **1M+ listening records**
- **Memory efficient** processing for large files
- **Fast analysis** - complete insights in under 2 minutes

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch: `git checkout -b feature/amazing-insight`
3. 💻 **Commit** your changes: `git commit -m 'Add amazing new insight'`
4. 📤 **Push** to branch: `git push origin feature/amazing-insight`
5. 🎯 **Submit** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Ideas for Contributions
- 🎨 New visualization types
- 🤖 Machine learning clustering of listening patterns
- 🌍 Cross-platform data integration (Apple Music, YouTube Music)
- 📱 Mobile app version
- 🔗 Social sharing features

## 📈 Roadmap

- [ ] 🤖 **ML clustering** for automatic personality detection
- [ ] 🌐 **Web dashboard** for non-technical users  
- [ ] 📱 **Mobile app** version
- [ ] 🎵 **Music recommendation engine** based on patterns
- [ ] 👥 **Social comparison** features
- [ ] 🔗 **Integration** with other music platforms

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Spotify** for providing rich listening data through their API
- **Kaggle community** for inspiration and dataset hosting
- **Open source contributors** who make projects like this possible

## 📞 Support

- 🐛 **Bug reports**: [Open an issue](https://github.com/yourusername/spotify-knowledge-map/issues)
- 💡 **Feature requests**: [Start a discussion](https://github.com/yourusername/spotify-knowledge-map/discussions)
- 📧 **Contact**: your.email@example.com

---

⭐ **Star this repository** if it helped you discover something surprising about your music taste!

🎵 Happy pattern hunting! 🎵
