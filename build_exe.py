#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EasyEDA to KiCad GUI - Executable builder

Copyright (C) 2024

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys
import subprocess

def build_exe():
    """easyeda2kicad GUIの実行形式（.exe）を作成する"""
    print("easyeda2kicad GUIの実行形式を作成しています...")
    
    # 必要なパッケージがインストールされているか確認
    packages = ["pyinstaller", "easyeda2kicad"]
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package}がインストールされていません。インストールします...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    # PyInstallerのオプション
    pyinstaller_options = [
        "pyinstaller",
        "--name=easyeda2kicad_gui",
        "--windowed",  # GUIアプリケーション用
        "--onefile",   # 単一の実行ファイルに
        "easyeda2kicad_gui.py"  # メインのPythonファイル
    ]
    
    # ファイルが存在するか確認し、必要に応じてオプションを削除
    if os.path.exists("LICENSE"):
        pyinstaller_options.insert(4, "--add-data=LICENSE;.")  # ライセンスファイルを含める
    
    # PyInstallerを実行
    subprocess.call(pyinstaller_options)
    
    print("ビルドが完了しました。")
    print("実行ファイルは dist/easyeda2kicad_gui.exe にあります。")

if __name__ == "__main__":
    build_exe() 