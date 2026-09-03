# 8. Event-Driven Architecture Diagrams

**Priority: ⭐⭐⭐**

[](https://images.openai.com/static-rsc-4/fmkXkdFXGy4shYslQKbxwXOv2cq7QD_Bn2dRIQDRN0WpfUCzmU9Vxxc-9eldNKItXDrEfuDdG7HQqMwny3uGaHifBrsjYWJm9vQ7wt-S6waSSxiM3X4Mrribu2rO4CGZVn2S6o-ZYhbaqQu34EPK86WvOKR72VOD8ent1JaF6NoOtSjTta_kEWVSyQv-yvPv?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/--1sMyXfxlm1rW__zApei14u3_WgGbaa-prJh3rqXIvU66ycsaMDMWx9NFUkOQX1X3ccZAWvgHE8J4f50joihPnkrdxSz1kDjiFfdMYoLjifeKSHtsiCbAVXEHM1QnwSSy9idWl7qh--A-wIF1smIrTj33IjRWIXj1DpRw4bB2Us1tWsOPw5izEvhClSIjzM?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/YAh406FwCuDzj3wwBRqvfIheXNNh_QNhNECIkqQ3SkeVYYWGMn_sVINsjVFgkAVF_fSWy6RqUh1-cE5ec4vQzA1JPf_oj4mAXa253bLXKLtx9eGjZGUEhtHoeSdn59w--TdYITEtBtBwHydOgtCAubopOVx3JSM-GtTFBZAbNYoqZSTOW3VdVBX07kUnJD-R?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/jN97d525m-haHfeZlFbRwHzqrPKpr1YRa_bqPLN1Z58IH8asjDHMsU6zG6w0yJwQLLpeU0BaC0aCGcbPIcQdw7JL6gCaCUnLE1YbyrdHi2u4FmpHcqkTgnmglgGZaTpDB6kM0MyrJaGXMyyEbd7X0TSJWxRPFvaKMjSS34TiiGdjd-gE-szB8EiO6W6aSnWL?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/I1j2EjS-fzDRoPE-ji9iXuUQQ8RF-H6zzS-6-W0aJr7M--amQtysxr1_lf559CLI83bWKqo_5JMC8oN4Fpyu3_sIQU9D4zeUeK72lUpv18hEHFA3TS9SAYSHOxr7kbs53hlZF9Xr3vk0RDaQApD86XA4OMq3MxGMg88y4YmLugrSbzSEc8L6P1nwXo6lMkqH?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/xaYSr0KacC3gRd3r91fffzzQJ5y6lOmQSv1RvsPTGCYUgZuSvUXLxV_rwmpVyI35lDqEhB6uMS_8VtrfABfQ-1WV8x9H2FCup6_YLIjczUCI2VCXAU3s_eKhkx_MXqzk_ezjnRZBUMDTEu2aHp_pZvgTU1yNdXDvBgZSUGk3lLR8fNPAwE2-5HYGuwqwxQ5v?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/zK8nlz0q6AKgxv3bKsjLz4F_wVMAnfKtJ5S8J4a4N8VL-6lqQ9y_73O_t07q_Olax-bWFVLachEv1Y_dBFE7qNLPN3L1W9AyfkNac643zCwaV9ghyOoHvOD9V3hGDqGhVAvTkzzNQGJn_7Olyx5ybsw6UJvau9Pf1e5UPh6nQI1lPnG5UPPLKc3z_kK9HRVq?purpose=fullsize)

Important for modern distributed systems:

- **Event Flow Diagram**
- **Event Storming**
- **Event Topology Diagram**
- **Message Flow Diagram**
- **Kafka Topic Architecture**
- **CQRS Diagram**
- **Event Sourcing Diagram**
- **Saga Diagram**
- **Outbox Pattern Diagram**
- **Pub/Sub Diagram**

Example:

```
Order Service
      |
      | OrderCreated
      v
    Kafka
   /     \
  v       v
Payment  Inventory
Service   Service
  |         |
  v         v
Payment   Stock
```