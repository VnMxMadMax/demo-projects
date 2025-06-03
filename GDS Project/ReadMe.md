# 🛒 Sales Dashboard (2021–2022)

This project features an interactive **Sales Performance Dashboard** built using **Google Data Studio**, designed to provide high-level insights into e-commerce transactions from August 2021 to January 2022. The dashboard allows stakeholders to monitor key metrics, analyze trends, and evaluate the effectiveness of promotional campaigns.

---

## 📊 Dashboard Highlights

- **Total Sales Revenue**: $1,990  
- **Average Item Price**: $30.15  
- **Total Items Sold**: 66  
- **Total Customers**: 29  
- **Time Period**: Aug 1, 2021 – Jan 20, 2022

---

## 📁 Dataset

The dataset contains transactional-level data including:
- `Date`
- `Buyer`
- `SKU` (Product Code)
- `Quantity`
- `Price`
- `Promo Code`
- `Discount Amount`
- `Country`

> 📄 File Used: [`Sales Data.csv`](./Sales%20Data.csv)

---

## 🔢 Calculated Fields

To enhance analysis, the following **calculated fields** were created in Google Data Studio:

### 1. `Sales Revenue`
```text
Quantity * Price
```

### 2. `Revenue After Discount`
```text
(Quantity * Price) - Discount Amount
```

### 3. `Promo Code (Cleaned)`
Groups variations of promo codes for cleaner campaign insights.
```sql
CASE
  WHEN PromoCode IN ('SALE01', 'SALE2021') THEN 'SALE01'
  WHEN PromoCode IN ('FLASH', 'FLASH20') THEN 'FLASH20'
  WHEN PromoCode IS NULL THEN 'N/A'
  ELSE PromoCode
END
```

---

## 📈 Key Visualizations

- **KPI Cards**: Display top metrics like revenue, price, item count, and customer count.
- **Time-Series Chart**: Monthly trend of sales and price variation.
- **Geo Heatmap**: Sales distribution by delivery country.
- **Pie & Bar Charts**: Product-level sales contribution.
- **Campaign Table**: Sales revenue vs. discount impact for each promo code.

---

## 🧠 Insights & Observations

- Majority of sales came from one product (`P001`) contributing 42.2% of total revenue.
- `CYBER2021` promo was the most effective campaign (8 buyers, $224 revenue).
- Most buyers were concentrated in the USA, as visualized on the Geo Chart.
- Sales peaked in January 2022, indicating strong year-end demand.

---

## 🛠️ Tools Used

- **Google Data Studio**
- **Google Sheets / CSV**
- **Data Cleaning & Transformation (within Data Studio)**

---

## 📌 How to Use

1. Open the Google Data Studio report link (if public).
2. Use the dropdown filters to explore data by:
   - Delivery Country
   - Coupon Code
   - SKU
   - Buyer
   - Date Range
3. Hover over charts for interactive data tooltips.

---

## 📎 Resources

- 📊 ![Dashboard Image](![Dashboard Image](https://github.com/user-attachments/assets/6370832a-f7dc-4aa2-ab89-0ee75b533c43))
- Dashboard URL - https://lookerstudio.google.com/reporting/69e8d80a-ef6c-475e-92ba-41f92943f3bd
---

## 🙋 Author

**Hammadur Rahman**  
Aspiring Data Analyst | Python & SQL Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/hammadur-rahman02/)  
💻 [GitHub](https://github.com/VnMxMadMax)

---

## 🚀 Future Work

- Add comparison with previous year’s sales.
- Connect live data sources using Google Sheets API.
- Deploy as an embeddable report on a portfolio website.

---
