'use strict';

/**
 * @ngdoc overview
 * @name highchartsBbqApp
 * @description
 * # highchartsBbqApp
 *
 * Main module of the application.
 */
angular
  .module('highchartsBbqApp', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
