/// <reference path="lib/angularjs/angular.d.ts"/>

'use string';

module Goz.App {

    var gozApp: angular.IModule = angular.module(
	'gozApp',
	['ui.router',
         'gozControllers']);
 
    angular.module('gozApp').config(function($stateProvider) {
        $stateProvider.state('transactions', { // Show all transactions
            url: '/transactions',
            templateUrl: 'static/partials/transactions.html',
            controller: 'TransactionListController'
        }).state('viewTransaction', { // Show a single transaction
            url: '/transactions/:id/view',
            templateUrl: 'static/partials/transaction-view.html',
            controller: 'TransactionViewController'
        // }).state('newTransaction', { //state for adding a new transaction
        //     url: '/transactions/new',
        //     templateUrl: 'partials/transaction-add.html',
        //     controller: 'TransactionCreateController'
        // }).state('editTransaction', { //state for updating a transaction
        //     url: '/transactions/:id/edit',
        //     templateUrl: 'partials/transaction-edit.html',
        //     controller: 'TransactionEditController'
        });
    }).run(function($state) {
        $state.go('transactions'); //make a transition to "transactions" state when app starts
    });
}
