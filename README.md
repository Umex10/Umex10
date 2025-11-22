<!-- README.md - animiertes Profil -->

<!--
  Hinweis: GitHub rendert Inline-SVG gut, CSS-Keyframes im SVG selbst funktionieren,
  manche externe CSS-Eigenschaften können auf GitHub variieren.
-->

<!-- HERO: großer animierter SVG-Header -->
<div align="center">

<!-- Umex10 hero SVG: aus deinem Ausgangs-SVG erweitert -->
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1200 380" preserveAspectRatio="xMidYMid meet">
  <defs>
    <!-- farbverlauf -->
    <linearGradient id="g1" x1="0" x2="1">
      <stop offset="0" stop-color="#00F1DC"/>
      <stop offset="0.44" stop-color="#5673F1"/>
      <stop offset="0.54" stop-color="#6744F1"/>
      <stop offset="1" stop-color="#FE00FF"/>
    </linearGradient>

    <!-- noise für glitch -->
    <filter id="glitch">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="6" xChannelSelector="R" yChannelSelector="G"/>
    </filter>

    <!-- blur für trailing -->
    <filter id="trail" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- mask für wipe-in -->
    <mask id="wipe">
      <rect x="0" y="0" width="1200" height="380" fill="black"/>
      <rect id="maskRect" x="-400" y="0" width="400" height="380" fill="white">
        <animate attributeName="x" from="-400" to="1200" dur="1s" begin="0.1s" fill="freeze" />
      </rect>
    </mask>

    <!-- particle circle shape -->
    <circle id="pt" r="4" fill="#fff" />
  </defs>

  <!-- background animated radial waves -->
  <rect width="1200" height="380" fill="#050014"/>
  <g opacity="0.12">
    <circle cx="300" cy="190" r="180" fill="url(#g1)">
      <animate attributeName="r" values="120;200;120" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.12;0.22;0.12" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="900" cy="120" r="140" fill="#FF6FD8">
      <animate attributeName="r" values="100;180;100" dur="10s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.08;0.18;0.08" dur="10s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- particle swarm -->
  <g id="particles" fill="#fff" opacity="0.9">
    <use href="#pt" x="100" y="40">
      <animate attributeName="cx" values="100;1100" dur="12s" repeatCount="indefinite" />
      <animate attributeName="cy" values="40;200" dur="8s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;1;0" dur="12s" repeatCount="indefinite" />
    </use>
    <use href="#pt" x="200" y="300" fill="#FE00FF">
      <animate attributeName="cx" values="200;1000" dur="14s" repeatCount="indefinite" />
      <animate attributeName="cy" values="300;60" dur="9s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;1;0" dur="14s" repeatCount="indefinite" />
    </use>
    <use href="#pt" x="600" y="10" fill="#00F1DC">
      <animate attributeName="cx" values="600;400;800" dur="10s" repeatCount="indefinite" />
      <animate attributeName="cy" values="10;220;60" dur="10s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;1;0" dur="10s" repeatCount="indefinite" />
    </use>
  </g>

  <!-- Umex10 eintretender Text mit typing/wipe -->
  <g mask="url(#wipe)">
    <text id="title" x="50%" y="45%" text-anchor="middle"
          font-family="monospace, sans-serif" font-size="72"
          font-weight="700" fill="url(#g1)" style="letter-spacing:2px;">
      umex10
    </text>
  </g>

  <!-- Glitch copy overlays -->
  <g filter="url(#glitch)" opacity="0.9">
    <text x="50%" y="45%" text-anchor="middle"
          font-family="monospace, sans-serif" font-size="72" font-weight="700" fill="#fff" opacity="0.06">
      umex10
    </text>
  </g>

  <!-- Neon trailing -->
  <text x="50%" y="45%" text-anchor="middle"
        font-family="monospace, sans-serif" font-size="72" font-weight="700" fill="none" stroke="url(#g1)" stroke-width="2" opacity="0.9" filter="url(#trail)">
    umex10
  </text>

  <!-- Slogan mit typing cursor animation (SVG-only) -->
  <g transform="translate(0,120)">
    <text id="slogan" x="50%" y="60%" text-anchor="middle" font-family="monospace" font-size="26" fill="#cbd5ff">
      <tspan id="s1">CodeFlow. Build. Ship. Repeat.</tspan>
    </text>
    <rect x="640" y="160" width="8" height="22" fill="#FE00FF" opacity="1">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
    </rect>
  </g>

  <!-- bottom animated bar (wave) -->
  <path d="M0 320 C300 280 900 360 1200 320 L1200 380 L0 380 Z" fill="url(#g1)" opacity="0.14">
    <animate attributeName="d" dur="6s" repeatCount="indefinite"
      values="
        M0 320 C300 280 900 360 1200 320 L1200 380 L0 380 Z;
        M0 330 C300 300 900 340 1200 330 L1200 380 L0 380 Z;
        M0 320 C300 280 900 360 1200 320 L1200 380 L0 380 Z" />
  </path>

  <!-- subtle footer text -->
  <text x="50%" y="360" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#9aa0ff" opacity="0.6">
    Welcome — this profile is animated with pure SVG and intent.
  </text>
</svg>

</div>

---

### Über mich

- **Name:** umex10  
- **Kurz:** Kreativer Entwickler, der auf visuelle Ideen und sauberen Code setzt.  
- **Style:** Experimental UI, WebGL/SVG-Spielereien, performant animierte Interfaces.

---

### Skills

- **Frontend:** HTML, CSS, SVG Animationen, JavaScript, WebGL  
- **Tools:** React, Vue, Vite, Three.js, D3  
- **DevOps:** Docker, CI/CD, GitHub Actions

---

### Projekte (Auswahl)

1. **CodeFlow** — Animiertes UI-Kit (SVG-first), Live-Demos und Komponenten  
2. **NeonLab** — Experimentelle Shader- und Partikelsysteme  
3. **DevOps-Stack** — Pipeline-Templates, IaC-Playbooks

---

### Features dieser README

- Große, animierte SVG-Hero-Grafik mit:
  - wipe-in Typing-Effekt für "umex10"
  - SMIL-Animationen für Partikel, Pulsationen, Wellen
  - feTurbulence-Glitch, Blur-Trail, animateMotion / animate-Attribute
- Kein externes JS nötig — alles im SVG oder Markdown
- Mobile-angepasst dank viewBox / preserveAspectRatio

---

### Pro-Tipps zum Einbauen

- Für beste Ergebnisse: GitHub rendert dieses Inline-SVG im README. Wenn du Probleme siehst, lade die SVG als separate Datei (z. B. hero.svg) in dein Repo und verlinke sie so:
  - ![Hero](./hero.svg)
- Du kannst Farben, Schriftgrößen und Text im SVG direkt anpassen. SMIL-Animationen sind leicht zu timen via dur und begin.

---

### Kontakt

- **GitHub:** https://github.com/umex10  
- **E-Mail:** in deinem Profil hinterlegen

---

Viel Erfolg — wenn du willst, kann ich dir die SVG in weitere Varianten aufsplitten (dunkel/hell, reduzierte Performance) oder die README um dynamische Shields und Live-Stats erweitern.
