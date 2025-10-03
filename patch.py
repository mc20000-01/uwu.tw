import os
import glob
import shutil

# Set the repo directory here
REPO_DIR = 'mistwarp'

build_dir = os.path.join(REPO_DIR, 'build')

for path in glob.glob(os.path.join(build_dir, '*.html')):
    print(f'Patching HTML {path}')
    with open(path, 'r') as f:
        contents = f.read()
        contents = contents.replace('</head>', '<meta name="robots" content="noindex"></head>')
        contents = contents.replace('<link rel="manifest" href="manifest.webmanifest">', '')
    with open(path, 'w') as f:
        f.write(contents)

for path in glob.glob(os.path.join(build_dir, '**', '*.js'), recursive=True):
    print(f'Patching JS {path}')
    with open(path, 'r') as f:
        contents = f.read()
        contents = contents.replace('https://trampoline.turbowarp.org', 'https://trampoline.turbowarp.xyz')
    with open(path, 'w') as f:
        f.write(contents)

# Remove specific files
for filename in ['sw.js', 'manifest.webmanifest', 'fullscreen.html', 'index.html']:
    os.remove(os.path.join(build_dir, filename))

# Copy files
shutil.copy(os.path.join(build_dir, 'editor.html'), os.path.join(build_dir, 'index.html'))
shutil.copy('robots.txt', os.path.join(build_dir, 'robots.txt'))