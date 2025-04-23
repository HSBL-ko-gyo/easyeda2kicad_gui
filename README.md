# EasyEDA to KiCad GUI

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[English](#english) | [日本語](#japanese)

<img src="https://github.com/user-attachments/assets/229c6a50-8848-4ca5-b0e7-d62c87626300"
     width="800"
     alt="画像">

---

<a name="english"></a>
## 🇬🇧 English

A simple and friendly GUI for the [easyeda2kicad](https://github.com/uPesy/easyeda2kicad.py) tool.  
This app lets you easily convert EasyEDA components to KiCad format.

### ✨ Features

- Convert parts using LCSC ID
- Choose what to convert: symbol, footprint, or 3D model
- Set your output folder
- Tweak various conversion settings
- Remembers your settings between sessions
- Installs `easyeda2kicad` automatically if needed
- LCSC ID validation
- Easy-to-use interface
- Log window with selectable text

### 📦 Download & Use

1. Go to the [Releases page](https://github.com/YOUR_USERNAME/easyeda2kicad_gui/releases)
2. Download the latest `easyeda2kicad_gui.exe`
3. Run the executable – the app helps you install what’s needed

### 🛠 For Developers

```bash
git clone https://github.com/HSBL-ko-gyo/easyeda2kicad_gui
cd easyeda2kicad_gui
pip install easyeda2kicad
```

### 🏗 Build the Executable

```bash
pip install pyinstaller
python build_exe.py
```

Output will be in `dist/`.

#### Custom Build Options

```python
pyinstaller_options = [
    "pyinstaller",
    "--name=easyeda2kicad_gui",
    "--windowed",
    "--onefile",
    "--add-data=LICENSE;.",
    "--add-data=README.md;.",
    "easyeda2kicad_gui.py"
]
```

---

### 🚀 How to Use

1. Enter LCSC ID  
2. Choose what to convert  
3. Set output folder  
4. Optional: configure settings  
5. Click "Convert"  
6. Check the log

---

### 🧰 Requirements

- Users: Windows OS  
- Developers: Python 3.6+, `easyeda2kicad`, `tkinter`

---

<a name="japanese"></a>
## 🇯🇵 日本語

[easyeda2kicad](https://github.com/uPesy/easyeda2kicad.py) をGUIでサクッと使えるツールです。

### ✨ 主な機能

- LCSC IDで部品を変換
- シンボル、フットプリント、3Dモデルを選んで変換
- 出力先の指定
- 変換オプションの設定
- 設定を自動保存
- 必要なら easyeda2kicad を自動インストール
- 空のLCSC IDをチェック
- わかりやすい画面
- ログウィンドウあり（コピペ可）

---

### 📦 ダウンロード＆使い方

1. [リリースページ](https://github.com/HSBL-ko-gyo/easyeda2kicad_gui/releases)へ  
2. 最新の `easyeda2kicad_gui.exe` をDL  
3. 実行するだけ！

---

### 🛠 開発者向け

```bash
git clone https://github.com/HSBL-ko-gyo/easyeda2kicad_gui
cd easyeda2kicad_gui
pip install easyeda2kicad
```

---

### 🏗 EXEの作り方

```bash
pip install pyinstaller
python build_exe.py
```

出力先は `dist/`。

#### ビルドオプション例

```python
pyinstaller_options = [
    "pyinstaller",
    "--name=easyeda2kicad_gui",
    "--windowed",
    "--onefile",
    "--add-data=LICENSE;.",
    "--add-data=README.md;.",
    "easyeda2kicad_gui.py"
]
```

---

### 🚀 使い方

1. LCSC IDを入力  
2. 変換内容を選択  
3. 出力先を指定  
4. 必要があればオプション設定  
5. 「変換」をクリック  
6. ログで確認！

---

### 🧰 必要な環境

- ユーザー向け：Windows  
- 開発者向け：Python 3.6以上、easyeda2kicad、tkinter

---

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

```
