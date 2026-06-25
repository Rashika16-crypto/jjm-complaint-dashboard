# 🚰 JJM Complaint Monitoring Dashboard

**Jal Jeevan Mission — Government of India | Chhattisgarh**

A real-world data analysis project built during my role as **Data Analyst & MIS Coordinator** at Jal Jeevan Mission. Tracks 500+ complaints across 10 districts, monitors SLA breaches, and measures officer performance.

---

## 📊 Dashboard Preview

![JJM Dashboard](outputs/jjm_dashboard.png)

---

## 🎯 Key Results

| KPI | Value |
|-----|-------|
| Total Complaints Analysed | 520 |
| Resolution Rate | 54.4% |
| SLA Breach Rate | 10.6% |
| Avg Resolution Time | 7.4 days |
| Avg Satisfaction Score | 3.85 / 5.0 |

---

## 🛠️ Tools & Technologies

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **Data** — Mock dataset modelled on real JJM operational data
- **Output** — 9-panel executive dashboard + district summary CSV

---

## 📁 Project Structure

```
jjm-complaint-dashboard/
├── jjm_analysis.py        ← Main analysis script
├── requirements.txt       ← Python dependencies
├── outputs/
│   ├── jjm_dashboard.png  ← 9-panel visual dashboard
│   └── district_summary.csv ← District-level KPI report
└── README.md
```

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Rashika16-crypto/jjm-complaint-dashboard.git
cd jjm-complaint-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
python jjm_analysis.py

# Output saved to outputs/ folder
```

---

## 📌 Insights Generated

- **District-level complaint volume** — identifies hotspot areas needing urgent attention
- **SLA breach rate per district** — flags districts exceeding 15% breach threshold (highlighted in red)
- **Officer resolution rates** — ranks 15 field officers; those below 60% target flagged
- **Category breakdown** — pipe leakage and motor failure are top complaint types
- **Monthly trend** — tracks seasonal complaint spikes for proactive planning
- **Satisfaction score distribution** — 65%+ complainants rate resolution 4/5 or above

---

## 👩‍💻 Author

**Rashika Misra** | Data Analyst & MIS Coordinator  
📧 rashikamisra25@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/rashika-tiwari07)
