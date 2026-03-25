# 📊 AI-Powered Data Analysis Chatbot with Natural Language Querying

This project is an AI-driven data analysis tool that allows users to interact with datasets using simple natural language questions.

Instead of writing complex Python or SQL queries, users can upload a dataset and ask questions like:

> “What is the total sales?”  
> “Group sales by product line”  
> “Plot sales by month”

The system translates these questions into executable Python (Pandas) code and returns the results instantly.

---

## 📸 Application Demo

### 🔹 Chat Interface
![Chat Interface](images/chat interface.png)

### 🔹 Dataset Upload & Preview
![Dataset Preview](images/dataset_preview.png)

### 🔹 Data Analysis Result (Table)
![Table Result](images/table_result.png)

### 🔹 Data Visualization (Chart)
![Chart Result](images/chart_result.png)

---

## 💡 Why I Built This

While learning data analysis and machine learning, I noticed that working with data often requires technical skills that not everyone has.

I wanted to explore how AI (specifically large language models) can bridge that gap by allowing users to analyze data conversationally.

This project combines:
- Data analysis (Pandas)
- AI (LLMs)
- Interactive UI (Streamlit)

into one practical application.

---

## ⚙️ How It Works

1. Upload a dataset (CSV)  
2. Ask a question in plain English  
3. The AI converts the question into Pandas code  
4. The code is executed  
5. The result (table or chart) is displayed  

---

## 🚀 Features

- Upload and explore CSV datasets  
- Ask questions in natural language  
- Automatic generation of Pandas code  
- Chat-style interface for continuous interaction  
- Displays results as tables and visualizations  
- Maintains conversation history  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- OpenAI API  
- Matplotlib  
- Seaborn  
- python-dotenv  

---

## 📌 Example Questions

- What is the total SALES?  
- What is the average PRICEEACH?  
- Group SALES by PRODUCTLINE  
- Plot SALES by MONTH_ID  
- Show the top 10 highest sales  

---

## 🧠 Key Learnings

Working on this project helped me understand:

- How LLMs can be used beyond chat (e.g., code generation)  
- The importance of prompt engineering for reliable outputs  
- How to safely execute AI-generated code  
- Building interactive data applications using Streamlit  
- Managing API keys securely using environment variables  

---

## ⚠️ Challenges Faced

Some challenges I encountered while building this project:

- Handling encoding issues when reading CSV files  
- Managing execution of AI-generated code (`eval` vs `exec`)  
- Improving performance by removing heavy agent frameworks  
- Formatting DataFrame outputs properly in a chat UI  
- Designing prompts that consistently return usable Python code  

---

## 🚧 Future Improvements

- Support for Excel files  
- More advanced visualizations  
- Downloadable analysis reports  
- Better handling of complex queries  
- Deployment as a public web app  

---

## 👨‍💻 Author

**Emmanuel Orunta**

---

This project is part of my learning journey in data analytics and AI.

It demonstrates how large language models can be used to simplify data analysis by transforming natural language into executable code.
