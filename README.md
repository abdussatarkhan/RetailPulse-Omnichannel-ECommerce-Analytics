# RetailPulse — Omnichannel E-Commerce & Supply Chain Intelligence

[![CI](https://github.com/abdussatarkhan/RetailPulse-Omnichannel-ECommerce-Analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/abdussatarkhan/RetailPulse-Omnichannel-ECommerce-Analytics/actions)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Star_Schema-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-RFM_Segmentation-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-Supply_Chain_ML-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Author](https://img.shields.io/badge/Author-Abdussatar-E50914?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abdussatarkhan)

> **Omnichannel retail analytics and supply chain intelligence platform tracking $139M+ Gross Merchandise Value (GMV), customer RFM behavioral segmentation, warehouse fulfillment SLA compliance, and checkout conversion drop-off funnels.**

---

## 🏛️ System Architecture

```mermaid
graph TD
    subgraph Multi-Channel Ingestion
        DTC[Shopify DTC Store] --> ETL[Python Data Pipeline]
        Amazon[Amazon Seller Central] --> ETL
        Retail[POS Retail Flagships] --> ETL
    end
    subgraph Data Warehouse
        ETL --> Star[(PostgreSQL 16 Star Schema: Orders, Products, Warehouses)]
        Star --> RFM[Customer RFM Segmentation Engine]
    end
    subgraph BI & Optimization
        RFM --> Dashboards[Power BI Executive Dashboards & ROAS Optimization]
    end
```

---

## 📊 Visual Analytics & Performance Showcase

<div align="center">

| Omnichannel GMV by Channel | RFM Customer Value Matrix |
| :---: | :---: |
| ![GMV by Channel](screenshots/01_omnichannel_kpi_hero.png) | ![RFM Segmentation](screenshots/02_rfm_customer_clusters.png) |

| Warehouse 48-Hour SLA Rates | Checkout Conversion Funnel |
| :---: | :---: |
| ![Warehouse SLA](screenshots/03_fulfillment_sla_heatmap.png) | ![Conversion Funnel](screenshots/04_funnel_conversion_rates.png) |

</div>

<div align="center">

[![Daily Streak](https://img.shields.io/badge/Daily%20Streak-Active%20%F0%9F%94%A5-brightgreen?style=flat-square&logo=github)](https://github.com/abdussatarkhan)
[![Master Portfolio](https://img.shields.io/badge/Portfolio-50%2B%20Enterprise%20Projects-0e75b6?style=flat-square&logo=github)](https://github.com/abdussatarkhan/abdussatarkhan)
[![Author: Abdussatar](https://img.shields.io/badge/Author-Abdussatar-24292e?style=flat-square&logo=github)](https://github.com/abdussatarkhan)

</div>


---

## 🌟 Key Technical Highlights

1. **RFM Segmentation Engine**: Categorizes 500k+ customer records into actionable cohorts (*Champions*, *Potential Loyalists*, *At-Risk*, *Lost*) to guide personalized retention marketing.
2. **Supply Chain SLA Optimization**: Tracks regional warehouse fulfillment cycles and stockout frequencies across 5 major distribution hubs.
3. **Executive DAX Formulas**: Pre-calculated measures for Customer Lifetime Value (LTV), Return on Ad Spend (ROAS), and Average Order Value (AOV).

---

## 🚀 Quickstart & Setup

```bash
# 1. Clone repository
git clone https://github.com/abdussatarkhan/RetailPulse-Omnichannel-ECommerce-Analytics.git
cd RetailPulse-Omnichannel-ECommerce-Analytics

# 2. Run data generator & tests
pip install pandas numpy pytest
python scripts/01_generate_synthetic_data.py
pytest tests/ -v
```

---

## 🗺️ Roadmap & Upcoming Features

- [x] Omnichannel Star Schema data warehouse DDL
- [x] RFM customer segmentation clustering algorithm
- [x] Warehouse fulfillment SLA tracking
- [ ] Customer basket affinity / market basket association rules (Apriori)
- [ ] Real-time inventory replenishment forecasting

---

## 👨‍💻 Author & Profile

Built by **Abdussatar** ([@abdussatarkhan](https://github.com/abdussatarkhan)).  
Connect on [LinkedIn](https://www.linkedin.com/in/abdus-satar-5150813b5/) or explore other repositories on [GitHub](https://github.com/abdussatarkhan).

---

## 📜 License
MIT License — see LICENSE for details.


---

<div align="center">

### 👨‍💻 Maintained by [Abdussatar (@abdussatarkhan)](https://github.com/abdussatarkhan)
Part of the **[Master Enterprise Data Analytics & AI Portfolio](https://github.com/abdussatarkhan/abdussatarkhan)**.

⭐ If you find this repository valuable, consider dropping a star! ⭐

</div>
