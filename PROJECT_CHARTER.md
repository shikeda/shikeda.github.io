# KRM Documentation Project Charter

## Purpose

## Purpose

This Charter defines the long-term governance and guiding principles of the KRM Documentation Project.

It provides a shared framework for both human contributors and AI assistants. Its purpose is to ensure that all future work follows consistent architectural principles, regardless of the individual contributor or AI system.

This Charter is intended to remain stable over time. Project plans, Roadmaps, AI instructions, and the Documentation itself should evolve under the principles defined here.

Although this Charter currently applies only to the KRM Documentation Project, its principles are intentionally written at a level that may later be reused by related documentation projects, including TSJ and KTB.

---

# 1. Project Overview

The KRM (Ruiju Myōgishō Database) Documentation currently serves primarily researchers in historical Japanese lexicography.

Its long-term objective is to become an authoritative reference for Digital Historical Japanese Lexicography.

The goal is not simply to improve a website.

The project seeks to establish a sustainable body of documentation describing

- the structure of the database,
- annotation methodology,
- editorial policy,
- publication workflow,
- maintenance procedures,
- and the design philosophy behind KRM.

Ultimately, KRM Documentation should become a reusable model for documenting historical lexical resources.

---

# 2. Governance

This Charter is the highest-level document governing the project.

The relationship among project documents is as follows.

PROJECT_CHARTER.md

↓

ROADMAP.md

↓

AGENTS.md
CLAUDE.md
(other AI-specific instructions)

↓

Documentation

↓

Database

When inconsistencies arise,
the Charter takes precedence.

Whenever major architectural decisions are made,
the Charter should be revised first,
followed by dependent documents.

---

# 3. Project Lifecycle

The project progresses through multiple phases.

Each phase has its own objective.

Later phases should not begin before the previous phase has been accepted.

## Phase 1

Current State Analysis

Understand the existing Documentation.

Identify strengths,
weaknesses,
architectural issues,
and implicit assumptions.

Deliverables:

Analysis Report

Documentation Blueprint

---

## Phase 2

Vision Design

Establish

Mission

Vision

Scope

Audience

Documentation Principles

Documentation Blueprint

---

## Phase 3

Roadmap Design

Transform the Vision into a practical development plan.

Produce

ROADMAP.md

including priorities,
milestones,
and implementation strategy.

---

## Phase 4

Project Standards

Create project-wide standards.

Typical outputs include

AGENTS.md

CLAUDE.md

future AI-specific instructions

style guides

editorial conventions

---

## Phase 5

Documentation Refactoring

Revise Documentation chapter by chapter.

This phase focuses on

information architecture

navigation

terminology

cross references

consistency

rather than scholarly revision.

---

## Phase 6

Long-term Maintenance

Maintain conceptual consistency.

Review terminology.

Improve usability.

Introduce new Documentation when necessary.

Incorporate future research without compromising scholarly integrity.

---

# 4. Role

For any individual task,
AI acts as

Information Architect

Technical Editor

Documentation Designer

AI is not acting as

a co-author,

a peer reviewer,

or a researcher proposing new scholarship.

---

# 5. Preservation Policy

The following should be regarded as authoritative during Documentation work.

Do not modify

- scholarly interpretations
- bibliography
- examples
- datasets
- encoding rules
- identifiers
- database specifications

Unless explicitly instructed otherwise.

Documentation work should instead focus on

- information architecture
- chapter organization
- navigation
- terminology
- cross references
- discoverability
- readability

---

# 6. Mission

Draft Mission

(The current Mission statement may evolve.)

The KRM Documentation is the authoritative reference for the structure,
construction,
annotation,
publication,
and long-term maintenance
of the Ruiju Myōgishō Database.

Its purpose is not only to document KRM itself,
but also to provide a reusable methodological framework for building digital lexical resources for historical Japanese texts.

---

# 7. Documentation Principles

When making proposals,
prioritize

1. Clarity over completeness.

2. Stable terminology over local conventions.

3. Self-contained pages over cross-page dependency.

4. Explicit structure over implicit knowledge.

5. Evidence over opinion.

6. Observation before recommendation.

7. Long-term maintainability over short-term convenience.

8. International readability without sacrificing scholarly precision.

---

# 8. Long-term Vision

The Documentation should evolve from

documentation for a database

into

reference documentation for a digital scholarly resource.

The project should always favor conceptual consistency over short-term optimization.

Design decisions should remain valuable ten years from now.

---

# 9. Repository Structure

The repository is organized as follows.

Documentation

content/docs/krm/

Static assets

static/images/

The current project focuses on the KRM Documentation.

The repository layout is intended to accommodate future documentation projects, such as TSJ and KTB, under the same directory structure.

---

# 10. Audience

The intended readership should gradually expand.

Primary Users

- Historical Japanese Lexicography
- Historical Japanese
- Kanji Studies

Secondary Users

- Digital Humanities
- Corpus Linguistics
- Text Encoding

Emerging Users

- AI / LLM developers
- Digital libraries
- Historical lexical resource developers

---

# 11. Scope

The Documentation should clearly define

In Scope

Out of Scope

Assumptions

Non-goals

These evolve together with the project.

---

# 12. Phase Rules

Each phase has different deliverables.

For example,

Analysis

↓

Vision

↓

Roadmap

↓

Project Standards

↓

Documentation Editing

↓

Maintenance

Earlier phases should not be skipped.

The Charter remains valid throughout every phase.

---

# 13. Current Task

This Charter defines the entire project.

The following task applies only to the current phase.

Current Phase

Phase 1

Current State Analysis

Do not edit Documentation.

Observe first.

Recommend second.

Evaluate the Documentation against generally accepted principles of reference documentation,
rather than against specific external projects.

Whenever possible,

refer to

file paths,

chapter titles,

directory names.

---

# 14. Success Criteria

The current phase is successful if it produces

- a reliable understanding of the Documentation
- an architectural diagnosis
- a Documentation Blueprint
- a realistic Roadmap
- prioritized next actions

without altering scholarly content.

---

# 15. Deliverables (Phase 1)

Produce

## Vision Package

Mission

Vision

One-sentence Description

Elevator Pitch

---

## Documentation Blueprint

Conceptual structure

Relationship to current Documentation

---

## Information Architecture

Navigation

Hierarchy

Cross references

Glossary

Appendices

---

## Documentation Roadmap

Vision

↓

Blueprint

↓

Implementation

---

## Prioritized Tasks

High

Medium

Low

Each task should include

affected files

expected work

brief rationale.

---

# 16. Living Document

This Charter is expected to evolve.

When the project's philosophy changes,

update this Charter first.

Then update

ROADMAP.md

AGENTS.md

CLAUDE.md

and any other dependent documents.

The Documentation itself should always reflect the principles established here,
rather than redefining them independently.