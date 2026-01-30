#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EasyEDA to KiCad GUI - A graphical user interface for the easyeda2kicad converter

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

import subprocess, sys, pathlib
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk, messagebox, font
import json
import os
import ctypes
import webbrowser
import importlib.util
import pkg_resources

# DPI認識を有効にする（Windows用）
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# 設定ファイルのパス
CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".easyeda2kicad_config.json")

# GitHubリポジトリのURL
GITHUB_URL = "https://github.com/HSBL-ko-gyo/easyeda2kicad_gui"

# easyeda2kicadがインストールされているかを正確に確認する
def is_easyeda2kicad_installed():
    return importlib.util.find_spec("easyeda2kicad") is not None

# 依存パッケージのインストール
def install_dependency():
    try:
        log_text.insert(tk.END, "easyeda2kicadをインストールしています...\n")
        log_text.see(tk.END)
        root.update()  # UIを更新
        
        proc = subprocess.Popen(
            [sys.executable, "-m", "pip", "install", "easyeda2kicad"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        for line in proc.stdout:
            log_text.insert(tk.END, line)
            log_text.see(tk.END)
            root.update()
        
        proc.wait()
        
        if proc.returncode == 0:
            log_text.insert(tk.END, "easyeda2kicadのインストールが完了しました。\n")
            log_text.see(tk.END)
            return True
        else:
            log_text.insert(tk.END, "インストール中にエラーが発生しました。\n")
            log_text.see(tk.END)
            messagebox.showerror(
                "インストールエラー", 
                "easyeda2kicadのインストール中にエラーが発生しました。\n"
                "手動でインストールしてください: pip install easyeda2kicad"
            )
            return False
    except Exception as e:
        messagebox.showerror(
            "インストールエラー", 
            f"easyeda2kicadのインストール中にエラーが発生しました: {e}\n"
            "手動でインストールしてください: pip install easyeda2kicad"
        )
        return False

# 依存パッケージのチェックとインストール
def check_dependencies():
    if is_easyeda2kicad_installed():
        return True
        
    result = messagebox.askyesno(
        "依存パッケージが見つかりません", 
        "easyeda2kicadパッケージがインストールされていません。\n"
        "自動的にインストールしますか？"
    )
    
    if result:
        return install_dependency()
    else:
        messagebox.showinfo(
            "情報", 
            "easyeda2kicadがインストールされていないため、変換機能は動作しません。\n"
            "手動でインストールしてください: pip install easyeda2kicad"
        )
        return False

# 設定を読み込む
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

# 設定を保存する
def save_config():
    config = {
        'output_folder': entry_out.get(),
        'conversion_options': {
            'symbol': sym_var.get(),
            'footprint': foot_var.get(), 
            '3d': three_d_var.get(),
            'full': full_var.get()
        },
        'options': {
            'overwrite': over_var.get(),
            'v5': v5_var.get(),
            'project_relative': proj_var.get(),
            'debug': dbg_var.get()
        }
    }
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"設定の保存に失敗しました: {e}")

def run_converter():
    # LCSC IDが空かチェック
    lcsc_id = entry_id.get().strip()
    if not lcsc_id:
        messagebox.showwarning("入力エラー", "LCSC IDを入力してください。")
        return
        
    # easyeda2kicadがインストールされているか確認
    if not is_easyeda2kicad_installed():
        if not check_dependencies():
            return
    
    cmd = [sys.executable, "-m", "easyeda2kicad",
           f"--lcsc_id={lcsc_id}"]
    
    if full_var.get():
        cmd.append("--full")
    else:
        if sym_var.get():    cmd.append("--symbol")
        if foot_var.get():   cmd.append("--footprint")
        if three_d_var.get(): cmd.append("--3d")
    
    out_path = entry_out.get()
    if out_path:
        cmd += ["--output", out_path]
    
    if over_var.get():   cmd.append("--overwrite")
    if v5_var.get():     cmd.append("--v5")
    if proj_var.get():   cmd.append("--project-relative")
    if dbg_var.get():    cmd.append("--debug")

    log_text.delete(1.0, tk.END)  # ログをクリア
    
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            text=True)
    
    def read_output():
        line = proc.stdout.readline()
        if line:
            log_text.insert(tk.END, line.rstrip() + "\n")
            log_text.see(tk.END)  # 自動スクロール
            root.after(10, read_output)
        else:
            proc.wait()
            log_text.insert(tk.END, f"Exit code {proc.returncode}\n")
            log_text.see(tk.END)
    
    root.after(10, read_output)

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        entry_out.delete(0, tk.END)
        entry_out.insert(0, folder)

def show_help():
    help_text = """
各オプションの説明:

■ 変換オプション:
  Symbol（シンボル）: 回路図記号を変換します
  Footprint（フットプリント）: 基板上のパターンを変換します
  3D（3Dモデル）: 3Dモデルを変換します
  Full (all)（すべて）: 上記すべてを変換します

■ 出力オプション:
  Output folder（出力フォルダ）: 変換したファイルの保存先

■ 追加オプション:
  Overwrite（上書き）: 既存のファイルを上書きします
  KiCad v5 format（KiCad v5形式）: KiCad バージョン5の形式で出力します
  Project-relative path（プロジェクト相対パス）: プロジェクトからの相対パスを使用します
  Debug（デバッグ）: 詳細なデバッグ情報を表示します

■ 操作方法:
  1. LCSC IDを入力します
  2. 変換したい内容にチェックを入れます
  3. 出力フォルダを選択します
  4. 必要なオプションを選択します
  5. Convertボタンをクリックして変換を開始します
    """
    messagebox.showinfo("ヘルプ", help_text)

def open_github():
    webbrowser.open(GITHUB_URL)

def on_closing():
    save_config()
    root.destroy()

# メインウィンドウの作成
root = tk.Tk()
root.title("easyeda2kicad GUI")
root.protocol("WM_DELETE_WINDOW", on_closing)  # 終了時に設定を保存

# フォントサイズを調整
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=10)
font.nametofont("TkTextFont").configure(size=10)
font.nametofont("TkFixedFont").configure(size=10)

# フレームの作成
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# LCSC ID 入力部分のフレーム
id_frame = ttk.Frame(frame)
id_frame.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=5)

ttk.Label(id_frame, text="LCSC ID").grid(row=0, column=0, sticky=tk.W)
entry_id = ttk.Entry(id_frame, width=15)
entry_id.grid(row=0, column=1, sticky=tk.W, padx=5)
ttk.Label(id_frame, text="EasyEDAの部品ID").grid(row=0, column=2, sticky=tk.W)

# チェックボックス変数
sym_var = tk.BooleanVar()
foot_var = tk.BooleanVar()
three_d_var = tk.BooleanVar()
full_var = tk.BooleanVar()
over_var = tk.BooleanVar()
v5_var = tk.BooleanVar()
proj_var = tk.BooleanVar()
dbg_var = tk.BooleanVar()

# オプションチェックボックス
ttk.Label(frame, text="変換オプション:").grid(row=1, column=0, sticky=tk.W, pady=5)
check_frame = ttk.Frame(frame)
check_frame.grid(row=2, column=0, columnspan=3, sticky=tk.W, pady=5)

sym_check = ttk.Checkbutton(check_frame, text="Symbol（シンボル）", variable=sym_var)
sym_check.grid(row=0, column=0, padx=5)

foot_check = ttk.Checkbutton(check_frame, text="Footprint（フットプリント）", variable=foot_var)
foot_check.grid(row=0, column=1, padx=5)

three_d_check = ttk.Checkbutton(check_frame, text="3D（3Dモデル）", variable=three_d_var)
three_d_check.grid(row=0, column=2, padx=5)

full_check = ttk.Checkbutton(check_frame, text="Full (all)（すべて）", variable=full_var)
full_check.grid(row=0, column=3, padx=5)

# 出力フォルダ
ttk.Label(frame, text="出力フォルダ:").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_out = ttk.Entry(frame, width=50)
entry_out.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
ttk.Button(frame, text="参照", command=browse_folder).grid(row=3, column=2, sticky=tk.W, pady=5, padx=5)

# 追加オプション
ttk.Label(frame, text="追加オプション:").grid(row=4, column=0, sticky=tk.W, pady=5)
option_frame = ttk.Frame(frame)
option_frame.grid(row=5, column=0, columnspan=3, sticky=tk.W, pady=5)

over_check = ttk.Checkbutton(option_frame, text="Overwrite（上書き）", variable=over_var)
over_check.grid(row=0, column=0, padx=5)

v5_check = ttk.Checkbutton(option_frame, text="KiCad v5 format（KiCad v5形式）", variable=v5_var)
v5_check.grid(row=0, column=1, padx=5)

proj_check = ttk.Checkbutton(option_frame, text="Project‑relative path（プロジェクト相対パス）", variable=proj_var)
proj_check.grid(row=0, column=2, padx=5)

dbg_check = ttk.Checkbutton(option_frame, text="Debug（デバッグ）", variable=dbg_var)
dbg_check.grid(row=0, column=3, padx=5)

# ボタン
button_frame = ttk.Frame(frame)
button_frame.grid(row=6, column=0, columnspan=3, pady=10)

ttk.Button(button_frame, text="変換", command=run_converter).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="ヘルプ", command=show_help).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="終了", command=on_closing).grid(row=0, column=2, padx=5)

# ログ表示エリア
log_frame = ttk.LabelFrame(frame, text="log")
log_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

# ログテキストウィジェットの設定を修正
log_text = scrolledtext.ScrolledText(log_frame, width=80, height=15, wrap=tk.WORD, font="TkFixedFont")
log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
log_text.config(state=tk.NORMAL)  # 確実に編集可能状態に設定

# フッターフレーム
footer_frame = ttk.Frame(frame)
footer_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

# GitHubリンク - ボタンに変更
github_button = ttk.Button(footer_frame, text="GitHub", width=10, command=open_github, style="Link.TButton")
github_button.grid(row=0, column=0, sticky=tk.W)

# リンクスタイルのボタンを作成
style = ttk.Style()
style.configure("Link.TButton", foreground="blue", background=root.cget('background'), font=('TkDefaultFont', 10))
style.map("Link.TButton", 
          foreground=[('active', 'dark blue')],
          background=[('active', root.cget('background'))])

# ウィンドウリサイズ対応
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(7, weight=1)
log_frame.columnconfigure(0, weight=1)
log_frame.rowconfigure(0, weight=1)

# 設定を読み込む
config = load_config()
if config:
    if 'output_folder' in config:
        entry_out.insert(0, config['output_folder'])
    
    # 変換オプションの読み込み
    if 'conversion_options' in config:
        conv_options = config['conversion_options']
        if 'symbol' in conv_options:
            sym_var.set(conv_options['symbol'])
        if 'footprint' in conv_options:
            foot_var.set(conv_options['footprint'])
        if '3d' in conv_options:
            three_d_var.set(conv_options['3d'])
        if 'full' in conv_options:
            full_var.set(conv_options['full'])
    
    # その他のオプションの読み込み
    if 'options' in config:
        options = config['options']
        if 'overwrite' in options:
            over_var.set(options['overwrite'])
        if 'v5' in options:
            v5_var.set(options['v5'])
        if 'project_relative' in options:
            proj_var.set(options['project_relative'])
        if 'debug' in options:
            dbg_var.set(options['debug'])

# メインループ開始
root.mainloop()
