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

<img src="/timeline_comic.png" class="absolute bottom-10 right-10 w-70" alt="Timeline Comic" />





---

# Behavioral Programming (BP)

<div class="grid grid-cols-[30%_5%_30%_5%_30%] gap-2 items-center justify-center mt-10">
  <div class="flex flex-col items-center">
    <h3 class="mb-4">Requirements</h3>
    <img src="/bp_requirements_lego.png" class="h-40 w-auto object-contain" />
  </div>
  
  <div class="flex justify-center">
    <span class="text-6xl font-bold text-gray-500">+</span>
  </div>

  <div class="flex flex-col items-center">
    <h3 class="mb-4">Execution engine</h3>
    <img src="/bp_engine_lego.png" class="h-40 w-auto object-contain" />
  </div>

  <div class="flex justify-center">
    <span class="text-6xl font-bold text-gray-500">=</span>
  </div>

  <div class="flex flex-col items-center">
    <h3 class="mb-4">Behavior</h3>
    <img src="/bp_behavior_lego.png" class="h-40 w-auto object-contain" />
  </div>
</div>

<div class="absolute bottom-20 left-10 text-sm text-gray-500">
  <p>1. David Harel, Assaf Marron, Gera Weiss. "Behavioral programming." Communications of the ACM 55.7 (2012): 90-100.</p>
  <p>2. Achiya Elyasaf. "Context-Oriented Behavioral Programming." Information and Software Technology 133 (2021): 106504.</p> 
</div>

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

# The future of programming

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="flex flex-col items-center text-center">
    <h3 class="mb-4 text-xl font-bold">Traditional Programming</h3>
    <img src="/traditional_programming_car.png" class="h-60 w-auto rounded-lg shadow-lg mb-4" />
    <p class="text-sm">Like driving a car: The driver must control every detail <br> (steering, gas, brakes) at all times.</p>
  </div>

  <div class="flex flex-col items-center text-center">
    <h3 class="mb-4 text-xl font-bold">Future Programming</h3>
    <img src="/future_programming_horse.png" class="h-60 w-auto rounded-lg shadow-lg mb-4" />
    <p class="text-sm">Like driving a carriage: The driver specifies the general direction, and the horse handles the details (obstacles, footing).</p>
  </div>
</div>

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
