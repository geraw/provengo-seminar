---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-01.png

LJ LJ]

| ’

What if your requirements document wasn’t a
LJ] LJ

dead artefact, but a living, testable asset?
We treat requirements, specifications, and test plans as static documents. They are written, reviewed, and then
quickly fall out of sync with the living system they describe. This gap is where complexity, ambiguity, and bugs are
born. It's time for a fundamental shift in perspective.
Al a [FT = | “4 \ 3 ; AH] = | @ N fe, LIVE TESTABLE
|S Ee EN BF 8
EE i ii iE <5 | TEN Cl
3 i de lead a 1 “Nek SS. B Zz «Qt R i ea
F TRH ll =] 1 EE IC) SCARE Ce
ER RE Fo Ne ASR La

1 : |mlepla | de va Ee +1 : LIVIN 9 7 > :

| Seceah NEN I SC ma

£ NotebookLM


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-02.png

® @ [J] [J] ®
The Blueprint is Brittle: Why Traditional
a ® ® ®
BDD is Reaching Its Limits.
The promise of Behavior-Driven Industry Chatter |
: © res Ch CARE) oe:

Development (BDD) was to bridge the == ves a.

- - = J [o - ; Last release was three years
business-technical divide. Yet, the rr — : a | ago... it looks pretty abandoned. |

: k J : a FN SR 1S Shs yy J
reality is often a maintenance nightmare as ee ———————
of fragile test suites and a disconnect = ; = ==F 0 ri ee ay
between Gherkin feature files and the | i So Es oie
underlying system logic. The “easy to — en
write markup” often creates more or de LR |
work than it saves J [57

A NotebookLM


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-03.png

The Future is a Living Model: A Single Source
of Truth for Your System.

Imagine a single, executable model of SN

your system's behaviour. It’s not a F 2.0 i />
document; it’s a dynamic ik ZN Pave 7%
representation you can query, visualise, . SS ji ES Developer
and use to generate tests. This model eZ FS 5

becomes the unambiguous source of "3 SF >

truth that bridges the gap between EE 8 2 < A
business, development, and QA, A Teh. 7 HON
ensuring everyone is building and | all =
testing the same system. Business Analyst QA Engineer


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-04.png

Provengo: The Tool Suite for Scenario-Driven
Model-Based Testing

=] =i el
Provengo is a tool that makes system i [=
requirements active. It enables you to build BZ a as
living models by codifying user stories and td? fi ey n=
business logic. This approach, called = z= L :
Scenario-Driven Model-Based Testing arto ol ons a
(SDMBT), allows for incremental Ea
development, starting with simple models and
gradually augmenting them with more FUR es ah ie
i br paler wipe ww ocd

Gera Weiss, Yeshayahu Weiss


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-05.png

a | ®

Encode Complex Business Rules as Clear, Executable Logic
With Provengo’s “Combi library, you can define specification parameters and their inter-dependencies

directly in the model. This transforms ambiguous business rules into testable code, eliminating misinterpretation.
O J ad
0 o—"°
// A sports car must have exactly two seats. S 5
vehicleType.whenSetTo("sports car") So Rn —— RE

E ~ O
.field(seatCount) he TR fo
.mustBe(2); O —4
Q Ee
// A truck can't have 6 seats. — En a ©
vehicleType.whenSetTo("truck") ol : CEs on Oo
.field(seatCount) Ee iy Oo
.cannotBe (6): — os
os
Provengo automatically visualises the entire test space from your model.
Er NotebookLM


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-06.png

From Abstract Model to Concrete Automation
A Provengo model isn't just a theoretical construct. It directly drives real-world automation through a rich set of libraries.
The model defines the “what” and “why,” while the libraries execute the “how” against your application’s UI and APIs.
Ul Automation (Selenium) API Testing (REST)
// @provengo summon selenium // @provengo summon rest
const session = new SeleniumSession("main"); const svc = new RESTSession(SERVER_ENDPOINT);
session.start("https://your.app.com"); // Create new customer
session.click("//a[contains(text(), 'Sign In')]"); svc.post("/customers", {
session.writeText("//input[@id="username']", "dave"); body: JSON.stringify({ "first_name":fName, ... }),
expectedResponseCodes: [200]
ke
EE mmm
Sign In <> 0) Gl
|
| By amin! 58
PO — LOK
Ei NotebookLM


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-07.png

A Complete, Local-First Workflow for Modelling and Testing.
Provengo is a command-line tool that runs locally. No data is transferred to our servers,
making it suitable for any environment, from local machines to air-tight CI/CD pipelines.
: :
Write your model
REPORT IC - in Javascript. a) ANALYZE
Review detailed |_= il Visualise the state space
execution reports. and verify your logic.
RU \ ~ J SAMPLE
Execute the scenarios = Generate a random or full set of
against your system. test scenarios from the model.
Bs provengo sample --size 100 ...


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-08.png

~ LJ LJ LJ .
Case Study: Reinventing Insurance Claims Processing
The Challenge The Provengo Solution The Impact
le Bed ii
EAE D) Siting M 0-25Y%
a fr we Si IY be E 2 2 0
3 Ob = : | B Reduction in Shorter project
operational costs. development cycle.
A large insurance company in the The client used Provengo to map
APAC region needed to and automate every aspect of
transition from manual claims their process. By fully defining = 0
processing to a web-based their policies within the model, D4 ; =0
automated system, navigating regulatory compliance became > —%
complex rules, multiple platforms, straightforward, and the Complete process Simplified compliance
and strict regulations. manual burden of processing clarity, improving with clear policy
was eliminated. confidence across definitions.
teams.
Ai NotebookLM


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-09.png

[J] LJ] 9
[J]
Case Study: Improving a Major Bank’s
Customer Experience
The Challenge The Provengo Solution The Impact
fh A major bank aimed The client built a
=| — to replace its Single 0 complete model of 50 0% > 30 %
| be 1 Sign-On (SSO) — their desired SSO Be or
L o system to reduce = capabilities, eduction In the HS Lea EE
customer friction idl ped =o EE ensuring seamless STD (System Test validated and
= while safeguarding 2 integration. Design) timeline. improved before
: O= data and ensuring “| Automation of implementation.
pe O=| regulatory critical tests and a
alignment across focus on risk-based
multiple platforms. coverage V4 vv
significantly
reduced Enhanced test Ensured regulatory
complexity for efficiency, freeing compliance via
internal teams. teams to focus on easy-to-follow
innovation. policy frameworks.
A NotebookLM


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-10.png

The Bigger Picture: From Complexity to Clarity
and Cost Savings.
Provengo transforms how enterprises create systems. By simplifying the complex, we ensure
regulatory compliance, free teams from stress, improve collaboration, and drive significant
cost reductions.
Fr v
15-25% | | Upto 50% | >30%
Total Cost Savings Faster Timelines Requirements Validated
(STD timeline reduction) Pre-Code
Operations that run smoother, faster, and smarter.


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-11.png

A Robust and Secure Toolchain, Built for
Professional Teams.
Provengo is designed to integrate seamlessly and securely into your existing development lifecycle.
= Local Execution: Runs entirely on o Selenium Integrated: Uses Selenium
your local machine or CI server. No Manager for automatic web driver
— internet connection is required for synchronisation, working out-of-the-
— operation. box. Supports remote Selenium Grids.
Zero Data Transfer: No models, code, IDE Support: A dedicated Provengo
oa ) ortest data are ever transferred to <>] Studio VSCode Plugin is available for an
Provengo’s servers. enhanced GUI experience.
« ; Br OC] % Platform Support: Installation
i ls pre Requires only Cd C packages available for Linux, Mac, and
= af A Windows.


---
layout: default
---

# Slide extracted from Executable_Requirements_Living_Models-12.png

Are you ready to begin simplifying the
complex?
Provengo helps you transform intricate processes into streamlined, efficient systems. We support
every step of your journey, from installation and training to ongoing process optimisation.

Book a Demo

hello@provengo.ai

Tel Aviv, Israel - HQ: +972-(0)774235850
Boston, USA - HQ: +1 (857) 799-0150


