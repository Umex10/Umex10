<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=26&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Hey%2C+I'm+Umejr+%F0%9F%91%8B;Full-Stack+Dev;Java+%E2%80%A2+TS+%E2%80%A2+React;Building+things+that+actually+work)](https://git.io/typing-svg)

<img src="https://komarev.com/ghpvc/?username=umejr&style=flat-square&color=6366f1" alt="profile views"/>

</div>

---

## � Apps

A quick overview of the repos worth seeing:

| &nbsp; | Repo | What it is |
|--------|------|-----------|
| 💬 | [**chatex**](https://github.com/umejr/chatex) | Social media app — Next.js + S-Boot with full JWT security layer |
| ✏️ | [**renderex**](https://github.com/umejr/renderex) | AI-powered note-taking — Next.js + Firebase + Gemini |
| ✅ | [**task-manager**](https://github.com/umejr/task-manager) | My first full-stack S-Boot app — React + S-Boot + Docker, live on Railway & Vercel |
| 🎮 | [**TicTacToe**](https://github.com/umejr/TicTacToe) | Networked multiplayer game — Java + JavaFX + TCP sockets + concurrency |
| 🌤️ | [**weather.app**](https://github.com/umejr/weather.app) | Weather app — React + TS + Vite + Tailwind |
| 👤 | [**dev-resume**](https://github.com/umejr/dev-resume) | My personal portfolio / resume, built with Next.js |
| 🚕 | [**smart-kassa**](https://github.com/umejr/smart-kassa) | Group project — taxi register system — React + Leaflet live tracking, dashboard & analytics |

---

## 🔍 Deep Dives

### 💬 Chatex — Social Media Platform with a real Security Layer

Full-stack **social media** app — users, posts, real-time chat. Built with **Next.js** + **S-Boot**. The security layer: a custom **JWT filter chain** intercepts every request before it reaches a controller. **Access token** (15 min) lives in the response body, the **refresh token** (30 days) goes into an `HttpOnly` cookie — invisible to JavaScript, XSS-proof by design. Each JWT carries a `type_jwt` claim so tokens can never be swapped.

`Next.js` `TS` `Tailwind` `Redux` `S-Boot` `S-Boot Security` `PostgreSQL` `Docker`

---

### 📝 Renderex — AI-Powered Note-Taking

Modern note-taking where markdown meets AI. **Firebase** handles the entire backend — auth, database, protected routes, user-scoped data — all without running a server. **Google Gemini** is wired in for context-aware content generation. Export to PDF, DOCX, Markdown or plain text, full tag system, dark/light theme with **Framer Motion** animations.

`Next.js` `TS` `Firebase` `Redux` `Gemini AI` `Framer Motion` `Tailwind`

---

### 🚕 Smart-Kassa — Taxi Register System with Live Map

A **Team-built (SCRUM) software** — a full register system for taxi companies. I built and designed the entire UI and was fully responsible for the route system — **Leaflet** for the interactive map, **live GPS tracking** during rides, turn-by-turn navigation to the destination. The **All Rides** view lists every recorded trip with sorting and animated entries. I also built the **Summary** page, the **Dashboard** with analytics, and the **Settings** — everything the driver actually interacts with every shift.

`React` `TS` `Leaflet` `Redux` `Tailwind` `Shadcn/ui` `Framer Motion` `Node.js` `Express` `PostgreSQL`

---

### 🎮 TicTacToe — Java Concurrency & Networking

Not just a game — **networked multiplayer** with a custom TCP server-client architecture built from scratch. Every client connection runs on its own thread, coordinated via `ConcurrentHashMap` for game sessions and `ConcurrentLinkedQueue` as the matchmaking pool. `AtomicBoolean` + `CountDownLatch` handle player sync, the countdown timer runs on a background thread with a `volatile` stop flag + `Thread.interrupt()` — JavaFX UI thread never touched. AI difficulty via a **Strategy pattern**: `EasyMove`, `MediumMove`, `HardMove` — swappable at runtime.

`Java` `JavaFX` `TCP Sockets` `Concurrency API` `JUnit 5` `Maven`

---

## 🛠️ Tech Stack

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=java,spring,ts,js,react,nextjs,tailwind,redux,firebase,postgres,docker,git&perline=6)](https://skillicons.dev)

</div>

---

## 📊 Stats

<div align="center">

<img height="160" src="https://github-readme-stats-tawny-sigma-83.vercel.app/api?username=Umex10&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" />
<img height="160" src="https://github-readme-stats-tawny-sigma-83.vercel.app/api/top-langs/?username=Umex10&layout=compact&theme=tokyonight&hide_border=true" />

<img src="https://streak-stats.demolab.com?user=Umex10&theme=tokyonight&hide_border=true" />

</div>

---

<div align="center">
<sub>Built by hand. No shortcuts.</sub>
</div>
