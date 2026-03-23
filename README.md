# 📈 Stock Market Movement Prediction
## Preprocessing & EDA Guide

---

## 🎯 Problem Statement

Predict whether a stock will move **UP** or **DOWN** using technical indicators:

- **RSI** (Relative Strength Index)
- **MACD** (Moving Average Convergence Divergence)  
- **SMA Ratio** (Simple Moving Average)
- **Volume Change**
- **Volatility**

---

## 🧹 Data Preprocessing

### ✅ Data Validation

| Aspect | Status | Details |
|--------|--------|---------|
| **Missing Values** | ✓ Checked | None significant |
| **Data Types** | ✓ Verified | All numerical features |
| **Domain Constraints** | ✓ Ensured | RSI ∈ [0, 100], Volatility ≥ 0 |

> 💡 **Focus was on validation rather than unnecessary cleaning**

### ⚙️ Feature Engineering

Created meaningful indicators to capture market dynamics:

| Indicator | Type | Purpose |
|-----------|------|---------|
| **RSI** | Momentum | Overbought/oversold conditions |
| **MACD** | Trend | Trend strength and direction |
| **SMA Ratio** | Trend | Short vs long-term trend comparison |
| **Volatility** | Risk | Market volatility measurement |
| **Volume Change** | Activity | Trading volume movements |

### 🔥 Interaction Features

To capture combined effects of multiple indicators:

```
rsi_macd = RSI × MACD
macd_sma = MACD × SMA_Ratio
rsi_sma = RSI × SMA_Ratio
rsi_macd_sma = RSI × MACD × SMA_Ratio
```

> 💡 **Goal: Capture interaction between momentum and trend signals**

### ⚖️ Feature Scaling

- **Method**: StandardScaler applied to all features
- **Result**: All features on comparable scale
- **Benefit**: Fair contribution during modeling

> *"Scaling ensures fair contribution of features during modeling."*

---

## 📊 Exploratory Data Analysis (EDA)

### 📉 Correlation with Target

| Feature | Correlation | Impact Level |
|---------|-------------|--------------|
| **MACD** | 0.87 | 🔥 **Strongest** |
| **RSI** | 0.42 | Moderate |
| **SMA Ratio** | 0.18 | Weak |
| **Volatility** | 0.22 | Weak |
| **Volume Change** | 0.05 | Negligible |

**🧠 Key Insight:** MACD is the most influential feature, indicating trend-based signals dominate stock movement.

---

### ⚔️ Interaction Feature Analysis

- ✓ Interaction features were tested comprehensively
- ✗ None outperformed standalone MACD
- 💬 *"Additional complexity does not always improve predictive power."*

---

### 📊 Class-wise Analysis

How indicators behave across UP/DOWN movements:

| Indicator | DOWN (0) | UP (1) |
|-----------|----------|--------|
| **MACD** | Higher | Lower |
| **RSI** | Slightly higher | Lower |

**🧠 Insight:** Higher MACD values are associated with downward movement, suggesting trend exhaustion at peaks.

---

### 🔥 RSI Zone Analysis

Probability of upward movement by RSI zone:

| RSI Zone | Probability of UP |
|----------|-------------------|
| **Low** (0-30) | 57.7% ⬆️ |
| **Neutral** (40-60) | 50.8% ↔️ |
| **High** (70-100) | 47.7% ⬇️ |

**🧠 Interpretation:**
- **Low RSI** → Oversold conditions → Upward reversal likely
- **High RSI** → Overbought conditions → Correction likely
- **Neutral RSI** → No clear directional bias

---

### 📈 Feature Behavior Over Time

- **MACD** → Highly volatile → Captures sharp changes
- **RSI** → Smooth curve → Stable momentum signal
- **SMA Ratio** → Relatively flat → Weak standalone signal

---

## 🧠 Final Insights

### Key Findings

✓ Stock movement is **multi-factor driven**  
✓ **MACD (trend)** is the strongest predictive signal  
✓ **RSI (momentum)** helps detect reversal points  
✓ Interaction features provide insights but don't dominate  
✓ Volume and volatility have limited standalone impact  

### Final Conclusion (Say This in Viva)

> *"Stock movement cannot be explained by a single indicator. It is driven by a combination of trend and momentum signals, with MACD playing a dominant role."*

---

## 🚀 Key Takeaways

✔️ **Data validation is as important as cleaning**  
✔️ **Feature engineering drives performance**  
✔️ **Simpler features can outperform complex combinations**  
✔️ **Financial intuition is critical for interpretation**  

> ✨ *This project focuses on transforming raw market data into meaningful signals for prediction.*

---

## 📋 Summary Table

| Phase | Key Action | Outcome |
|-------|-----------|---------|
| **Validation** | Check data quality & constraints | No significant issues |
| **Engineering** | Create momentum/trend indicators | 5 base + 4 interaction features |
| **Scaling** | StandardScaler normalization | Features on comparable scale |
| **EDA** | Correlation & behavior analysis | MACD dominates (r=0.87) |
| **Interpretation** | Feature interaction testing | Simpler is better |

---

**Last Updated:** 2025  
**Status:** ✅ Complete & Production Ready