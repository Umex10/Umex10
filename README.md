<a href="https://dev-resume-v2.vercel.app">
  <img src="./assets/v2/hero.svg" width="100%" alt="Umejr Džinović — Backender, Frontender, Full-Stacker, CI/CDer, Tester, and one day a Señior"/>
</a>

<p align="center">
  <a href="https://dev-resume-v2.vercel.app"><b>dev-resume-v2.vercel.app</b></a>
  &nbsp;·&nbsp;
  <a href="mailto:umi.dzinovic10@gmail.com">umi.dzinovic10@gmail.com</a>
</p>

Next.js and Spring Boot developer, studying software engineering at FH JOANNEUM. I build Spring Boot APIs with stateless JWT auth and the Next.js apps on top — containerised with Docker, shipped through CI/CD. Currently writing my bachelor thesis and learning Kubernetes, gRPC and microservices.

<br/>

`02 / shell`

## Ask the terminal.

<img src="./assets/v2/terminal.svg" width="100%" alt="A zsh terminal running neofetch for umex10"/>

The real one lives on [my site](https://dev-resume-v2.vercel.app/#shell) — try `help`, `open authkit`, `accent orange` or `sudo hire-me`.

<br/>

`03 / work`

## Selected work.

> **● currently building — Overex** · project work + bachelor thesis
>
> Flash-sale ticketing on Kubernetes. Thousands of buyers, one last ticket — the platform has to stay up and must never sell it twice. Spring Boot microservices, gRPC between services, RS256 JWTs from my AuthKit.
>
> **Thesis:** strategies against overselling at 1 / 3 / 5 / 10 replicas — **ticket lock system** · Redis reservation · queue with Kafka.
>
> `Java 21` `Spring Boot` `Microservices` `gRPC` `Kubernetes` `Docker` `PostgreSQL` `Redis` `Kafka`

<table>
<tr>
<td width="26%" valign="top">
  <a href="https://github.com/Umex10/authkit">
    <img src="./assets/phone/authkit.jpg" width="100%" alt="AuthKit on mobile"/>
  </a>
</td>
<td width="74%" valign="top">

### AuthKit — authentication microservice

**[github.com/Umex10/authkit](https://github.com/Umex10/authkit)**

A drop-in auth microservice — one **Spring Boot** API, two interchangeable clients: a **Next.js** web app and a **React Native (Expo)** app that speak to the same backend.

Fully **stateless JWT**: a short-lived access token plus a long-lived refresh token, kept in an HTTP-only cookie on the web and in the device keystore on mobile. Role-based access with `@PreAuthorize`, a protected `GET /me` and a live **Swagger UI**. One `docker compose up` brings up Postgres and the backend; tested with JUnit 5, MockMvc, Vitest and Playwright.

`Java 21` `Spring Boot 4` `Spring Security` `JWT` `PostgreSQL` `Next.js 16` `React Native` `RTK Query` `Docker`

</td>
</tr>
</table>

<table>
<tr>
<td width="26%" valign="top">
  <a href="https://github.com/Umex10/chatex">
    <img src="./assets/phone/chatex.jpg" width="100%" alt="Chatex on mobile — the feed with shouts, likes and reshouts"/>
  </a>
</td>
<td width="74%" valign="top">

### Chatex — social website

**[github.com/Umex10/chatex](https://github.com/Umex10/chatex)**

Shouts, reshouts and real-time chat on a fully stateless security chain. Every request runs through a custom `JwtAuthenticationFilter` that validates the Bearer token and fills the `SecurityContextHolder` — CSRF off, CORS locked to the frontend origin.

Users post **Shouts** with likes, reshouts, quotes and comments, follow each other, chat over **WebSocket** and manage their profiles.

`Next.js` `TypeScript` `Spring Boot` `Spring Security` `JWT` `PostgreSQL` `Redux` `WebSocket` `shadcn/ui` `Docker`

</td>
</tr>
</table>

<table>
<tr>
<td width="26%" valign="top">
  <a href="https://github.com/Umex10/renderex">
    <img src="./assets/phone/renderex.jpg" width="100%" alt="Renderex on mobile — the landing page"/>
  </a>
</td>
<td width="74%" valign="top">

### Renderex — AI note-taking

**[github.com/Umex10/renderex](https://github.com/Umex10/renderex)**

Modern note-taking where markdown meets AI. **Firebase** carries the backend — auth, database and user-scoped data without running a server — and **Gemini** writes along with you. Export to PDF, DOCX, Markdown or plain text, tags, dark and light theme.

`Next.js` `TypeScript` `Firebase` `Redux` `Gemini AI` `Framer Motion` `Tailwind`

</td>
</tr>
</table>

<table>
<tr>
<td width="26%" valign="top">
  <a href="https://github.com/Umex10/dsa-exercises-website">
    <img src="./assets/phone/dsa.jpg" width="100%" alt="DSA Solutions on mobile — the issue overview"/>
  </a>
</td>
<td width="74%" valign="top">

### DSA Solutions — LeetCode & algorithms

**[github.com/Umex10/dsa-exercises-website](https://github.com/Umex10/dsa-exercises-website)** · **[exercises repo](https://github.com/Umex10/dsa-exercises)**

Solved **LeetCode** issues and data-structures exercises, each in **Java** with an explanation of the idea and its **time and space complexity**. The site pulls solutions and notes straight from the exercises repo through the **GitHub API**, with filters by difficulty.

`Java` `Next.js` `Algorithms` `DSA` `GitHub API` `Tailwind`

</td>
</tr>
</table>

<table>
<tr>
<td width="26%" valign="top">
  <a href="https://dev-resume-v2.vercel.app">
    <img src="./assets/phone/dev-resume-v2.jpg" width="100%" alt="Dev-Resume v2 on mobile — the intro"/>
  </a>
</td>
<td width="74%" valign="top">

### Dev-Resume v2 — this portfolio

**[dev-resume-v2.vercel.app](https://dev-resume-v2.vercel.app)** · **[github.com/Umex10/dev-resume-v2](https://github.com/Umex10/dev-resume-v2)**

A zsh terminal you can actually type into, project deep dives with real source code from the repos, a live GitHub contribution skyline in three.js and the pipeline below. Built on **Next.js 16** with Cache Components and intercepting routes; tested with Vitest and Playwright on desktop and mobile.

`Next.js 16` `React 19` `TypeScript` `Tailwind 4` `shadcn/ui` `React Three Fiber` `Shiki` `Playwright` `Vercel`

</td>
</tr>
</table>

<br/>

`05 / ship`

## Commit to container.

<img src="./assets/v2/pipeline.svg" width="100%" alt="CI pipeline: push, test, build, docker, publish, deploy — passed"/>

- **docker** — multi-stage images for every service; one `docker compose up` brings up Postgres, the backend and Swagger.
- **ci/cd** — GitHub Actions: test → build → image → deploy. Railway for the Spring Boot side, Vercel for Next.js.
- **testing** — JUnit 5, MockMvc and Spring Security Test on the backend; Vitest, Testing Library and Playwright on the web.

<br/>

`06 / stack`

## The toolbox.

| | |
| --- | --- |
| **Strengths** | Spring Boot · Next.js · JWT (HS256 / RS256) · Spring Security |
| **Languages** | Java · TypeScript · JavaScript · SQL · HTML/CSS · YAML |
| **Backend** | REST · WebSocket · JPA · Swagger · PostgreSQL · Firebase |
| **Frontend** | React 19 · Server Actions · proxy / middleware · instrumentation · Tailwind · shadcn/ui · RTK Query |
| **Mobile** | React Native · Expo |
| **Testing** | JUnit 5 · MockMvc · Vitest · Testing Library · Playwright |
| **Ship** | Docker · Docker Compose · GitHub Actions · CI/CD · Railway · Vercel · Git |
| **Learning** | Kubernetes · gRPC · Microservices · Redis · Kafka |

<br/>

`07 / contact`

## Let's talk.

Got a role, a project, or a bug that needs squashing? **[umi.dzinovic10@gmail.com](mailto:umi.dzinovic10@gmail.com)** · **[dev-resume-v2.vercel.app](https://dev-resume-v2.vercel.app)**

<sub>Built by hand. No shortcuts. One day a Señior.</sub>
