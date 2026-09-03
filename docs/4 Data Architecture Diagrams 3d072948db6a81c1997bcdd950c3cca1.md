# 4. Data Architecture Diagrams

**Priority: ⭐⭐⭐**

[](https://images.openai.com/static-rsc-4/9sf01ahVoFjsAeiuXy0rh6jSrSL6ZeghVcJVWgbbzuh1PjBNiK2fz4RGy-pG831dk_yrSi62yaY4cMFr1aBlRXHqIDB_bpnKUJ1BMF_PAbJocRc4BoqeV-8zGVGc50UD19Ze15tsb737XSLTkZoYUzfFDl-rLmvQsZ8EI0ez4t67BinvsUp-ZnpJqECATip0?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/YEW-iH06EOae7lw4pQc8TseQm6uMBI-HEmj9X8Bz6qxkCIqWHpacYSxwRQcVgxDK9DOvhFAzm78ose0eq-s2N1zUI9ihMHpnk3vMGP2SzMyBdiMYk4dLIUImL_XqGSjmXZKsTn1S0viijwEvY6U6UvtlomY6rInCQPiasYR7xvkSqBqd4MppipvR9I_R0sD-?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/qOOkHh9vMUGAxWVW9KDarRcadIPZeLblY7wh9lhKSXH91QJy6yMp1XqC9ENsybtPo2cYLDIq01m5Yzz5dK2JWGHeuadSv2Ch9HC3LcKZtN13ZU-hjoAM_ebX4MCkYWAJnEnNyRh82XJ27MfnO-dlpyiLr6cBQBmZsYq2JBkGaDOmN1sJJQDWVai9W4OUB9gJ?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/G-WDy2HT9ogCsCT0hQe0DZWfsSrgEZ_pt18atJjLV0rrH9rCQ89TLQDWD7I6hi7jpgEVBbVB6Z5n1LgRbyBN8G0iAfQFKQydEms3godmMaxFAuhD7-7g0AVrYbkjLqWtsF4OFb-RNKN13xTOmE5t_rYGrLvNHtZgMpnjOaWILfESibW8MBIK7VqIEBG_NDF4?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/LMRuPMIUM9Kor84kl2oAzJDpHwZwqACW11LASDrfQwgV8Typp8Ga-DVKyaqnqdQjxGKAQN04XPsKbJvT8NGkEXI0dGEylUl_CJuBO_sMdKfaFEtLh51AbiOC4y6x5_7vrXpwtuL7Cq0lLOhZ7Rb92AZ4AC9HY6-xk2HoLKjmyTpc09dXH9WtHpsLxQ-SbQzU?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/j5xmWJqh33Q3NELvaGsyOMUthiprcXEunCkgT8bhqXb5nq_L0durR_XjqQYVa4ATcndtHkZ7OnSLcimm7EHPMTMmKonpyYhH3mSL3hkg_EU0F3F3OODBAyUtO3yRo3vzcfg9V5x-Sf8Jx-Ojv8unKnnUOYb5sackINL7GUBMm21yB3AsBBy7zrrWB1nE5Xrc?purpose=fullsize)

An architect should understand:

### ERD — Entity Relationship Diagram

Shows:

```
Customer
   |
   | 1:N
   v
Order
   |
   | 1:N
   v
OrderItem
```

### Other important data diagrams

- **Logical Data Model**
- **Physical Data Model**
- **Conceptual Data Model**
- **ER Diagram**
- **Data Flow Diagram (DFD)**
- **Data Lineage Diagram**
- **Data Pipeline Diagram**
- **ETL/ELT Architecture Diagram**
- **Data Warehouse Architecture**
- **Data Lake Architecture**
- **Data Mesh Architecture**
- **Event/Data Streaming Architecture**

For a modern architect, **data lineage** becomes particularly important:

```
Source DB
   ↓
CDC
   ↓
Kafka
   ↓
Data Processing
   ↓
Data Warehouse
   ↓
BI / Reports
```