(function () {
    "use strict";
    //ui.bootstrap is needed for Accordion
    var tms = angular.module('tms', ['ngRoute', 'ngCookies',
        'home', 'auth', 'registration', 'template', 'fixedTop', 'footer']);
}());
