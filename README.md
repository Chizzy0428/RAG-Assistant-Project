# RAG-Assistant-Project


##  RAG-Powered PDF Question Answering Assistant

This project is a simple and interactive **RAG (Retrieval-Augmented Generation)** assistant built with **Streamlit**, allowing users to upload PDF documents and ask natural language questions about them. It uses **LangChain**, **FAISS**, and **OpenAI’s GPT** to retrieve context-relevant answers from uploaded files.



###  Live Demo

You can deploy this on [Streamlit Cloud](https://streamlit.io/cloud) for a free public web app.
to access my deployed project use this link - https://rag-assistant-project-eeyp5rpbdh6cpgy4x5kmbb.streamlit.app/



###  Features

* Upload **any PDF document**
* Ask **questions** in natural language
* Get **contextual answers** with source references
* Powered by **LangChain**, **OpenAI**, and **FAISS**
* Deployable with **Streamlit Cloud**
* Uses **Streamlit Secrets** for secure API key management



###  Tech Stack

| Tool        | Description                                 |
| ----------- | ------------------------------------------- |
| `Streamlit` | Web app UI framework                        |
| `LangChain` | LLM orchestration and pipeline management   |
| `OpenAI`    | GPT-3.5 or GPT-4 for generating answers     |
| `FAISS`     | Fast vector similarity search for documents |
| `PyMuPDF`   | PDF parsing and content extraction          |



###  Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/pdf-rag-assistant.git
cd pdf-rag-assistant
```

2. **Create virtual environment and activate it**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add `.env` file (for local dev only)**

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

>  For production on Streamlit Cloud, you’ll add the key via their **Secrets Manager** instead of `.env`.



###  Running the App

```bash
streamlit run app.py
```

---

###  Secrets Setup on Streamlit Cloud

When deploying, add your secret in **Settings → Secrets**:

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxx"
```



###  How It Works

1. You upload a PDF file.
2. The file is parsed using **PyMuPDF**.
3. It’s split into chunks and embedded with **OpenAI Embeddings**.
4. Vectors are stored in a **FAISS** index.
5. When you ask a question:

   * The app retrieves the most relevant chunks.
   * The **ChatOpenAI** model uses the context to answer.
6. It returns an answer and shows the relevant sources.



### Example Use Cases

* Research paper summarization
* Textbook Q\&A
* Legal or business document understanding
* Personal knowledge assistant


### Example Folder Structure

```
pdf-rag-assistant/
│
├── app.py
├── requirements.txt
├── .env (ignored)
└── README.md
```



### License

This project is open-source under the MIT License.



### Author

I'm Chizaram – Data Scientist, AI Developer
If you have questions or want to collabrate please do reach out





