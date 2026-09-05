# Neer Bhardwaj — Systems Architecture & Engineering Compendium

[![Live Demo](https://img.shields.io/badge/Live%20Demo-neerbhardwaj.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://neerbhardwaj.vercel.app)
[![Architecture](https://img.shields.io/badge/C%2B%2B20-LLVM%2018%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](https://neerbhardwaj.vercel.app)
[![Status](https://img.shields.io/badge/Status-Verified%20Production-059669?style=for-the-badge)](https://neerbhardwaj.vercel.app)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> **Live Website:** [https://neerbhardwaj.vercel.app](https://neerbhardwaj.vercel.app)  
> **Master Compendium Document:** [`Neer_Bhardwaj_Master_Engineering_Skills_Compendium.pdf`](Neer_Bhardwaj_Master_Engineering_Skills_Compendium.pdf)

---

## 🏛 Overview

An exhaustive technical compendium indexing **41 production engineering competencies** across **8 core disciplines**, engineered from first principles over 28+ production codebases.

The system explores the complete execution stack: from low-level compiler intermediate representation (LLVM IR) and deterministic spatial game networking to zero-knowledge cryptographic vaults, high-frequency CPU computer vision pipelines, and resilient multi-agent runtimes.

---

## ⚡ Core Technical Pillars

| Discipline | Specification & Implementation | Invariants & Guarantees |
| :--- | :--- | :--- |
| **Compilers & Toolchains** | LLVM 18+ IR, Recursive Descent AST, Type Checker, Custom Stdlib (`omlib`) | Zero runtime dependencies, predictable codegen |
| **Spatial Concurrency** | Modern C++20 Multithreaded ECS, 64Hz UDP Socket Delta Replication | ASan/TSan clean, bounded lock contention |
| **Cryptographic Security** | Authenticated AES-256-GCM, PBKDF2 (600,000 iter), In-Memory Scrubbing | Zero plaintext exposure, constant-time verification |
| **Computer Vision** | MediaPipe 468 3D Mesh, SolvePnP 3D Head Pose tracking | Deterministic 60 FPS CPU execution |
| **Distributed Orchestration** | Deterministic state machine replication, telemetry ingest, resilient failover | Linearizable reads, partitioned self-healing |

---

## 🖥 Interactive Web Compendium Features

This repository powers the interactive portfolio and technical compendium at **[neerbhardwaj.vercel.app](https://neerbhardwaj.vercel.app)**:

- **41-Skill Search & Filter Index:** Real-time search across 8 engineering disciplines with deep-dive modal breakdowns.
- **Systems Workbench:** Live interactive simulation modules demonstrating memory management, compiler pipeline stages, and concurrent scheduling.
- **Invariants Matrix:** Mathematical formulations, algorithmic complexity bounds, and system invariant specifications.
- **In-Browser Terminal CLI:** Embedded terminal interface emulator with custom commands (`help`, `skills`, `specs`, `fetch`, `clear`).
- **Command Palette (`⌘K` / `Ctrl+K`):** Keyboard-driven search navigation for instant access to any skill or specification.
- **Tactile Web Audio:** Micro-interaction acoustic feedback powered by the Web Audio API.
- **Master PDF Integration:** Integrated download and preview of the 7-page technical engineering compendium.

---

## 📁 Repository Structure

```
.
├── index.html          # Core single-page application layout & editorial interface
├── style.css           # Custom design system, typography & micro-interactions
├── app.js              # Application logic, audio engine, command palette, & CLI shell
├── skills-data.js      # Structured database of 41 engineering competencies & specs
├── Neer_Bhardwaj_Master_Engineering_Skills_Compendium.pdf # Complete PDF compendium
├── serve.py            # Local resilient HTTP development server with hot-reload
├── launch.bat          # One-click Windows development launcher
├── .vercelignore       # Build exclusion rules for clean Vercel deployments
└── README.md           # Project documentation & architecture overview
```

---

## 🚀 Getting Started

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NeerBhardwaj1/Achievements-and-skills-till-now.git
   cd Achievements-and-skills-till-now
   ```

2. **Run the local server:**
   - On Windows: Double-click `launch.bat` or run:
     ```powershell
     python serve.py
     ```
   - Or with any standard static file server:
     ```bash
     npx serve .
     ```

3. **Open in Browser:**
   Navigate to `http://localhost:3000` (or the port displayed in your terminal).

---

## ☁️ Deployment

The website is continuously deployed on **Vercel**:

```bash
# Deploy to production
npx vercel --prod
```

---

## 📬 Contact & Advisory

- **Engineering Compendium:** [https://neerbhardwaj.vercel.app](https://neerbhardwaj.vercel.app)
- **GitHub:** [@NeerBhardwaj1](https://github.com/NeerBhardwaj1)

---

© Neer Bhardwaj. All rights reserved.
