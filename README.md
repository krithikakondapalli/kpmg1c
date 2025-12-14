# KPMG Trusted AI: Energy Usage and Sustainability
### ***Break Through Tech x Cornell Tech AI Studio Project 2025-26***

### 👥 **Team Members**

**Example:**

| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Krithika Kondapalli    | @krithikakondapalli | Data collection, exploration, model selection, overall project coordination            |
| Athena Tian   | @athenatian06     | [add here]   |
| Sandy Zheng     | @sandyzhengg23  |   [add here]               |
| Mercy Ifiegbu      | @mercy-ifi       |  [add here] |
| Shreyosee Chowdary       | @shreychow    |   [add here]         |

---

## 🎯 **Project Highlights**

**Example:**

- Built Random Forest regression models to analyze and predict energy usage of GenAI systems across LLM, MLLM, and Diffusion tasks.
- Identified key drivers of energy consumption, including tensor parallelism, token output, batch size, and throughput.
- Demonstrated that model type alone is insufficient—energy efficiency depends on how models are deployed and used.
- Delivered actionable, energy-aware AI strategies aligned with KPMG’s Trusted AI and sustainability goals.

---

## 👩🏽‍💻 **Setup and Installation**

- No special setup required.
- Run the provided Jupyter Notebook (.ipynb) using the datasets located in the Data_ML_Energy folder.

---

## 🏗️ **Project Overview**

This project was completed as part of the Break Through Tech AI Fellowship at Cornell Tech, in collaboration with KPMG as the AI Studio host company.

### Objective & Scope
- Analyze the energy consumption of generative AI models used in real-world enterprise settings.
- Identify which features within each model type drive energy usage.
- Propose sustainable, operational strategies for using AI more responsibly.

### Real-World Significance
- Finance ranks among the highest sectors for AI energy burden relative to market capitalization.
- As KPMG scales AI-powered audit and analytics tools, energy-efficient deployment is critical for cost control, sustainability, and trustworthy AI adoption.
---

## 📊 **Data Exploration**

### Dataset
- Source: **ML.Energy Leaderboard Dataset**
- Size: ~470 model configurations
- Model types:
  - **LLM (~314)**
  - **MLLM (~42)**
  - **Diffusion (~118)**
- Tasks: text generation, chat, code, text-to-image, image-to-video, text-to-video

### Key Features
- GPU type  
- Tensor Parallelism (TP)  
- Pipeline Parallelism (PP)  
- Energy per request (J)  
- Average TPOT (latency)  
- Token throughput (tokens/sec)  
- Average and max batch size  

### EDA Insights
- Larger models and higher parallelism generally increase total energy usage.
- Energy patterns vary significantly by **task type** and **modality**.
- LLMs, MLLMs, and Diffusion models require **separate analytical treatment**.

### Preprocessing Steps
- Standardized energy metrics across model types
- Handled missing or non-applicable features
- Log-transformed skewed energy values
- Normalized energy outputs (e.g., energy per token for LLMs)

---

## 🧠 **Model Development**

### Models Used
- Baseline: Linear Regression, Ridge Regression
- Final Model: **Random Forest Regression**

### Why Random Forest?
- Captures **non-linear relationships**
- Robust to outliers and correlated features
- Automatically ranks feature importance

### Our Approaches
- **Option A:** Single model across all task types  
- **Option B:** Separate models per task type (LLM, MLLM, Diffusion)

**Final approach:** Option B, enabling clearer and more actionable insights.

---

## 📈 **Results & Key Findings**

- Task-specific models significantly outperformed a single global model.
- **Tensor parallelism** reduces latency but increases total energy consumption.
- **Token output length and modality** are major drivers of energy usage.
- Energy efficiency depends on:
  - Input shape (sequence length, batch size, frames)
  - Hardware architecture (GPU type, memory, throughput)
  - Deployment configuration (parallelism strategy)

---

## 🚀 **Next Steps**

### Limitations
- Limited company-specific deployment data
- Software/framework-level effects not fully captured

### Future Work
- Incorporate **KPMG-specific workloads and datasets**
- Expand coverage of hardware types and providers
- Build a **lightweight energy-aware dashboard**
- Define organizational standards for deploying higher-energy models

---

## 📄 **References** 

- ML Energy Leaderboard: https://huggingface.co/spaces/ml-energy/leaderboard
- Other Research:
    - https://arxiv.org/html/2504.17674v1 
    - https://huggingface.github.io/AIEnergyScore/#documentation

---

## 🙏 **Acknowledgements** 

We thank our **Break Through Tech AI Studio Coach** and **KPMG Advisors** for their guidance and support:

- Dr. Uohna June Thiessen (AI Studio Coach)
- Agnieszka Jeter, Kathi Ray, Sarah Greene, Yoganand Agnihotram, Ashley Singhal (KPMG Advisors)

---
