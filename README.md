# Describe Discharge Agent

## Overview

Describe Discharge Agent is an AI-powered multi-stage workflow for extracting, validating, and generating structured discharge summaries from hospital discharge documents.

The system combines OCR processing, rule-based extraction, Large Language Models (Gemini), safety validation, conflict detection, and a self-learning feedback loop to transform unstructured medical discharge reports into structured clinical summaries.

---

## Key Features

### Clinical Information Extraction

- Diagnosis Extraction
- Medication Extraction
- Medication Reconciliation
- Procedure Extraction
- Allergy Extraction
- Follow-up Instruction Extraction
- Hospital Course Extraction
- Discharge Condition Extraction
- Pending Result Extraction
- Demographics Extraction
- Date Extraction

### Safety and Validation

- Drug Interaction Checking
- Clinical Conflict Detection
- Clinician Review Recommendations
- Medication Hallucination Detection
- Missing Information Detection

### AI Capabilities

- OCR Text Correction using Gemini
- Medication Normalization using Gemini
- Automated Discharge Summary Generation
- Multi-Step Agent Planning Workflow

### Self-Learning System

- Simulated Doctor Review
- Reward-Based Evaluation
- Persistent Correction Memory
- Automatic Error Learning
- Iterative Summary Improvement

---

## System Architecture

text Hospital Discharge PDF             │             ▼       OCR Extraction             │             ▼       OCR Correction             │             ▼       Planner Agent             │  ┌──────────┼──────────┐  ▼          ▼          ▼  Extractors  Validators  Safety Checks   │           │            │  ▼           ▼            ▼  Structured Clinical State             │             ▼      Summary Generator             │             ▼     Clinician Review Layer             │             ▼      Final Discharge Summary              ▲             │       Learning Engine             │  ┌──────────┼──────────┐  ▼          ▼          ▼  Reward     Memory     Corrections 

---

## Project Structure

text src/ │ ├── agents/ │   └── Workflow orchestration and planning │ ├── extractors/ │   ├── Diagnosis Extractor │   ├── Medication Extractor │   ├── Procedure Extractor │   ├── Allergy Extractor │   ├── Follow-up Extractor │   ├── Demographics Extractor │   └── Additional clinical extractors │ ├── models/ │   └── Data models │ ├── tools/ │   ├── OCR Corrector │   ├── Medication Reconciliation │   ├── Drug Interaction Checker │   ├── Conflict Detector │   ├── Summary Generator │   ├── Learning Engine │   ├── Reward Calculator │   ├── Simulated Doctor │   └── Correction Memory │ ├── workflows/ │ └── tests/ 

---

## Technology Stack

- Python
- Gemini API
- Regular Expressions
- Agent-Based Workflow Design
- Rule-Based Medical Information Extraction
- Reinforcement Learning Inspired Feedback Loop
- Git & GitHub

---

## Setup

### Clone Repository

bash git clone https://github.com/SinghTanyash/describe-discharge-agent.git cd describe-discharge-agent 

### Create Virtual Environment

bash python3 -m venv describe_env source describe_env/bin/activate 

### Install Dependencies

bash pip install -r requirements.txt 

### Configure Environment Variables

Create a .env file:

env GEMINI_API_KEY=your_api_key_here 

---

## Running the Project

### Full Agent Workflow

bash PYTHONPATH=src python src/tests/test_agent.py 

### Individual Component Tests

bash PYTHONPATH=src python src/tests/test_demographics.py PYTHONPATH=src python src/tests/test_allergy.py PYTHONPATH=src python src/tests/test_medication_verifier.py PYTHONPATH=src python src/tests/test_learning_loop.py 

---

## Example Outputs

The system generates:

- Diagnoses
- Procedures
- Hospital Course
- Discharge Medications
- Follow-up Instructions
- Pending Results
- Clinician Review Recommendations
- Structured Discharge Summaries

---

## Learning Loop

The project includes a feedback-driven learning mechanism:

1. Initial discharge summary generated.
2. Simulated doctor reviews output.
3. Reward score calculated.
4. Corrections stored in memory.
5. Future summaries automatically improved.

This enables continuous improvement without retraining the model.

---

## Future Enhancements

- FHIR Integration
- HL7 Compatibility
- Real Clinical Knowledge Base Integration
- Multi-Language Support
- Hospital Information System Integration
- Human-in-the-Loop Review Dashboard

---

## Author

Tanyash Singh

AI-Powered Clinical Document Processing Project

Version: v1.0