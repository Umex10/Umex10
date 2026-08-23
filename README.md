```text
             .::;;;||||(((|||;:     .           Umex10@github ----------------------------------------------
          .:;;|(((tttt(tt((tttt((|:   .         . OS: ........................................... Linux Mint
        :;;|(tttt((((((((((((((((ttt|.  .       . Host: ............................................... Graz
      .;||(ttt(((((((((((((((((((|((tt(:        . Kernel: ..................... Software Engineering Student
     ;|;(ttt((tttt((((((((((((((((((|((tt. .    . IDE: .............................................. VSCode
  .|.t##wkkkwkjjfftftt((((tt((((((((((((|(f| .                                                              
  |:f%%%%%%%###wwwkjjjkjjfft((((((((((((((((:   . Languages: ...................................... Java, TS
 |;(%%%%@@@@@@%%%%%%%%#kjftttt(((((((((((((((   . Languages.Frameworks: .................... Next.js, S-Boot
:|.%%#%@@@@@@@@@@%%%%#wkjjft(tfjjft((((f(((((;  . Languages.Markup: ................... HTML, CSS, SQL, YAML
| k@@@@@@@@@@@@@@@@@@@%%%kkkw##wftttttjt(t((((                                                              
|.%@@@@@@@@@@@@@@@@@@@@@%##%wkjffffjjjj(ft((tf  . Hobbies.Software: .................. Coding fullstack apps
;(%%@@@@@@@@@@@@@@@@@@@@@%%#kkkkwwwwkwkjjtttf(  . Hobbies.Focus: .................. Auth systems, clean APIs
 f%%@@@@@@@@@@@@@@@@@@@@%%%###%%%%%##%wwjfjjt(                                                              
:t%%%@@@@@@@@@@@@@@@@@@@%%#%%%@@@@@@@%%%kwkftt  Contact ----------------------------------------------------
;|w%%%@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@#kjft  . Work: ........................... umi.dzinovic10@gmail.com
:;fw%%%%@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@%wjj(  . DevResume: ................... dev-resume-sigma.vercel.app
..fjw%%%%%%%@@@@@@%%%%%%%@@@@@@@@@@@@@@@%#kjf.  . GitHub: ........................................... Umex10
 .;jjjk#%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@%#wkj;                                                               
   |jjfj%###%%%%###%%#w#%@@@@@@@@@@@@@%#wkj| .  GitHub Stats -----------------------------------------------
  . (jjfk############%%%%@@@@@@@@@@@%#wkkj| .   . Reps: .................... 9 | Followers: 7 | Following: 5
   . |jkjjkw#######%#######%%@@@@%%#wkjjf: .    . Contributions: .......................... streak: 201 days
    . :fkjjjjwwwwkkjjjjjjjjkkwwwwkkkjjf|  .     . Labeld: ........................ authkit, chatex, renderex
     .  |tffft(|((|(ffjjjjjfffjjjffft|  .       . Stack.Live: ...................... Docker, Railway, Vercel
       .  ;||((ttttfffftttjfjftftt|:   .                                                                    
        ..   .;||(fft(((ttffft|;:   ..                                                                      
```

<div align="center">

<a href="https://dev-resume-sigma.vercel.app"><img src="https://img.shields.io/badge/Dev--Resume-visit-6e40c9?style=for-the-badge" alt="Dev Resume"/></a>
<a href="mailto:Umejr.Dzinovic@edu.fh-joanneum.at"><img src="https://img.shields.io/badge/Email-contact-2ea043?style=for-the-badge" alt="Email"/></a>

</div>

---

## 🔍 Dives

---

<table>
<tr>
<td width="30%" valign="top">
  <a href="https://github.com/Umex10/authkit">
    <img src="./assets/mobile/authkit.jpg" width="100%" alt="AuthKit on mobile — the dashboard right after sign-up"/>
  </a>
</td>
<td width="70%" valign="top">

### 🔐 AuthKit — Drop-in Authentication Microservice

A reusable, **production-style auth system** packaged as a monorepo: one **Spring Boot** backend and **two interchangeable frontends** — a **Next.js** web app and a **React Native (Expo)** mobile app — that both speak to the same API.

The security layer is fully **stateless JWT**: a short-lived **access token** (15 min) plus a long-lived **refresh token** (30 days) kept in an **HTTP-only cookie** on web and in the **device keystore** on mobile. Role-based authorization (`USER` / `ADMIN`) via `@PreAuthorize`, a protected `GET /me` route, and a live **Swagger UI**.

Both clients use **Redux Toolkit Query** with silent token refresh and route guards. One `docker compose up` brings up Postgres + backend, and it ships with tests everywhere.

`Java 21` `S-Boot` `Spring Security` `JWT` `PostgreSQL` `Next.js` `React 19` `React Native` `Expo` `RTK Query` `Docker`

</td>
</tr>
</table>

---

<table>
<tr>
<td width="30%" valign="top">
  <a href="https://github.com/Umex10/chatex">
    <img src="./assets/mobile/chatex.jpg" width="100%" alt="Chatex on mobile — the feed with shouts, likes and reshouts"/>
  </a>
</td>
<td width="70%" valign="top">

### 💬 Chatex — Social Website

A social website with a full auth system. The **S-Boot-Security** `Security-Chain` is fully stateless — CSRF disabled, CORS locked to the frontend origin.

Every request runs through a custom `JwtAuthentication` (`OncePerRequest`) that pulls the Bearer token from the `Authorization` header, validates it via **JWT**, and sets the `SecurityContextHolder` — giving every downstream controller direct access to the authenticated user. Token strategy: short-lived **access token** (15 min) + long-lived **refresh token** (30 days, HttpOnly cookie).

Users post **Shouts** with likes, reshouts, quotes and comments, follow each other, chat over **WebSocket**, and manage their accounts (avatar, banner, bio, location).

`Next.js` `TS` `S-Boot` `S-Boot-Security` `JWT` `P-SQL` `Redux` `WebSocket` `Shadcn/ui` `Docker`

</td>
</tr>
</table>

---

<table>
<tr>
<td width="30%" valign="top">
  <a href="https://github.com/Umex10/dsa-exercises-website">
    <img src="./assets/mobile/dsa.jpg" width="100%" alt="DSA Solutions on mobile — the issue overview"/>
  </a>
</td>
<td width="70%" valign="top">

### 🧩 LeetCode & DSA Exercises — Issue Solving

A dedicated website where I thoroughly document my solved **LeetCode** issues and **Data Structures & Algorithms** exercises.

Every solution is coded in **Java** and comes with an in-depth explanation of the underlying logic, accompanied by a precise **Time and Memory Complexity** analysis. The site pulls the solutions, notes and code straight from the exercises repo through the **GitHub API**, and features a robust **filtering system** to search and sort issues by difficulty.

`Java` `Next.js` `Algorithms` `DSA` `Time/Space Complexity` `GitHub API` `Tailwind`

</td>
</tr>
</table>

---

<table>
<tr>
<td width="30%" valign="top">
  <a href="https://github.com/Umex10/renderex">
    <img src="./assets/mobile/renderex.jpg" width="100%" alt="Renderex on mobile — the landing page"/>
  </a>
</td>
<td width="70%" valign="top">

### 📝 Renderex — AI-Driven Note-Taking

Modern note-taking where markdown meets AI. **Firebase** handles the entire backend — auth, database, protected routes, user-scoped data — all without running a server.

**Google Gemini** is wired in for context-aware content generation. Export to PDF, DOCX, Markdown or plain text, full tag system, dark/light theme with **Framer Motion** animations.

`Next.js` `TS` `Firebase` `Redux` `Gemini AI` `Framer Motion` `Tailwind`

</td>
</tr>
</table>

---

<table>
<tr>
<td width="30%" valign="top">
  <a href="https://dev-resume-sigma.vercel.app">
    <img src="./assets/mobile/dev-resume.jpg" width="100%" alt="Dev Resume on mobile — the hero section"/>
  </a>
</td>
<td width="70%" valign="top">

### 👤 Dev-Resume — Portfolio & CV

My developer resume as a single-page site: intro, availability, apps, skills and a working contact form that sends mail through **Resend**.

Built with **Next.js 16** and **React 19**, animated with **Framer Motion**, charts via **Recharts**, form validation with **Zod** + `react-hook-form`. Live at **[dev-resume-sigma.vercel.app](https://dev-resume-sigma.vercel.app)**.

`Next.js` `React 19` `TS` `Framer Motion` `Recharts` `Resend` `Zod` `Tailwind`

</td>
</tr>
</table>

---

### 🚕 Smart-Kassa — Taxi Register System with Live Track

A **Team-built (in SCRUM) software** — a full register system for the taxi industry. I built and designed the entire UI and was fully responsible for the route system — **Leaflet** for the interactive map, **live GPS tracking** during rides, turn-by-turn navigation to the destination. The **All Rides** view lists every recorded trip with sorting and animated entries. I also built the **Summary** page, the **Dashboard** with analytics, and the **Settings** — everything the driver actually interacts with every shift.

`React` `TS` `Leaflet` `Redux` `Tailwind` `Shadcn/ui` `Framer Motion` `Node.js` `Express` `PostgreSQL`

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=java,ts,js,react,nextjs,spring,tailwind,redux,firebase,postgres,docker,git&perline=6" alt="Tech Stack"/>

</div>

---

<div align="center">
<sub>Built by hand. No shortcuts.</sub>
</div>
