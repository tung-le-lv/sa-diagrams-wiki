# 14. Architecture Decision Diagrams

**Priority: ⭐⭐**

These aren't traditional "architecture diagrams," but they're extremely useful.

### Decision Tree

```
Need asynchronous communication?
        |
       Yes
        |
   Need ordering?
      /   \
    Yes    No
    |       |
 Kafka    SQS
```

### Trade-off Matrix

For example:

| Option | Cost | Complexity | Scalability |
| --- | --- | --- | --- |
| Monolith | Low | Low | Medium |
| Modular Monolith | Medium | Medium | High |
| Microservices | High | High | Very High |

Other useful artifacts:

- **Architecture Decision Record (ADR)**
- **Decision Matrix**
- **Trade-off Matrix**
- **Option Comparison Diagram**