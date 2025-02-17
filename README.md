# Visual AI Agent Skeleton

An integration framework combining Daydreams and OmniParser for GUI-aware AI agents.

## Overview

This project provides a foundation for building AI agents that can understand and interact with graphical user interfaces. By combining Daydreams for decision-making with OmniParser for visual understanding, developers can create custom solutions for visual parsing and AI-driven automation.

## Key Features

- Visual Understanding: Screen parsing and UI element detection using OmniParser
- Intelligent Decision Making: Context-aware processing through the Daydreams framework 
- Groq Integration: Language model integration for visual analysis and action planning
- Real-time Processing: Live capture and analysis of screen content

## Getting Started

### Prerequisites

```bash
# Python version
python >= 3.8

# Required packages
pip install fastapi pydantic groq torch requests
```

### Environment Setup

```bash
# Configure API key
export GROQ_API_KEY=your_api_key_here
```

### Installation

```bash
# Clone repository
git clone https://github.com/username/visual-ai-agent.git

# Install dependencies
cd visual-ai-agent
pip install -r requirements.txt

# Replace dummy models
cp your_trained_models/* weights/
```

## Project Structure

```
├── src/
│   └── visual_ai_agent.py    # Main server and agent implementation
├── util/
│   └── omniparser.py         # OmniParser implementation
├── tools/
│   └── screen_capture.py     # Screen capture utilities
└── weights/
    ├── icon_detect/          # Icon detection models
    └── icon_caption_florence/ # Caption generation models
```

## Usage

```python
# Start the agent
from src.visual_ai_agent import VisualAIAgent

# Initialize components
agent = VisualAIAgent(
    parser_url="localhost:8000",
    model_path="weights/icon_detect"
)

# Start processing
agent.start()
```

## Technical Details

### Core Components

```python
# Screen Capture
class ScreenCapture:
    def capture(self) -> Image:
        """Capture current screen state"""
        pass

# Visual Parser
class OmniParser:
    def parse(self, image: Image) -> dict:
        """Parse UI elements from image"""
        pass

# Context Manager 
class ContextManager:
    def update(self, parsed_data: dict):
        """Update agent context with new data"""
        pass

# Decision Engine
class GroqEngine:
    def analyze(self, context: dict) -> Action:
        """Determine next action based on context"""
        pass
```

### Configuration

```python
# Server settings
SERVER_CONFIG = {
    'host': 'localhost',
    'port': 8000,
    'timeout': 30
}

# Model paths
MODEL_PATHS = {
    'icon_detect': 'weights/icon_detect/model.pt',
    'caption': 'weights/icon_caption_florence/model.safetensors'
}

# Agent settings
AGENT_CONFIG = {
    'update_interval': 0.5,
    'context_size': 1000,
    'action_timeout': 5
}
```

## Development

### Testing

```bash
# Run unit tests
pytest tests/

# Run integration tests
pytest tests/integration/

# Run specific test
pytest tests/test_parser.py -k "test_icon_detection"
```

### Logging

```python
# Configure logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler()
    ]
)
```

## Contributing

```bash
# Fork repository
git clone https://github.com/your-username/visual-ai-agent.git

# Create branch
git checkout -b feature/your-feature

# Commit changes
git commit -m "Add your feature"

# Push changes
git push origin feature/your-feature

# Create pull request
# Submit through GitHub interface
```

## License

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
