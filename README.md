# spec2chat-demo

chatbot engine inspired by a random arxiv paper i found while doomscrolling

## what is this

basically you feed it openapi specs and it spits out a task-oriented chatbot. no handcrafting dialogue rules, the thing generates the whole flow itself — slot filling, service picking, question asking, all that.

the paper it's based on:

> **Spec2chat: A Python library for task-oriented dialogue generation from OpenAPI specifications**
> Rodríguez-Sánchez, M. J., Ruiz-Zafra, A., Callejas, Z., & Benghazi, K.
> *SoftwareX*, Vol. 32, December 2025, 102409
> DOI: [10.1016/j.softx.2025.102409](https://doi.org/10.1016/j.softx.2025.102409)

## what's in here

- `backend-go/` — go backend, handles service integration and orchestration
- `bot-python/` — python chatbot engine, implements the spec2chat dialogue logic
- docker setup so you don't gotta fight your machine

## how to run it

### stuff you need

- docker + docker compose
- python 3.10+ if you wanna run without docker
- go 1.21+ if you're messing with the backend

### steps

1. clone it

   ```bash
   git clone https://github.com/nafi-mly/spec2chat-demo
   cd spec2chat-demo
   ```

2. set up env vars

   ```bash
   cp .env.example .env
   ```

   you'll need:
   - `OPENAI_API_KEY` — for the LLM dialogue generation
   - `MONGODB_URI` — mongo connection string (defaults to `mongodb://localhost:27017`)

3. fire it up

   ```bash
   docker compose up --build
   ```

   spins up the python bot, go backend, and whatever services it needs

4. run the integration test

   ```bash
   ./test.sh
   ```

## how it actually works

1. **service definition** — openapi specs with custom `x-domain` and `x-question` fields tell the bot what services exist and what to ask
2. **slot filling** — bot yanks required params out of whatever the user typed
3. **service selection** — if multiple services match, bot asks a clarifying question
4. **question generation** — LLM generates natural questions to fill missing slots
5. **dialogue completion** — once slots are filled, it fires the service call

the python lib exposes a simple API:

```python
from spec2chat import run_chatbot

response = run_chatbot("I want a cheap vegetarian restaurant")
# keep the convo going by passing the updated state:
response = run_chatbot("yes", **response)
```

## structure

```
spec2chat-demo/
├── backend-go/          # go backend service
├── bot-python/          # python chatbot engine
├── docker-compose.yml   # docker orchestration
├── .env.example         # env var template
├── test.sh              # integration test script
└── README.md
```

## links

- paper: https://doi.org/10.1016/j.softx.2025.102409
- pypi: https://pypi.org/project/spec2chat/ — `pip install spec2chat`
