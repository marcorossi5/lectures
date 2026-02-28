[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-2a76dd?logo=github)](https://marcorossi5.github.io/lectures/)

# Lectures — Marco Rossi

**AI Engineer** · Practical AI for industry professionals

A public collection of slide decks from my lectures and workshops, covering real-world AI applications across industries. Each presentation is self-contained and available directly in the browser — no installation required.

Browse all lectures at **[marcorossi5.github.io/lectures](https://marcorossi5.github.io/lectures/)**.

---

## Structure

```
slides/
  YYYYMMDD_topic_name/
    index.html          # self-contained reveal.js presentation
templates/
  index_template.html   # index page template (edit to change layout/style)
scripts/
  generate_index.py     # generates slides/index.html from the template
```

## Adding a new lecture

1. Create a folder under `slides/` named `YYYYMMDD_topic_name`
2. Place a self-contained `index.html` inside it
3. Push to `main` — the index page is rebuilt and the site is redeployed automatically

The lecture will be accessible at `https://marcorossi5.github.io/lectures/YYYYMMDD_topic_name/`.

## Local preview

Generate the index page locally before pushing:

```bash
python3 scripts/generate_index.py
open slides/index.html
```

## Deployment

GitHub Actions builds and deploys the site on every push to `main` via [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml). The workflow generates the index page, then uploads the entire `slides/` directory as a GitHub Pages artifact.

> Make sure GitHub Pages is configured to use **GitHub Actions** as the source in the repository settings.
