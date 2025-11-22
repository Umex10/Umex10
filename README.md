<!-- KRANKES README MIT ANIMATIONEN -->

<p align="center">
  <!-- Titel mit Animation -->
  <svg fill="none" width="100%" xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
      <div xmlns="http://www.w3.org/1999/xhtml">
        <style>
          .wrapper { height: 20vh; display: grid; place-items: center; }
          .text {
            width: 6ch;
            animation: typing 2s steps(6), blink .5s step-end infinite alternate, rainbow 5s infinite;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid;
            font-family: monospace;
            font-size: 5em;
            background: linear-gradient(90deg, #00f1dc, #5673f1, #6744f1, #fe00ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }
          @keyframes typing { from { width: 0 } }
          @keyframes blink { from, to { border-color: transparent } 50% { border-color: #fe00ff; } }
          @keyframes rainbow {
            0% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(180deg); }
            100% { filter: hue-rotate(360deg); }
          }
        </style>
        <div class="wrapper">
          <div class="text">umex10</div>
        </div>
      </div>
    </foreignObject>
  </svg>
</p>

---

## ⚡ Willkommen bei meinem kranken Account ⚡

<p align="center">
  <!-- Glitch Effekt -->
  <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
    <foreignObject width="100%" height="100%">
      <div xmlns="http://www.w3.org/1999/xhtml">
        <style>
          .glitch {
            font-size: 3em;
            font-family: monospace;
            position: relative;
            color: #fff;
            animation: flicker 1.5s infinite alternate;
          }
          .glitch::before, .glitch::after {
            content: attr(data-text);
            position: absolute;
            left: 0;
          }
          .glitch::before {
            animation: glitchTop 1s infinite linear alternate-reverse;
            color: #0ff;
            clip: rect(0, 900px, 0, 0);
          }
          .glitch::after {
            animation: glitchBottom 1s infinite linear alternate-reverse;
            color: #f0f;
            clip: rect(0, 900px, 0, 0);
          }
          @keyframes glitchTop {
            0% { clip: rect(0, 9999px, 0, 0); }
            50% { clip: rect(0, 9999px, 9999px, 0); transform: translate(-5px, -5px); }
            100% { clip: rect(0, 9999px, 0, 0); }
          }
          @keyframes glitchBottom {
            0% { clip: rect(0, 9999px, 0, 0); }
            50% { clip: rect(0, 9999px, 9999px, 0); transform: translate(5px, 5px); }
            100% { clip: rect(0, 9999px, 0, 0); }
          }
          @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.3; }
            100% { opacity: 1; }
          }
        </style>
        <div class="glitch" data-text="CodeFlow.">CodeFlow.</div>
      </div>
    </foreignObject>
  </svg>
</p>

---

## 🚀 Animationen überall

- 🌈 **Regenbogen-Schrift** mit Hue-Rotation  
- ⚡ **Glitch-Effekt** für Hacker-Vibes  
- 🔥 **Typing-Animation** wie ein Terminal  
- 💥 **Blinkende Cursor** für Retro-Style  

---

<p align="center">
  <!-- Rotierendes Logo -->
  <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
    <foreignObject width="100%" height="100%">
      <div xmlns="http://www.w3.org/1999/xhtml">
        <style>
          .spin {
            font-size: 2em;
            font-family: monospace;
            animation: spin 5s linear infinite;
            background: linear-gradient(90deg, #ff0000, #00ff00, #0000ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }
          @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
          }
        </style>
        <div class="spin">🔥 umex10 🔥</div>
      </div>
    </foreignObject>
  </svg>
</p>
