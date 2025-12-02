---
theme: default
title: "From Behavioral Programming Research to Provengo"
---

# From Research to Startup  
## The Provengo Story  

### Achiya Elyasaf & Gera Weiss  
Faculty of Computer and Information Science   
Ben-Gurion University of the Negev 

---

# Why We Founded Provengo

<div class="grid grid-cols-[60%_40%] gap-4">
<div>

- We wanted to prove that our research ideas are practical

  - We beleived that we have programming methaphore can change the world 😎

- We identified a domain where our research ideas seems most advantageous 
  - Based on a MEMIMAD project we ran with IAI

  - We found that our research ideas can be applied to testing

  - We planned to first take testing then take Berlin


- We contemplated other options 

  - With students in the management department 



</div>
<div class="flex flex-col items-center justify-center h-full gap-4">

  <img src="/search_for_industrial_use_comic.png" class="max-h-50 w-auto rounded-lg shadow-lg border border-gray-200" alt="Search for Industrial Use" />
  <img src="/research_to_startup_comic.png" class="max-h-50 w-auto rounded-lg shadow-lg border border-gray-200" alt="Research to Startup" />

</div>
</div>

---

# Timeline Overview

- **2010** — Behavioral Programming introduced  

- **2010–2020** — Research expansion  
- **2017–2020** — BPjs implementation & public open source release
- **2021** — Registered a patent on BPjs for testing
- **2022** — Provengo founded via Oasis accelerator  
- **2022–present** — Customer successes + platform development
- **2022–present** — Research expansion in collaboration with Provengo




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

# BPjs — open-source JavaScript engine for BP  

- "Industrial" grade 

- Execution:

```
bpjs run test.js

```

- Verification

```
bpjs verify test.js
```

- Integration with the external world


- A Plug-N-Play architecture


- URL: https://github.com/bthink-bgu/bpjs

---

# Horse vs. Car



---

# Satelite project 

- IAI liked it but didn't use it

- We registered a patent on BPjs for testing

- We understood that testing is a possible penetration point



---

# Why BP Fits Testing


- Tests are stories  
- Many bugs appear only in interleavings  
- BP naturally generates interleavings  
- Combines human scenario insight with automation

---



# Founding Provengo (2021)

- OASIS accelerator helped shape an initial business plan  
- Founders: Achiya Elyasaf, Gera Weiss, Michael Bar-Sinai, Dror Elad  

<img src="/provengo_team.png" class="h-80 w-auto rounded-lg shadow-lg border border-gray-200 mt-4" alt="Provengo Team" />



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
