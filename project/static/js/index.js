import jQuery from 'jquery';
import 'bootstrap/dist/css/bootstrap.css';
import '@fortawesome/fontawesome-free/css/all.css';

require('popper.js');
require('bootstrap');
require('../scss/styles.scss');


global.jQuery = jQuery;
global.$ = global.jQuery;

import {navItemHandler, buttonDateHandler} from './init/navbar';
import {getAllClients} from './init/feedClients';
import {buttonHandler} from './handlers/button';
import { 
    commandFood,
    getClientFood,
    commentUpdate,
    command} from './handlers/planning';


window.app = (function app () {
    // TODO: make a setting api call
    return {
      models: {},
      collections: {},
      views: {},
      router: null,
      apiRoot: '/api/frontend/',
      icons: [],
    };
  }(jQuery));
  

window.app.buttonDateHandler = buttonDateHandler;
window.app.navItemHandler = navItemHandler;
window.app.getAllClients = getAllClients;
window.app.buttonHandler = buttonHandler;
window.app.commandFood = commandFood;
window.app.getClientFood = getClientFood;
window.app.commentUpdate = commentUpdate;
window.app.command = command;