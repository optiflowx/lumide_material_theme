# lumide_material_theme

Community Material Theme color schemes for [Lumide](https://lumide.dev/) IDE.

Modeled after [lumide_vscode_themes](https://github.com/SoFluffyOS/lumide_vscode_themes): themes are declared in `plugin.yaml` and loaded from `assets/themes/` in Lumide’s native theme format.

## Themes

| Theme | uiTheme |
| --- | --- |
| Community Material Theme | dark |
| Community Material Theme High Contrast | high-contrast |
| Community Material Theme Darker | dark |
| Community Material Theme Darker High Contrast | high-contrast |
| Community Material Theme Palenight | dark |
| Community Material Theme Palenight High Contrast | high-contrast |
| Community Material Theme Ocean | dark |
| Community Material Theme Ocean High Contrast | high-contrast |
| Community Material Theme Lighter | light |
| Community Material Theme Lighter High Contrast | high-contrast |

## Load in Lumide

1. Open Lumide → **Plugins** pane
2. **Load Local Plugin**
3. Select this package directory (`packages/lumide_material_theme`)
4. Open the color theme picker and choose a Community Material Theme variant

## Notes

- Theme JSON uses Lumide’s format (`colors` + semantic `tokenColors` map), converted from Material Theme palettes.
- Upstream [Community Material Theme](https://github.com/myambitions/vsc-community-material-theme) stores encrypted VS Code theme blobs; plaintext palette sources come from [Safe Material Theme](https://github.com/k-i-o/vsc-safe-material-theme).

## License

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
