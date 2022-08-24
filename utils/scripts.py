from re import A
from .loading import LoadingSpinner
from .utils import getBanners, getContent, formatProjectName
import subprocess


def createDesktopProject(clientName: str) -> None:
    banners = getBanners()
    content = getContent()
    client  = formatProjectName(clientName)
    
    with LoadingSpinner(desc=banners['dependencies_for_desktop'], end=banners['OK']):
        subprocess.run([f"""

cd {client}
npm install electron dotenv --save &> /dev/null
cd ../
touch {client}/main.js
echo "{content['main']}" >> {client}/main.js
touch {client}/.env
echo "{content['env']}" >> {client}/.env
sed -i '' 's/  "private": true,/  "private": true,\\n\\t"homepage": ".\/",\\n\\t"main": "main.js",/' ./{client}/package.json
sed -i '' 's/  "scripts": {'{'}/  "scripts": {'{'}\\n\\t  "desk": "ELECTRON_DISABLE_SECURITY_WARNINGS=true electron .",\\n\\t  "desk:prod": "react-scripts build \&\& electron .",/' ./{client}/package.json

        """], shell=True)


def createClientProject(clientName: str, isDesktopApp=False) -> None:
    banners = getBanners()
    content = getContent()
    client  = formatProjectName(clientName)
    srcDir  = f'{client}/src'

    with LoadingSpinner(desc=banners['new_project'], end=banners['OK']):
        subprocess.run([f"""

npx create-react-app {client} &> /dev/null
cd {client}
npm install -D tailwindcss postcss autoprefixer &> /dev/null
npx tailwindcss init -p &> /dev/null

        """], shell=True)

    print(banners['file_structure'], end=' ')
    subprocess.run([f"""

rm -f {srcDir}/App.css
rm -f {srcDir}/App.js
rm -f {srcDir}/App.test.js
rm -f {srcDir}/index.css
rm -f {srcDir}/index.js
rm -f {srcDir}/logo.svg
rm -f {srcDir}/reportWebVitals.js
rm -f {srcDir}/setupTests.js
touch {srcDir}/index.js
echo "{content['index']}" >> {srcDir}/index.js
touch {client}/jsconfig.json
echo "{'{'}" >> {client}/jsconfig.json
sed -i '' 's/{'{'}/{'{'}"compilerOptions": {'{'}"baseUrl": "src", "paths": {'{'}"*": ["src\/*"]{'}}}'}/' ./{client}/jsconfig.json
    """], shell=True)
    print(banners['OK'])

    print(banners['creating_assets'], end=' ')
    subprocess.run([f"""

mkdir {srcDir}/assets
mkdir {srcDir}/assets/styles
touch {srcDir}/assets/styles/index.css
touch {srcDir}/assets/styles/layout.css
rm -f {client}/tailwind.config.js
touch {client}/tailwind.config.js
echo "{content['tailwind_config']}" >> {client}/tailwind.config.js
echo "{content['index_css']}" >> {srcDir}/assets/styles/index.css

    """], shell=True)
    print(banners['OK'])

    print(banners['creating_components'], end=' ')
    subprocess.run([f"mkdir {srcDir}/components && touch {srcDir}/components/.keep"], shell=True)
    print(banners['OK'])

    print(banners['creating_hooks'], end=' ')
    subprocess.run([f"mkdir {srcDir}/hooks && touch {srcDir}/hooks/.keep"], shell=True)
    print(banners['OK'])

    print(banners['creating_helpers'], end=' ')
    subprocess.run([f"mkdir {srcDir}/helpers && touch {srcDir}/helpers/.keep"], shell=True)
    print(banners['OK'])

    print(banners['creating_views'], end=' ')
    subprocess.run([f"""

mkdir {srcDir}/views
mkdir {srcDir}/views/modals && touch {srcDir}/views/modals/.keep   
mkdir {srcDir}/views/pages && touch {srcDir}/views/pages/.keep
touch {srcDir}/views/app.js
echo "{content['app']}" >> {srcDir}/views/app.js

    """], shell=True)
    print(banners['OK'])

    if isDesktopApp:
        createDesktopProject(clientName=client)

    print(banners['git_project'], end=' ')
    subprocess.run([f"""

cd {client}
# pwd
# sudo rm -d -r .git
git init --initial-branch=develop &> /dev/null

"""], shell=True)
    print(banners['OK'])

