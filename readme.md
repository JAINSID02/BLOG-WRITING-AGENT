# BlogForge

> **A multi-agent AI blog generation system built with LangGraph that researches, plans, writes, and assembles high-quality technical articles using autonomous AI agents.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-blue?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![Mistral](https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge\&logo=streamlit)

---

## Overview

BlogForge is a multi-agent AI application that transforms a single topic into a well-structured technical blog.

Instead of relying on a single LLM prompt, the application orchestrates multiple specialized AI agents using **LangGraph**. Each agent is responsible for a specific stage of the workflow, including routing, research, planning, content generation, and final assembly.

The backend is designed around modular AI agents, structured state management, and parallel execution, making the system easier to extend and maintain than a traditional prompt-based application.

---

## Features

* Multi-agent architecture powered by LangGraph
* Intelligent routing to determine when web research is required
* Automated research using Tavily Search
* Structured blog planning with Pydantic models
* Parallel section generation using worker agents
* Evidence-aware content generation with citation support
* Automatic Markdown blog generation
* Modern Streamlit interface
* Download generated blogs as Markdown files

---

## Architecture

```text
                    User Topic
                         │
                         ▼
                 Router Agent
                         │
         ┌───────────────┴───────────────┐
         │                               │
     Skip Research                 Research Agent
         │                               │
         └───────────────┬───────────────┘
                         ▼
                  Planning Agent
                         │
                         ▼
              Parallel Worker Agents
                         │
                         ▼
                  Reducer Agent
                         │
                         ▼
                Final Markdown Blog
```

---

## How It Works

BlogForge follows a graph-based workflow where each AI agent performs a specific responsibility before passing its output to the next stage.

### 1. Router Agent

The workflow begins by analyzing the user's topic. Based on the request, the router decides whether the blog can be generated using the model's existing knowledge or if external web research is required.

### 2. Research Agent

If research is needed, BlogForge retrieves relevant information using the Tavily Search API. The collected sources are cleaned, deduplicated, and converted into structured evidence for downstream agents.

### 3. Planning Agent

Instead of generating the entire article in one prompt, the planning agent creates a structured outline containing section titles, objectives, word targets, and writing constraints.

### 4. Parallel Worker Agents

Each planned section is assigned to an independent worker agent. These agents generate their sections simultaneously while following the overall blog plan and using the available evidence when required.

### 5. Reducer Agent

Finally, all generated sections are combined into a single Markdown document, preserving the correct order and formatting before being returned to the user.

---

## Technology Stack

| Category          | Technologies         |
| ----------------- | -------------------- |
| **Language**      | Python               |
| **AI Frameworks** | LangGraph, LangChain |
| **LLM**           | Mistral AI           |
| **Research**      | Tavily Search API    |
| **Validation**    | Pydantic             |
| **Frontend**      | Streamlit            |
| **Environment**   | python-dotenv        |
| **Output**        | Markdown             |

---

## Project Structure

```text
BlogForge/
│
├── app.py                # Streamlit frontend
├── main.py               # LangGraph workflow
├── requirements.txt
├── .env
└── README.md
```

The backend follows a modular, graph-based architecture where each node is responsible for a single stage of the content generation pipeline. The Streamlit frontend serves as a lightweight interface for interacting with the backend workflow.

## Getting Started

### Prerequisites

Before running the project, make sure you have:

* Python 3.11 or later
* A Mistral AI API Key
* A Tavily Search API Key

---

## Installation

Clone the repository.

```bash
git https://github.com/JAINSID02/BLOG-WRITING-AGENT.git
cd BlogForge
```

Create and activate a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Running the Application

Launch the Streamlit application.

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Example Workflow

1. Enter a technical topic.
2. Click **Generate**.
3. The Router Agent determines whether research is required.
4. If needed, the Research Agent gathers relevant sources.
5. The Planning Agent creates the blog outline.
6. Worker Agents generate each section in parallel.
7. The Reducer Agent assembles the final Markdown document.
8. Preview or download the generated blog.

---

## Future Improvements

Some planned enhancements include:

* Support for multiple LLM providers
* RAG with private knowledge bases
* SEO optimization
* Human-in-the-loop editing
* Multi-language blog generation
* PDF and HTML export
* Direct publishing to blogging platforms
* Persistent conversation memory
* Token usage and cost tracking

## Why I Built This

I built BlogForge to explore how modern AI applications can move beyond single-prompt interactions by using autonomous, specialized agents. The goal was to design a system that separates research, planning, content generation, and orchestration into independent components while maintaining a clean and scalable architecture.

This project strengthened my understanding of multi-agent workflows, LangGraph orchestration, structured outputs, and building production-oriented LLM applications.

---

## License

This project is licensed under the **MIT License**.

Feel free to use, modify, and build upon it for personal or commercial projects.

---

## Connect With Me

I'm always interested in discussing AI engineering, LLM applications, and backend system design.

* **GitHub:** [https://github.com/](https://github.com/JAINSID02)[JAINSID02](https://github.com/JAINSID02)
* **LinkedIn:** [https://linkedin.com/in/](https://linkedin.com/in/jisidharthjain)[jisidharthjain](https://linkedin.com/in/jisidharthjain)

If you found this project interesting or helpful, consider giving it a ⭐ on GitHub.

---

> **Built with Python, LangGraph, Mistral AI, Tavily Search, and Streamlit.**
