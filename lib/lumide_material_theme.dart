import 'package:lumide_api/lumide_api.dart';

/// Community Material Theme plugin for the Lumide IDE.
///
/// Contributes Material Theme variants via
/// `plugin.yaml` -> `contributes.themes`. No runtime work is needed —
/// the IDE loads the JSON theme assets automatically.
class MaterialThemePlugin extends LumidePlugin {
  @override
  Future<void> onActivate(LumideContext context) async {
    // Themes are registered via plugin.yaml contributes.themes.
    // No runtime work required — the IDE loads assets/themes/*.json.
  }
}
