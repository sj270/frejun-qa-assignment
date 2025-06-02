# FreJun QA Assignment – Sneha Kumari

## ✅ Tech Stack

- Python
- Pytest
- Playwright
- pytest-html (report)
- pytest-xdist (parallel)

---

## ✅ Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd frejun-qa-assignment

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

#Run all tests and generate HTML report:
pytest --html=report.html

#Run all tests in parallel and generate HTML report:
pytest -n auto --html=report.html
