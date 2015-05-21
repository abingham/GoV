/// <reference path="lib/angularjs/angular.d.ts"/>
/// <reference path="lib/underscore/underscore.d.ts"/>

'use strict';

/* Controllers */

module Goz.Controller {

    var gozControllers: angular.IModule = angular.module(
	'gozControllers',
	['gozServices']);

    // A single transaction
    interface Transaction {
        id: string;
        payee: string;
    };
    
    interface GozScope extends angular.IScope {
        // All transactions in a journal
        transactions: Transaction[];
    }

    // The main controller for Goz.
    //
    gozControllers.controller(
	'TransactionListController',
	['$scope',
         'Transactions',
	 ($scope: GozScope,
          Transactions) => {
              $scope.transactions = Transactions.query();
	 }]);

}
