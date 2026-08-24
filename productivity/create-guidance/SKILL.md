---
name: create-guidance
description: Clarify vague or high-level requests, propose options, and give direct step-by-step guidance. Use when a user asks for help understanding what to do, how to do it, or needs intent clarification to turn a goal into actionable steps.
---

# Create Guidance

## Overview

Turn unclear goals into clear, actionable guidance by proactively researching the user's intent — investigating the workspace and the internet — then presenting a well-informed proposal for confirmation before producing the final guidance.

## Workflow

### 1) Guess the intention

- Read the user's request and infer the most likely goal, scope, and success criteria.
- Restate your best guess of the intent in one sentence (internally).

### 2) Investigate proactively (workspace + internet)

Do NOT ask the user what's missing. Instead, research on their behalf:

**Workspace investigation:**
- Explore the current project structure, tech stack, existing configs, and related files.
- Look for patterns, conventions, and constraints already established in the codebase.

**Internet research:**
- Search for the general consensus, best practices, and common approaches related to the user's intent.
- Find what the community/industry standard is for accomplishing this kind of goal.
- Gather concrete examples, tools, libraries, or frameworks that are commonly used.

### 3) Formulate your solution

Based on your research:
- Synthesize what you found into a concrete proposed approach.
- Identify the recommended path: what tools/methods to use, what steps to follow, what tradeoffs exist.
- Note any assumptions you're making and any gaps you couldn't fill through research.

### 4) Present proposal and confirm

Present your findings to the user as a proposal:

**Proposal template:**
- "Here's what I think you're asking for: [restate intent]"
- "Based on my research, here's the general approach: [summary of findings]"
- "My recommended solution: [concrete plan with key steps]"
- "Assumptions I'm making: [list any]"
- "Is this what you're looking for?"

Wait for the user to confirm (yes) or correct you.

### 5) Create the guidance (after confirmation)

Only after the user confirms:
- Provide 2-3 realistic options with tradeoffs (time, cost, complexity, risk).
- Recommend one option based on stated constraints and your research.
- Give ordered, concrete steps the user can follow immediately.
- Include prerequisites, tools, checkpoints, and references where useful.

### 6) Close the loop

- Ask if the user wants to refine any part of the guidance.
- Offer to adjust depth, scope, or approach based on feedback.

## Response structure (after confirmation)

- Summarize intent in one sentence.
- State assumptions (if any).
- List options (2-3 bullets) with tradeoffs.
- Recommend one path in 1-2 sentences.
- Provide numbered steps with prerequisites and tools.

## Key principles

- **Research first, ask later.** Never ask the user to fill gaps you can fill yourself through investigation.
- **Present a proposal, not questions.** The user should only need to say "yes" or "not quite, I meant X."
- **Be informed.** Your proposal should reflect real-world best practices and the actual project context, not generic advice.
- Keep guidance concrete and actionable; avoid vague advice.
- Match the user's level; explain jargon briefly if it appears.
- If the request is infeasible or unsafe, explain why and offer a safe alternative.
