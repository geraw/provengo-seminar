---
theme: default
title: "From Behavioral Programming Research to Provengo"
colorSchema: "light"
---

# From Research to Startup  
## The Provengo Story  

<div class="absolute top-10 right-10 flex gap-6">
  <img src="/provengo_logo_transparent.png" class="h-12" />
  <img src="/bgu_logo.png" class="h-12" />
</div>

### Achiya Elyasaf & Gera Weiss  
Faculty of Computer and Information Science   
Ben-Gurion University of the Negev

<!--
<div dir="rtl">
לפני מספר שנים, גרא ואני החלטנו להקים חברת סטארט אפ בתחום של בדיקות תוכנה.
כל הקמה של חברה חדשה היא כמובן מורכבת ומאתגרת, אבל בתהליך שאנחנו עשינו, ועדיין עושים, יש מרכיבים רבים המשלבים אקדמיה ותעשייה באופן שעשוי לעניין את הקהל שיושב פה ולכן חשבנו שזה נושא טוב לסמינר.
</div>
21 seconds
-->

---

# Why We Founded Provengo?

<div class="grid grid-cols-[65%_35%] gap-4">
<div>


- We wanted to prove that our research ideas are practical

  - We believed that our programming metaphor could change the world 😎

- We identified a domain where our research ideas seemed most advantageous
  - Based on a MEMIMAD project we ran with IAI

  - We found that our research ideas could be applied to testing

  - We planned to first take testing then take Berlin


- We contemplated other options 

  - With students in the management department 



</div>
<div class="flex flex-col items-center justify-center h-full gap-4">

  <img src="/search_for_industrial_use_comic.png" class="max-h-50 w-auto rounded-lg shadow-lg border border-gray-200" alt="Search for Industrial Use" />
  <img src="/research_to_startup_comic.png" class="max-h-50 w-auto rounded-lg shadow-lg border border-gray-200" alt="Research to Startup" />

</div>
</div>

<!--
<div dir="rtl">
אז כמו כל סטרט אפ - זה מתחיל ברעיון שישנה את העולם. במקרה שלנו, היתה לנו פרדיגמת תכנות חדשה, שנדבר עליה בהמשך, שהאמנו שהיא יכולה לשנות לטובה את עולם התכנות.

אבל עולם פיתוח התוכנה לא יזנח בבת אחת את object oriented וכדי לחדור צריך אסטרטגיה טובה.

בעקבות פרויקט מוצלח עם התעשיה האווירית, שגם עליו נדבר, חשבנו על עולם הטסטים - כל החברות רוצות בדיקות מערכת יותר טובות ולרוב אין משהו בסיסי איכותי להתחיל איתו. 

פה התחלנו. בדקנו את הרעיון בניסוי עם המחלקה לניהול ויצאנו לדרך. 
</div>
45 seconds
-->

---

# Timeline Overview

- **2010** — Behavioral Programming introduced  

- **2010–2020** — Research expansion  
- **2017–2020** — BPjs implementation & public open source release
- **2021** — COBP development & patent registeration on BPjs for testing
- **2022** — Provengo founded via Oasis accelerator  
- **2022–present** — Customer successes + platform development
- **2022–present** — Research expansion in collaboration with Provengo

<img src="/timeline_comic_david.png" class="absolute bottom-10 right-10 w-70" alt="Timeline Comic" />

<!--
<div dir="rtl">
ב 2010, דוד הראל, גרא וייס ואסף מרון פיתחו את פרדיגמת התכנות - "תכנות התנהגותי" (או בקצרה BP). הפרדיגמה עברה תהליך הבשלה מחקרי במשך עשור. שבסיומו עלה לאוויר כלי קוד פתוח בשם BPjs, שמאפשר לפתח תוכנות התנהגותיות, לחבר אותם לכלים חיצוניים, ולבצע בדיקות פורמליות של התוכנות.

ב 2021 הפרדיגמה עברה הרחבה לתכנות התנהגותי מבוסס הקשרים, מה שאפשר לפרדיגמה להיות יותר פרקטית למערכות גדולות והגשנו פטנט על בדיקות מבוססות BP.

אחרי הפטנט התחלנו תהליך של מסחור ביחד עם BGN ו Oasis והקמנו את פרובנגו.  שיתוף הפעולה הזה ממשיך גם היום גם בפן המחקרי וגם בפן העסקי.
</div>
60 seconds
-->

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

<!--
<div dir="rtl">
כאמור, בבסיס של פרובנגו יושבת פרדיגמת תכנות בשם "תכנות התנהגותי". הרעיון הבסיסי של הפרדימה זה alignment, או תאימות בין הדרישות של המערכת לבין המודולים של הקוד. כל דרישה מתורגמת לתסריט בודד שאומר מה המערכת יכולה לעשות, צריכה לעשות, ואסור לה לעשות. 

את הספסיפיקציה הזו אנחנו יודעים להריץ באופן אוטומטי כך שכל התסריטים תמיד מתקיימים. באופן זה אנחנו מקבלים מערכת ריאקטיבית עובדת.
</div>
40 seconds
-->

---

# BP Example

<div class="grid grid-cols-2 gap-4">
<div>

```javascript {1-9|1-9|all|2,7,13,20|3,7,14,20|3,8,13,21|8,14,20|13,21}
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

<div class="bg-gray-100 p-4 rounded font-mono text-sm grid grid-cols-1">
  <div v-click="1" v-click.hide="2" class="col-start-1 row-start-1">
    HOT, HOT, COLD, COLD<br>
    HOT, COLD, HOT, COLD<br>
    HOT, COLD, COLD, HOT<br>
    ...
  </div>
  <div class="col-start-1 row-start-1">
    <div v-click="3">1. HOT</div>
    <div v-click="4">2. COLD</div>
    <div v-click="5">3. HOT</div>
    <div v-click="6">4. COLD</div>
  </div>
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

<!--
<div dir="rtl">
כדי להבין את הפרדימה, יש פה דוגמת צעצוע, hello world.

בואו נניח מערכת עם שתי דרישות: כשהמערכת עולה צריך לשפוך פעמיים חמים ופעמיים מים קרים. במערכת כזו יש מספר ריצות אקראיות. (קליק)
</div>
150 seconds
-->

---

# BPjs: an open-source implementation of BP

<div class="grid grid-cols-[60%_40%] gap-4">
<div>

- **Embedded Formal Model**
  - Uses Mozilla **Rhino** to run JavaScript within Java
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

<!--
<div dir="rtl">
ב 2021, מיכאל בר-סיני, אז דוקטורנט של גרא, פיתח את BPjs. 

בפלטפורמה זו, המפתח כותב תוכנות BP ב javascript. כדי להריץ, יש פה stack שלם שעוטף את התוכנה ומריץ JS בתוך מנוע rhino של מוזילה שרץ על java. 
 
הסיבה לערימה הזו היא שזה מאפשר לנו לבצע וריפיקציה פורמלית של תכונות בטיחות וחיות של המערכת. זה גם מאפשר לנו חיבור למערכות אחרות, וזה מאפשר גמישות בהרחבות לפרדיגמה. 
</div>
35 seconds
-->

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

<!--
<div dir="rtl">
כשאנחנו נוהגים במכונית, אנחנו צריכים לשלוט בה בכל רגע נתון. כמה גז לתת, מתי ללחוץ על הברקס, הגה, וכו'. הסוס הוא חיה תבונית. הנהג רק צריך לומר לו לזוז קדימה, והסוס יודע איך להמנע ממכשולים ואיך לא ליפול לצדדים.

BP מאפשר את אותו הדבר כמו הסוס. תגדיר רק את הדרישות, מה מותר מה אסור ומה צריך - ואנחנו נדע להריץ את זה באופן נכון, בניגוד למשל ל LLM.

זה החזון שלנו לעולם התכנות.
</div>
30 seconds
-->

---

# Satellite project 

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
  - <span class="text-blue-600">**Pivot to testing as a market entry point**</span>
</div>

<script setup>
import { ref, onMounted } from 'vue'

const satelliteVideo = ref(null)

onMounted(() => {
  if (satelliteVideo.value) {
    satelliteVideo.value.currentTime = 10
    satelliteVideo.value.playbackRate = 2.0
  }
})
</script>

<div class="relative h-full w-full">
  <div class="absolute inset-0 flex items-start justify-center pt-4">
    <video ref="satelliteVideo" controls autoplay muted loop class="w-full h-auto rounded-lg shadow-lg">
      <source src="/On-Board_Satellite_Software_Development_Testing.mp4" type="video/mp4">
    </video>
  </div>

  <img src="/iai_logo_new.png" class="absolute -top-20 right-10 h-16 object-contain" alt="IAI Logo" />
  
  <div class="absolute bottom-15 right-0 flex items-center gap-3 bg-white/90 p-2 rounded-lg shadow-sm border border-gray-100">
    <img src="/aviran_sadon_nobg.png" class="w-12 h-12 rounded-full border border-gray-200 object-cover" />
    <div class="text-xs text-left leading-tight">
      <div class="font-bold">Aviran Sadon</div>
      <div class="text-gray-500">Lead Developer</div>
    </div>
  </div>
</div>
</div>

<!--
<div dir="rtl">
אוקי, אז עד עכשיו, ראינו את הפרדיגמה על דוגמת צעצוע, אבל מה אפשר לעשות עם זה?

ב-2020 התחלנו פרויקט עם התעשייה האווירית, בו פיתחנו לווין אמיתי באמצעות BP. בפינה הימנית עליונה רואים את החומרה האמיתי של הלווין, מתקשרת עם חומרה חיצונית.  

בפרויקט הזה הדגמנו גם התכנות לבניית מערכות שלמות וגם את היכולת לבדוק מערכות כקופסה שחורה באמצעות BP.

זו היתה נקודת המפנה שבה הבנו שעולם הבדיקות יכול להיות כרטיס הכניסה שלנו לתעשייה.
</div>
40 seconds
-->

---

# A patent for using BP for testing satellites (2021)

<div class="grid grid-cols-[70%_30%] gap-4">
<div>

- **Patent**: "Scenario based method for testing software"
- **US Patent No.**: 11,138,100 (Issued Oct 5, 2021)
- **Inventors**: Gera Weiss, Aviran Sadon, Achiya Elyasaf, Michael Bar-Sinai

<br>

<div class="text-12pt">

### The Core Innovation
- **Modeling**:  
  Test logic is defined as independent behavioral threads (b-threads).

- **Interleaving**: <br>
  The BP execution engine naturally interleaves these threads at runtime.
- **Emergence**: <br>
  Complex test scenarios emerge from the interaction of simple rules.
- **Simulation**: <br>
  Includes simulation of environment and subsystems 

</div>

</div>
<div class="flex items-center justify-center">
  <img src="/provengo_workflow_comic.png" class="h-90 w-200 rounded-lg" alt="Provengo Workflow" />
</div>
</div>

<!--
<div dir="rtl">
כשהבנו שיש לנו משהו ביד, כתבנו פטנט שעיקרו:
המשתמש מגדיר תסריטים של דברים שהוא רוצה לבדוק, ואנחנו מייצרים מזה מודל מורכב של מערכת הבדיקות.

מהמודל אנחנו יכולים לייצר תסריטי בדיקה, test suites, וגם לייצר אנליזות ודוחות לגבי המוכנות של המוצר לצאת לשוק.
</div>
20 seconds
-->

---

# Founding Provengo (2022)

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

<!--
<div dir="rtl">
השלב הבא - הקמת חברה. הצטרפנו למחזור הראשון של Oasis של BGN, חברת המסחור של האוניברסיטה, שם הכרנו את דרור אלעד וביחד הקמנו את החברה. 

המוקד של החברה - מיצוי הפוטנציאל של מרחב הבדיקות. יצירת טסטים באופן אוטומטי מתוך מודלים פשוטים. הטסטרים צריכים להתמקד במה לבדוק, בדרישות, ואנחנו ננתח את זה ונבנה באמצעות אלגוריתמים את הבדיקות עצמן.

דרור המנכ"ל, מיכאל (שיצר את BPjs ובינתיים כבר סיים את הדוקטורט) הוא ה chief of technology, וגרא ואני scientific founders, ואני אסביר את ההגדרה הזו מיד.
</div>
45 seconds
-->

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

<!--
<div dir="rtl">
בד"כ כשיש פטנט אקדמי, למשל מישהו רושם פטנט על חומר חדש שהוא מצא. כדי למסחר אותו, צריך למצוא דרך לייצר אותו באופן מסחרי, וזה כבר לא עניינה של אקדמיה. לכן, BGN היתה בטוחה שברגע שרשמנו פטנט - החברה עצמה לא מעניינת אותנו. במקרה שלנו זה לא אפשרי. 

מצד אחד, לא רצינו להיות עובדי חברה, רצינו להמשיך לחקור. מצד שני - ברור שהחברה צריכה גב מחקרי כדי לקדם רעיון שהוא יושב על basic science גולמי.

כך נוצר שיתוף פעולה סימביוטי מאוד מעניין שבו פרובנגו מספקת data ומוצר ואנחנו מספקים את הפתרונות המדעיים לצרכים של החברה. 
</div>
45 seconds
-->

---

# Provengo Platform Today

<div class="grid grid-cols-[55%_45%] gap-4 items-center">
<div>

### The Provengo CLI
A layered architecture for model-based testing:

- **Analysis Tools & Engines** (Top)
  - Verification, Sampling, Coverage Analysis
  - Automated test suite creation
- **Libraries / DSLs**
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

<!--
<div dir="rtl">
טוב, אז עבר קצת זמן, בינתיים יש לנו את ה provengo cli שזה כלי שיושב מעל bpjs, מוסיף לו כל מיני domain-specific languages בשביל טסטים. מעל זה יש ספריות לחבר את המודל לכלי אוטומציה. לבסוף, מעל לכל, יש כלים מתקדמים לאנליזה, לכיסוי הבדיקות, ולווריפיקציה של המודל ושל המערכת.
</div>
20 seconds
-->

---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Living Requirements
## What if your requirements document wasn't a dead artifact?

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Current State</strong>: Traditional specifications, requirements, and test plans are treated as static, 'dead' documents.
- <strong class="text-blue-800">The Problem</strong>: They are authored and reviewed once, but immediately begin to drift from the  implementation.

- <strong class="text-blue-800">The Result</strong>: This synchronization gap breeds hidden complexity, ambiguity in interpretation, and costly bugs discovered late.
- <strong class="text-blue-800">The Solution</strong>: Shift to a <strong class="text-blue-800">Living, Testable Asset</strong>, a model that evolves alongside the code.

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/living_vs_dead.png" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# The Blueprint is Brittle
## Why Traditional BDD is Reaching Its Limits?

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">The Promise</strong>: Behavior-Driven Development (BDD) promised to bridge the gap between business requirements and technical implementation.
- <strong class="text-blue-800">The Reality</strong>: Instead of clarity, we often get a maintenance nightmare.
    - Fragile test suites that break with every UI change.
    - A deep disconnect between Gherkin feature files and the underlying system logic.
    - The "easy to write markup" creates a facade of simplicity but adds significant overhead.

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/brittle_bdd.png" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# The Future is a Living Model
## A Single Source of Truth

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Executable Model</strong>: It’s no longer a static document, but a dynamic, runnable representation of the system.

- <strong class="text-blue-800">Capabilities</strong>: You can query logic, visualize flows, and generate test scenarios from one central source.
- <strong class="text-blue-800">The Bridge</strong>: It connects Business (Analyst), Development, and QA around a shared language.
- <strong class="text-blue-800">The Goal</strong>: Ensure everyone builds, tests, and validates the exact same system behavior.

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/single_source_of_truth.png" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Provengo: Scenario-Driven Model-Based Testing

<div class="text-sm text-gray-500 mb-4">
<strong>Authors:</strong> Michael Bar-Sinai, Achiya Elyasaf, Gera Weiss, Yeshayahu Weiss <br>
<strong>Venue:</strong> IEEE/ACM International Conference on Automated Software Engineering (ASE) 2023
</div>

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Active Requirements</strong>: Transforms static requirements into executable code that validates the system.

- <strong class="text-blue-800">Living Models</strong>: We directly codify user stories, flows, and business constraints into a single coherent model.
- <strong class="text-blue-800">SDMBT Approach</strong>:
    - **Start Simple**: Begin with basic scenarios <br> (Happy Paths).
    
    - **Iterate**: Incrementally layer on complex constraints and edge cases.
    - **Scale**: The model grows with the system, remaining a valid test source.



</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/scenario_driven_mbt.png" class="h-90 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Encode Complex Business Rules
## Transform Ambiguity into Executable Logic

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Combi Library</strong>: A powerful engine to define parameters, constraints, and their inter-dependencies directly within the model.
- <strong class="text-blue-800">Eliminate Misinterpretation</strong>: Replace vague documents with strict code.
- <strong class="text-blue-800">Visualisation</strong>: The model automatically generates the full state space, making gaps in logic visible immediately.

```javascript
// Example: A sports car must have exactly two seats
vehicleType.whenSetTo("sports car")
    .field(seatCount).mustBe(2);

// A truck can't have 6 seats
vehicleType.whenSetTo("truck")
    .field(seatCount).cannotBe(6);
```

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/untangling_rules.png" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# From Abstract Model to Concrete Automation

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Drivers</strong>: The model defines the "what" (business logic) and "why" (requirements). Drivers handle the "how" (execution).

- <strong class="text-blue-800">Rich Ecosystem</strong>: 
    - **UI Automation**: Seamless Selenium/Playwright integration.

    - **API Testing**: Direct REST API calls.
- <strong class="text-blue-800">Code Example</strong>:

```javascript
// @provengo summon selenium
const session = new SeleniumSession("main");
session.start("https://your.app.com");
session.click("//a[contains(text(), 'Sign In')]");
```

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/abstract_to_automation.png" class="h-95 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Robust & Secure Toolchain

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Local Execution</strong>: The engine runs 100% on your local machine or CI server. No dependency on 3rd party servers.

- <strong class="text-blue-800">Zero Data Transfer</strong>: Your sensitive models, test data, and reports never leave your network. No cloud upload.

- <strong class="text-blue-800">Integrations</strong>:
    - **Selenium Manager**: Automatic management and synchronization of web drivers.

    - **IDE Support**: Best-in-class VSCode extension for modeling and debugging.

- <strong class="text-blue-800">Cross-Platform</strong>: Full support for Linux, Mac, and Windows environments.

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/secure_toolchain.png" class="h-100 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Case Study: Insurance Claims Processing

| Challenge | Solution | Impact |
| --- | --- | --- |
| Manual claims processing, complex rules, strict regulations. | **Map & Automate**: Modeled every aspect of the process. | **0-25%** Cost reduction.<br>**Shorter** project timelines. |
|  | **Policy Definition**: Regulatory compliance became straightforward. | **Simplified** compliance. |

<div class="flex items-center justify-center mt-8">
  <img src="/slides_images/insurance_support.png" class="w-full h-60 rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>

 
<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Case Study: Major Bank SSO

| Challenge | Solution | Impact |
| --- | --- | --- |
| Replace SSO system, reduce friction, ensure data safety. | **Complete Model**: Modeling desired SSO capabilities. | **50%** Reduction in STD timeline. |
| Regulatory alignment. | **Integration**: Ensured seamless integration and compliance. | **>30%** Validated pre-implementation. |

<div class="flex items-center justify-center mt-8">
  <img src="/slides_images/bank_sso_success.png" class="w-full h-60 rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>


<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Demo: Testing an Online Store
## Modeling Low-Level Interactions Separate from High-Level Integration

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">The SUT</strong>: An online store (Prestashop).
- <strong class="text-blue-800">The Approach</strong>:
    - **Separation of Concerns**: We modeled the low-level interactions (Login, Add to Cart) separately from the high-level integration model.
    - **Goal**: Verify end-to-end flows.
- <strong class="text-blue-800">The Bugs</strong>:
    - Found critical logic bugs in Prestashop related to inventory management and checkout flows.

</div>
<div class="flex items-center justify-center">
  <img src="/prestashop_screenshot.png" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

# Prestashop Demonstration

<script setup>
import { ref, onMounted } from 'vue'

const videoEl = ref(null)

onMounted(() => {
  if (videoEl.value) {
    videoEl.value.currentTime = 90
    videoEl.value.playbackRate = 3
  }
})
</script>

<div class="grid grid-cols-[60%_40%] gap-2 mt-4 h-full">

<!-- Left Column: Explanations -->
<div class="grid grid-cols-1">
  
  <!-- Phase 1: Low-Level Interactions (Visible initially, Hidden on Click 1) -->
  <div v-click.hide="1" class="col-start-1 row-start-1 space-y-2">
    <div>
      <h3 class="text-xl font-bold text-blue-800">Low-Level Interactions</h3>
      <h4 class="text-lg text-gray-500">Reusable Sub-Models</h4>
    </div>
    
  <div class="flex flex-col gap-0">
    <div class="flex flex-col items-center">
        <strong class="mb-1 text-sm text-blue-800">Login Model</strong>
        <img src="/slides_images/online_store_login.png" class="w-full" />
    </div>
    <div class="flex flex-col items-center">
        <strong class="mb-1 text-sm text-blue-800">Add to Cart Model</strong>
        <img src="/slides_images/online_store_add_to_cart.png" class="w-full shadow-md rounded-lg" />
    </div>
  </div>
  </div>

  <!-- Phase 2: High-Level Integration (Visible on Click 1) -->
  <div v-click="1" class="col-start-1 row-start-1 space-y-4">
    <div>
      <h3 class="text-xl font-bold text-blue-800">High-Level Integration</h3>
      <h4 class="text-lg text-gray-500">Composing End-to-End Tests</h4>
    </div>

  <div class="space-y-2 text-sm">
    <div class="bg-blue-50 p-1 rounded">
      <strong class="text-blue-800 block mb-0">Composition</strong>
      We compose the low-level blocks into high-level scenarios.
    </div>
    <div class="bg-blue-50 p-1 rounded">
      <strong class="text-blue-800 block mb-0">Verification</strong>
      We can verify "Admin takes item out of stock" vs "User tries to buy item". Provengo explores the interleavings.
    </div>
    <img src="/slides_images/online_store_end_to_end.png" class="w-full shadow-md rounded-lg mt-2" />
  </div>
  </div>

</div>

<!-- Right Column: Video -->
<div class="flex items-start justify-center h-full pt-20">
    <video ref="videoEl" controls autoplay muted loop class="w-full h-auto rounded-lg shadow-lg">
      <source src="/Provengo-BPFlow-PrestaShop.mp4" type="video/mp4">
    </video>
</div>

</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# Generating Test Suites
## From Model to Coverage

<div class="grid grid-cols-[50%_50%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Automatic Generation</strong>:
    - We use Provengo to generate a test suite that satisfies specific coverage criteria.
    - We can explicitly request scenarios that hit specific events or states.

</div>
<div class="flex flex-col items-start bg-gray-900 rounded-lg p-4 text-white font-mono text-sm overflow-x-auto w-full">
<div class="text-gray-400 mb-2"># Generate tests covering "Out of Stock" events</div>

```bash
provengo analyze -f html \
  --coverage-goal "event(OutOfStock)" \
  --limit 100
```

<div class="text-gray-400 mt-4 mb-2"># Run the generated suite</div>

```bash
provengo run --test-suite suite-1
```
</div>
</div>


<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

# Generalized Coverage Criteria for <br> Combinatorial Sequence Testing

<div class="text-sm">

<div class="text-gray-500 mb-4">
Achiya Elyasaf, Eitan Farchi, Oded Margalit, Gera Weiss, Yeshayahu Weiss, <br> IEEE Transactions on Software Engineering (2023)
</div>

<img src="/combinatorial_testing_illustration.png" class="absolute top-10 right-10 w-60 rounded-lg shadow-lg border border-gray-200 z-10" />

- <span class="text-red-600 font-bold">The Challenge</span><br>
  - How to effectively verify systems with infinite state spaces and complex sequences? <br> <br>
- <span class="text-blue-600 font-bold">Generalized Coverage</span>
  - Extending combinatorial interaction testing (CIT) to **event sequences**.
  - Allows testers to define *projection functions* that capture domain-specific "interesting" behaviors. <br> <br>
- <span class="text-purple-600 font-bold">Statistical Approach</span> 
  - **Bayesian Risk Assessment**: Quantifies the probability of remaining bugs based on observed successful executions.
  - **Exploration vs. Exploitation**: Balances covering new behavioral patterns vs. deepening coverage of known risky areas. <br> <br>
- <span class="text-green-600 font-bold">Practical Outcome</span>
  - A mathematically grounded method to generate minimized, high-coverage test suites from BP models.
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

# Black-Box Bug Amplification <br> for Multithreaded Software

<div class="text-sm">

<div class="text-gray-500 mb-4">
Yeshayahu Weiss, Gal Amram, Achiya Elyasaf, Eitan Farchi, Oded Margalit, Gera Weiss, <br> Mathematics (2025)
</div>

<img src="/bug_amplification_16_10.png" class="absolute top-4 right-10 w-50 rounded-lg shadow-lg border border-gray-200 z-10 object-cover" />

- <span class="text-red-600 font-bold">The Problem</span>
  - **Heisenbugs**: Concurrency bugs that are rare, non-deterministic, and often vanish when instrumented.
  - Traditional testing (random/stress) is inefficient at finding these low-probability events.

- <span class="text-blue-600 font-bold">Black-Box Learning</span>
  - Treating the system and scheduler as valid black boxes.
  - Training **predictive models** on execution traces to estimate failure probabilities.

- <span class="text-green-600 font-bold">Amplification Loop</span>
  - **Feedback-Directed Search**: Using the model to guide the test generation towards input regions with higher suspected bug density.
  - **Order-of-Magnitude Improvement**: Demonstrated 10x+ increase in bug manifestation rates compared to random baselines.

</div>



<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---
layout: default
---

<img src="/provengo_logo_transparent.png" class="absolute top-6 right-6 w-24 z-50" />

# The Bigger Picture
## From Complexity to Clarity and Cost Savings

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Transform Enterprise Development</strong>: We simplify the complex, untangling the knots of legacy processes.
- <strong class="text-blue-800">Strategic Benefits</strong>:
    - **Compliance**: Ensure every regulatory requirement is met and traceable.
    - **Collaboration**: Unite Business, Dev, and QA under one shared model.
- <strong class="text-blue-800">Measurable Results</strong>:
    - <strong class="text-blue-800">15-25%</strong> Total Cost Savings.
    - <strong class="text-blue-800">Up to 50%</strong> Faster Delivery Timelines.
    - <strong class="text-blue-800">>30%</strong> Requirements Validated Pre-Code.

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/roi_impact.png" class="h-90 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>




<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

# Harsh Reality 

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Deep Tech Environment</strong>: Navigating a challenging fundraising landscape requires proving deep technical value over hype.

- <strong class="text-blue-800">Lean Engineering</strong>: We are a lean startup, building a robust core with a focused team.

- <strong class="text-blue-800">Customer-Centric Growth</strong>:
    - **Pilots**: Demonstrating immediate ROI in real-world environments.
    - **Value**: Shifting from "potential" to "proven impact".

</div>
<div class="flex items-center justify-center">
<img src="/slides_images/coding_under_fire.jpg" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

# Future Vision

<div class="grid grid-cols-[65%_35%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">Advanced Authoring</strong>:
    - **Visual Studio**: Intuitive drag-and-drop scenario creation.
    - **AI Assistant**: LLMs converting natural language specs into executable BP models.

- <strong class="text-blue-800">Scale & Depth</strong>:
    - **Cloud SaaS**: High-throughput, fully managed event exploration.
    - **Deep Verification**: Stronger model-checking integration for mathematical certainty.
- <strong class="text-blue-800">Ecosystem</strong>: Domain-specific test libraries for rapid adoption in Fintech, Healthcare, and IoT.

</div>
<div class="flex items-center justify-center">
  <img src="/slides_images/future_vision_engineering_interface.png" class="h-90 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>


<!--
<div dir="rtl">
Speaker notes here...
</div>
--> 

---

# Conclusion: Research ↔ Industry Reflections

<div class="grid grid-cols-[55%_45%] gap-8 items-center mt-8">
<div class="space-y-4">

- <strong class="text-blue-800">The Feedback Loop</strong>:
    - **From Industry**: Real-world scale exposes gaps in current theory and provides "hard problems" worth solving.

    - **From Research**: Principled, mathematically sound foundations prevent ad-hoc, brittle solutions.

- <strong class="text-blue-800">Symbiosis</strong>: This continuous cycle drives innovation that is both rigorous and practically applicable.
- <strong class="text-blue-800">Impact</strong>: Transforming abstract formal methods into concrete developer tools.

</div> 
<div class="flex items-center justify-center">
  <img src="/slides_images/research_industry_bridge.png" class="h-80 w-auto rounded-lg shadow-xl border-2 border-gray-100 object-cover" />
</div>
</div>

<!--
<div dir="rtl">
Speaker notes here...
</div>
-->
