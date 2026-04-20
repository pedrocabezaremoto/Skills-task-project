---
alwaysApply: true
---

Prompt Engineering: Re-write the task description into a structured entry point
that guides an AI agent to build the solution from scratch.

---

## GOAL

The first step is to transform a raw task description into a structured prompt. This prompt
functions as a Job Application/Freelance Brief that an AI agent will use to come up with a
solution.

---

## RULES TO FOLLOW TO MAKE THE PROMPT

**Clarity:** Ensure the goal and tech stack are unambiguous.

**Context:** Include all necessary information for the agent to create the correct tests
and solution (Golden Patch).

**Expected interface:** Include a section within the rewritten prompt to define every
newly introduced file, function, or class that an external module or test suite will
interact with. You should include:

● **NOTE:** There should be an expected interface for every test case

○ Path: [Exact file path as it appears in the intended structure]  
○ Name: [Class.method or function name]  
○ Type: [e.g., class, method, function, or interface]  
○ Input: [Parameters and types, e.g., chunk: GlibcChunk]  
○ Output: [Return type, e.g., None or Promise<void>]  
○ Description: [Briefly describe observable side effects or behavior asserted by tests]

**Language-Specific Fields (as applicable):**

○ **TypeScript/Java:** Inheritance: extends <Base>; implements <IfaceA, IfaceB>  
○ **Go:** Embedding / Implements: embeds <TypeA>; implements <IfaceA, IfaceB>  
○ **Python:** Bases / Overrides: bases: <BaseA, BaseB>; overrides: <Base.method>  
○ **Annotations / Decorators:** @Override, @Inject, @dataclass, @cached_property, @sealed

---

## Common Prompt Structure Pattern

### Typical Ordering (two main patterns)

**Pattern A** (most common — 12/20):

1. # Title
2. ## Description / Context
3. ## Tech Stack
4. ## Key Requirements (with ### subsections)
5. ## Expected Interface (with ### per function/class/endpoint)
6. ## Current State

**Pattern B** (for larger/more detailed tasks — 8/20):

1. # Title
2. ## Description
3. ## Current State
4. ## Required Implementation
5. ## Expected Interface (with ## and ### groupings)
6. ## Deliverables / Acceptance Criteria

### Expected Interface Format (universal across all)

Every entry in the Expected Interface section follows this per-item schema:

- **Path:** <exact file path>
- **Name:** <Class.method or function or endpoint>
- **Type:** <class | function | method | API Endpoint | React Component | interface | Prisma Model | ...>
- **Input:** <parameters and types>
- **Output:** <return type or HTTP response>
- **Description:** <what it does and what tests verify>

Some tasks add language-specific fields like Annotations: @override (Flutter/Dart) or include testID
mappings (React Native), TypeScript type definitions inline, or Prisma schema field requirements.

---

### EXAMPLE

**Task description:**

Need experienced designer/developer for website to show menu and hours for our
Aroy Dee Thai Restaurant customer so the customer can easily see all info.
Please create the website and logo. Link to menu. Hours: 9am-10pm Tue-Sun,
closed Mon.

**Re-written prompt:**

Need experienced designer/developer for website to show menu and hours for our
Aroy Dee Thai Restaurant customer so the customer can easily see all info.
Please create the website and logo. Link to menu. Hours: 9am-10pm Tue-Sun,
closed Mon.

# Title  
Build Complete Thai Restaurant Website

## Description  
Need a complete React-based restaurant website for Aroy Dee Thai built from
scratch. The site currently has no implementation and needs full development of
all components, styling, and functionality.

## Expected Interface

- **Path:** src/components/MenuSection.js  
- **Name:** MenuSection  
- **Type:** React Component  
- **Input:** props: { categoryName: string, items: Array }  
- **Description:** A public component that renders a collapsible list of menu items. Bases / Overrides: overrides: React.Component

## Current State  
Empty repository with test files only.

## Required Implementation  
Build a complete mobile-first Thai restaurant website with React that passes
all 72 comprehensive tests covering rendering, content accuracy, interactions,
menu structure, visual design, and component functionality.

- Create complete React application structure with App component, MenuSection
  component, and MenuItem component
- Implement collapsible menu sections with toggle functionality
- Create 13 menu categories with full menu items, prices, and descriptions
- Design Thai-inspired aesthetic with custom SVG decorations (logo, dividers,
  ornaments)
- Implement responsive CSS that works on mobile (≤480px) and desktop (≥768px)
  viewports
- Display restaurant information (address, hours, spice warning)
- Create elegant menu header section
- Ensure all 72 tests pass covering rendering, content, interaction, menu
  accuracy, and visual design