# youtube_downloader.spec
# -*- mode: python ; coding: utf-8 -*-
import os
import glob

block_cipher = None

project_dir = os.getcwd()
pillow_dir = os.path.join(project_dir, 'venv', 'Lib', 'site-packages', 'PIL')

# Recopilar todos los archivos de Pillow
pillow_files = glob.glob(os.path.join(pillow_dir, '**', '*.*'), recursive=True)
pillow_binaries = [(file, os.path.join('PIL', os.path.relpath(file, pillow_dir))) for file in pillow_files]

a = Analysis(
    ['youtube.py'],
    pathex=[project_dir],
    binaries=pillow_binaries,
    datas=[
        (os.path.join(project_dir, 'youtube_black.png'), '.'),
        (os.path.join(project_dir, 'bin', 'yt-dlp.exe'), 'bin'),
        (os.path.join(project_dir, 'bin', 'ffmpeg.exe'), 'bin')
    ],
    hiddenimports=['PIL', 'PIL.Image', 'PIL.ImageTk', 'PIL._imaging'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='youtube_downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='youtube_downloader',
)