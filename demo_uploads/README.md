Place demo video files in this folder, then update `demo_entries.json` with:

- `title`: the project or demo name
- `description`: the explanation you want recruiters to read
- `filename`: the exact video filename in this folder, like `lovable-demo.mp4`
- `status`: optional label like `Private demo`, `In progress`, or `Coming soon`
- `project_url`: optional link if the project goes live later
- `thumbnail`: optional image filename from this folder

After adding or changing demos, run:

```bash
python3 generate_portfolio.py
```
