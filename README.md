<div align="center">

# 🚑 ORION-Health: AI-Assisted Emergency Triage System

### *Next-Generation Autonomous Multi-Agent Clinical Decision Support & Urgency Scoring Platform*

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![React](https://img.shields.io/badge/React_18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![LightGBM](https://img.shields.io/badge/LightGBM-GREEN?style=for-the-badge)](https://lightgbm.readthedocs.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI_GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![WebSockets](https://img.shields.io/badge/WebSockets-Realtime-FF6F00?style=for-the-badge&logo=socketdotio&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-blue.style=for-the-badge)]()

---

<p align="center">
  <b>ORION-Health</b> bridges the gap between emergency medical intake and rapid care prioritization. Powered by a <b>modular multi-agent AI engine</b>, it processes patient vitals and symptoms, calculates objective numerical urgency scores using <b>LightGBM machine learning</b>, generates structured clinical justifications via <b>GPT-4o / Gemini GenAI</b>, and keeps healthcare professionals strictly in control through <b>human-in-the-loop zero-latency override channels</b>.
</p>

[Key Features](#-key-features--capabilities) •
[System Architecture](#-system-architecture) •
[Multi-Agent Pipeline](#-multi-agent-ai-pipeline) •
[Sequence Flow](#-end-to-end-sequence-flow) •
[Tech Stack](#-technology-stack) •
[API Specs](#-rest-api--websocket-specifications) •
[Quickstart](#-quickstart--installation-guide)

---
</div>

## 🚨 Problem Statement & Clinical Solution

### ⚡ The Emergency Triage Crisis
Emergency Departments (EDs) are fast-paced, high-stress clinical environments. Medical staff face immense pressure when conducting manual patient triage:
- **Cognitive Overload & Decision Fatigue**: Surging patient volumes cause delays, inconsistent scoring, or risk of mis-triage.
- **Static EHR & Lack of Decision Support**: Legacy healthcare systems record data post-facto but offer zero predictive urgency intelligence.
- **Lack of Transparency & Automation**: Critical resuscitation cases are not automatically fast-tracked with instant multi-channel notifications.

### 🛡️ The ORION-Health Solution
ORION-Health serves as an **AI Clinical Assistant**, elevating nurse and physician decision-making while safeguarding clinical authority:
- 📊 **Precision Risk Scoring**: Multi-parameter LightGBM ML model evaluates heart rate, blood pressure, $\text{SpO}_2$, temperature, respiratory rate, and pain score.
- 🧠 **Explainable AI (XAI)**: Synthesizes transparent clinical rationale using OpenAI GPT-4o / Gemini 1.5 Pro to justify every triage tier.
- 👨‍⚕️ **Human-in-the-Loop (HITL)**: Clinicians review recommendations with 1-click overrides, feeding corrective data back into the Learner Agent.
- 🚨 **Instant Emergency Fast-Track**: Automatically triggers background email/SMS/WhatsApp escalation alerts for critical patients ($\text{Score} \ge 7.5$).
- ⚡ **Real-Time WebSocket Sync**: Multi-screen live queue updates keep doctor dashboards, emergency panels, and admin monitors perfectly synchronized.

---

## ✨ Key Features & Capabilities

| Feature | Description | Technical Implementation |
| :--- | :--- | :--- |
| **🏥 Smart Patient Intake** | Fast, intuitive symptom and vital sign submission with auto-fill from pre-registration lookup. | React 18 / Next.js 16 + Pydantic v2 Schema Validation |
| **🧠 Multi-Agent Core** | Orchestrates tasks across specialized micro-agents: Observer, Planner, Action, Learner, Explainer. | Python 3.10+ Async Agent Architecture |
| **📊 LightGBM Risk Scoring** | Computes objective 0–10 numerical risk scores based on vital signs & clinical risk indicators. | Scikit-learn + LightGBM ML Pipeline with fallback rule engine |
| **💬 GenAI Medical Reasoning** | Generates human-readable clinical justifications and differential diagnosis considerations. | OpenAI GPT-4o API / Gemini 1.5 Pro with Ollama offline fallback |
| **🔴 Emergency Fast-Track** | Highlights resuscitation cases in pulsing red and triggers background alerts. | BackgroundTasks + SMTP Email + Twilio WhatsApp/SMS |
| **👨‍⚕️ Doctor Overrides** | Allows clinicians to adjust priority tiers, record clinical notes, and log reasons. | Learner Agent + DoctorActions DB Table |
| **🔄 Live WebSocket Stream** | Pushes instantaneous queue state changes to all connected doctor & admin panels. | Centralized FastAPI WebSocket Connection Manager |

---

## 🏗️ System Architecture

ORION-Health implements a 6-layer micro-modular architecture designed for sub-second response times, data consistency, and fail-safe clinical deployment.

```mermaid
flowchart TB
    subgraph FRONTEND ["💻 1. FRONTEND PRESENTATION LAYER (React 18 / Next.js 16)"]
        direction TB
        subgraph PAGES ["Dashboards & Views"]
            P_Register["🏥 Patient Intake Form<br/>(PatientRegister.tsx)"]
            P_PreReg["📋 Pre-Registration<br/>(PreRegister.tsx)"]
            P_Doctor["⚕️ Doctor Queue Dashboard<br/>(DoctorPanel.tsx)"]
            P_Emergency["🔴 Emergency Fast-Track<br/>(EmergencyPanel.tsx)"]
            P_History["📈 Analytics & History<br/>(DoctorHistory.tsx)"]
        end
        subgraph SERVICES ["State & Communication"]
            API_Client["Axios & Fetch API Client<br/>(orion-api.ts)"]
            WS_Client["WebSocket Listener Hook<br/>(orion-ws.ts)"]
        end
        PAGES --> SERVICES
    end

    subgraph GATEWAY ["🌐 2. API GATEWAY & SECURITY LAYER (FastAPI + Starlette)"]
        direction TB
        CORS["CORS Middleware & Security"]
        Validation["Pydantic Data Validation Schemas"]
        subgraph CONTROLLERS ["API Route Controllers"]
            R_Patient["POST /api/patient/submit"]
            R_Triage["POST /api/triage/assess"]
            R_Doctor["GET /api/doctor/patients & POST /override"]
            R_Admin["GET /api/admin/logs"]
            R_PreReg["GET & POST /api/preregister"]
        end
        WS_Manager["Central WebSocket Manager<br/>(/ws)"]
        
        CORS --> Validation
        Validation --> CONTROLLERS
    end

    subgraph MULTI_AGENT ["🧠 3. MULTI-AGENT ORCHESTRATION ENGINE"]
        direction TB
        Observer["1️⃣ OBSERVER AGENT<br/>Signal Extraction & Vital Signs Normalization"]
        Planner["2️⃣ PLANNER AGENT<br/>ML Urgency Scoring & Task Planning"]
        Explainer["3️⃣ EXPLAINER AGENT<br/>Clinical Rationale Generation (GPT-4o)"]
        Action["4️⃣ ACTION AGENT<br/>Workflow Triggers & Notification Dispatcher"]
        Learner["5️⃣ LEARNER AGENT<br/>Doctor Override Tracking & Feedback Analytics"]

        Observer --> Planner
        Planner --> Explainer
        Explainer --> Action
    end

    subgraph AI_CORE ["🤖 4. AI & MACHINE LEARNING REASONING CORE"]
        direction TB
        FeatureEng["Feature Engineering Matrix<br/>(features.py)"]
        MLModel["LightGBM Urgency Scoring Model<br/>(model.py)"]
        subgraph LLM_SUITE ["GenAI LLM Suite (llm.py)"]
            GPT4["OpenAI GPT-4o<br/>(Primary Medical Reasoner)"]
            Gemini["Google Gemini 1.5 Pro<br/>(Secondary Backup LLM)"]
            Ollama["Ollama / Llama 3<br/>(Offline Fallback Engine)"]
        end

        FeatureEng --> MLModel
        MLModel --> LLM_SUITE
    end

    subgraph AUTOMATION ["⚡ 5. AUTOMATION & NOTIFICATION ENGINE"]
        direction TB
        BgTasks["FastAPI BackgroundTasks & AsyncIO Event Loop"]
        WorkflowRules["Priority Action Trigger Rules<br/>(workflows.py)"]
        subgraph ALERTS ["Emergency Notification Services (alerts.py)"]
            EmailAlert["SMTP Email Dispatcher"]
            TwilioAlert["Twilio API (SMS / WhatsApp)"]
        end
        BgTasks --> WorkflowRules
        WorkflowRules --> ALERTS
    end

    subgraph PERSISTENCE ["🗄️ 6. DATA STORAGE & PERSISTENCE LAYER"]
        direction TB
        ORM["SQLAlchemy ORM Layer"]
        subgraph DB ["SQLite Relational Database (orion.db)"]
            T_Patients["Patients Table"]
            T_Triage["Triage Results Table"]
            T_Doctor["Doctor Actions Table"]
            T_Audit["Audit Logs Table"]
            T_PreReg["Pre-Registration Table"]
        end
        subgraph LOGGING ["Structured Audit Logging"]
            Loguru["Loguru JSON Logger"]
            GSheets["Google Sheets API Sync"]
        end
        ORM --> DB
        DB --> LOGGING
    end

    %% Cross-layer links
    SERVICES <-->|HTTP REST Requests| CORS
    WS_Client <-->|Live WebSocket Frames| WS_Manager

    R_Patient --> Observer
    R_Triage --> Observer
    R_Doctor -->|Override Feedback| Learner

    Observer --> FeatureEng
    Planner --> MLModel
    Explainer --> LLM_SUITE

    Action --> BgTasks
    Action --> WS_Manager
    Action --> ORM
    Learner --> ORM

    classDef frontendFill fill:#0d1b2a,stroke:#00e5ff,stroke-width:2px,color:#ffffff;
    classDef gatewayFill fill:#1a233a,stroke:#7c4dff,stroke-width:2px,color:#ffffff;
    classDef agentFill fill:#0a2540,stroke:#00b0ff,stroke-width:2px,color:#ffffff;
    classDef aiFill fill:#1c0038,stroke:#d500f9,stroke-width:2px,color:#ffffff;
    classDef autoFill fill:#261200,stroke:#ff9100,stroke-width:2px,color:#ffffff;
    classDef dbFill fill:#002b11,stroke:#00e676,stroke-width:2px,color:#ffffff;

    class FRONTEND frontendFill;
    class GATEWAY gatewayFill;
    class MULTI_AGENT agentFill;
    class AI_CORE aiFill;
    class AUTOMATION autoFill;
    class PERSISTENCE dbFill;
```

---

## 🧠 Multi-Agent AI Pipeline

The system delegates operational responsibilities across specialized autonomous agents:

$$\text{REST Request} \longrightarrow \text{Observer Agent} \longrightarrow \text{Planner Agent} \longrightarrow \text{Explainer Agent} \longrightarrow \text{Action Agent} \longrightarrow \text{Learner Agent}$$

```
+---------------------------------------------------------------------------------------------------+
| 1. OBSERVER AGENT (Signal Extraction & Vital Signs Normalization)                                 |
|    - Input: Raw patient details, symptoms, and vital sign arrays.                                 |
|    - Output: Normalized clinical feature vector (Heart Rate, Systolic/Diastolic BP, SpO2, Temp, RR).  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
| 2. PLANNER AGENT (Machine Learning Urgency Scoring)                                               |
|    - Input: Structured vital sign vector & risk indicators.                                       |
|    - Algorithm: LightGBM / Scikit-learn trained on synthetic emergency clinical datasets.         |
|    - Output: Objective Numerical Urgency Score (0.0 to 10.0) + Priority Tier Classification.         |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
| 3. EXPLAINER AGENT (GenAI Clinical Justification)                                                 |
|    - Input: Urgency score, vital anomalies, and patient verbal problem statement.                 |
|    - LLM Engine: OpenAI GPT-4o / Gemini 1.5 Pro via structured prompt engineering.               |
|    - Output: Concise medical reasoning, risk breakdown, and suggested emergency interventions.    |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
| 4. ACTION AGENT (Workflow Automation & Real-Time Dispatch)                                        |
|    - Database: Saves record to SQLite Patients, TriageResults, and AuditLogs tables.              |
|    - Background Tasks: Fires emergency email and Twilio WhatsApp/SMS alerts if score >= 7.5.     |
|    - WebSockets: Emits NEW_PATIENT event payload to all connected doctor dashboards.              |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
| 5. LEARNER AGENT (Human-in-the-Loop Feedback Loop)                                                |
|    - Action: Captures clinician priority overrides, doctor notes, and override justifications.    |
|    - Feedback: Records entry in DoctorActions DB table & calculates threshold feedback analytics. |
+---------------------------------------------------------------------------------------------------+
```

---

## 🔄 End-to-End Sequence Flow

```mermaid
sequenceDiagram
    autonumber
    actor Patient as 🏥 Patient / Nurse
    participant React as 💻 Frontend Client
    participant FastAPI as 🌐 FastAPI Server
    participant Observer as 👁️ Observer Agent
    participant Planner as 🧠 Planner Agent (ML)
    participant Explainer as 💬 Explainer Agent (LLM)
    participant Action as ⚡ Action Agent
    participant DB as 🗄️ SQLite Database
    participant WS as 🔄 WebSocket Hub
    actor Doctor as ⚕️ Attending Physician

    Patient->>React: Submits Vitals & Symptoms Form
    React->>FastAPI: POST /api/patient/submit
    FastAPI->>Observer: Extract & normalize clinical signals
    Observer-->>Planner: Structured Feature Vector
    Planner->>Planner: Compute LightGBM Urgency Risk Score (0-10)
    Planner->>Explainer: Forward Score + Anomalies
    Explainer->>Explainer: Query GPT-4o for Clinical Rationale
    Explainer-->>Action: Urgency Score + Tier + AI Explanation
    Action->>DB: Save Patient Record & Triage Result
    Action->>Action: Trigger Background Email / Twilio SMS (if Critical)
    Action->>WS: Broadcast NEW_PATIENT Event
    WS-->>Doctor: Instant Queue Update on Doctor Dashboard
    FastAPI-->>React: 200 OK + Triage Assessment JSON

    Note over Doctor, DB: Doctor Review & Override Flow
    Doctor->>React: Reviews AI Explanation & Submits Override
    React->>FastAPI: POST /api/doctor/override
    FastAPI->>DB: Record Override in DoctorActions Table
    FastAPI->>WS: Broadcast OVERRIDE_UPDATED Event
    WS-->>React: Real-time Sync Across All Doctor Screens
```

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **FastAPI** (Python 3.10+) | High-performance async REST API core & routing |
| **ASGI Server** | **Uvicorn** | Asynchronous server implementation |
| **ML Risk Engine** | **LightGBM**, **Scikit-learn**, **NumPy**, **Pandas** | Numerical risk prediction & feature matrix handling |
| **GenAI LLM Suite** | **OpenAI GPT-4o**, **Google Gemini 1.5 Pro**, **Ollama (Llama 3)** | Explainable AI (XAI) clinical justification |
| **Agent Framework** | **LangChain**, **LlamaIndex** | Multi-agent state orchestration & memory |
| **Database & ORM** | **SQLite**, **SQLAlchemy** | Relational data persistence & async CRUD operations |
| **Real-Time Layer** | **WebSockets** (Native Starlette) | Zero-latency bidirectional dashboard synchronization |
| **Automation & Alerts** | **FastAPI BackgroundTasks**, **SMTP Email**, **Twilio API** | Event-driven emergency notifications & escalation |
| **Validation & Security** | **Pydantic v2**, **python-dotenv**, **CORS Middleware** | Type safety, input sanitization, and environment management |
| **Frontend UI** | **React 18**, **Next.js 16**, **Vite**, **Tailwind CSS**, **Framer Motion** | Responsive futuristic medical control center dashboards |

---

## 🗂️ Project Directory Structure

```
orion-backend/
│
├── app/
│   ├── main.py                # 🚀 FastAPI application entry point & WebSocket hub
│   ├── config.py              # ⚙️ Environment variables loader & system configurations
│   ├── database.py            # 🔌 SQLAlchemy database engine & session creation
│   ├── websocket.py           # 🔄 Central WebSocket connection & message manager
│   ├── ai_pipeline.py         # 🧠 Master multi-agent orchestration coordinator
│   │
│   ├── routes/                # 🌐 REST API Router Endpoints
│   │   ├── patient.py         # Patient intake submission & history endpoints
│   │   ├── triage.py          # AI triage execution endpoints
│   │   ├── doctor.py          # Doctor patient queue & override endpoints
│   │   ├── admin.py           # Admin monitoring & system audit logs
│   │   └── preregister.py     # Pre-registration patient lookup APIs
│   │
│   ├── agents/                # 🤖 Multi-Agent Logic Modules
│   │   ├── observer.py        # 1️⃣ Observer Agent: Feature & signal extraction
│   │   ├── planner.py         # 2️⃣ Planner Agent: ML urgency prediction
│   │   ├── explainer.py       # 3️⃣ Explainer Agent: GenAI clinical rationale
│   │   ├── action.py          # 4️⃣ Action Agent: Automation & alert dispatcher
│   │   └── learner.py         # 5️⃣ Learner Agent: Doctor override feedback tracker
│   │
│   ├── ai/                    # 🔬 Machine Learning & LLM Core
│   │   ├── model.py           # LightGBM urgency risk prediction model (with rule fallback)
│   │   ├── features.py        # Feature engineering & matrix normalization
│   │   ├── ollama.py          # Offline LLM fallback integration handler
│   │   └── prompts.py         # Structured medical prompts for GPT-4o / Gemini
│   │
│   ├── automation/            # ⚡ Automation & Notification Services
│   │   ├── alerts.py          # SMTP Email & Twilio WhatsApp/SMS alert dispatchers
│   │   └── workflows.py       # Condition-driven priority task triggers
│   │
│   ├── db/                    # 🗄️ Database Models & Operations
│   │   ├── models.py          # SQLAlchemy table models (Patients, Triage, Overrides, Audit)
│   │   ├── crud.py            # Async CRUD database operations
│   │   ├── prereg_db.py       # Pre-registration database operations
│   │   └── learning_db.py     # Doctor feedback analytics database operations
│   │
│   ├── schemas/               # 📋 Pydantic Validation Schemas
│   │   ├── patient.py         # Intake request validation schema
│   │   ├── triage.py          # AI output payload validation schema
│   │   ├── doctor.py          # Override payload validation schema
│   │   └── preregister.py     # Pre-registration payload schema
│   │
│   └── utils/                 # 🛠️ Helper Utilities
│       └── helpers.py         # ID generators, timestamp formatting, JSON helpers
│
├── orion-frontend/            # 💻 React 18 / Next.js 16 Frontend Application
│   ├── src/
│   │   ├── app/               # Next.js App Router pages
│   │   ├── components/        # Reusable UI components (Patient, Doctor, Admin panels)
│   │   └── lib/               # Direct FastAPI API (`orion-api.ts`) & WebSocket (`orion-ws.ts`) services
│   ├── package.json           # Frontend dependencies
│   └── next.config.ts         # Next.js configuration
│
├── data/                      # 📊 Synthetic demo datasets
├── logs/                      # 📝 Runtime application log files
├── run.py                     # 🚀 Backend server startup launcher script
├── requirements.txt           # 📦 Python backend dependencies
└── README.md                  # 📖 Comprehensive repository documentation
```

---

## 🗄️ Database Schemas & Entity Relationships

The SQLite database (`orion.db`) uses SQLAlchemy ORM with five core operational tables:

```
+-----------------------------------------------------------------------------------+
|                                  PATIENTS TABLE                                   |
+-----------------------------------------------------------------------------------+
| id (PK)           | INTEGER      | Primary Key Auto-Increment                     |
| patient_id        | VARCHAR(50)  | Unique Patient Identifier (e.g., P-98421)      |
| name              | VARCHAR(100) | Full Name                                      |
| age               | INTEGER      | Patient Age                                    |
| gender            | VARCHAR(20)  | Patient Gender                                 |
| pain_score        | INTEGER      | Patient Reported Pain Scale (0 - 10)           |
| symptoms          | TEXT         | Primary Complaints & Verbal Problem Statement |
| heart_rate        | FLOAT        | Heart Rate (bpm)                               |
| blood_pressure    | VARCHAR(20)  | Blood Pressure Reading (e.g., "140/90")        |
| temperature       | FLOAT        | Body Temperature (°C)                          |
| spo2              | FLOAT        | Oxygen Saturation Level (%)                    |
| respiratory_rate  | FLOAT        | Respiratory Rate (breaths/min)                 |
| medical_history   | TEXT         | Chronic Conditions & Medical History           |
| timestamp         | DATETIME     | Entry Creation Timestamp                       |
+-----------------------------------------------------------------------------------+
                                         |
                                         | 1 : 1
                                         v
+-----------------------------------------------------------------------------------+
|                               TRIAGE_RESULTS TABLE                                |
+-----------------------------------------------------------------------------------+
| id (PK)           | INTEGER      | Primary Key Auto-Increment                     |
| patient_id        | VARCHAR(50)  | Foreign Key -> Patients.patient_id            |
| urgency_score     | FLOAT        | Machine Learning Calculated Risk Score (0-10)  |
| priority_tier     | VARCHAR(50)  | Tier: Critical / High / Moderate / Mild / Low  |
| ai_explanation    | TEXT         | GPT-4o / Gemini Clinical Rationale             |
| confidence_score  | FLOAT        | Model Prediction Confidence (0.0 - 1.0)        |
| estimated_wait_min| INTEGER      | Calculated Estimated Wait Time (minutes)       |
| features_json     | TEXT         | Serialized Feature Vector                      |
| timestamp         | DATETIME     | Evaluation Timestamp                           |
+-----------------------------------------------------------------------------------+
                                         |
                                         | 1 : N
                                         v
+-----------------------------------------------------------------------------------+
|                               DOCTOR_ACTIONS TABLE                                |
+-----------------------------------------------------------------------------------+
| id (PK)           | INTEGER      | Primary Key Auto-Increment                     |
| patient_id        | VARCHAR(50)  | Foreign Key -> Patients.patient_id            |
| doctor_id         | VARCHAR(50)  | Attending Doctor ID (e.g., DR-101)             |
| original_score    | FLOAT        | AI Recommended Score                           |
| override_priority | VARCHAR(50)  | Doctor Assigned Override Tier                  |
| doctor_notes      | TEXT         | Clinical Notes & Observations                  |
| override_reason   | TEXT         | Rationale for Modifying AI Score               |
| timestamp         | DATETIME     | Override Timestamp                             |
+-----------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------+
|                                AUDIT_LOGS TABLE                                   |
+-----------------------------------------------------------------------------------+
| id (PK)           | INTEGER      | Primary Key Auto-Increment                     |
| event_type        | VARCHAR(100) | Event Type (e.g., TRIAGE_SUBMIT, OVERRIDE)     |
| event_source      | VARCHAR(50)  | Source Module (e.g., ActionAgent, DoctorRoute) |
| details_json      | TEXT         | Structured Event Payload                       |
| timestamp         | DATETIME     | Event Timestamp                                |
+-----------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------+
|                             PRE_REGISTRATION TABLE                                |
+-----------------------------------------------------------------------------------+
| id (PK)           | INTEGER      | Primary Key Auto-Increment                     |
| hospital_name     | VARCHAR(100) | Hospital Name                                  |
| patient_name      | VARCHAR(100) | Patient Name                                   |
| age               | INTEGER      | Patient Age                                    |
| problem           | TEXT         | Stated Medical Issue                           |
| email             | VARCHAR(100) | Notification Email                             |
| timestamp         | DATETIME     | Pre-registration Timestamp                     |
+-----------------------------------------------------------------------------------+
```

---

## 🔌 REST API & WebSocket Specifications

### Interactive API Documentation
When the backend server is running, FastAPI automatically generates interactive documentation:
- 📖 **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 📑 **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Core REST Endpoints

#### 1. Submit Patient for AI Triage
- **Endpoint**: `POST /api/patient/submit`
- **Request Body**:
  ```json
  {
    "name": "Saurav Sharma",
    "age": 48,
    "gender": "Male",
    "pain_score": 8,
    "symptoms": "Severe crushing chest pain radiating to jaw, diaphoresis, shortness of breath",
    "heart_rate": 118,
    "blood_pressure": "160/100",
    "temperature": 37.4,
    "spo2": 92,
    "respiratory_rate": 26,
    "medical_history": "Hypertension, Type 2 Diabetes"
  }
  ```
- **Response**: `200 OK`
  ```json
  {
    "status": "success",
    "patient_id": "P-98421",
    "urgency_score": 9.4,
    "priority_tier": "Critical (Emergency)",
    "ai_explanation": "Patient presents with acute high-risk cardiac symptoms combined with severe hypoxia (SpO2 92%), tachycardia (118 bpm), and severe hypertension. Fast-track immediately to Resuscitation Bay.",
    "estimated_wait_time": 0
  }
  ```

#### 2. Fetch Prioritized Patient Queue (Doctor Dashboard)
- **Endpoint**: `GET /api/doctor/patients?batch=1`
- **Response**: `200 OK` Array of prioritized patient records ordered by urgency score descending.

#### 3. Fetch Emergency Cases Queue
- **Endpoint**: `GET /api/doctor/emergency?batch=1`
- **Response**: `200 OK` Filtered stream of critical patients requiring immediate resuscitation.

#### 4. Submit Doctor Override
- **Endpoint**: `POST /api/doctor/override`
- **Request Body**:
  ```json
  {
    "patient_id": "P-98421",
    "doctor_id": "DR-101",
    "override_priority": "Critical",
    "doctor_notes": "Signs consistent with Acute Coronary Syndrome. Order STAT ECG and Troponin.",
    "override_reason": "Clinical urgency verification"
  }
  ```

#### 5. Search Pre-Registered Patients
- **Endpoint**: `GET /api/preregister/search/{query}`

---

### Real-Time WebSocket Channel
- **URL**: `ws://localhost:8000/ws`
- **Event Messages**:
  - `NEW_PATIENT`: Dispatched when a new patient triage assessment is finalized.
  - `OVERRIDE_UPDATED`: Dispatched when an attending physician overrides a priority score.
  - `EMERGENCY_ALERT`: Dispatched when a critical resuscitation patient enters the queue.

---

## ⚡ Quickstart & Installation Guide

### Prerequisites
- **Python**: `3.10` or higher
- **Node.js**: `18.x` or higher & `npm`

---

### 1. Launch FastAPI Backend
```bash
# 1. Navigate to backend directory
cd orion-backend

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Install backend dependencies (if not already installed)
pip install -r requirements.txt

# 4. Start backend server
python run.py
```
> The server will start on **`http://localhost:8000`**.

---

### 2. Launch Next.js / React Frontend
```bash
# 1. Open a new terminal and navigate to frontend directory
cd orion-backend/orion-frontend

# 2. Install dependencies (if needed)
npm install --legacy-peer-deps

# 3. Launch dev server
npm run dev
```
> The application dashboard will open on **`http://localhost:3000`**.

---

## 🏆 Presentation Pitch & Key Talking Points for Judges

> *"ORION-Health is built using a modular multi-agent backend that cleanly decouples signal extraction, machine learning risk scoring, GenAI explainability, and background workflow automation. By enforcing strict human-in-the-loop oversight through real-time WebSockets and zero-latency doctor override channels, we combine the speed of AI decision support with absolute clinical safety."*

---

<div align="center">
  <b>Built with ❤️ for Emergency Healthcare Decision Support</b>
</div>