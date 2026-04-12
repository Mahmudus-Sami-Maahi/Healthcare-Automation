# 🩺 Doctor Search Chatbot 

A user-friendly AI-powered chatbot that helps users find doctors, their specialties, hospital details, and availability using natural language queries. This project uses **Streamlit**, **LangChain**, and **Groq LLM** to provide intelligent search over a structured dataset.

---

## 🚀 Features

* 🔍 Search doctors using natural language (e.g., "heart doctor", "skin specialist")
* 🧠 Smart keyword mapping to medical specialties
* 📊 Uses structured CSV dataset (`doctors_data.csv`)
* 💬 Interactive chatbot interface with Streamlit
* ⚡ Fast responses powered by Groq LLM
* 🧾 Clean and structured output format

---

## 📁 Project Structure

```
DoctorSearch/
│
├── Searching_system.py     # Main Streamlit chatbot app
├── doctors_data.csv        # Dataset of doctors
├── Data_Scraping.ipynb     # Notebook for scraping data (optional)
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
```

---

## ⚙️ Installation Guide

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd DoctorSearch
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration (IMPORTANT)

This project uses **Groq LLM**, so you must add your API key.

### Step:

Open `Searching_system.py` and replace:

```python
os.environ["Your Model"] = "Your API Key"
```

👉 With:

```python
os.environ["GROQ_API_KEY"] = "your_actual_api_key_here"
```

---

## ▶️ How to Run the Application

Run the Streamlit app:

```bash
streamlit run Searching_system.py
```

Then open your browser and go to:

```
http://localhost:8501
```

---

## 💡 How to Use (User Manual)

### 🧑‍💻 User Interaction Steps

1. Open the app in your browser
2. Enter a query in the input box
3. Click the **Send** button
4. View results displayed below

---

### 📝 Example Queries

Try these:

* `heart doctor`
* `skin specialist`
* `doctors in Evercare hospital`
* `neurologist available tomorrow`
* `doctor for headache`

---

### 🧠 Smart Understanding

The chatbot automatically maps symptoms to departments:

| User Input   | Interpreted As |
| ------------ | -------------- |
| heart pain   | Cardiologist   |
| skin rash    | Dermatologist  |
| headache     | Neurologist    |
| child doctor | Pediatrician   |
| pregnancy    | Gynecologist   |

---

### 📋 Output Format

The chatbot responds like:

```
Doctor Name: Dr. XYZ
Specialization: Cardiologist
Department: Cardiology
Hospital: Evercare Hospital
Address: Dhaka
Booking Time: 10:00 AM
Available Time: 2:00 PM
```

---

## ⚠️ Rules & Limitations

* ❗ Only answers based on provided dataset
* ❗ No external knowledge used
* ❗ Non-medical queries return:

  ```
  I am a medical bot. I do not know other information.
  ```
* ❗ If no match:

  ```
  No matching doctor found.
  ```

---

## 🛠️ Customization

### Update Dataset

Replace or edit:

```
doctors_data.csv
```

Ensure columns include:

* Doctor Name
* Specialization
* Department
* Hospital
* Address
* Booking Time
* Available Time

---

### Modify Prompt Behavior

Edit the prompt inside:

```
Searching_system.py
```

You can:

* Add new specialties
* Improve keyword mapping
* Change output format

---

## 📊 Optional: Data Scraping

Use:

```
Data_Scraping.ipynb
```

To:

* Scrape doctor data
* Clean and export CSV

---

## 🐞 Troubleshooting

### Common Issues

**1. Streamlit not found**

```bash
pip install streamlit
```

**2. API Key Error**

* Make sure `GROQ_API_KEY` is set correctly

**3. CSV not loading**

* Ensure file path is correct
* File must be in same directory

---

## 📌 Future Improvements

* 🔎 Add filters (location, time)
* 🌐 Deploy online (Streamlit Cloud)
* 🗣️ Voice input support
* 📱 Mobile optimization
* 🧠 Better NLP matching

---

## 🤝 Contributing

Feel free to fork the repo and improve:

* UI design
* Search accuracy
* Data quality

---

## 📄 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Developed as an AI-powered healthcare assistant project.

---

⭐ If you like this project, don't forget to give it a star!
