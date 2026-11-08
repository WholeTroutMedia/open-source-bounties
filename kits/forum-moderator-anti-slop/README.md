# Free Developer Forum Moderator Anti-Slop & Code-Compilation Helper (`forum_slop_auditor.py`)

**Helps Discourse, GitHub Discussions, Reddit, and Hugging Face moderators automatically flag zero-effort ChatGPT spam and broken code while welcoming real engineers.**

## What It Checks
- **Syntax & AST Compilation**: Parses code snippets in forum replies (`ast.parse`) to verify the code actually compiles before or after posting.
- **Robotic Boilerplate Filter**: Flags robotic AI-slop intros (*"Certainly! Here is..."*, *"As an AI language model..."*) and em-dashes.

## Usage
```bash
python3 forum_slop_auditor.py --file sample_post.md
```
