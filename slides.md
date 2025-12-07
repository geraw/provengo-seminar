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

<img src="/timeline_comic_david.png" class="absolute bottom-10 right-10 w-70" alt="Timeline Comic" />





---

# Behavioral Programming (BP)

<div class="grid grid-cols-[30%_5%_30%_5%_30%] gap-2 items-start justify-center mt-10">
  <div class="flex flex-col items-center text-center">
    <h3 class="mb-4">Requirements</h3>
    <img src="/bp_requirements_lego.png" class="h-40 w-auto object-contain" />
    <p class="text-xs mt-2">Scenarios specifying what may, must, <br> and must-not happen over time</p>
  </div>
  
  <div class="flex justify-center mt-20">
    <span class="text-6xl font-bold text-gray-500">+</span>
  </div>

  <div class="flex flex-col items-center text-center">
    <h3 class="mb-4">Execution engine</h3>
    <img src="/bp_engine_lego.png" class="h-40 w-auto object-contain" />
    <p class="text-xs mt-2">A universal execution machine</p>
  </div>

  <div class="flex justify-center mt-20">
    <span class="text-6xl font-bold text-gray-500">=</span>
  </div>

  <div class="flex flex-col items-center text-center">
    <h3 class="mb-4">Behavior</h3>
    <img src="/bp_behavior_lego.png" class="h-40 w-auto object-contain" />
    <p class="text-xs mt-2">A reactive system</p>
  </div>
</div>

<div class="absolute bottom-10 left-10 text-sm text-gray-500">
  <p>1. David Harel, Assaf Marron, Gera Weiss. "Behavioral programming." Communications of the ACM 55.7 (2012): 90-100.</p>
  <p>2. Achiya Elyasaf. "Context-Oriented Behavioral Programming." Information and Software Technology 133 (2021): 106504.</p> 
</div>

---

# BP Example

<div class="grid grid-cols-2 gap-4">
<div>

```javascript {all|2,7,13,20|3,7,14,20|3,8,13,21|8,14,20|13,21}
bthread("Hot", function() {
  request("HOT")
  request("HOT")
})

bthread("Cold", function() {
  request("COLD")
  request("COLD")
})

bthread("No two HOT in a row", function() {
  while(true) {
    waitFor("HOT")
    sync({waitFor:"COLD", block:"HOT"})
  }
})

bthread("No two COLD in a row", function() {
  while(true) {
    waitFor("COLD")
    sync({waitFor:"HOT", block:"COLD"})
  }
})

```

</div>

<div>

### Execution Trace

<div class="bg-gray-100 p-4 rounded  font-mono text-sm">
  <div v-click="1">1. HOT</div>
  <div v-click="2">2. COLD</div>
  <div v-click="3">3. HOT</div>
  <div v-click="4">4. COLD</div>
</div>

<br>
<br>

<div class="mt-4 relative flex items-end">
  <div class="text-3xl mr-[-20px] z-10 transform translate-y-2">👩‍🏫</div>
  <div class="bg-[#2d3e30] p-4 rounded-lg border-4 border-[#8b5a2b] shadow-xl transform -rotate-1 flex-1">
    <h4 class="text-white/90 text-center mb-2 font-hand text-lg border-b border-white/20 pb-1">Execution Rules</h4>
    <ul class="list-disc list-inside text-white/90 font-hand text-sm space-y-2">
      <li>Event triggered if requested & not blocked</li>
      <li>B-thread advances if it requests or waits for the event</li>
    </ul>
  </div>
</div>

</div>
</div>
---

# BPjs: an open-source implementation of BP

<div class="grid grid-cols-[60%_40%] gap-4">
<div>

- **Embedded Formal Model**
  - Uses **Rhino** to run JavaScript within a Java application
  - The JavaScript code is a formal behavioral model

- **Verification Tools**
  - Built-in support for **Safety** and **Liveness** verification

- **Rich Ecosystem**
  - Open architecture that allows easy extension
  - For example, **COBP** adds context to BP models

- **Open Source**
  - <carbon-logo-github class="inline-block mr-1" /> [github.com/bthink-bgu/bpjs](https://github.com/bthink-bgu/bpjs)

</div>

<div class="relative flex flex-col items-center justify-center h-full">
  <img src="/bpjs_architecture_lego_v2.png" class="w-full rounded-lg shadow-lg border border-gray-200" alt="BPjs Architecture" />

<div class="absolute right-2 bottom-2 flex items-center gap-3 bg-white/90 p-2 rounded-lg shadow-sm border border-gray-100">
  <img src="/michael_bar_sinai_nobg.png" class="w-12 h-12 rounded-full border border-gray-200 object-cover" />
  <div class="text-xs text-left leading-tight">
    <div class="font-bold">Michael Bar-Sinai</div>
    <div class="text-gray-500">Lead Developer</div>
  </div>
</div>





</div>
</div>

---

# Our view of the future of programming

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

<div class="grid grid-cols-2 gap-4 h-full">
<div class="text-sm leading-tight">

- **Scenario-Based On-Board Software**
  - Modular design using "scenarios" and "anti-scenarios"
  - Direct translation of specifications to code
  - Real-time execution
  <br>
  <br>
- **Formal Verification**
  - Automated model-checking for safety and robustness
  - Automated test scenario generation using **BPjs**
  <br>
  <br>
- **Hybrid Laboratory**
  - Programmed **real space-ready hardware** and **OS**
  <br>
  <br>
- **Outcome**
  - IAI approved the project, but not ready for adoption
  - Led to patent on BPjs for testing
  - Pivot to testing as a market entry point
</div>

<div class="relative h-full w-full">
  <div class="absolute inset-0 flex items-center justify-center">
    <Youtube id="spmH5sjIwN8" width="100%" height="300" />
  </div>

  <img src="/iai_logo_new.png" class="absolute -top-10 right-10 h-16 object-contain" alt="IAI Logo" />
  
  <div class="absolute bottom-8 right-0 flex items-center gap-3 bg-white/90 p-2 rounded-lg shadow-sm border border-gray-100">
    <img src="/aviran_sadon_nobg.png" class="w-12 h-12 rounded-full border border-gray-200 object-cover" />
    <div class="text-xs text-left leading-tight">
      <div class="font-bold">Aviran Sadon</div>
      <div class="text-gray-500">Lead Developer</div>
    </div>
  </div>
</div>
</div>



---

# Why BP Fits Testing


<div class="grid grid-cols-[60%_40%] gap-4">
<div>

- **Tests are Stories**  
  BP scenarios directly map to requirements and user stories

- **Taming Complexity**  
  Naturally handles complex interleavings and race conditions where bugs hide
  
- **Shift Left**  
  Catches design flaws early by executing the specification itself

- **Separation of Concerns**  
  Decouples test logic ("what to test") from technical implementation ("how to drive the UI")

- **Smart Automation**  
  Combines human insight with automated exploration to generate meaningful test coverage

</div>
<div class="flex items-center justify-center">
  <img src="/provengo_workflow_comic.png" class="max-h-80 w-auto rounded-lg shadow-lg border border-gray-200" alt="Provengo Workflow" />
</div>
</div>

---



# Founding Provengo (2021)

<div class="grid grid-cols-[60%_40%] gap-4">
<div>

<img src="/provengo_logo_transparent.png" class="h-12 w-auto mb-6 object-contain" alt="Provengo Logo" />

- **We believed we can revolutionize testing**
  - Unlock the potential of mapping the test space
  - Generate tests automatically from lightweight models

- **Focus on specification**
  - Testers focus on *what* to test (requirements)
  - Algorithms build the test suites

- **Requirement-centric analysis**
  - Test results analyzed relative to requirements
  - Coverage guaranteed against requirements, not just code

</div>

<div class="flex flex-col items-center justify-center gap-4">
  <img src="/provengo_mbt_diagram.png" class="h-70 w-auto rounded-lg shadow-md border border-gray-200 object-contain" alt="Model-Based Testing Concept" />
  <div class="relative flex flex-col items-center">
    <img src="/provengo_founders_comic.png" class="h-30 w-auto rounded-lg shadow-xl border-0 border-gray-100 object-cover block" alt="Provengo Founders" />
    <p class="absolute -bottom-10 text-[10px] text-center leading-none bg-white/80 px-1 rounded">Supported by OASIS</p>
  </div>
</div>
</div>



---

# BGN Agreement

<div class="grid grid-cols-[50%_50%] gap-4 items-center">
<div class="text-[15px]">

- **Parallel Progress**
  - Scientific research alongside product development
  - Facilitated via a dedicated **Research Project** <br> (similar to IAI collaboration)

- **Symbiotic Exchange**
  - **University → Company**: Scientific knowledge & innovation
  - **Company → University**: products & data for research

- **Strategic Partnership**
  - BGU is a **Shareholder**
  - BPjs core remains open source

</div>

<div class="flex flex-col items-center justify-center">
  <img src="/bgn_provengo_lego_v2.png" class="h-90 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" alt="BGN-Provengo Symbiosis" />
</div>
</div>

---

# Provengo Platform Today

<div class="grid grid-cols-[55%_45%] gap-4 items-center">
<div>

### The Provengo CLI
A layered architecture for model-based testing:

- **Analysis Tools & Engines** (Top)
  - Verification, Sampling, Coverage Analysis
  - Automated test suite creation
- **Libraries \ DSLs**
  - Domain Specific Languages for testing
  - Integrations for Actuators/Sensors (e.g., Selenium)
- **BP Core** (Foundation)
  - Behavioral Programming execution engine
  - State management and event orchestration

</div>

<div class="flex flex-col items-center justify-center">
  <img src="/provengo_cli_architecture_lego.png" class="h-90 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" alt="Provengo CLI Architecture" />
</div>
</div>

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
