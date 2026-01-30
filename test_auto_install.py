#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
easyeda2kicad自動インストール機能のテストスクリプト
"""

import importlib.util
import sys

def is_easyeda2kicad_installed():
    """修正後のチェック関数"""
    return importlib.util.find_spec("easyeda2kicad") is not None

if __name__ == "__main__":
    print("=" * 60)
    print("easyeda2kicad 自動インストール機能のテスト")
    print("=" * 60)
    
    # 現在の状態を確認
    installed = is_easyeda2kicad_installed()
    print(f"\neasyeda2kicadのインストール状況: {'インストール済み' if installed else '未インストール'}")
    
    if installed:
        print("\n⚠️  easyeda2kicadが既にインストールされています。")
        print("自動インストール機能をテストするには、一時的にアンインストールする必要があります。")
        print("\n以下のコマンドでアンインストールできます:")
        print("  pip uninstall easyeda2kicad -y")
        print("\nその後、GUIアプリを起動して自動インストールをテストしてください。")
        print("テスト後、再度インストールする場合:")
        print("  pip install easyeda2kicad")
    else:
        print("\n✅ easyeda2kicadは未インストールです。")
        print("GUIアプリを起動すると、自動インストールのダイアログが表示されるはずです。")
        print("\n次のステップ:")
        print("1. python easyeda2kicad_gui.py を実行")
        print("2. 自動インストールの確認ダイアログが表示されることを確認")
        print("3. 'はい'を選択してインストールが正常に完了することを確認")
    
    print("\n" + "=" * 60)
