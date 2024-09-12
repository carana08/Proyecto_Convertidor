# youtube_downloader.spec
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['youtube.py'],
    pathex=['.'],
    binaries=[('bin/yt-dlp.exe', 'bin/yt-dlp.exe')],
    datas=[('youtube_black.png', '.'), ('Música', '.'), ('Videos', '.')],
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