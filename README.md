# Market AI Research (Phase 1)

> **Purpose:** research, backtesting, and paper trading only. This project does
> not promise returns, accuracy, or live-trading safety.

## What we are building now — simple Hinglish explanation

Abhi hum AI agent ya machine learning **nahin** bana rahe hain. Pehle hum ek
safe foundation bana rahe hain: Python project, isolated environment, aur ek
small program that proves your computer can run the project. Isko building ki
foundation samjho—pehle foundation strong, phir indicators, strategy, aur
backtesting.

Our first program does **not** download prices, produce a signal, or place a
trade. It only prints a health-check message.

## Phase 1 roadmap

- [x] **1. Environment bootstrap:** project folder, virtual environment, and a
  health-check program.
- [ ] **2. Historical data:** choose one instrument and timeframe, then load and
  validate OHLCV candles.
- [ ] **3. Indicators:** calculate SMA, EMA, RSI, MACD, ATR, and volume features.
- [ ] **4. One explicit strategy:** define entry, stop-loss, target, and a
  `NO TRADE` condition in plain rules.
- [ ] **5. Backtester:** simulate trades candle by candle without looking into
  future candles; include fees and slippage.
- [ ] **6. Report and tests:** calculate trade and equity metrics, inspect the
  results, and test critical calculations.

We will not start machine learning until the complete Phase 1 strategy and
backtest are working and checked.

## Software to install on Windows

1. **Python 3.11 or newer** from [python.org](https://www.python.org/downloads/windows/).
   During installation, tick **“Add Python to PATH”** before clicking
   **Install Now**.
2. **Visual Studio Code** from [code.visualstudio.com](https://code.visualstudio.com/).
   It is the editor where you will open this folder. Install the Microsoft
   **Python** extension when VS Code suggests it.
3. **Git for Windows** from [git-scm.com](https://git-scm.com/download/win).
   Git records versions of our work. It is useful but not required to run this
   first program.

## First setup — Windows PowerShell

Open **PowerShell**: press the Windows key, type `PowerShell`, and press Enter.

### A. Check Python

```powershell
py --version
```

Expected: something similar to `Python 3.11.x` or newer. If `py` is not found,
install Python using the instructions above, close PowerShell, reopen it, and
run the command again.

### B. Create and open the project folder

Choose a simple location such as your Documents folder:

```powershell
cd $HOME\Documents
mkdir market-ai-research
cd market-ai-research
code .
```

`code .` opens the current folder in VS Code. If PowerShell says `code` is not
recognized, open VS Code manually and choose **File → Open Folder**.

Copy this repository's files into that folder before continuing.

### C. Create and activate a virtual environment

A virtual environment is a private Python package area for this one project.
It prevents one project’s packages from interfering with another’s.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Expected: your prompt begins with `(.venv)`. If PowerShell blocks the activation
script, run this **once in the current PowerShell window**, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### D. Install only the first-step requirements

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

There are no third-party packages yet; that is intentional. The first program
uses Python’s built-in tools only.

### E. Run and test the first program

```powershell
python main.py
python -m unittest discover -s tests -v
```

Expected health-check output includes `Status: setup is working`. The test
should finish with `OK`.

## Current project layout

```text
market-ai-research/
├── main.py              # First safe health-check program
├── requirements.txt     # Packages needed at the current milestone
├── tests/
│   └── test_main.py     # Automated check for main.py
└── README.md            # Beginner-friendly instructions and roadmap
```

## Stop point / what to send next

Run the four commands in sections C–E. Then send the complete output here—both
success output and any error text are useful. **Stop there**; do not install
machine-learning packages or build a strategy yet.
