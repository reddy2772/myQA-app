# QA App using Gemma (LangChain + Streamlit)

This project is a simple Question Answering web application built using **LangChain**, **Streamlit**, and a locally running AI model (**Gemma 2B via Ollama**).

---

## Features

* Ask any question through a web interface
* Uses a local AI model (no internet required after setup)
* Clean and simple UI using Streamlit
* Built using LangChain for prompt handling

---

## Technologies Used

* Python
* LangChain
* Streamlit
* Ollama
* Gemma 2B Model

---

## Project Structure

```
myQA-app/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/reddy2772/myQA-app.git
cd myQA-app
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install Ollama and model

```
ollama pull gemma:2b
```

---

## Run the Application

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## How It Works

1. User enters a question in the Streamlit UI
2. LangChain formats the prompt
3. The prompt is sent to Gemma model via Ollama
4. Model generates response
5. Answer is displayed on the screen

---

## Example

**Input:**
What is Artificial Intelligence?

**Output:**
Artificial Intelligence is the simulation of human intelligence in machines...

---

## Note

* This app uses a **pre-trained model**
* It does NOT fetch real-time internet data
* Answers are generated based on learned knowledge

---

## Future Improvements

* Add chat history (memory)
* Add PDF-based Q&A (RAG)
* Improve UI

---

## Conclusion

This project demonstrates how to build a simple AI-powered application using local LLMs and modern frameworks like LangChain and Streamlit.

---
