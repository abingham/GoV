/// <reference path="lib/angularjs/angular.d.ts" />
/// <reference path="lib/angularjs/angular-resource.d.ts" />
/// <reference path="lib/underscore/underscore.d.ts" />

module Goz.Service {
    var gozServices: angular.IModule = angular.module(
        'gozServices',
        ['ngResource']);

    gozServices.factory(
	'Transactions',
	['$resource',
	 function($resource: angular.resource.IResourceService) {
	     return $resource('/api/transactions/:id')
	 }
	]);
}
