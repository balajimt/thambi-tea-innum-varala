// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
var ById = function (id) {
    return document.getElementById(id);
}
var jsonfile = require('jsonfile');
var favicon = require('favicon-getter').default;
var path = require('path');
var uuid = require('uuid');
var bookmarks = path.join(__dirname, '/bookmarks.json');
const FIRST_OPTION = "https://colab.research.google.com/github/eyaler/avatars4all/blob/master/melaflefon.ipynb#scrollTo=P3LihClHbUd3"
const SECOND_OPTION = "https://www.youtube.com/watch?v=NUYvbT6vTPs"
var omni = ById('url'),
    view = ById('view');

function updateURL(event) {
    if (event.keyCode === 13) {
        omni.blur();
        let val = omni.value;
        let https = val.slice(0, 8).toLowerCase();
        let http = val.slice(0, 7).toLowerCase();
        if (https === 'https://') {
            view.loadURL(val);
        } else if (http === 'http://') {
            view.loadURL(val);
        } else if (http === 'file://') {
            view.loadURL(val);
        } else {
            view.loadURL('http://' + val);
        }
    }
}

function updateNav(event) {
    omni.value = view.src;
}

omni.addEventListener('keydown', updateURL);
view.addEventListener('did-finish-load', updateNav);
