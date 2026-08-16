#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import webbrowser

APP = "RASTA USB MAP FOUNTAIN"
VERSION = "v0.2.1 TEST"
HERE = Path(__file__).resolve().parent
SERVER = HERE / "Map_Fountain_Server.py"
PORT = 8443

BG = "#f3f5f7"
TEXT = "#17233a"
MUTED = "#5f6b7a"
ACCENT = "#d6a300"
GOOD = "#176b3a"
BLUE = "#1756A9"

def python_executable():
    exe = Path(sys.executable)
    if exe.name.lower() in {"pythonw.exe", "pythonw"}:
        p = exe.with_name("python.exe" if exe.suffix.lower() == ".exe" else "python")
        if p.exists():
            return str(p)
    return str(exe)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP} {VERSION}")
        self.geometry("980x650")
        self.minsize(900, 600)
        self.configure(bg=BG)

        self.mbtiles_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Choose an MBTiles file.")
        self.url_var = tk.StringVar(value="")
        self.proc = None
        self.reader_thread = None
        self.log_lines = []

        self._build_ui()
        self.protocol("WM_DELETE_WINDOW", self._close)

    def _build_ui(self):
        header = tk.Frame(self, bg=BG)
        header.pack(fill="x", padx=24, pady=(18,8))
        tk.Label(header, text="RASTA USB MAP FOUNTAIN",
                 font=("Segoe UI", 24, "bold"), fg=TEXT, bg=BG).pack(side="left")
        tk.Label(header, text="MBTILES • HTTPS • USB • ARCGIS EARTH MOBILE",
                 font=("Segoe UI", 10, "bold"), fg=MUTED, bg=BG).pack(side="right", pady=10)

        body = tk.Frame(self, bg=BG)
        body.pack(fill="both", expand=True, padx=24, pady=4)

        choose = ttk.LabelFrame(body, text="1. Choose MBTiles map")
        choose.pack(fill="x", pady=8)
        row = tk.Frame(choose, bg=BG)
        row.pack(fill="x", padx=14, pady=14)
        ttk.Entry(row, textvariable=self.mbtiles_var).pack(side="left", fill="x", expand=True, padx=(0,10))
        ttk.Button(row, text="CHOOSE MBTILES", command=self.choose_mbtiles).pack(side="right")

        controls = ttk.LabelFrame(body, text="2. Serve map to Android over USB tether")
        controls.pack(fill="x", pady=8)
        r2 = tk.Frame(controls, bg=BG)
        r2.pack(fill="x", padx=14, pady=14)

        self.start_btn = tk.Button(
            r2, text="START HTTPS MAP FOUNTAIN", command=self.start_server,
            bg=ACCENT, fg=TEXT, font=("Segoe UI", 12, "bold"),
            padx=18, pady=10, relief="flat"
        )
        self.start_btn.pack(side="left")

        self.stop_btn = ttk.Button(r2, text="STOP SERVER", command=self.stop_server, state="disabled")
        self.stop_btn.pack(side="left", padx=12)

        self.qr_btn = ttk.Button(r2, text="OPEN QR", command=self.open_qr, state="disabled")
        self.qr_btn.pack(side="left", padx=0)

        status = ttk.LabelFrame(body, text="3. Live status")
        status.pack(fill="x", pady=8)
        tk.Label(status, textvariable=self.status_var, anchor="w", justify="left",
                 bg=BG, fg=BLUE, font=("Segoe UI", 10, "bold")).pack(fill="x", padx=14, pady=(12,4))
        tk.Label(status, textvariable=self.url_var, anchor="w", justify="left",
                 bg=BG, fg=GOOD, font=("Consolas", 10)).pack(fill="x", padx=14, pady=(0,12))

        logbox = ttk.LabelFrame(body, text="Server activity")
        logbox.pack(fill="both", expand=True, pady=8)
        self.log = tk.Text(logbox, height=16, wrap="none", bg="#101214", fg="#e8e8e8",
                           insertbackground="white", font=("Consolas", 9))
        self.log.pack(fill="both", expand=True, padx=8, pady=8)
        self.log.configure(state="disabled")

        foot = tk.Frame(body, bg=BG)
        foot.pack(fill="x", pady=(2,0))
        tk.Label(foot, text="No Internet required • HTTPS port 8443 • ArcGIS Earth Mobile WMTS",
                 bg=BG, fg=MUTED).pack(side="right")

    def choose_mbtiles(self):
        p = filedialog.askopenfilename(
            title="Choose raster MBTiles",
            filetypes=[("MBTiles", "*.mbtiles"), ("All files", "*.*")]
        )
        if not p:
            return
        self.mbtiles_var.set(p)
        self.status_var.set(f"SELECTED: {Path(p).name} — ready to start Map Fountain.")
        self.url_var.set("")

    def _append_log(self, text):
        self.log.configure(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def start_server(self):
        if self.proc and self.proc.poll() is None:
            return
        mb = Path(self.mbtiles_var.get().strip())
        if not mb.is_file():
            messagebox.showerror(APP, "Choose a valid .mbtiles file first.")
            return

        # Clear old generated live URL/QR so we don't show stale data.
        for name in ("CURRENT_WMTS_URL.txt", "CURRENT_PHONE_TEST_URL.txt",
                     "CURRENT_WMTS_QR.svg", "CURRENT_WMTS_QR.html"):
            try:
                (HERE / name).unlink()
            except FileNotFoundError:
                pass

        cmd = [python_executable(), "-u", str(SERVER), str(mb), "--port", str(PORT)]
        flags = 0
        si = None
        if os.name == "nt":
            flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = 0

        try:
            self.proc = subprocess.Popen(
                cmd,
                cwd=str(HERE),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                bufsize=1,
                creationflags=flags,
                startupinfo=si,
            )
        except Exception as exc:
            messagebox.showerror(APP, str(exc))
            return

        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.qr_btn.config(state="disabled")
        self.status_var.set("STARTING HTTPS MAP FOUNTAIN...")
        self.url_var.set("")
        self._append_log("")
        self._append_log(f"START {mb}")

        self.reader_thread = threading.Thread(target=self._read_output, daemon=True)
        self.reader_thread.start()
        self.after(250, self._poll_state)

    def _read_output(self):
        assert self.proc and self.proc.stdout
        for raw in iter(self.proc.stdout.readline, ""):
            line = raw.rstrip("\r\n")
            self.after(0, self._append_log, line)

    def _poll_state(self):
        if not self.proc:
            return

        if self.proc.poll() is not None:
            code = self.proc.returncode
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")
            if code == 0:
                self.status_var.set("Server stopped.")
            else:
                self.status_var.set(f"SERVER FAILED — exit code {code}. See activity log.")
            return

        url_file = HERE / "CURRENT_WMTS_URL.txt"
        if url_file.is_file():
            try:
                url = url_file.read_text(encoding="utf-8").strip()
            except Exception:
                url = ""
            if url:
                self.url_var.set(url)
                self.status_var.set("LIVE — HTTPS WMTS serving selected MBTiles over USB tether.")
                self.qr_btn.config(state="normal")

        self.after(500, self._poll_state)

    def stop_server(self):
        if not self.proc or self.proc.poll() is not None:
            return
        try:
            if os.name == "nt":
                subprocess.run(
                    ["taskkill", "/PID", str(self.proc.pid), "/T", "/F"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                    timeout=10,
                )
            else:
                self.proc.terminate()
        except Exception:
            try:
                self.proc.kill()
            except Exception:
                pass
        self.status_var.set("Stopping server...")

    def open_qr(self):
        page = HERE / "CURRENT_WMTS_QR.html"
        if not page.is_file():
            messagebox.showerror(APP, "QR has not been generated yet.")
            return
        os.startfile(str(page)) if os.name == "nt" else webbrowser.open(page.as_uri())

    def _close(self):
        if self.proc and self.proc.poll() is None:
            self.stop_server()
            time.sleep(0.2)
        self.destroy()

if __name__ == "__main__":
    App().mainloop()
