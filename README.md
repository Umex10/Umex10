<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=26&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Hey%2C+I'm+Umejr+%F0%9F%91%8B;Full-Stack+Dev;Java+%E2%80%A2+TS+%E2%80%A2+React;Building+things+that+actually+work)](https://git.io/typing-svg)

<img src="https://komarev.com/ghpvc/?username=umejr&style=flat-square&color=6366f1" alt="profile views"/>

</div>

---

## 🚀 The Arsenal | Project Overview

A quick look at the repositories worth exploring:

| &nbsp; | Repo | Core Focus |
| :---: | :--- | :--- |
| 🛡️ | [**chatex**](https://github.com/umejr/chatex) | Social media platform with a robust JWT security layer. |
| 🧠 | [**renderex**](https://github.com/umejr/renderex) | AI-powered Markdown note-taking via Gemini & Firebase. |
| 🎯 | [**task-manager**](https://github.com/umejr/task-manager) | Full-stack S-Boot app, live deployed on Railway & Vercel. |
| ⚡ | [**TicTacToe**](https://github.com/umejr/TicTacToe) | Networked multiplayer game with heavy Java concurrency. |
| ☁️ | [**weather.app**](https://github.com/umejr/weather.app) | Clean, fast, and responsive weather application. |
| 👨‍💻 | [**dev-resume**](https://github.com/umejr/dev-resume) | My personal developer portfolio & resume. |
| 🚖 | [**smart-kassa**](https://github.com/umejr/smart-kassa) | Taxi register system with live GPS tracking & analytics. |

---

## 🔬 Deep Dives | Under the Hood

### 🛡️ Chatex — Secure Social Media Platform
Full-stack **social media** app supporting users, posts, and real-time chat, built with a heavy focus on backend security.
* **The Security Layer:** A custom **JWT filter chain** intercepts every request before it hits the controller.
* **Token Architecture:** Access tokens (15 min) live in the response body. Refresh tokens (30 days) are secured in an `HttpOnly` cookie—**XSS-proof by design** and invisible to JavaScript.
* **Validation:** Each JWT carries a strictly verified `type_jwt` claim to ensure tokens can never be swapped.

> **Stack:** `Next.js` • `TypeScript` • `Tailwind` • `Redux` • `Spring Boot` • `Spring Security` • `PostgreSQL` • `Docker`

---

### 🧠 Renderex — AI-Powered Note-Taking
Modern note-taking where Markdown meets AI. Entirely serverless architecture.
* **Serverless Backend:** **Firebase** handles auth, real-time database, protected routes, and user-scoped data seamlessly.
* **Context-Aware AI:** **Google Gemini** is wired directly in for intelligent content generation.
* **UI/UX:** Multi-format export (PDF, DOCX, MD, TXT), comprehensive tag system, and fluid dark/light themes powered by **Framer Motion**.

> **Stack:** `Next.js` • `TypeScript` • `Firebase` • `Redux` • `Gemini AI` • `Framer Motion` • `Tailwind`

---

### 🚖 Smart-Kassa — Live Tracking Taxi Register
A **SCRUM-driven** team project delivering a complete register system for taxi companies. 
* **My Role:** Built and designed the entire UI and engineered the interactive route system.
* **Live Tracking:** Integrated **Leaflet** for the interactive map, real-time GPS tracking during rides, and turn-by-turn navigation.
* **Driver Dashboard:** Built the *All Rides* log with animated entries, the *Summary* analytics dashboard, and critical driver settings.

> **Stack:** `React` • `TypeScript` • `Leaflet` • `Redux` • `Tailwind` • `Shadcn/ui` • `Framer Motion` • `Node.js` • `Express` • `PostgreSQL`

---

### ⚡ TicTacToe — Advanced Java Concurrency & Networking
Not just a simple game—a fully **networked multiplayer** experience powered by a custom TCP server-client architecture built from scratch.
* **Multi-Threading:** Every client connection runs on a dedicated thread. Coordinated via `ConcurrentHashMap` for active sessions and `ConcurrentLinkedQueue` for the matchmaking pool.
* **Thread Safety:** Handled by `AtomicBoolean` and `CountDownLatch`. Background timers run with a `volatile` stop flag and `Thread.interrupt()` to strictly protect the JavaFX UI thread.
* **Modular AI:** Implements the **Strategy Pattern** (`EasyMove`, `MediumMove`, `HardMove`), allowing difficulty swapping at runtime.

> **Stack:** `Java` • `JavaFX` • `TCP Sockets` • `Concurrency API` • `JUnit 5` • `Maven`

---

## ⚙️ Core Stack

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=java,spring,ts,js,react,nextjs,tailwind,redux,firebase,postgres,docker,git&perline=6)](https://skillicons.dev)

</div>

---

## 📈 GitHub Analytics

<div align="center">

<img height="160" src="https://github-readme-stats-tawny-sigma-83.vercel.app/api?username=Umex10&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub Stats" />
<img height="160" src="https://github-readme-stats-tawny-sigma-83.vercel.app/api/top-langs/?username=Umex10&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />

<img src="https://streak-stats.demolab.com?user=Umex10&theme=tokyonight&hide_border=true" alt="GitHub Streak" />

</div>

<br>

<div align="center">
<sub><b>Built by hand. No shortcuts.</b></sub>
</div>
