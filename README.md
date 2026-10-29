# AgroPulse AI 🌾
### Omnichannel Multilingual Agritech Intelligence & Crop Diagnostics Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()

> **AgroPulse AI** empowers farmers with real-time **Computer Vision leaf disease detection**, **Grad-CAM visual explainability heatmaps**, **Location-based Multilingual Assistance** across 8 Indian languages (Hindi, Telugu, Tamil, Marathi, Kannada, Odia, Assamese, English), **Real-Time Everyday Weather & Spore Risk Alerts**, **Certified Krishi Vigyan Kendra Farmer Prescription Cards**, and **Live APMC Mandi commodity market prices**.

---

## 🌟 Key Features

1. **🌿 AI Leaf Diagnostic Laboratory & Grad-CAM Heatmap:**
   - Detects crop diseases in under 300ms from photos or camera captures.
   - Evaluates physiological biomarkers: Excess Green Index (ExG), Chlorosis (yellowing), and Necrotic lesion spread.
   - **Grad-CAM Explainability:** Interactive toggle between raw leaf photo and thermal lesion heatmap segmenting active pathogen lesions (Red), chlorosis stress (Yellow), and healthy tissue (Green).
   - Outputs disease name, scientific pathogen, severity level (Moderate, Severe, Critical), and AI confidence percentage.

2. **📍 Location-Based Auto-Detection & 8 Indian Languages:**
   - Detects state via browser GPS coordinates or location dropdown.
   - Automatically switches interface, remedies, and voice speech to the state's native tongue:
     - **Odisha** $\rightarrow$ Odia (`or`)
     - **Tamil Nadu** $\rightarrow$ Tamil (`ta`)
     - **Assam** $\rightarrow$ Assamese (`as`)
     - **Maharashtra** $\rightarrow$ Marathi (`mr`)
     - **Karnataka** $\rightarrow$ Kannada (`kn`)
     - **Andhra Pradesh / Telangana** $\rightarrow$ Telugu (`te`)
     - **UP / MP / Punjab** $\rightarrow$ Hindi (`hi`)
     - **Pan-India / International** $\rightarrow$ English (`en`)

3. **📄 Official Certified Farmer Prescription Card (PDF / Print):**
   - Generates an official Krishi Vigyan Kendra (KVK) certified clinical prescription card with unique tracking code (e.g. `RX-AGP-2026-4387`).
   - Displays exact chemical fungicide/bactericide dilution per liter of water, organic preparations, and cultural practices.
   - Includes official green certification stamp and digital signature from Chief Plant Pathologist.
   - Optimized print stylesheet for instant 1-page A4 printing or PDF saving.

4. **🌦️ Real-Time Everyday Weather Telemetry & Farmer Alerts:**
   - Connected live to Open-Meteo REST API (zero tokens/API keys required).
   - Computes biological **Fungal Spore Multiplication Index (FMI)** based on temperature and humidity.
   - Detects heavy rain wash-off hazards (>10mm) and calculates safe morning pesticide spraying windows.
   - Live color-coded farmer alert banner (🚨 Critical / ⚠️ High Risk / 🟢 Safe Spraying).

5. **🎙️ Multilingual Voice Agronomist:**
   - Speak in native languages or type queries.
   - Streams audio speech answers using Text-to-Speech (TTS) directly in the browser.
   - 100% offline uptime with deterministic agronomy graph + optional Google Gemini 2.0 Flash cloud reasoning.

6. **📈 APMC Mandi Market Tracker:**
   - Real-time wholesale prices across Indian APMC yards with trend indicators (+% rising, -% falling) and trade advice.

---

## 📸 System Architecture & Workflow

| System Architecture | End-to-End Workflow Flowchart |
| :---: | :---: |
| ![Architecture](docs/system_architecture.jpg) | ![Workflow](docs/workflow_flowchart.jpg) |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure Python 3.10 or higher is installed.

### 2. Install Dependencies
```bash
cd E:\agropulse-ai
pip install -r requirements.txt
```

### 3. Launch the Application
Run the one-click runner:
```bash
python run.py
```
*This starts the FastAPI server on `http://localhost:8000` and automatically opens the dashboard in your default web browser.*

---

## 📁 Project Structure

```text
agropulse-ai/
├── backend/
│   ├── main.py                  # FastAPI server with all REST endpoints
│   ├── vision_engine.py         # Leaf disease classifier, ExG, & Grad-CAM heatmap generator
│   ├── voice_engine.py          # Multilingual Speech-to-Text & Text-to-Speech
│   ├── advisory_engine.py       # Agronomist reasoning engine (offline + Gemini)
│   ├── weather_engine.py        # Open-Meteo live API & Fungal Spore Index calculator
│   └── mandi_engine.py          # APMC wholesale price tracker & trade advice
├── data/
│   ├── disease_database.json    # Verified agronomic database (38 diseases x 8 languages)
│   ├── mandi_prices.json        # Benchmark market prices across Indian APMCs
│   └── sample_leaves/           # Built-in sample leaf images for instant testing
├── frontend/
│   ├── index.html               # Responsive web dashboard & Prescription Modal
│   ├── style.css                # Custom UI styles & @media print A4 prescription stylesheet
│   └── app.js                   # Client-side camera, mic, GPS detection, & Grad-CAM toggle
├── docs/
│   ├── MASTER_PROJECT_REPORT.md # Comprehensive engineering report & mathematical formulations
│   ├── ARCHITECTURE.md          # System architecture, data flow, and API specs
│   ├── EXPLAIN_TO_FRIENDS.md    # Master guide for explaining the project to teammates
│   ├── VIVA_AND_INTERVIEW_QA.md # 15 tough questions & winning answers for viva reviews
│   ├── system_architecture.jpg  # Visual architecture infographic diagram
│   └── workflow_flowchart.jpg   # Visual workflow flowchart diagram
├── create_samples.py            # Generates test leaf images
├── update_all_languages_db.py   # Database localization compiler
├── run.py                       # One-click start script
├── requirements.txt             # Python package dependencies
└── README.md
```

---

## 📚 Complete Project Documentation
- **[Master Project Engineering Report](docs/MASTER_PROJECT_REPORT.md):** Complete mathematical formulas, module breakdowns, and deployment specs.
- **[How to Explain to Your Friends](docs/EXPLAIN_TO_FRIENDS.md):** Step-by-step presentation script and elevator pitch.
- **[Viva & Technical Interview Defense](docs/VIVA_AND_INTERVIEW_QA.md):** Top 15 tough questions and winning academic answers.
- **[System Architecture](docs/ARCHITECTURE.md):** Technical component diagrams and REST specifications.
