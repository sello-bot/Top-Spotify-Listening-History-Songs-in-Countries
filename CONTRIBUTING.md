# 🤝 Contributing to Spotify Knowledge Map

Thank you for your interest in contributing! We welcome contributions from everyone, whether you're fixing bugs, adding features, or improving documentation.

## 🚀 Quick Start

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/yourusername/spotify-knowledge-map.git
   cd spotify-knowledge-map
   ```
3. **Create** a new branch for your feature:
   ```bash
   git checkout -b feature/your-amazing-feature
   ```
4. **Make** your changes
5. **Test** your changes
6. **Commit** and push:
   ```bash
   git commit -m "Add: your amazing feature description"
   git push origin feature/your-amazing-feature
   ```
7. **Create** a Pull Request

## 🎯 Types of Contributions We're Looking For

### 🐛 Bug Fixes
- Fix incorrect pattern detection
- Resolve visualization issues
- Handle edge cases in data processing

### ✨ New Features
- Additional pattern analysis algorithms
- New visualization types
- Cross-platform data integration
- Machine learning clustering
- Social comparison features

### 📚 Documentation
- Improve README clarity
- Add code comments
- Create tutorials
- Write usage examples

### 🎨 Design & UX
- Improve visualizations
- Better color schemes
- Interactive dashboard elements
- Mobile-friendly layouts

## 📋 Development Setup

### Prerequisites
- Python 3.8+
- Git
- Jupyter Notebook

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e .[dev]

# Set up pre-commit hooks
pre-commit install
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_pattern_analyzer.py
```

## 📝 Coding Standards

### Python Style
- Follow **PEP 8** style guidelines
- Use **Black** for code formatting: `black .`
- Use **flake8** for linting: `flake8 src/`
- Maximum line length: **88 characters**

### Code Structure
```python
# Good: Clear function names with docstrings
def analyze_listening_patterns(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyze temporal and behavioral patterns in listening data.
    
    Args:
        df: DataFrame with listening history
        
    Returns:
        Dictionary containing pattern analysis results
    """
    pass

# Good: Type hints where helpful
def calculate_skip_rate(plays: List[bool]) -> float:
    return sum(plays) / len(plays) if plays else 0.0
```

### Documentation
- **Docstrings** for all public functions
- **Type hints** for function parameters and returns
- **Comments** for complex logic
- **README updates** for new features

## 🧪 Testing Guidelines

### Test Structure
```
tests/
├── test_data_loader.py
├── test_pattern_analyzer.py
├── test_visualizer.py
└── fixtures/
    └── sample_data.csv
```

### Writing Tests
```python
import pytest
from src.pattern_analyzer import analyze_listening_patterns

def test_analyze_empty_dataframe():
    """Test behavior with empty input."""
    empty_df = pd.DataFrame()
    result = analyze_listening_patterns(empty_df)
    assert result == {}

def test_analyze_basic_patterns():
    """Test basic pattern detection."""
    # Use fixture data
    df = load_test_data('basic_listening_history.csv')
    result = analyze_listening_patterns(df)
    
    assert 'peak_hour' in result
    assert isinstance(result['peak_hour'], int)
    assert 0 <= result['peak_hour'] <= 23
```

## 📊 Adding New Analysis Features

### Pattern Analysis Template
```python
def analyze_new_pattern(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyze a new type of listening pattern.
    
    Args:
        df: DataFrame with required columns: ['timestamp', 'artistName', ...]
        
    Returns:
        Dictionary with analysis results
    """
    # Validation
    required_cols = ['timestamp', 'artistName']
    if not all(col in df.columns for col in required_cols):
        return {}
    
    # Analysis logic
    pattern_data = df.groupby('some_column').agg({'metric': 'mean'})
    
    # Return structured results
    return {
        'pattern_name': 'New Pattern',
        'key_insight': 'Main finding',
        'data': pattern_data.to_dict(),
        'visualization_data': prepare_viz_data(pattern_data)
    }
```

### Visualization Template
```python
def plot_new_pattern(data: Dict[str, Any]) -> go.Figure:
    """Create visualization for new pattern analysis."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['x_values'],
        y=data['y_values'],
        mode='lines+markers',
        name='Pattern Data'
    ))
    
    fig.update_layout(
        title='📊 Your New Pattern Analysis',
        xaxis_title='X Axis Label',
        yaxis_title='Y Axis Label',
        template='plotly_white'
    )
    
    return fig
```

## 🎨 UI/UX Guidelines

### Visualization Standards
- **Consistent color palette**: Use theme colors across all plots
- **Clear labels**: Always include axis labels and titles
- **Interactive elements**: Hover information, zoom, pan
- **Accessibility**: Color-blind friendly palettes
- **Mobile responsive**: Test on different screen sizes

### Text and Messaging
- **Friendly tone**: Use emojis and conversational language
- **Clear insights**: Explain what patterns mean
- **Actionable**: Tell users what they can do with insights
- **Personal**: Make it about "you" not "the user"

## 🔍 Review Process

### Pull Request Requirements
- [ ] **Tests pass**: All existing and new tests must pass
- [ ] **Code formatted**: Run `black .` and `flake8`
- [ ] **Documentation updated**: README, docstrings, comments
- [ ] **Type hints added**: For new functions
- [ ] **Example provided**: Show how to use new features

### Review Checklist
- [ ] Code follows project style guidelines
- [ ] New features have appropriate tests
- [ ] Documentation is clear and complete
- [ ] No breaking changes (or properly documented)
- [ ] Performance considerations addressed

## 🐛 Bug Reports

### Before Submitting
1. **Search existing issues** to avoid duplicates
2. **Update to latest version** to see if bug persists
3. **Test with sample data** to isolate the issue

### Bug Report Template
```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
1. Load data with format: ...
2. Run analysis: ...
3. See error: ...

**Expected Behavior**
What you expected to happen.

**Screenshots/Code**
```python
# Code that reproduces the issue
```

**Environment:**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- Package versions: [run `pip freeze`]

**Additional Context**
Any other context about the problem.
```

## 💡 Feature Requests

### Feature Request Template
```markdown
**Feature Description**
A clear description of what you want to happen.

**Use Case**
Why would this feature be useful? Who would use it?

**Possible Implementation**
If you have ideas about how to implement this.

**Additional Context**
Screenshots, mockups, or examples from other tools.
```

## 🏆 Recognition

Contributors will be:
- **Listed** in the README contributors section
- **Mentioned** in release notes for significant contributions
- **Invited** to join the core contributor team for ongoing contributions

## 📞 Getting Help

- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Issues**: Use GitHub Issues for bugs
- 📧 **Email**: contact@example.com for sensitive matters

## 🎉 First Time Contributors

New to open source? Here are some beginner-friendly ways to contribute:

1. **Fix typos** in documentation
2. **Add comments** to existing code
3. **Write tests** for untested functions
4. **Create examples** showing how to use features
5. **Improve error messages** to be more helpful

Look for issues labeled `good first issue` to get started!

---

Thank you for helping make Spotify Knowledge Map better for everyone! 🎵✨
