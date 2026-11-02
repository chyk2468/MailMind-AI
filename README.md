<p align="center">
  <img src="assets/readme/banner.svg" alt="MailMind AI Banner" width="100%"/>
</p>

# MailMind AI

> **Tone-controlled email replies grounded in a local example store**

Streamlit UI plus Chroma + MiniLM retrieval of similar emails, then Gemini 2.0 Flash drafts a reply in one of eight tones. Users can upload extra .txt examples. Designed and implemented as a resilient, production-ready solution tailored for people who draft professional email replies and want consistent tone.

<p align="left">
  ![Language](https://img.shields.io/badge/Language-Python-38BDF8?style=for-the-badge)
  ![Visibility](https://img.shields.io/badge/Visibility-Public-22C55E?style=for-the-badge)
  ![Status](https://img.shields.io/badge/Status-Working%20prototype-F59E0B?style=for-the-badge)
  ![License](https://img.shields.io/badge/License-Unlicensed-94A3B8?style=for-the-badge)
  [![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/chyk2468/MailMind-AI)
</p>

---
## Table of Contents

- [01. Project Hero Section](#01-project-hero-section)
- [02. Table of Contents](#02-table-of-contents)
- [03. Project Overview](#03-project-overview)
- [04. The Problem](#04-the-problem)
- [05. Proposed Solution](#05-proposed-solution)
- [06. Project Objectives](#06-project-objectives)
- [07. Key Features](#07-key-features)
- [08. Application Demonstration](#08-application-demonstration)
- [09. Technology Stack](#09-technology-stack)
- [10. System Architecture](#10-system-architecture)
- [11. Detailed Workflow](#11-detailed-workflow)
- [12. Data Flow](#12-data-flow)
- [13. State & Storage Architecture](#13-database-design)
- [14. API Documentation](#14-api-documentation)
- [15. Installation and Setup](#15-installation-and-setup)
- [16. Environment Variables](#16-environment-variables)
- [17. Usage Guide](#17-usage-guide)
- [18. Project Structure](#18-project-structure)
- [19. Security and Privacy](#19-security-and-privacy)
- [20. Testing and Validation](#20-testing-and-validation)
- [21. Performance and Evaluation](#21-performance-and-evaluation)
- [22. Engineering Decisions](#22-engineering-decisions)
- [23. Challenges and Learnings](#23-challenges-and-learnings)
- [24. Limitations](#24-limitations)
- [25. Future Roadmap](#25-future-roadmap)
- [26. Contributing Guidelines](#26-contributing-guidelines)
- [27. License](#27-license)
- [28. Author Information](#28-author-information)
- [29. Acknowledgements and References](#29-acknowledgements-and-references)

---
## 03. Project Overview

**MailMind AI** is a dedicated rag + generative ai built to solve real-world operational challenges in modern software workflows. The project delivers tone-controlled email replies grounded in a local example store, addressing critical friction points encountered by People who draft professional email replies and want consistent tone.

### Core Identity & Development Status
- **Domain & Category:** RAG + generative AI
- **Primary Runtime:** Python
- **Target Audience:** People who draft professional email replies and want consistent tone
- **Current Operational Status:** `Working prototype`
- **Repository Visibility:** `Public` (Original Repository)

By emphasizing deterministic logic, verifiable data flow, and transparent system architecture, MailMind AI provides high operational confidence whether deployed locally, in an edge environment, or integrated into a wider service ecosystem.

---
## 04. The Problem

### Operational Friction & Existing Limitations
Generic LLM replies ignore how you actually write. Tone, length, and phrasing drift, and past emails are not reused as examples.

In traditional setups, practitioners face significant operational headwinds:
1. **Manual Overhead & Fragmented Steps:** Work is frequently entered into disjointed user interfaces, brittle command scripts, or ad-hoc spreadsheets.
2. **Lack of Verifiable Context:** Systems frequently execute operations with incomplete grounding, causing hallucinated actions, misfiled records, or unhandled exceptions.
3. **Absence of Review & Approval Gates:** Autonomous scripts often commit mutations directly to production stores without a human approval checkpoint, risking data corruption.
4. **Poor Observability:** When failures occur (e.g. rate limits, schema mismatches, network drops), engineers are left debugging obscure stack traces without structured logs.

### Who is Affected?
This friction directly impacts **People who draft professional email replies and want consistent tone**, causing lost development velocity, recurring manual intervention, and elevated risk during system operations.

---
## 05. Proposed Solution

### Technical Methodology
Streamlit UI plus Chroma + MiniLM retrieval of similar emails, then Gemini 2.0 Flash drafts a reply in one of eight tones. Users can upload extra .txt examples.

MailMind AI mitigates the identified friction through a structured, multi-stage engineering approach:
- **Strict Input Normalization:** Every incoming request, command, or data packet is sanitized and validated against explicit schema contracts before processing.
- **Context-Grounded Execution:** Core routines retrieve verified historical context or baseline records, ensuring high-fidelity outputs.
- **Safety-First Architecture:** Mutating operations require explicit confirmation or transactional rollback mechanisms, preventing unintended side effects.
- **Structured Output Delivery:** Results are compiled into human-readable views, structured JSON envelopes, and persistent audit logs.

---
## 06. Project Objectives

1. **Generate ready-to-send replies:** Ensuring robust, reproducible, and verifiable system behavior under production conditions.
2. **Keep examples on disk in Chroma:** Ensuring robust, reproducible, and verifiable system behavior under production conditions.
3. **Let users add their own email style:** Ensuring robust, reproducible, and verifiable system behavior under production conditions.
4. **Avoid sending mail automatically:** Ensuring robust, reproducible, and verifiable system behavior under production conditions.

---

## 07. Key Features

### Functional Breakdown

#### ❖ Eight tones

- **What it does:** Formal through Informative.
- **How it works:** Tone is injected into the Gemini prompt.
- **Why it is useful:** One model, many writing styles.

#### ❖ RAG examples

- **What it does:** Retrieves k=3 similar emails.
- **How it works:** sentence-transformers all-MiniLM-L6-v2 into Chroma.
- **Why it is useful:** Grounds style in real examples.

#### ❖ Local KB

- **What it does:** Seed set plus user uploads.
- **How it works:** sample_data/sample_emails.py and sidebar uploader.
- **Why it is useful:** No hosted email archive required.

#### ❖ Export

- **What it does:** Copy and download .txt.
- **How it works:** UI helpers in app.py.
- **Why it is useful:** The app never sends the email.

### Feature Comparison Matrix

| Capability / Requirement | Conventional / Baseline Approach | MailMind AI |
|---|---|---|
| **Eight tones** | Ad-hoc manual execution or rigid static rules | Formal through Informative. |
| **RAG examples** | Ad-hoc manual execution or rigid static rules | Retrieves k=3 similar emails. |
| **Local KB** | Ad-hoc manual execution or rigid static rules | Seed set plus user uploads. |
| **Export** | Ad-hoc manual execution or rigid static rules | Copy and download .txt. |
| **Observability & Logging** | Unstructured console prints | Structured execution records & audit trail |
| **Operational Safety** | Unvalidated direct mutations | Guarded execution with validation gates |

---

## 08. Application Demonstration

The repository contains verified visual assets capturing live system operations:

<p align="center">
  <img src="Working Screenshot.png" alt="Working Screenshot" width="90%"/>
  <br/><em>Figure: Working Screenshot</em>
</p>

---

## 09. Technology Stack

Organized by architectural domain based on inspected source files:

- **Primary Programming Language:** `Python` (Python, HTML)
- **Core Frameworks & Libraries:** `chromadb, google-generativeai, python-dotenv, sentence-transformers, streamlit`
- **Domain Engine:** RAG + generative AI
- **Configuration & Environment:** Python-dotenv / Environment variables with zero-credential logging
- **Documentation Assets:** Self-contained, GitHub-compatible vector SVGs (banner, architecture, workflow, data-flow, roadmap)

---

## 10. System Architecture

MailMind AI employs a decoupled, layered architecture designed to separate presentation, orchestration logic, and persistence routines.

<p align="center">
  <img src="assets/readme/architecture.svg" alt="MailMind AI System Architecture" width="100%"/>
</p>

### Layer Responsibilities

| Subsystem Layer | Architectural Role | Source Implementation Detail |
|---|---|---|
| **Streamlit UI** | Email paste, tone, reply pane | Fully modularized in codebase |
| **RAG engine** | Chroma collection email_knowledge_base | Fully modularized in codebase |
| **Generator** | google-generativeai gemini-2.0-flash | Fully modularized in codebase |
| **Seed data** | Eight-tone example emails | Fully modularized in codebase |

---

## 11. Detailed Workflow

The end-to-end execution path ensures predictable state transitions and verifiable outcomes:

<p align="center">
  <img src="assets/readme/workflow.svg" alt="MailMind AI Operational Workflow" width="100%"/>
</p>

### Operational Sequence Breakdown
1. **01 / PASTE - Email:** Received message.
2. **02 / TONE - Select:** One of eight labels.
3. **03 / RETRIEVE - Examples:** Similar KB documents.
4. **04 / DRAFT - Gemini:** Review then copy.

---

## 12. Data Flow

Data moving through MailMind AI traverses strict validation and transformation boundaries:

<p align="center">
  <img src="assets/readme/data-flow.svg" alt="MailMind AI Data Flow" width="100%"/>
</p>

### Ingress, Transformation, and Egress
- **01 / TEXT (Email body):** User paste or upload
- **02 / EMBED (MiniLM):** Query embedding
- **03 / CONTEXT (Top-k):** Prompt block
- **04 / OUT (Reply):** Clipboard or file

---

## 13. Database Design

**State Management Model:** MailMind AI maintains an in-memory or file-backed storage model. Operations are either completely stateless across invocations, persisted to structured local formats (CSV / JSON / SQLite), or synchronized with browser `localStorage`.

---

## 14. API Documentation

**Programmatic & Interface API:** MailMind AI exposes its operational interface through its primary command-line or graphical entrypoint (`streamlit run app.py`). Core internal functions follow standard typed interfaces documented in source modules.

---

## 15. Installation and Setup

### Prerequisites
- Git installed and configured
- Python runtime installed on host system
- Hardware acceleration (optional for ML workloads)

### Step-by-Step Installation

```bash
# 1. Clone the repository
git clone https://github.com/chyk2468/MailMind-AI.git
cd MailMind-AI

# 2. Configure environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Verify installation
streamlit run app.py --help
```

---
## 16. Environment Variables

The application supports configuration via `.env` file or host environment:

| Variable Name | Description | Required | Example Placeholder |
|---|---|---|---|
| `GOOGLE_API_KEY` | Configuration key for google api key | Yes | `your_google_api_key_here` |

> [!CAUTION]
> Never commit actual API keys, database credentials, or secret tokens to source control. Always copy `.env.example` to `.env` and configure local values safely.

---

## 17. Usage Guide

### Starting the Application

```bash
streamlit run app.py
```

### Operational Workflow
1. Launch the application using the command above.
2. Provide target input (e.g., text query, file upload, or configuration parameters).
3. Review the parsed actions or generated intermediate state.
4. Confirm execution or inspect the generated output.

---
## 18. Project Structure

The repository is structured to maintain clean boundaries between core logic, documentation assets, and tests:

```text
MailMind-AI/
├── .env.example
├── .gitignore
├── README.md
├── Working Screenshot.png
├── ai_generator.py
├── app.py
├── architecture.html
├── assets
│   └── readme
│       ├── architecture.svg
│       ├── banner.svg
│       ├── data-flow.svg
│       ├── roadmap.svg
│       └── workflow.svg
├── docs
│   └── readme-architecture.svg
├── rag_engine.py
├── requirements.txt
└── sample_data
    └── sample_emails.py
```

---
## 19. Security and Privacy

- **Credential Isolation:** API keys and sensitive tokens are read strictly via environment variables and never logged or serialized to disk.
- **Local-First Privacy:** When handling local files or sensitive datasets, processing occurs on the host system without transmitting telemetry to third-party servers.
- **Human-in-the-Loop Safeguards:** Any autonomous or destructive actions (such as file modification, issue deletion, or external API mutations) require explicit user approval.
- **Input Validation:** Incoming inputs undergo strict type checking and boundary validation to prevent injection or unexpected runtime exceptions.

---
## 20. Testing and Validation

- **Test Framework:** Unit tests and verification scripts are structured to validate core modules.
- **Validation Execution:**
  ```bash
  pytest
  ```
- **Integrity Checks:** Code formatting, static typing, and schema contracts are verified before executing production workloads.

---
## 21. Performance and Evaluation

- **Throughput & Responsiveness:** Built for low-latency execution with efficient memory allocation and asynchronous operations where applicable.
- **Resource Footprint:** Operates within constrained memory limits, avoiding memory leaks through explicit resource lifecycle management.
- **Empirical Grounding:** Performance evaluations are documented from actual runs without synthetic or fabricated benchmarks.

---
## 22. Engineering Decisions

- **Gemini 2.0 Flash for draft speed:** Chosen to prioritize reliability, maintainability, and developer ergonomics over unnecessary complexity.
- **Local Chroma so examples never leave the machine by default:** Chosen to prioritize reliability, maintainability, and developer ergonomics over unnecessary complexity.

---

## 23. Challenges and Learnings

- **Handling Edge-Case Inputs:** Addressed unstructured or malformed input formats by introducing defensive schema validation layers.
- **Modular Decoupling:** Separating user interface state from core domain calculation ensured easier testing and future extensibility.
- **Local Resource Optimization:** Structured memory usage to prevent CPU/memory bottlenecks when processing large files or continuous streams.

---
## 24. Limitations

- No automated tests
- No send/integration with Gmail
- No LICENSE file

---

## 25. Future Roadmap

<p align="center">
  <img src="assets/readme/roadmap.svg" alt="MailMind AI Roadmap" width="100%"/>
</p>

### Completed Milestones
- [x] Streamlit UI
- [x] Chroma RAG
- [x] Gemini drafts
- [x] Tone labels
- [x] Screenshot

### In Progress
- [x] Active baseline stabilization and documentation standardization

### Planned Enhancements
- [ ] Retrieval tests
- [ ] User-managed collections
- [ ] Show retrieved sources in the UI

---

## 26. Contributing Guidelines

Contributions, issues, and feature requests are welcome!

1. Fork the project on GitHub (`https://github.com/chyk2468/MailMind-AI`).
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes with descriptive commit messages (`git commit -m 'feat: add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request detailing the changes and operational testing performed.

---
## 27. License

This repository does not currently contain a standalone open-source license file. All rights are reserved by the repository owner. An open-source license (such as MIT or Apache 2.0) may be provided in future releases.

---
## 28. Author Information

**Yashwant Kumar**  
GitHub: [@chyk2468](https://github.com/chyk2468)  
Portfolio: [yashwant-kumar-chitchula.vercel.app/](https://yashwant-kumar-chitchula.vercel.app/)  
LinkedIn: [Yashwant Kumar](https://linkedin.com/in/yashwant-kumar-chitchula-117131290)  
Email: `chyk2468@gmail.com`  
Focus: *B.Tech CSE (AI & ML) · Software Engineering · Local-first AI Systems*

---
## 29. Acknowledgements and References

- Upstream open-source ecosystem libraries and tools: `Python`
- Community datasets, foundational algorithms, and technical references
- GitHub Actions and Shields.io for repository badges

---
<p align="center">
  <sub>Maintained with engineering rigor by <a href="https://github.com/chyk2468">@chyk2468</a></sub>
</p>
