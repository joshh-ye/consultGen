# Quickstart

Clone the repo and run the following commands on your machine:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create your package
#    - openai_chat.py: write your prompt function using the `chat_content` function  
#    - remove_lines.py (or your module): implement the “remove first three lines” logic  
#    - test_<module>.py: add your pytest tests  

# 3. Run the unit tests
python -m pytest .
