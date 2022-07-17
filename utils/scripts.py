from re import A
from .loading import LoadingSpinner
from .utils import getBanners, getContent, formatProjectName
import subprocess


def createDesktopProject(clientName: str) -> None:
    banners = getBanners()
    content = getContent()
    client  = formatProjectName(clientName)
    print(banners['BN6'], end=' ')
    subprocess.run([f"""
touch {client}/main.js
echo "{content['main']}" >> {client}/main.js
    """], shell=True)
    print(banners['OK']) 

    print(banners['BN7'], end=' ')
    subprocess.run([f"""
sed -i '' 's/  "private": true,/  "private": true,\\n\\t"homepage": ".\/",\\n\\t"main": "main.js",/' ./{client}/package.json
sed -i '' 's/  "scripts": {'{'}/  "scripts": {'{'}\\n\\t  "desk": "ELECTRON_DISABLE_SECURITY_WARNINGS=true electron .",\\n\\t  "desk:prod": "react-scripts build \&\& electron .",/' ./{client}/package.json
    """], shell=True)
    print(banners['OK']) 

    with LoadingSpinner(desc=banners['BN8'], end=banners['OK']):
        subprocess.run([f"""
cd {client}
npm install electron dotenv --save &> /dev/null
        """], shell=True)


def createClientProject(clientName: str, isDesktopApp=False) -> None:
    banners = getBanners()
    content = getContent()
    client  = formatProjectName(clientName)
    srcDir  = f'{client}/src'

    with LoadingSpinner(desc=banners['BN1'], end=banners['OK']):
        subprocess.run([f"""
npx create-react-app {client} &> /dev/null
cd {client}
npm install -D tailwindcss postcss autoprefixer &> /dev/null
npx tailwindcss init -p &> /dev/null
        """], shell=True)

    print(banners['BN2'], end=' ')
    subprocess.run([f"""
rm -f {srcDir}/App.css
rm -f {srcDir}/App.js
rm -f {srcDir}/App.test.js
rm -f {srcDir}/index.css
rm -f {srcDir}/index.js
rm -f {srcDir}/logo.svg
rm -f {srcDir}/reportWebVitals.js
rm -f {srcDir}/setupTests.js
    """], shell=True)
    print(banners['OK'])

    print(banners['BN3'], end=' ')
    subprocess.run([f"""
touch {srcDir}/index.js
mkdir {srcDir}/pages
mkdir {srcDir}/assets && touch {srcDir}/assets/.keep
mkdir {srcDir}/components && touch {srcDir}/components/.keep
mkdir {srcDir}/hooks && touch {srcDir}/hooks/.keep
mkdir {srcDir}/contexts && touch {srcDir}/contexts/.keeP
mkdir {srcDir}/styled-components && touch {srcDir}/styled-components/.keep
mkdir {srcDir}/services && touch {srcDir}/services/.keep
mkdir {srcDir}/utilities && touch {srcDir}/utilities/.keep
mkdir {srcDir}/pages/app
touch {srcDir}/pages/app/app.js {srcDir}/pages/app/app.css
mkdir {srcDir}/pages/app/components && touch {srcDir}/pages/app/components/.keep
mkdir {srcDir}/pages/app/assets && touch {srcDir}/pages/app/assets/.keep
mkdir {srcDir}/pages/app/hooks && touch {srcDir}/pages/app/hooks/.keep
mkdir {srcDir}/pages/app/services && touch {srcDir}/pages/app/services/.keep
mkdir {srcDir}/pages/app/utilities && touch {srcDir}/pages/app/utilities/.keep
touch {srcDir}/index.css
rm -f {client}/tailwind.config.js
touch {client}/tailwind.config.js
echo "{content['tailwind_config']}" >> {client}/tailwind.config.js
echo "{content['index_css']}" >> {srcDir}/index.css
    """], shell=True)
    print(banners['OK'])

    print(banners['BN4'], end=' ')
    subprocess.run([f"""
echo "{content['index']}" >> {srcDir}/index.js
echo "{content['app']}" >> {srcDir}/pages/app/app.js
"""], shell=True)
    print(banners['OK'])

    print(banners['BN5'], end=' ')
    subprocess.run([f"""
cd {client}
sudo rm -d -r .git
git init --initial-branch=develop &> /dev/null
"""], shell=True)
    print(banners['OK'])

    if isDesktopApp:
        createDesktopProject(clientName=client)
