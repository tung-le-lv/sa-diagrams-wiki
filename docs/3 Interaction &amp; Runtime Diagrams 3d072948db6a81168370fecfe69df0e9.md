# 3. Interaction &amp; Runtime Diagrams

**Priority: ⭐⭐⭐**

[](https://images.openai.com/static-rsc-4/fAY8n2xAiVUmz6xlMNrvbVSSUbQaPs2G3Sb4W4HKdd1X86pdFTMmVKCelYZnMKKQol4WZwKAYxcukO2yplbNfcXURACSRxpfIo6477sJnHmj95kpUb1uInRhQAy7B5RrZFxULR546e2jlCUcK58MCwqrw9VQCZ2HUaqFzQbhfbarr3NVXJN0apAlKr1WQ3oz?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/3luFtWXXydNLcRQRYBwAcV1pEcn008_JgUmHcZ76polfm3N8GKbr-BsFFTM6lzywqJxNUXxjL4nnY0PkpLjpRXIGX5oZzdXAgre2nXU5LAZ4PUjLKJtX5vuNHLdIDCve6ZTbyQFxR1Y0P0rhE-SfSqaqiL_XUR-wNPqMpvapdZnZFm2QmzPvcUgYHrDQro-v?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/jN97d525m-haHfeZlFbRwHzqrPKpr1YRa_bqPLN1Z58IH8asjDHMsU6zG6w0yJwQLLpeU0BaC0aCGcbPIcQdw7JL6gCaCUnLE1YbyrdHi2u4FmpHcqkTgnmglgGZaTpDB6kM0MyrJaGXMyyEbd7X0TSJWxRPFvaKMjSS34TiiGdjd-gE-szB8EiO6W6aSnWL?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/9UlZDuUfLf-NtY3L5Ch1alugQj91Sd3cEOb8dBTtz16JzBdItGGgJZxl_FD93eHikTC5IGCrw-sypd0arcpJnsfPk9CyF5YaLhcOKCpIFyZIwVEyTJwxt0ByUR3KJDWCZlmhogzMdTpu_XClCpg3UeF9F5SvZbCP6hOxZoehUQpBKSfkEPsN1zqJ4G4qbE8n?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/EB-PYbw0kXpIUAI22jgfL1Gbr5A2rnObf4mMneaqtX29vc6Ze-fOk0KgtYoH_hBzI2MV5XotbhOsUTq2RcUU20kw169Y9ib1c2nySQob2rD7StbzwqPTPfSxXB826KTY7UyOBIOpcoOXkyNcrCLbPUPGzt-e9qGbYczHHNzS9gdya9NUAmEeY7-lMcfIw6GQ?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/bJ0BqBzh4_vXcVGxKD-6ZxGLgm4xNcQW4LOb1V0rPTyFQpb8F-DYokZGuFRaTQRASnbtzll2ypCWwmJ30t4Yv9UJfwcm_9P6mJNRsHvlALbTvTBq-I7ZfEGRMfVYgBcD-Keie82LOGg3SWjr8FAMzzsYb6Pd5H2AJGjAc45DI1bXv1aGiIWCGb7cnK7kf_eq?purpose=fullsize)

These are extremely important for distributed systems.

### Sequence Diagram

Shows:

```
Client
   |
   v
API
   |
   v
Order Service
   |
   v
Payment Service
   |
   v
Kafka
   |
   v
Notification Service
```

Useful for understanding:

- synchronous calls
- asynchronous calls
- API interactions
- events
- retries
- timeouts
- failure paths
- distributed transactions

### Other useful runtime diagrams

- **Interaction Diagram**
- **Event Flow Diagram**
- **Message Flow Diagram**
- **Request Flow Diagram**
- **Data Flow Diagram**
- **Process Flow Diagram**
- **Swimlane Diagram**