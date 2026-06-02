Describe Discharge Agent

Overview

Describe Discharge Agent is an AI-powered workflow for processing hospital discharge summaries.

The system extracts structured medical information from OCR-processed discharge documents and generates a concise discharge summary using Gemini.

Features

- OCR-based PDF text extraction
- Diagnosis extraction
- Medication extraction
- Follow-up instruction extraction
- Hospital course extraction
- Pending result extraction
- Agent-based workflow orchestration
- Execution trace logging
- Gemini-powered discharge summary generation
- Clinician review flagging

Architecture

PDF → OCR → Extractors → Agent State → Planner → Gemini → Discharge Summary

Extractors

- Diagnosis Extractor
- Medication Extractor
- Follow-up Extractor
- Hospital Course Extractor
- Pending Result Extractor

Agent Workflow

1. Extract diagnoses
2. Extract medications
3. Extract follow-up instructions
4. Extract hospital course
5. Extract pending results
6. Generate structured state
7. Generate discharge summary using Gemini

Project Structure

src/
├── agents/
├── extractors/
├── models/
├── tools/
├── workflows/
└── tests/

Setup

bash python3 -m venv describe_env source describe_env/bin/activate pip install -r requirements.txt 

Create a .env file:

env GEMINI_API_KEY=your_api_key 

Run Tests

bash PYTHONPATH=src python src/tests/test_agent.py PYTHONPATH=src python src/tests/test_llm_summary.py 

Example Output

The system generates:

- Diagnoses
- Hospital course
- Discharge medications
- Follow-up instructions
- Pending results
- Clinician review recommendation

Future Improvements

- Medication normalization
- Better OCR cleanup
- FHIR compatibility
- Structured JSON discharge summaries
- Multi-patient support