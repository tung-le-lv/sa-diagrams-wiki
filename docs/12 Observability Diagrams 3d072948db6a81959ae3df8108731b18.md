# 12. Observability Diagrams

**Priority: ⭐⭐**

Very useful for production architecture.

- **Observability Architecture**
- **Logging Architecture**
- **Metrics Architecture**
- **Tracing Architecture**
- **Monitoring Architecture**
- **Alerting Architecture**

Example:

```
Microservices
   |
   +---- Logs ----> OpenSearch
   |
   +---- Metrics -> Prometheus
   |
   +---- Traces --> OpenTelemetry
                         |
                         v
                    Observability
```