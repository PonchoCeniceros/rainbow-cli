from colorama import init, Fore, Back, Style
import re, json

def logo() -> None:
    print()
    print(f"{Style.BRIGHT}{Fore.RED    }            _       _                   ")
    print(f"{Style.BRIGHT}{Fore.GREEN  }  _ __ __ _(_)_ __ | |__   _____      __")
    print(f"{Style.BRIGHT}{Fore.YELLOW } | '__/ _` | | '_ \| '_ \ / _ \ \ /\ / /")
    print(f"{Style.BRIGHT}{Fore.BLUE   } | | | (_| | | | | | |_) | (_) \ V  V / ")
    print(f"{Style.BRIGHT}{Fore.MAGENTA} |_|  \__,_|_|_| |_|_.__/ \___/ \_/\_/  ")
    print(f"{Style.BRIGHT}{Fore.CYAN   }                                        ")

def finish() -> None:
    sb = Style.BRIGHT
    a = Fore.RED
    b = Fore.GREEN
    c = Fore.YELLOW
    d = Fore.BLUE
    e = Fore.MAGENTA
    f = Fore.CYAN
    print()
    print(f" {sb}{a}e{b}n{c}j{d}o{e}y{f} {a}c{b}o{c}d{d}i{e}n{f}g{a}!{Fore.RESET}")
    print()


def getBanners() -> dict:
    sb  = Style.BRIGHT
    rst = Fore.RESET
    a = Fore.RED
    b = Fore.GREEN
    c = Fore.YELLOW
    d = Fore.BLUE
    e = Fore.MAGENTA
    f = Fore.CYAN

    return {
        "new_project": f" {sb}creating new project{rst}...",
        "file_structure": f" {sb}creating file structure{rst}...",
        "creating_assets": f" creating {sb}{a}assets{rst} folder and {sb}{d}Tailwind{rst} configuration...",
        "creating_components": f" creating {sb}{c}components{rst} folder...",
        "creating_hooks": f" creating {sb}{e}hooks{rst} folder...",
        "creating_helpers": f" creating {sb}{b}helpers{rst} folder...",
        "creating_views": f" creating {sb}{f}views{rst} folder and {sb}{c}main{rst} component...",
        "dependencies_for_desktop": f" installing dependencies for desktop applications...",
        "git_project": f" instantiating {sb}{b}git{rst} project...",

        "jsconfig_json": f"please copy {sb}{c}" + '{"compilerOptions": {"baseUrl": "src", "paths": {"*": ["src/*"]}}}' + f"{rst} on jsconfig.json",
        "OK": f"{sb}{b}ok{rst}",
    }

def getContent() -> dict:
        tailwindConfig = \
"/** @type {import('tailwindcss').Config} */" + \
"""
module.exports = {
        content: [""" + \
f"""
              './src/**/*.{{"js,jsx,ts,tsx"}}',""" + \
"""
        ],
        theme: {
                extend: {},
        },
        plugins: [],
}
"""
        return {
#
# contenido de index.js
#
        'index': """import React from 'react';
import {createRoot} from 'react-dom/client';
import App from './views/app';
import 'assets/styles/index.css';

const container = document.querySelector('#root');
const root = createRoot(container);
root.render(<App />);
""",
#
# contenido de pages/app.js
#
        'app': """import React from 'react';

const App = () => {
  return (
    <h1 className='text-8xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-green-300 to-blue-600'>
    Happy coding!
    </h1>
  );
};

export default App;
        """,
#
# contenido de .env
#
        'env': """NODE_ENV=development
APP_WIDTH=1024
APP_HEIGHT=512 
        """,
#
# contenido de main.js
#
        'main': """const {app, ipcMain, BrowserWindow} = require('electron');
const path = require('path');
const url = require('url');
require('dotenv').config();

// inter-process communication
//
// ipcMain.on('', (event, response) => {
// });

function createWindow() {
  const mainWindow = new BrowserWindow({
    title: 'Generador de registros r√°pidos de producci√≥n',
    width: parseInt(process.env.APP_WIDTH),
    height: parseInt(process.env.APP_HEIGHT),
    fullscreen: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  const appUrl = (process.env.NODE_ENV === 'production') ? url.format({
    pathname: path.join(\`\${__dirname}\`.replace('/src', ''), 'build/index.html'),
    protocol: 'file:',
    slashes: true,
  }) : 'http://localhost:3000/';
  mainWindow.loadURL(appUrl);
  mainWindow.setMenu(null);

  process.env.NODE_ENV !== 'production' && mainWindow.openDevTools();
}

app.commandLine.appendSwitch('lang', 'es');

app.whenReady().then(() => {
  createWindow();

  app.on('activate', function() {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function() {
  if (process.platform !== 'darwin') app.quit();
});
        """,
#
# contenido de tailwind.config.js
#
        'tailwind_config': tailwindConfig,
#
# contenido de index.css
#
        'index_css': """@tailwind base;
@tailwind components;
@tailwind utilities;
        """,
        }


def formatProjectName(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()

