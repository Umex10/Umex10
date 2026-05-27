<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=26&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Hey%2C+I'm+Umejr+%F0%9F%91%8B;Full-Stack+Dev;Java+%E2%80%A2+TS+%E2%80%A2+React;Building+things+that+actually+work)](https://git.io/typing-svg)

</div>

---

## 🚀 Apps

A quick overview of the repos worth seeing:

| &nbsp; | Repo | What it is |
|--------|------|-----------|
| 💬 | [**chatex**](https://github.com/Umex10/chatex) | JWT-Authentication, Layered Backend (Controller, Service, Model), Fast Sql-Queries |
| 👤 | [**dev-resume**](https://github.com/Umex10/dev-resume) | My dev resume, built with Next.js |
| 🧩 | [**dsa-exercises-website**](https://github.com/Umex10/dsa-exercises-website) | Detailed LeetCode solutions & DSA notes — Java solutions + Next.js website |
| ✏️ | [**renderex**](https://github.com/Umex10/renderex) | AI-Driven note-taking — Next.js + Firebase + Gemini |
| 🚕 | [**smart-kassa**](https://github.com/Umex10/smart-kassa) | In Team — taxi register system — React + Leaflet live tracking, dashboard & analytics |
| ✅ | [**task-manager**](https://github.com/Umex10/task-manager) | My first full-stack S-Boot app — React + S-Boot + Docker, live on Railway & Vercel |
| 🎮 | [**TicTacToe**](https://github.com/Umex10/TicTacToe) | Networked multiplayer game — Java + JavaFX + TCP sockets + concurrency |
| 🌤️ | [**weather.app**](https://github.com/Umex10/weather.app) | Weather app — React + TS + Vite + Tailwind |

---

## 🔍 Deep Dives

### 💬 Chatex — Social Website

A social-Website with a JWT auth system. The **S-Boot-Security** `Security-Chain` is fully stateless — CSRF disabled, CORS locked to the frontend origin. Every request runs through a custom **`JwtAuthentication`** (`OncePerRequest`) that pulls the Bearer token from the `Authorization` header, validates it via **JWT**, and sets the `SecurityContextHolder` — giving every downstream controller direct access to the authenticated user. Token strategy: short-lived **access token** (15 min) + long-lived **refresh token** (30 days, HttpOnly cookie). Users can post **Shouts**, manage their accounts (avatar, banner, bio, location), and the `AuthController` builds sign-up, sign-in, and token refresh endpoints.

`Next.js` `TS` `S-Boot` `S-Boot-Security` `JWT` `P-SQL` `Redux` `Shadcn/ui` `Container & Images`

---

### 🧩 LeetCode & DSA Exercises — Issue Solving

A dedicated website where I thoroughly document my solved **LeetCode** issues and Data Structures & Algorithms (DSA) exercises. Every solution is coded in **Java** and comes with an in-depth explanation of the underlying logic, accompanied by a precise **Time and Memory Complexity** analysis. The website features a robust **filtering system**, allowing users to easily search and sort issues. Built with **Next.js**.

`Java` `Next.js` `Algorithms` `DSA` `Time/Space Complexity` `Tailwind`

---

### 📝 Renderex — AI-Driven Note-Taking

Modern note-taking where markdown meets AI. **Firebase** handles the entire backend — auth, database, protected routes, user-scoped data — all without running a server. **Google Gemini** is wired in for context-aware content generation. Export to PDF, DOCX, Markdown or plain text, full tag system, dark/light theme with **Framer Motion** animations.

`Next.js` `TS` `Firebase` `Redux` `Gemini AI` `Framer Motion` `Tailwind`

---

### 🚕 Smart-Kassa — Taxi Register System with Live Track

A **Team-built (SCRUM) software** — a full register system for taxi companies. I built and designed the entire UI and was fully responsible for the route system — **Leaflet** for the interactive map, **live GPS tracking** during rides, turn-by-turn navigation to the destination. The **All Rides** view lists every recorded trip with sorting and animated entries. I also built the **Summary** page, the **Dashboard** with analytics, and the **Settings** — everything the driver actually interacts with every shift.

`React` `TS` `Leaflet` `Redux` `Tailwind` `Shadcn/ui` `Framer Motion` `Node.js` `Express` `PostgreSQL`

---

## 🛠️ Tech Stack

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=java,spring,ts,js,react,nextjs,tailwind,redux,firebase,postgres,docker,git&perline=6)](https://skillicons.dev)

</div>

---

<div align="center">
<sub>Built by hand. No shortcuts.</sub>
</div>
