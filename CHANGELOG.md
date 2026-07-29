## 0.1.1

- Remove `resolution: workspace` so the package installs cleanly from pub.dev / Lumide Marketplace
- Depend on `lumide_api: ^1.8.0`

## 0.1.0

- Initial Lumide Community Material Theme plugin
- 10 color theme variants (Default, Darker, Palenight, Ocean, Lighter + High Contrast)
- Themes use Lumide-native JSON format under `assets/themes/` (aligned with [lumide_vscode_themes](https://github.com/SoFluffyOS/lumide_vscode_themes))
- Fixed semantic token colors to match VS Code Material Theme (purple keywords, blue functions, coral variables)
- Separated Lumide pane (`ui.neutral6`) and window (`ui.neutral7`) backgrounds from editor/sideBar colors
