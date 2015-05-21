/// <reference path="lib/angularjs/angular.d.ts"/>
/// <reference path="lib/underscore/underscore.d.ts"/>
/// <reference path="lib/angular-ui-router/angular-ui-router.d.ts"/>

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
    
    interface TransactionListScope extends angular.IScope {
        // All transactions in a journal
        transactions: Transaction[];
    }

    // Main list of transactions
    gozControllers.controller(
	'TransactionListController',
	['$scope',
         'Transactions',
	 ($scope: TransactionListScope,
          Transactions) => {
              $scope.transactions = Transactions.query();
	 }]);

    interface TransactionViewScope extends angular.IScope {
        transaction: Transaction;
    }
    
    gozControllers.controller(
        'TransactionViewController',
        ['$scope',
         '$stateParams',
         'Transactions',
         ($scope: TransactionViewScope,
          $stateParams,
          Transactions) => {
              $scope.transaction = Transactions.get({ id: $stateParams.id });
          }]);
}
