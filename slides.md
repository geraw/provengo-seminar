---
theme: default
title: "From Behavioral Programming Research to Provengo"
---

# From Research to Startup  
## The Provengo Story  
### Achiya Elyasaf & Gera Weiss  
Faculty of Computer Science & Information Science  
Ben-Gurion University of the Negev

---

# Motivation  
### Why We Founded Provengo

<div class="grid grid-cols-[60%_40%] gap-4">
<div>

- We wanted to prove that our research ideas are practical

- We identified a domain where BP seems most advantageous based on a MEMIMAD project we ran with IAI

- We contemplated other options using a project we ran with students in the management department (Israel <-> Canada collaboration)

- We identified a need and a market:

  - Testing complex software is hard
  - Concurrency, interleavings, and business logic lead to subtle bugs
  - Traditional test design misses rare behaviors
  - Behavioral Programming (BP) offers a powerful alternative
  - We believed BP could revolutionize test design

</div>
<div class="flex items-center justify-center">

![Research to Startup](/research_to_startup_comic.png)

</div>
</div>

---

# Timeline Overview

- **2010** — Behavioral Programming introduced  
- **2010–2020** — Research expansion  
- **2017–2020** — BPjs implementation  
- **2021** — Provengo founded via Oasis accelerator  
- **2022–present** — Customer successes + platform development

---

# Behavioral Programming — Core Idea

- System modeled as **behavior threads (b-threads)**  
- Threads coordinate by requesting, waiting for, blocking events  
- Independent scenarios jointly determine allowed events

---

# BP Example

```javascript
bthread("inventoryCheck", function() {
  while(true) {
    request("AddToCart");
    waitFor("InventoryConfirmed");
    block("CheckoutUntilConfirmed");
  }
});
```

---

# Why BP Fits Testing

- Tests are stories  
- Many bugs appear only in interleavings  
- BP naturally generates interleavings  
- Combines human scenario insight with automation

---

# BPjs — The Foundation of Provengo

- Open-source JavaScript engine for BP  
- Execution, exploration, verification  
- Integration with REST + Selenium  
- Provengo builds a test-design platform on top of BPjs

---

# Founding Provengo (2021)

- Oasis accelerator helped shape business plan  
- Founders: Achiya Elyasaf, Gera Weiss, Fr. Michael Bar-Sinai  
- CEO: Dror Elad

---

# BGN Agreement

- Allowed continuation of academic research  
- BPjs remains open source  
- University–industry collaboration strengthened both sides

---

# Provengo Platform Today

- Story-based testing language  
- Multi-session Selenium + REST orchestration  
- Automatic generation of meaningful tests  
- CI/CD integrations  
- Cloud test runner

---

# Success Stories

- Customers with complex concurrency patterns  
- Found bugs undetectable with standard testing  
- Improved coverage + reduced manual efforts

---

# Financial Reality

- Challenging deep-tech fundraising environment  
- Lean engineering  
- Focus on customer pilots and demonstrating value

---

# Future Vision

- Powerful UI for scenario creation  
- AI-assisted authoring (LLMs → BP models)  
- High-throughput event exploration  
- Stronger model-checking integration  
- Domain-specific test libraries  
- Fully managed SaaS

---

# Research ↔ Industry Reflections

- Industry exposes new research questions  
- Research provides principled foundations  
- Collaboration strengthens both sides

---

# Thank You
