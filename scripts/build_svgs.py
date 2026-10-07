"""Builds the animated profile SVGs (hero, terminal, pipeline) in the style of dev-resume v2.

    python3 scripts/build_svgs.py

Needs fonttools + brotli + Pillow. Fonts (Archivo, Martian Mono — OFL) are subset and embedded,
because GitHub renders README images without access to web fonts. Animations are SMIL.
"""

import base64
import io
import math
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT.parent / "assets" / "v2"

# ── colours: same OKLCH tokens as the site (dark theme) ──────────────────────


def oklch(L, C, H):
    a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    l_, m_, s_ = L + 0.3963377774 * a + 0.2158037573 * b, L - 0.1055613458 * a - 0.0638541728 * b, L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_**3, m_**3, s_**3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)

    def enc(x):
        x = max(0.0, min(1.0, x))
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

    return "#" + "".join(f"{round(enc(c) * 255):02x}" for c in rgb)


BG, INK, MUTE = "#08090c", "#edf0f5", "#8a92a2"
ACC, ACC2, OK = oklch(0.72, 0.16, 292), oklch(0.76, 0.16, 52), oklch(0.78, 0.15, 150)
LINE, SEG, SEG2, PANEL = "rgba(255,255,255,.09)", "rgba(255,255,255,.13)", "rgba(255,255,255,.06)", "#0e1016"

# ── fonts ─────────────────────────────────────────────────────────────────────

FONTS = {"A": TTFont(SRC / "archivo-112-800.ttf"), "M": TTFont(SRC / "martian-mono-400.ttf")}
FILES = {"A": SRC / "archivo-112-800.ttf", "M": SRC / "martian-mono-400.ttf"}


def width(text, font, size, spacing=0.0):
    f = FONTS[font]
    cmap, hmtx, upem = f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm
    return sum(hmtx[cmap[ord(c)]][0] for c in text) * size / upem + spacing * len(text)


def font_face(font, family, text):
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern"]
    s = subset.Subsetter(opts)
    f = TTFont(FILES[font])
    s.populate(text="".join(sorted(set(text))))
    s.subset(f)
    buf = io.BytesIO()
    f.flavor = "woff2"
    f.save(buf)
    data = base64.b64encode(buf.getvalue()).decode()
    return f"@font-face{{font-family:{family};src:url(data:font/woff2;base64,{data}) format('woff2')}}"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(w, h, body, texts, label):
    """Wrap a drawing; embeds only the glyphs used (texts = {'A': str, 'M': str})."""
    faces = "".join(font_face(k, k, v) for k, v in texts.items() if v)
    style = f"<style>{faces}.a{{font-family:A}}.m{{font-family:M}}</style>"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">'
        f"<title>{esc(label)}</title>{style}{body}</svg>"
    )


# ── timeline helpers (SMIL, one shared loop per file) ────────────────────────


def discrete(attr, D, points):
    """points: [(t, value)] — value holds from t until the next point. t=0 must be present."""
    pts = sorted(points)
    kt = ";".join(f"{t / D:.5f}" for t, _ in pts)
    vs = ";".join(str(v) for _, v in pts)
    return f'<animate attributeName="{attr}" dur="{D}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{kt}" values="{vs}"/>'


def show_between(D, on, off):
    pts = [(0, 0), (on, 1)] if on > 0 else [(0, 1)]
    if off < D:
        pts.append((off, 0))
    return discrete("opacity", D, pts)


def portrait_cells(cell, gap, x0, y0, factor=1.3):
    im = Image.open(SRC / "umejr-tiny.png").convert("RGB")
    out = []
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = (min(255, round(c * factor)) for c in im.getpixel((x, y)))
            out.append(f'<rect x="{x0 + x * cell:.1f}" y="{y0 + y * cell:.1f}" width="{cell - gap:.1f}" height="{cell - gap:.1f}" fill="#{r:02x}{g:02x}{b:02x}"/>')
    return "".join(out), im.width * cell, im.height * cell


# ── hero ─────────────────────────────────────────────────────────────────────

ROLES = [
    ("Backender", "// spring boot · jwt · postgres"),
    ("Frontender", "// next.js · react · shadcn"),
    ("Full-Stacker", "// api to pixel, both ends"),
    ("CI/CDer", "// docker · github actions"),
    ("Tester", "// junit · vitest · playwright"),
    ("Señior", "// one day I'm a full-stack Señior"),
]


def hero():
    W, H, PAD = 1200, 500, 56
    A, M = [], []
    body = [
        "<defs>"
        f'<radialGradient id="g1" cx="12%" cy="0%" r="60%"><stop offset="0" stop-color="{ACC}" stop-opacity=".30"/><stop offset="1" stop-color="{ACC}" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="g2" cx="100%" cy="100%" r="55%"><stop offset="0" stop-color="{ACC2}" stop-opacity=".18"/><stop offset="1" stop-color="{ACC2}" stop-opacity="0"/></radialGradient>'
        f'<clipPath id="card"><rect width="{W}" height="{H}" rx="24"/></clipPath>'
        "</defs>",
        f'<g clip-path="url(#card)"><rect width="{W}" height="{H}" fill="{BG}"/><rect width="{W}" height="{H}" fill="url(#g1)"/><rect width="{W}" height="{H}" fill="url(#g2)"/>',
    ]
    # The site's dotted wave field, flattened: rows get denser and brighter towards the viewer.
    dots = []
    for r in range(16):
        k = r / 15
        y_base, step = 250 + 210 * k**1.4, 30 - 16 * k
        x = -20.0
        while x < W + 20:
            y = y_base + (6 + 10 * k) * math.sin(x / 140 + r * 0.55)
            dots.append(f'<circle cx="{x:.0f}" cy="{y:.1f}" r="{0.7 + 0.8 * k:.2f}"/>')
            x += step
    body.append(f'<g fill="{ACC}" opacity=".32">{"".join(dots)}</g>')
    body.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="23.5" fill="none" stroke="{LINE}"/></g>')

    # top row
    top = "Based in Graz, Austria · umex10"
    M.append(top + "dev-resume v2fig.01 — portrait.jpg")
    body.append(f'<circle cx="{PAD + 3}" cy="51" r="3.5" fill="{ACC}"><animate attributeName="opacity" values="1;.35;1" dur="2s" repeatCount="indefinite"/></circle>')
    body.append(f'<text class="m" x="{PAD + 16}" y="56" font-size="13" fill="{MUTE}">{esc(top)}</text>')

    # portrait
    cell = 7
    px0, py0 = W - PAD - 36 * cell, 92
    cells, pw, ph = portrait_cells(cell, 1.2, px0, py0)
    body.append(f'<text class="m" x="{px0}" y="{py0 - 14}" font-size="11" fill="{MUTE}">fig.01 — portrait.jpg</text>')
    body.append(f'<rect x="{px0 - 6}" y="{py0 - 6}" width="{pw + 10.8}" height="{ph + 10.8}" rx="16" fill="#05070a" stroke="{LINE}"/>{cells}')

    # name
    size, ls = 108, -5.4
    for word, y in (("UMEJR", 196), ("DŽINOVIĆ", 300)):
        A.append(word)
        body.append(f'<text class="a" x="{PAD - 4}" y="{y}" font-size="{size}" letter-spacing="{ls}" fill="{INK}">{word}</text>')

    # typewriter — same rhythm as the site: 90ms/char, hold 1.8s, delete 42ms/char, 320ms gap
    tsize, tls, ty = 42, -1.2, 404
    TYPE, HOLD, DEL, GAP = 0.09, 1.8, 0.042, 0.32
    t, plan = 0.5, []
    for word, note in ROLES:
        n = len(word)
        plan.append((word, note, t))
        t += n * TYPE + HOLD + n * DEL + GAP
    D = round(t, 3)
    cursor = [(0, PAD)]
    for i, (word, note, s) in enumerate(plan):
        A.append(word)
        M.append(note)
        n = len(word)
        widths = [width(word[:k], "A", tsize, tls) for k in range(n + 1)]
        pts = [(0, 0)]
        for k in range(1, n + 1):
            pts.append((s + k * TYPE, widths[k] + 6))
            cursor.append((s + k * TYPE, PAD + widths[k] + 3))
        h = s + n * TYPE + HOLD
        for k in range(1, n + 1):
            pts.append((h + k * DEL, widths[n - k] + (6 if k < n else 0)))
            cursor.append((h + k * DEL, PAD + widths[n - k] + (3 if k < n else 0)))
        cut = n - 2  # the "-er" suffix is the joke: accent2, slanted
        head, tail = word[:cut], word[cut:]
        x_tail = PAD + width(head, "A", tsize, tls)
        body.append(
            f'<clipPath id="tw{i}"><rect x="{PAD - 2}" y="{ty - 46}" height="60" width="0">{discrete("width", D, pts)}</rect></clipPath>'
            f'<g clip-path="url(#tw{i})">'
            f'<text class="a" x="{PAD}" y="{ty}" font-size="{tsize}" letter-spacing="{tls}" fill="{ACC}">{esc(head)}</text>'
            f'<text class="a" x="{x_tail}" y="{ty}" font-size="{tsize}" letter-spacing="{tls}" fill="{ACC2}" transform="skewX(-10) translate({ty * math.tan(math.radians(10)):.1f} 0)">{esc(tail)}</text>'
            "</g>"
        )
        nx = PAD + widths[n] + 26
        body.append(f'<text class="m" x="{nx:.1f}" y="{ty - 10}" font-size="13" fill="{MUTE}" opacity="0">{esc(note)}{show_between(D, s + n * TYPE + 0.15, h)}</text>')
    body.append(
        f'<rect y="{ty - 34}" width="3" height="40" fill="{ACC}" x="{PAD}">{discrete("x", D, [(t_, f"{x:.1f}") for t_, x in cursor])}'
        '<animate attributeName="opacity" values="1;0;1" keyTimes="0;.5;1" calcMode="discrete" dur="1s" repeatCount="indefinite"/></rect>'
    )

    # bottom row
    left, right = "Spring Boot · Next.js · Docker · CI/CD", "Ø 1.20 · MSD Kapfenberg · writing my bachelor thesis"
    M.append(left + right)
    body.append(f'<line x1="{PAD}" x2="{W - PAD}" y1="440" y2="440" stroke="{LINE}"/>')
    body.append(f'<text class="m" x="{PAD}" y="468" font-size="12" fill="{MUTE}">{esc(left)}</text>')
    body.append(f'<text class="m" x="{W - PAD}" y="468" font-size="12" fill="{MUTE}" text-anchor="end">{esc(right)}</text>')

    label = "Umejr Džinović — Backender, Frontender, Full-Stacker, CI/CDer, Tester, and one day a Señior"
    return svg(W, H, "".join(body), {"A": "".join(A), "M": "".join(M)}, label)


# ── terminal ─────────────────────────────────────────────────────────────────

NEOFETCH = [
    ("OS", "Linux Mint"),
    ("Host", "Graz, Austria"),
    ("Kernel", "Software Engineering Student"),
    ("Shell", "zsh 5.9"),
    ("IDE", "VSCode"),
    ("Languages", "Java, TypeScript"),
    ("Strengths", "Next.js, Spring Boot"),
    ("Ship", "Docker, GitHub Actions"),
    ("Focus", "auth systems, JWT HS256 / RS256"),
    ("Now", "bachelor thesis — Overex"),
    ("Learning", "Kubernetes, gRPC, microservices"),
    ("Goal", "one day a Señior"),
]


def prompt(x, y, M):
    """Powerline prompt: umejr ▸ ~/dev-resume ▸ main."""
    parts, fs = [], 13
    segs = [("umejr", ACC, "#05070a"), ("~/dev-resume", SEG, INK), ("main", SEG2, ACC)]
    cx = x
    for i, (label, bg, fg) in enumerate(segs):
        M.append(label)
        w = width(label, "M", fs) + 22
        tip = cx + w
        parts.append(f'<path d="M{cx} {y - 17}h{w}l9 12l-9 12h-{w}{"" if i == 0 else "l9 -12z"}" fill="{bg}"/>')
        parts.append(f'<text class="m" x="{cx + (11 if i == 0 else 17)}" y="{y}" font-size="{fs}" fill="{fg}">{label}</text>')
        cx = tip + 3
    return "".join(parts), cx + 12


def terminal():
    W, H = 1200, 684
    D = 16.0
    A, M = [], []
    body = [
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{PANEL}" stroke="{LINE}"/>',
        f'<line x1="0" x2="{W}" y1="42" y2="42" stroke="{LINE}"/>',
        '<circle cx="24" cy="21" r="6" fill="#ff5f57"/><circle cx="44" cy="21" r="6" fill="#febc2e"/><circle cx="64" cy="21" r="6" fill="#28c840"/>',
    ]
    title = "umejr@graz — ~/dev-resume — zsh"
    M.append(title)
    body.append(f'<text class="m" x="{W / 2}" y="25" font-size="12" fill="{MUTE}" text-anchor="middle">{title}</text>')

    fs, x = 15, 28

    def line(y, spans):
        out, cx = [], x
        for t, c in spans:
            M.append(t)
            out.append(f'<text class="m" x="{cx:.1f}" y="{y}" font-size="{fs}" fill="{c}" xml:space="preserve">{esc(t)}</text>')
            cx += width(t, "M", fs)
        return "".join(out)

    body.append(line(80, [("Last login: today on ttys001", MUTE)]))
    body.append(line(106, [("Welcome to ", INK), ("umex10", ACC), (" — zsh 5.9 (x86_64-linux-mint)", INK)]))
    body.append(line(132, [("Type ", MUTE), ("help", ACC), (" to see what I can do.", MUTE)]))

    p, cmd_x = prompt(x, 178, M)
    body.append(p)
    cmd = "neofetch"
    M.append(cmd)
    t0, step = 0.8, 0.11
    pts = [(0, 0)] + [(t0 + k * step, width(cmd[:k], "M", fs) + 2) for k in range(1, len(cmd) + 1)] + [(D - 0.4, 0)]
    body.append(
        f'<clipPath id="cmd"><rect x="{cmd_x}" y="160" height="26" width="0">{discrete("width", D, pts)}</rect></clipPath>'
        f'<text class="m" x="{cmd_x}" y="178" font-size="{fs}" fill="{INK}" clip-path="url(#cmd)">{cmd}</text>'
    )
    typed_end = t0 + len(cmd) * step
    body.append(
        f'<rect y="164" width="9" height="18" fill="{ACC}" opacity=".85" x="{cmd_x}">'
        f'{discrete("x", D, [(0, cmd_x)] + [(t0 + k * step, f"{cmd_x + width(cmd[:k], 'M', fs) + 2:.1f}") for k in range(1, len(cmd) + 1)] + [(D - 0.4, cmd_x)])}'
        f"{show_between(D, 0, typed_end + 0.35)}</rect>"
    )

    # output
    out_t = typed_end + 0.35
    cells, _, _ = portrait_cells(3, 0.45, x, 206)
    body.append(f'<g opacity="0">{cells}{show_between(D, out_t, D - 0.4)}</g>')
    ix, iy = 168, 222
    M.append("umex10@graz")
    body.append(f'<g opacity="0">{show_between(D, out_t, D - 0.4)}<text class="m" x="{ix}" y="{iy}" font-size="{fs}" fill="{ACC}">umex10<tspan fill="{INK}">@</tspan>graz</text>')
    body.append(f'<line x1="{ix}" x2="{ix + 112}" y1="{iy + 12}" y2="{iy + 12}" stroke="{MUTE}"/></g>')
    for i, (k, v) in enumerate(NEOFETCH):
        y = iy + 40 + i * 26
        M.append(k + ": " + v)
        kw = width(k + ": ", "M", fs)
        body.append(
            f'<g opacity="0">{show_between(D, out_t + 0.12 + i * 0.07, D - 0.4)}'
            f'<text class="m" x="{ix}" y="{y}" font-size="{fs}" fill="{ACC}">{esc(k)}<tspan fill="{MUTE}">:</tspan></text>'
            f'<text class="m" x="{ix + kw:.1f}" y="{y}" font-size="{fs}" fill="{INK}">{esc(v)}</text></g>'
        )
    bar_y = iy + 40 + len(NEOFETCH) * 26 - 8
    swatches = "".join(f'<rect x="{ix + i * 22}" y="{bar_y}" width="20" height="12" fill="{c}"/>' for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840", ACC, ACC2, MUTE, INK]))
    body.append(f'<g opacity="0">{show_between(D, out_t + 1.0, D - 0.4)}{swatches}</g>')

    p2, cur_x = prompt(x, bar_y + 56, [])
    body.append(
        f'<g opacity="0">{show_between(D, out_t + 1.2, D - 0.4)}{p2}'
        f'<rect x="{cur_x}" y="{bar_y + 38}" width="9" height="18" fill="{ACC}"><animate attributeName="opacity" values="1;0;1" keyTimes="0;.5;1" calcMode="discrete" dur="1s" repeatCount="indefinite"/></rect></g>'
    )

    # status bar
    fy = H - 28
    body.append(f'<line x1="0" x2="{W}" y1="{fy}" y2="{fy}" stroke="{LINE}"/>')
    left, right = "zsh 5.9 · utf-8 · arrow", "violet · neofetch"
    M.append(left + right)
    body.append(f'<text class="m" x="20" y="{fy + 18}" font-size="11" fill="{MUTE}">{left}</text>')
    rw = width(right, "M", 11)
    body.append(f'<circle cx="{W - 20 - rw - 14}" cy="{fy + 14}" r="3.5" fill="{ACC}"/><text class="m" x="{W - 20}" y="{fy + 18}" font-size="11" fill="{MUTE}" text-anchor="end">{right}</text>')

    return svg(W, H, "".join(body), {"M": "".join(M)}, "Terminal: neofetch for umex10 — Linux Mint, Graz, Java and TypeScript, Next.js and Spring Boot")


# ── pipeline ─────────────────────────────────────────────────────────────────

STAGES = [
    ("push", "git push origin main", "1s"),
    ("test", "JUnit · Playwright", "58s"),
    ("build", "mvn verify · next build", "1m 12s"),
    ("docker", "multi-stage image", "36s"),
    ("publish", "push → ghcr.io", "9s"),
    ("deploy", "Railway · Vercel", "21s"),
]


def pipeline():
    W, H, D = 1200, 236, 11.0
    START, STEP, RESET = 0.8, 0.95, 10.4
    A, M = [], []
    body = [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="22" fill="{PANEL}" stroke="{LINE}"/>', f'<line x1="0" x2="{W}" y1="52" y2="52" stroke="{LINE}"/>']
    head = [("ci · ", MUTE), ("main", INK), (" · run #142 · authkit", MUTE)]
    cx = 24.0
    for t, c in head:
        M.append(t)
        body.append(f'<text class="m" x="{cx:.1f}" y="31" font-size="13" fill="{c}" xml:space="preserve">{esc(t)}</text>')
        cx += width(t, "M", 13)

    # status, swapped per stage
    states = [(0, "queued", ACC)] + [(START + i * STEP, f"running · {n}", ACC) for i, (n, _, _) in enumerate(STAGES)] + [(START + len(STAGES) * STEP, "passed · 3m 17s", OK)]
    for j, (on, text, color) in enumerate(states):
        off = states[j + 1][0] if j + 1 < len(states) else RESET
        M.append(text)
        tw = width(text, "M", 13)
        body.append(
            f'<g opacity="0">{show_between(D, on, off) if on > 0 else discrete("opacity", D, [(0, 1), (states[1][0], 0), (RESET, 1)])}'
            f'<circle cx="{W - 24 - tw - 12:.1f}" cy="27" r="3.5" fill="{color}"/>'
            f'<text class="m" x="{W - 24}" y="31" font-size="13" fill="{color}" text-anchor="end">{esc(text)}</text></g>'
        )

    col = (W - 48) / len(STAGES)
    for i, (name, sub, dur) in enumerate(STAGES):
        x0 = 24 + i * col
        run_on, done_on = START + i * STEP, START + (i + 1) * STEP
        A.append(name)
        M.append(sub + dur + "queuedrunning")
        icx, icy = x0 + 15, 92
        # connector
        lx, lw = x0 + 40, col - 52
        body.append(f'<rect x="{lx:.1f}" y="{icy - 1}" width="{lw:.1f}" height="2" fill="{SEG}"/>')
        body.append(
            f'<rect x="{lx:.1f}" y="{icy - 1}" height="2" fill="{ACC}" width="0">'
            f'<animate attributeName="width" dur="{D}s" repeatCount="indefinite" keyTimes="0;{done_on / D:.5f};{min(done_on + 0.9, RESET - 0.01) / D:.5f};{RESET / D:.5f};1" values="0;0;{lw:.1f};{lw:.1f};0" calcMode="linear"/></rect>'
        )
        # icons: waiting · running · done
        body.append(
            f'<g opacity="1">{discrete("opacity", D, [(0, 1), (run_on, 0), (RESET, 1)])}'
            f'<circle cx="{icx}" cy="{icy}" r="14" fill="none" stroke="{MUTE}" stroke-dasharray="3 3"/></g>'
        )
        body.append(
            f'<g opacity="0">{show_between(D, run_on, done_on)}'
            f'<circle cx="{icx}" cy="{icy}" r="14" fill="none" stroke="{SEG}" stroke-width="2"/>'
            f'<path d="M{icx} {icy - 14}a14 14 0 0 1 14 14" fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round">'
            f'<animateTransform attributeName="transform" type="rotate" from="0 {icx} {icy}" to="360 {icx} {icy}" dur=".8s" repeatCount="indefinite"/></path></g>'
        )
        body.append(
            f'<g opacity="0">{show_between(D, done_on, RESET)}'
            f'<circle cx="{icx}" cy="{icy}" r="15" fill="{ACC}"/>'
            f'<path d="M{icx - 6} {icy}l4 4l8 -8" fill="none" stroke="#05070a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></g>'
        )
        # text, dimmed while queued
        body.append(
            f'<g opacity=".45">{discrete("opacity", D, [(0, 0.45), (run_on, 1), (RESET, 0.45)])}'
            f'<text class="a" x="{x0}" y="146" font-size="22" letter-spacing="-.6" fill="{INK}">{name}</text>'
            f'<text class="m" x="{x0}" y="170" font-size="10.5" fill="{MUTE}">{esc(sub)}</text></g>'
        )
        for on, off, text in ((0, run_on, "queued"), (run_on, done_on, "running"), (done_on, RESET, dur)):
            anim = discrete("opacity", D, [(0, 1), (run_on, 0), (RESET, 1)]) if on == 0 else show_between(D, on, off)
            body.append(f'<text class="m" x="{x0}" y="192" font-size="11" fill="{ACC}" opacity="{1 if on == 0 else 0}">{anim}{esc(text)}</text>')

    return svg(W, H, "".join(body), {"A": "".join(A), "M": "".join(M)}, "CI pipeline: push, test, build, docker, publish, deploy — passed")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in (("hero", hero), ("terminal", terminal), ("pipeline", pipeline)):
        data = fn()
        (OUT / f"{name}.svg").write_text(data, encoding="utf-8")
        print(f"{name}.svg  {len(data) / 1024:.0f} KB")
