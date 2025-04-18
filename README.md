# EasyEDA to KiCad GUI

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[English](#english) | [日本語](#japanese)

<img src="https://github.com/user-attachments/assets/229c6a50-8848-4ca5-b0e7-d62c87626300"
     width="800"
     alt="画像">

<a name="english"></a>
## 🇬🇧 English

A simple GUI for the [easyeda2kicad](https://github.com/uPesy/easyeda2kicad.py) converter tool. This application provides a user-friendly interface to convert EasyEDA components to KiCad format.

### Features

- Convert EasyEDA components to KiCad format using LCSC ID
- Choose what to convert (Symbol, Footprint, 3D model)
- Set output directory
- Various conversion options
- Save settings between sessions (including conversion options)
- Automatic installation of easyeda2kicad if needed
- LCSC ID validation to prevent empty submissions
- Easy to use interface
- Log window with selectable text

### Download and Use

1. Go to the [Releases page](https://github.com/YOUR_USERNAME/easyeda2kicad_gui/releases)
2. Download the latest `easyeda2kicad_gui.exe` file
3. Run the executable

The application will automatically check if easyeda2kicad is installed and offer to install it if needed.

### For Developers

If you want to modify or contribute to this project:

1. Clone this repository:

```bash
git clone https://github.com/HSBL-ko-gyo/easyeda2kicad_gui
cd easyeda2kicad_gui
```

2. Install the required dependencies:

```bash
pip install easyeda2kicad
```

### Building the Executable

If you want to build the executable yourself:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run the build script:

```bash
python build_exe.py
```

3. The executable will be created in the `dist` directory

#### Detailed Build Process

The build process automates the following steps:

- Verifies that required packages (PyInstaller and easyeda2kicad) are installed
- Creates a single-file executable with the `--onefile` option
- Uses the `--windowed` option to avoid displaying a console window
- Includes license and documentation files in the executable
- Generates the output file in the `dist` folder

The created executable is standalone and does not require Python or any dependencies to be installed on the target computer.

If you need to customize the build, you can edit the `build_exe.py` script:

```python
# PyInstallerのオプション
pyinstaller_options = [
    "pyinstaller",
    "--name=easyeda2kicad_gui",  # 出力ファイル名
    "--windowed",                # GUIアプリケーション用
    "--onefile",                 # 単一の実行ファイルに
    "--add-data=LICENSE;.",      # ライセンスファイルを含める
    "--add-data=README.md;.",    # READMEを含める
    "easyeda2kicad_gui.py"       # メインのPythonファイル
]
```

### Usage

1. Enter the LCSC ID of the component you want to convert
2. Select what you want to convert (Symbol, Footprint, 3D model or all)
3. Choose an output directory
4. Select additional options if needed
5. Click "Convert" to start the conversion process
6. View the results in the log window

Settings including your conversion options and output folder will be automatically saved between sessions.

### Requirements

- For end users: Windows operating system
- For developers:
  - Python 3.6 or later
  - easyeda2kicad
  - tkinter (usually included with Python)

---

<a name="japanese"></a>
## 🇯🇵 日本語

[easyeda2kicad](https://github.com/uPesy/easyeda2kicad.py)変換ツール用のシンプルなGUIアプリケーションです。このアプリケーションは、EasyEDAの部品をKiCad形式に変換するための使いやすいインターフェースを提供します。

### 機能

- LCSC IDを使用してEasyEDAの部品をKiCad形式に変換
- 変換対象を選択（シンボル、フットプリント、3Dモデル）
- 出力ディレクトリの設定
- 様々な変換オプション
- セッション間の設定保存（変換オプションを含む）
- 必要に応じてeasyeda2kicadを自動インストール
- 空のLCSC ID入力に対する検証機能
- 使いやすいインターフェース
- 選択可能なテキストを含むログウィンドウ

### ダウンロードと使用方法

1. [リリースページ](https://github.com/HSBL-ko-gyo/easyeda2kicad_gui/releases)にアクセス
2. 最新の`easyeda2kicad_gui.exe`ファイルをダウンロード
3. 実行ファイルを実行

アプリケーションは自動的にeasyeda2kicadがインストールされているか確認し、必要に応じてインストールするオプションを提供します。

### 開発者向け情報

このプロジェクトを修正または貢献したい場合：

1. リポジトリをクローン：

```bash
git clone https://github.com/HSBL-ko-gyo/easyeda2kicad_gui
cd easyeda2kicad_gui
```

2. 必要な依存関係をインストール：

```bash
pip install easyeda2kicad
```

### 実行ファイルのビルド方法

実行ファイルを自分でビルドする場合：

1. PyInstallerをインストール：

```bash
pip install pyinstaller
```

2. ビルドスクリプトを実行：

```bash
python build_exe.py
```

3. 実行ファイルは`dist`ディレクトリに作成されます

#### ビルドプロセスの詳細

ビルドプロセスは以下のステップを自動化します：

- 必要なパッケージ（PyInstallerとeasyeda2kicad）がインストールされているか確認
- `--onefile`オプションを使用して単一ファイルの実行ファイルを作成
- `--windowed`オプションを使用してコンソールウィンドウを表示しないようにする
- ライセンスとドキュメントファイルを実行ファイルに含める
- 出力ファイルを`dist`フォルダに生成

作成された実行ファイルはスタンドアロンで、ターゲットコンピュータにPythonや依存関係をインストールする必要はありません。

ビルドをカスタマイズする必要がある場合は、`build_exe.py`スクリプトを編集できます：

```python
# PyInstallerのオプション
pyinstaller_options = [
    "pyinstaller",
    "--name=easyeda2kicad_gui",  # 出力ファイル名
    "--windowed",                # GUIアプリケーション用
    "--onefile",                 # 単一の実行ファイルに
    "--add-data=LICENSE;.",      # ライセンスファイルを含める
    "--add-data=README.md;.",    # READMEを含める
    "easyeda2kicad_gui.py"       # メインのPythonファイル
]
```

### 使い方

1. 変換したいコンポーネントのLCSC IDを入力
2. 変換したい項目を選択（シンボル、フットプリント、3Dモデル、または全て）
3. 出力ディレクトリを選択
4. 必要に応じて追加オプションを選択
5. 「変換」ボタンをクリックして変換処理を開始
6. ログウィンドウで結果を確認

変換オプションや出力フォルダなどの設定は、セッション間で自動的に保存されます。

### 必要条件

- エンドユーザー向け：Windowsオペレーティングシステム
- 開発者向け：
  - Python 3.6以降
  - easyeda2kicad
  - tkinter（通常、Pythonに含まれています）

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

This software includes the [easyeda2kicad](https://github.com/uPesy/easyeda2kicad) tool which is also licensed under the AGPL-3.0 license. 
