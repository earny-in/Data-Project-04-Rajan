# Unsupervised Learning

## Introduction

Unsupervised Learning is a type of Machine Learning where the model learns from **unlabeled data**. Unlike Supervised Learning, the dataset does not contain the correct output or labels.

The main goal of Unsupervised Learning is to find hidden patterns, relationships, or groups in the data.

---

## What is Unsupervised Learning?

Unsupervised Learning is a Machine Learning technique in which the model is trained using **unlabeled data**. The model explores the data on its own and identifies similarities, differences, or patterns without any guidance.

In simple words, the model learns from data without knowing the correct answers.

---

## What is Unlabeled Data?

Unlabeled data means the dataset contains only input data and no output labels.

### Example

| Customer ID | Age | Annual Income |
|-------------|-----|---------------|
| 101         | 22  | ₹30,000       |
| 102         | 45  | ₹80,000       |
| 103         | 25  | ₹35,000       |
| 104         | 50  | ₹90,000       |

Here, there is **no label** such as "High Value Customer" or "Low Value Customer". The model has to find groups by itself.

---

## How Unsupervised Learning Works

```
Unlabeled Data
       │
       ▼
Choose an Algorithm
       │
       ▼
Find Patterns or Groups
       │
       ▼
Generate Insights
```

### Steps

1. Collect unlabeled data.
2. Choose an Unsupervised Learning algorithm.
3. The model finds hidden patterns or similarities.
4. Similar data points are grouped together.
5. The results are used for analysis or decision-making.

---

## Types of Unsupervised Learning

### 1. Clustering

Clustering groups similar data points together.

**Examples**

- Customer Segmentation
- Product Recommendation
- News Grouping
- Image Segmentation

---

### 2. Association

Association finds relationships between different items.

**Examples**

- Market Basket Analysis
- Frequently Bought Together Products
- Recommendation Systems

---

## Difference Between Clustering and Association

| Clustering | Association |
|------------|-------------|
| Groups similar data | Finds relationships between items |
| Creates clusters | Creates rules |
| Example: Customer Segmentation | Example: Bread → Butter |

---

## Common Unsupervised Learning Algorithms

Some commonly used algorithms are:

- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Apriori Algorithm
- Principal Component Analysis (PCA)

---

## Real-Life Applications

- Customer Segmentation
- Product Recommendation
- Fraud Detection
- Market Basket Analysis
- Social Network Analysis
- Image Compression

---

## Advantages

- No labeled data required
- Finds hidden patterns
- Useful for data exploration
- Can work with large datasets

---

## Limitations

- Results are harder to evaluate
- Accuracy is difficult to measure
- May create incorrect groups
- Requires careful interpretation

---

## Example

Suppose an online shopping company has customer data but no labels.

The algorithm analyzes customer behavior and automatically creates groups like:

```
Cluster 1 → Students

Cluster 2 → Working Professionals

Cluster 3 → Senior Citizens
```

These groups can later be used for marketing and recommendations.

---

## My Understanding

After learning Unsupervised Learning, I understood that the model does not know the correct answers beforehand. Instead, it explores the data, finds hidden patterns, and groups similar data together. This makes it useful when labeled data is not available.

---

## Key Points

- Uses unlabeled data.
- Finds hidden patterns.
- No correct output is provided during training.
- Mainly used for Clustering and Association.
- Useful for data analysis and customer segmentation.

---

## Conclusion

Unsupervised Learning is a Machine Learning technique that works with unlabeled data. It helps discover hidden patterns, relationships, and groups without any predefined labels. It is widely used in recommendation systems, customer segmentation, and data analysis.