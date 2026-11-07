# Free Hugging Face Dataset & Model Anti-Theft Shield (`hf_canary_injector.py`)

**Protect your open-source AI datasets on Hugging Face and GitHub from copycat scraper bots that re-upload your work under their own name.**

## Quick Start
```bash
# 1. Inject 20 cryptographic canary rows into your JSONL dataset:
python3 hf_canary_injector.py --inject my_dataset.jsonl --owner "your-hf-username"

# 2. Verify whether a suspected copycat dataset contains your stolen rows:
python3 hf_canary_injector.py --verify suspected_copy.jsonl --owner "your-hf-username"
```
