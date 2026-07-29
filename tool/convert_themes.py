#!/usr/bin/env python3
"""Convert VS Code Material Theme JSON into Lumide theme format."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DST = ROOT / "assets" / "themes"
BASE = (
    "https://raw.githubusercontent.com/k-i-o/vsc-safe-material-theme/"
    "master/dist/themes"
)

THEMES = [
    ("Material-Theme-Default.json", "default.json", "Community Material Theme", "dark"),
    (
        "Material-Theme-Default-High-Contrast.json",
        "default-hc.json",
        "Community Material Theme High Contrast",
        "dark",
    ),
    ("Material-Theme-Darker.json", "darker.json", "Community Material Theme Darker", "dark"),
    (
        "Material-Theme-Darker-High-Contrast.json",
        "darker-hc.json",
        "Community Material Theme Darker High Contrast",
        "dark",
    ),
    (
        "Material-Theme-Palenight.json",
        "palenight.json",
        "Community Material Theme Palenight",
        "dark",
    ),
    (
        "Material-Theme-Palenight-High-Contrast.json",
        "palenight-hc.json",
        "Community Material Theme Palenight High Contrast",
        "dark",
    ),
    ("Material-Theme-Ocean.json", "ocean.json", "Community Material Theme Ocean", "dark"),
    (
        "Material-Theme-Ocean-High-Contrast.json",
        "ocean-hc.json",
        "Community Material Theme Ocean High Contrast",
        "dark",
    ),
    ("Material-Theme-Lighter.json", "lighter.json", "Community Material Theme Lighter", "light"),
    (
        "Material-Theme-Lighter-High-Contrast.json",
        "lighter-hc.json",
        "Community Material Theme Lighter High Contrast",
        "light",
    ),
]

DARK_TOKENS = {
    "keyword": "#C792EA",
    "string": "#C3E88D",
    "number": "#F78C6C",
    "type": "#FFCB6B",
    "class": "#FFCB6B",
    "enum": "#FFCB6B",
    "interface": "#FFCB6B",
    "struct": "#FFCB6B",
    "annotation": "#FFCB6B",
    "function": "#82AAFF",
    "variable": "#f07178",
    "property": "#f07178",
    "regexp": "#89DDFF",
    "constant": "#89DDFF",
    "readonlyProperty": "#89DDFF",
}

LIGHT_TOKENS = {
    "keyword": "#9C3EDA",
    "string": "#91B859",
    "number": "#F76D47",
    "type": "#E2931D",
    "class": "#E2931D",
    "enum": "#E2931D",
    "interface": "#E2931D",
    "struct": "#E2931D",
    "annotation": "#E2931D",
    "function": "#6182B8",
    "variable": "#E53935",
    "property": "#E53935",
    "regexp": "#39ADB5",
    "constant": "#39ADB5",
    "readonlyProperty": "#39ADB5",
}


def fetch(name: str) -> dict:
    url = f"{BASE}/{name}"
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))


def color(colors: dict, *keys: str, default: str | None = None) -> str | None:
    for key in keys:
        if key in colors and colors[key]:
            return colors[key]
    return default


def find_token_fg(token_colors: list, scope_substrings: list[str]) -> str | None:
    for entry in token_colors:
        scopes = entry.get("scope")
        if scopes is None:
            continue
        if isinstance(scopes, str):
            scopes = [scopes]
        joined = " ".join(scopes)
        for needle in scope_substrings:
            if needle in joined:
                fg = entry.get("settings", {}).get("foreground")
                if fg:
                    return fg
    return None


def darken(hex_color: str, factor: float = 0.08) -> str:
    h = hex_color.lstrip("#")
    if len(h) == 8:
        h = h[:6]
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    r = max(0, int(r * (1 - factor)))
    g = max(0, int(g * (1 - factor)))
    b = max(0, int(b * (1 - factor)))
    return f"#{r:02X}{g:02X}{b:02X}"


def lighten(hex_color: str, factor: float = 0.04) -> str:
    h = hex_color.lstrip("#")
    if len(h) == 8:
        h = h[:6]
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    r = min(255, int(r + (255 - r) * factor))
    g = min(255, int(g + (255 - g) * factor))
    b = min(255, int(b + (255 - b) * factor))
    return f"#{r:02X}{g:02X}{b:02X}"


def convert(src: dict, label: str, kind: str) -> dict:
    colors = src.get("colors", {})
    token_list = src.get("tokenColors", [])

    editor_bg = color(colors, "editor.background", default="#263238")
    editor_fg = color(colors, "editor.foreground", default="#EEFFFF")
    selection = color(colors, "editor.selectionBackground", default="#80CBC420")
    cursor = color(colors, "editorCursor.foreground", default="#FFCC00")
    line_number = color(colors, "editorLineNumber.foreground", default="#465A64")
    line_number_active = color(
        colors, "editorLineNumber.activeForeground", default=line_number
    )
    line_highlight = color(colors, "editor.lineHighlightBackground", default="#00000050")
    find_match = color(colors, "editor.findMatchHighlightBackground", default="#00000050")
    bracket_border = color(colors, "editorBracketMatch.border", default="#FFCC0050")
    suggest_bg = color(colors, "editorSuggestWidget.background", default=editor_bg)
    suggest_selected = color(
        colors, "editorSuggestWidget.selectedBackground", default="#00000050"
    )
    suggest_fg = color(colors, "editorSuggestWidget.foreground", default=editor_fg)
    suggest_highlight = color(
        colors, "editorSuggestWidget.highlightForeground", default="#80CBC4"
    )
    suggest_border = color(colors, "editorSuggestWidget.border", default="#FFFFFF10")
    hover_bg = color(colors, "editorHoverWidget.background", default=editor_bg)
    hover_border = color(colors, "editorHoverWidget.border", default="#FFFFFF10")
    error_fg = color(colors, "editorError.foreground", default="#f0717870")
    warning_fg = color(colors, "editorWarning.foreground", default="#FFCB6B70")
    info_fg = color(colors, "editorInfo.foreground", default="#82AAFF70")
    panel_border = color(colors, "panel.border", "sideBar.border", default="#FFFFFF10")
    codelens = color(colors, "editorCodeLens.foreground", default=line_number)
    inserted = color(colors, "diffEditor.insertedTextBackground", default="#89DDFF20")
    removed = color(colors, "diffEditor.removedTextBackground", default="#ff9cac20")
    primary = color(colors, "activityBar.activeBorder", "focusBorder", default="#80CBC4")
    secondary = color(colors, "editorWarning.foreground", default="#FFCB6B70")

    window_bg = color(
        colors,
        "sideBar.background",
        "activityBar.background",
        "titleBar.activeBackground",
        default=editor_bg,
    )
    pane_bg = editor_bg
    if window_bg.lower() == pane_bg.lower():
        window_bg = darken(pane_bg, 0.08) if kind == "dark" else lighten(pane_bg, 0.06)

    mid_surface = color(colors, "tab.inactiveBackground", "panelTitle.activeBackground")
    if not mid_surface or mid_surface.lower() in {pane_bg.lower(), window_bg.lower()}:
        # Blend between pane and window for a mid surface.
        mid_surface = pane_bg if kind == "dark" else window_bg

    comment_fg = find_token_fg(token_list, ["comment"]) or (
        "#546E7A" if kind == "dark" else "#90A4AE"
    )

    accents = DARK_TOKENS if kind == "dark" else LIGHT_TOKENS

    token_colors = {
        **accents,
        "comment": {"foreground": comment_fg, "fontStyle": "italic"},
        "documentationComment": {"foreground": comment_fg, "fontStyle": "italic"},
        "typeParameter": editor_fg,
        "escapeSequence": editor_fg,
        "operator": editor_fg,
        "punctuation": editor_fg,
        "plain": editor_fg,
        "staticMethod": {"foreground": accents["function"], "fontStyle": "italic"},
        "staticProperty": {"foreground": accents["property"], "fontStyle": "italic"},
    }

    if kind == "dark":
        ui_neutrals = {
            "ui.neutral1": editor_fg,
            "ui.neutral2": editor_fg,
            "ui.neutral3": panel_border,
            "ui.neutral4": line_number_active or line_number,
            "ui.neutral5": mid_surface,
            "ui.neutral6": pane_bg,
            "ui.neutral7": window_bg,
        }
    else:
        # Light: neutrals 1-2 are surfaces; 4-7 are text (Modern Light style).
        secondary_pane = window_bg if window_bg.lower() != pane_bg.lower() else lighten(pane_bg, 0.0)
        # Prefer a distinct secondary surface for sidebar-like panes.
        if secondary_pane.lower() == pane_bg.lower():
            secondary_pane = darken(pane_bg, 0.03)
        muted = line_number_active or line_number
        ui_neutrals = {
            "ui.neutral1": secondary_pane,
            "ui.neutral2": pane_bg,
            "ui.neutral3": panel_border,
            "ui.neutral4": muted,
            "ui.neutral5": muted,
            "ui.neutral6": editor_fg,
            "ui.neutral7": darken(editor_fg, 0.35) if editor_fg else "#1F2328",
        }

    out_colors = {
        "editor.background": pane_bg,
        "editor.foreground": editor_fg,
        "editor.selectionBackground": selection,
        "editorCursor.foreground": cursor,
        "editorLineNumber.foreground": line_number,
        "editorLineNumber.activeForeground": line_number_active,
        "editor.lineHighlightBackground": line_highlight,
        "editor.findMatchHighlightBackground": find_match,
        "editorBracketMatch.border": bracket_border,
        "editorBracketMatch.background": pane_bg,
        "editorSuggestWidget.background": suggest_bg,
        "editorSuggestWidget.selectedBackground": suggest_selected,
        "editorSuggestWidget.foreground": suggest_fg,
        "editorSuggestWidget.highlightForeground": suggest_highlight,
        "editorSuggestWidget.border": suggest_border,
        "editorHoverWidget.background": hover_bg,
        "editorHoverWidget.border": hover_border,
        "editorError.foreground": error_fg,
        "editorWarning.foreground": warning_fg,
        "editorInfo.foreground": info_fg,
        "panel.background": pane_bg,
        "panel.border": panel_border,
        "diffEditor.insertedTextBackground": inserted,
        "diffEditor.removedTextBackground": removed,
        "editorGutter.background": pane_bg,
        "panelTitle.activeBackground": pane_bg,
        "panel.foreground": editor_fg,
        "editorCodeLens.foreground": codelens,
        "diffEditor.modifiedTextBackground": "#2090D3",
        "ui.primary": primary,
        "ui.secondary": secondary,
        **ui_neutrals,
        "symbolIcon.methodForeground": accents["function"],
        "symbolIcon.functionForeground": accents["function"],
        "symbolIcon.fieldForeground": accents["property"],
        "symbolIcon.classForeground": accents["class"],
        "symbolIcon.interfaceForeground": accents["interface"],
        "symbolIcon.moduleForeground": accents["class"],
        "symbolIcon.keywordForeground": accents["keyword"],
        "symbolIcon.snippetForeground": accents["string"],
    }

    return {
        "name": label,
        "type": kind,
        "colors": out_colors,
        "tokenColors": token_colors,
    }


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    for src_name, out_name, label, kind in THEMES:
        print(f"Converting {src_name} -> {out_name}")
        src = fetch(src_name)
        out = convert(src, label, kind)
        path = DST / out_name
        path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    main()
