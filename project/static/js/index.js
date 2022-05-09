import jQuery from 'jquery';
import 'bootstrap/dist/css/bootstrap.css';
import '@fortawesome/fontawesome-free/css/all.css';
import {
  displayUnit,
  displayExpirationDate,
  selectAllPeriodicity,
  submitFlux,
} from './forms/fluxFormsHelpers';

// make jquery available in underscore; bootstrap and backbone
global.jQuery = jQuery;
global.$ = global.jQuery;
require('popper.js');
require('bootstrap');
require('../scss/styles.scss');
