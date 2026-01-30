# v0.0.3 - Bug Fixes

## 🐛 バグ修正

### easyeda2kicad 自動インストール機能の改善
- **依存関係チェックの強化**: `pkg_resources` から `importlib.util.find_spec` に変更し、パッケージ検出の信頼性を大幅に向上しました
- **Windows環境での実行問題を解決**: `easyeda2kicad` を `python -m easyeda2kicad` 経由で実行するように変更し、PATH設定に依存しない確実な動作を実現しました

### ログ表示の改善
- **インデント崩れを修正**: ログウィンドウのフォントを等幅フォント (`TkFixedFont`) に変更し、部品情報や表形式のデータが正しく揃って表示されるようになりました

## 📥 ダウンロード

`easyeda2kicad_gui.exe` をダウンロードして実行してください。
初回起動時に必要な依存パッケージが自動的にインストールされます。

## 🙏 謝辞

Issue報告およびバグ報告をしていただいた皆様に感謝いたします。

---

# v0.0.3 - Bug Fixes (English)

## 🐛 Bug Fixes

### Improved easyeda2kicad Auto-Installation
- **Enhanced dependency check**: Replaced `pkg_resources` with `importlib.util.find_spec` for significantly more reliable package detection
- **Resolved Windows execution issues**: Changed to run `easyeda2kicad` via `python -m easyeda2kicad`, ensuring reliable operation without PATH dependency

### Improved Log Display
- **Fixed indentation issues**: Changed log window font to monospaced font (`TkFixedFont`), ensuring parts information and tabular data are properly aligned

## 📥 Download

Download and run `easyeda2kicad_gui.exe`.
Required dependencies will be automatically installed on first launch.

## 🙏 Acknowledgments

Thanks to everyone who reported issues and bugs.
