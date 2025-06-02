# 📊 Sales Analytics Dashboard

This is a full-stack interactive dashboard for Superstore Sales Data using:

- **Flask** as the backend API  
- **Elasticsearch** as the search & analytics engine  
- **HTML + CSS + Bootstrap + js** for frontend visuals  
- **Kibana** for advanced heatmaps and analytics dashboards

---

## 🔧 Tech Stack

| Component      | Technology                 |
|----------------|----------------------------|
| Backend        | Flask (Python)             |
| Search Engine  | Elasticsearch 8.x          |
| Frontend       | Bootstrap 5, HTML, CSS, JS |
| Data           | Superstore Dataset         |
| Visualization  | Kibana                     |

---

## 🚀 Features

- 🔍 Filter by Region, Category, Profit/Loss, and Date Range  
- 📑 Paginated results with full summary table  
- 🌗 Dark mode toggle for UI  
- 📊 Visual insights using Chart.js:
  - Sales Over Time
  - Sales by Category
  - Sales by Region
  - Profit vs Loss (Pie Chart)
- 🔥 Kibana Dashboard

---

## 📸 Screenshots

![Webpage](https://github.com/user-attachments/assets/d29b836a-a3bf-4ae9-b0bd-4878d75beae2)
![Webpage Table](https://github.com/user-attachments/assets/a3ac1e2e-701d-4d36-b6e0-ac6741171165)
![Kibana Dashboard](https://github.com/user-attachments/assets/e4f936a8-c6ad-4682-8502-2f116066e6f0)

---

## 📂 Folder Structure

```
sales-dashboard-project/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── README.md
├── dashboard.ndjson          # Exported Kibana Dashboard
├── screenshots/
│   ├── Dashboard.png
│   └── Webpage.png
└── static/ (optional)
```

---

## 🏁 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sales-dashboard-project.git
cd sales-dashboard-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Elasticsearch (via Docker)
```bash
docker run -d -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" elasticsearch:8.13.4
```

### 4. Run the Flask App
```bash
python app.py
```

Then open your browser at:  
[http://localhost:5000](http://localhost:5000)

---

## 📊 Kibana Dashboard

To load the Kibana dashboard:

1. Open Kibana: `http://localhost:5601`
2. Go to **Stack Management > Saved Objects**
3. Click **Import**, upload `dashboard.ndjson`
4. Go to **Dashboards** and open the imported dashboard

---

## 📦 Data Used

This project uses the [Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final), cleaned and indexed into Elasticsearch.

---

## 🎥 Demo Video

_(Optional: Add Loom or YouTube link here if available)_

---

## 👤 Author

**Hammadur Rahman**  
[GitHub](https://github.com/VnMxMadMax)  
[LinkedIn](https://www.linkedin.com/in/hammadur-rahman02/)  
[Email](mailto:hammadurrahman171@gmial.com)

---

## 📃 License

This project is for academic and demonstration purposes only.
