# 6. Security Architecture Diagrams

**Priority: ⭐⭐⭐**

[](https://images.openai.com/static-rsc-4/p6hAeCYzeV2ECkxrH1iW1mG7kfZXjRY-Flr_O7IYmN1KcYtPdVbnktcU7ZkKKmA3BQYqhcqeJuA2xKbFQRcSrXoitmXR3qsu8B1NX50Kkm8NUfHdMNJNFmmV8Xl8xIgfhyKNwU1ptSOipMjdClYJQ_Jk625AmNS__z118ij5C7x7lTTkPUHLXoO1Ug9jU6LL?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/oFVS4muwfHSU_v_J_OZe-8d0RWwoUix2h0IniQELuMjLcFkuhQoDSGZWdazP6h9m00DS1bxOtTmBOLcdC_GXr4hTjSUqPyUghDxSfq4LWJQKBCp8risp7pFSCj696tPk6E6qYV1C6t5bGFSd4-JZkfeoThVAYNNxAfK6yUXyRnVcmFNZZeJt-5B1ZhT-pfyQ?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/nsVMHZMWGT99M3bIj4SDh-mSGOXw2fdttAgdT-FLwFKwtiWXSAjJ6xTEo3ar3GFUMWNxCUBsaEul4bTaNmOuKfrMQKU1ISvh1pm3JEhHIMat9_Yy0rgVumg42HkAk9h83TczT9UwjE2NhQPZfAK2v571SZjWalOUIKRy3R89CAz9XSYfro5SxPx0pzEo9uWg?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/hKOnP37T1LG-MysIGdA6zI2ICH8600H08Rlq9xz-3GzIS0RsOgIPNpR-sOMCHJ0W4uonFu49AaXlGdnWhMm0b1Z3WkOtBMYUZ8NsQl3WSmy7JEMH2AIOdlZo-K2w3JEofDBynO9LRp__aeqhB6AePdAdaCGMi96BPFXzh3ic9u4H31GGTrwF43EPZjL0zKxC?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/Wd1sx3XcUd_QL45UoY2vztfu4_B_8j-U-Ktsn6ZV7I8aBfxau9qsUJ_ihU4JQjB_AfN-t3_XShFGlCvCfpCrzS_tZRFFwBvfBA1Lsqpq15pXjPMTp_Ixk6RZEeTs8QthaMGi1R3BnJgi9k0tK-PrpeJvLHTxlc6NJPiPyeugWbVML5Rw-2MKNyguZq1bS5gx?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/A4C4kPmJELsnyVaLKmWh0BOpuIVXm9ab4jVh0v75mwCZMKOZHDHVUKGgZcla98sIDvhRbxcpQo9ZvpVYKJeqNSB0NU9la-tG3_FXEQy4gQC7Jarn1wcYNwMrIgm92bk6yWmdkRe9a8jnXdrWdDIX8jVzWGxuILdGVQEZeACFqozrSLLVHidFVAn_pNNpK5Jf?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/4WScTGJSmDfonrqXybOXNYqY19wdlBLtd-JNi51YMDidSdVHMa4HHT6aawTXZUct_TK3YKjsoVyiAkNWmB0LwPgROWBHzRRg6o7F7wDhsh6eigA5jsBM_mXRLT9UmO19wNU-9goWN7SV7f41GwYKeFknlhlfLzeQcm1I5AUwrtpkdVorBsASUMXxCuSDv3NC?purpose=fullsize)

[](https://images.openai.com/static-rsc-4/M0fFqfXgx5WkCiL5W51mLgDfUj1ue-rjZGH-W6qHqEb38q_j7HP5mJ86JKiGzbwe4H_s2r0dfY_jGWQmOBQAuUjhNiPaSim2vNiuXu2KJU5ak0syEeNj--9o6KGWc7oJYxbETBwMJXwffrSIJuUs1RlTVv3wi94TGZZ1qrBCyLQ1mzBh3lrzERjD9lbW8mvU?purpose=fullsize)

An architect should know:

- **Security Architecture Diagram**
- **Trust Boundary Diagram**
- **Threat Model Diagram**
- **Data Classification Diagram**
- **Authentication Flow Diagram**
- **Authorization Flow Diagram**
- **OAuth 2.0 Flow**
- **OIDC Flow**
- **Zero Trust Architecture**
- **Network Security Diagram**
- **Identity Architecture**
- **Encryption / Key Management Diagram**

For example:

```
User
 ↓
Identity Provider
 ↓
OAuth/OIDC
 ↓
API Gateway
 ↓
Authorization
 ↓
Microservice
```