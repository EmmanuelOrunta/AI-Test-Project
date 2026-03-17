# AI-Test-Project
📊 AI-Powered Data Analysis Chatbot with Natural Language Querying

This project is an AI-driven data analysis tool that allows users to interact with datasets using simple natural language questions.

Instead of writing complex Python or SQL queries, users can upload a dataset and ask questions like:

“What is the total sales?”
“Group sales by product line”
“Plot sales by month”

The system translates these questions into executable Python (Pandas) code and returns the results instantly.

💡 Why I Built This

While learning data analysis and machine learning, I noticed that working with data often requires technical skills that not everyone has.

I wanted to explore how AI (specifically large language models) can bridge that gap by allowing users to analyze data conversationally.

This project is my attempt to combine:

Data analysis (Pandas)

AI (LLMs)

User-friendly interfaces (Streamlit)

into one practical application.

⚙️ How It Works

The workflow is simple:

Upload a dataset (CSV)

Ask a question in plain English

The AI converts the question into Pandas code

The code is executed

The result (table or chart) is displayed

🚀 Features

Upload and explore CSV datasets

Ask questions in natural language

Automatic generation of Pandas code

Chat-style interface for continuous interaction

Supports summaries, aggregations, and visualizations

Maintains conversation history

🛠️ Tech Stack

Python

Streamlit

Pandas

OpenAI API

Matplotlib / Seaborn

📌 Example Questions

Here are some example queries you can try:

What is the total SALES?

What is the average PRICEEACH?

Group SALES by PRODUCTLINE

Plot SALES by MONTH_ID

Show the top 10 highest sales

🧠 Key Things I Learned

Working on this project helped me understand:

How LLMs can be used beyond chat (e.g., code generation)

The importance of prompt engineering for reliable outputs

How to safely execute AI-generated code

How to build interactive data apps using Streamlit

Managing API keys securely using environment variables

⚠️ Challenges Faced

Some of the challenges I encountered:

Handling encoding issues when reading CSV files

Managing execution of AI-generated code (eval vs exec)

Improving response speed by removing heavy agent frameworks

Formatting outputs (especially DataFrames) properly in the UI

Designing prompts that consistently return usable code****
