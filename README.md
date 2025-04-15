# Language-Translation-App
Language Translation App built using LangChain and Chainlit, integrating OpenAI’s GPT-3.5-Turbo to translate text into Thai. The project allows real-time streaming and is wrapped in a simple Chainlit interface.

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/language-translation-app.git
cd language-translation-app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to the .env file

# Run the app
chainlit run app.py
