"""
AgroPulse AI - One-Click Application Runner
Starts the FastAPI uvicorn server and automatically launches the dashboard in your default browser.
"""

import os
import sys
import time
import webbrowser
import threading
import uvicorn

def open_browser():
    time.sleep(1.5)
    url = "http://localhost:8000"
    print(f"\n[AgroPulse AI] Launching dashboard in browser: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    print("=" * 60)
    print("🌱 AgroPulse AI - Multilingual Agritech Intelligence")
    print("=" * 60)
    print("Starting FastAPI Application on http://localhost:8000")
    print("Leaf Diagnostics | Multilingual Voice AI | APMC Mandi Rates")
    print("Press CTRL+C to stop the server.")
    print("=" * 60)

    # Launch browser in a background thread
    threading.Thread(target=open_browser, daemon=True).start()

    # Run Uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
