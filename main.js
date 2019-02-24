console.log('main process working');

const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require("path");
const url = require("url");
const Menu = electron.Menu;

let win;

function createWindow(){
    win = new BrowserWindow({minWidth: 970 , minHeight: 745 , show: false});
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }));

    // win.webContents.openDevTools();

    win.once('ready-to-show', () => {
        win.show()
    });

    win.on('closed', () => {
        win = null;
    });

        
}


app.on('ready', function(){
    createWindow();
    const menu  = null;
    Menu.setApplicationMenu(menu);
});

