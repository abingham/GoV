/// <reference path="../lib/angularjs/angular.d.ts"/>
/// <reference path="../lib/underscore/underscore.d.ts"/>

'use strict';

/* Controllers */

module Goz.Controller {

    var gozControllers: angular.IModule = angular.module(
	'gozControllers',
	[]);
    
    interface GozScope extends angular.IScope {}

    // The main controller for Goz.
    //
    gozControllers.controller(
	'GozCtrl',
	['$scope',
	 ($scope: GozScope) => {
	 }]);

}
