# Smart AI Help Desk!

A customer support chatbot using Rasa (Python) for the backend and a modern HTML/JS frontend.
An intelligent AI-powered chatbot designed to handle real-time customer support queries using advanced machine learning tools and natural language processing.
Overview
This project implements a smart conversational AI system that can understand customer inquiries, provide relevant responses, and escalate complex issues when necessary. Built with modern AI/ML frameworks, it offers seamless integration for customer service workflows.

##Why did we use Rasa (and not others)?
-Rasa is an open-source conversational AI framework built in Python.
-It gives full control over NLU (intent/entity extraction), dialogue management, and custom actions.
-It is highly customizable, production-ready, and supports advanced features (like custom pipelines, fallback, and integrations).
-Rasa works well with YAML training data and is easy to extend for new intents/entities.
-It is free, has a strong community, and is not tied to any cloud provider.
**We did not use:
Dialogflow, IBM Watson, Microsoft Bot Framework, etc. because they are cloud-based, less customizable, may have usage costs, and often lock you into their ecosystem.

##Key Features:
-Real-time Query Processing: Instant responses to customer inquiries
-Natural Language Understanding: Advanced NLP for context-aware conversations
-Intent Classification: Automatically categorizes and routes customer requests
-Escalation System: Smart handoff to human agents when needed

## Features:
- Personalized greetings (extracts any name)
- Fallback and human agent transfer
- Download chat history
- File/image upload
- Clean, modern chat UI

## How to Run Locally:
1. Train: `rasa train`
2. Start server: `rasa run --enable-api --cors "*"`
3. Open `chat.html` in your browser

## TECHSTACK & DEPLOYMENT:
- Backend:
- Built with **Rasa** (Python)
- Hosted on **Render.com** (or your chosen cloud platform)
- Exposes a REST API for chatbot communication

- Frontend: Pure HTML, CSS, and JavaScript (no frameworks)
- File: `chat.html`
- used streamlit for ui before then switched , cause it only got very limited functionalities!(if neede ,its available as {app.py}).

## Author
hrishi 