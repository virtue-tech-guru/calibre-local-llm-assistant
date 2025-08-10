# LLM Assisted Book Reading
This is the reading assistance. Translation, summarization and simplification of hard contents. 

Accelerate your reading journey, whether you are reading a technical book or a novel. Perhaps you are reading a book in a foreign language and want to improve your skills in that language. Simply describe what you want to do in the prompt, and you will receive the output in the format you expect.

Usage:
- Start ollama
- Integrate required fastapi endpoint on Calibre Lookup
```python
http://localhost:8000/assistant/{word}
```
- Select model
- Adding meta prompt or persona while reading books to help you.
- Apply
- Select text on book, it will automatically handle your instructed task.

Features:
- Depending on available GPU on PC, you can directly use as fast as commercial LLMs
- Integrate endpoint with Calibre Lookup.
- Built in ollama support with diverse models on it.
- Built in Feynman Filter approach for learning by teaching paradigm.

Tests:
- Tested with llama3.2:1b

Planned Features:
- Extract unstructured data from epubs mobi or books convey to structured for making this app allowed to use by data engineers. 



