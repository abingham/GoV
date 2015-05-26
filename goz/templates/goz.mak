<!doctype html>
<html lang="en" ng-app="gozApp">
    <head>
	<meta charset="utf-8">
	<title>Goz</title>
        <link rel="stylesheet" href="static/bower_components/bootstrap/dist/css/bootstrap.css">
	<!-- <link rel="stylesheet" href="static/bower_components/bootstrap-table/dist/bootstrap-table.min.css">
	<link rel="stylesheet" href="static/bower_components/angular-ui-select/dist/select.min.css">
	<link rel="stylesheet" href="static/bower_components/angular-multi-select/isteven-multi-select.css"> -->
	<link rel="stylesheet" href="static/css/app/goz.css">

	<script src="static/bower_components/jquery/dist/jquery.min.js"></script>
	<script src="static/bower_components/angular/angular.js"></script>
	<!-- <script src="static/bower_components/angular-route/angular-route.js"></script> -->
	<script src="static/bower_components/angular-resource/angular-resource.js"></script>
        <script src="static/bower_components/angular-ui-router/release/angular-ui-router.min.js"></script>
	<!-- <script src="static/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>
	<script src="static/bower_components/bootstrap-table/dist/bootstrap-table.min.js"></script>
	<script src="static/bower_components/underscore/underscore-min.js"></script>
	<script src="static/bower_components/snap.svg/dist/snap.svg-min.js"></script>
	<script src="static/bower_components/angular-sanitize/angular-sanitize.min.js"></script>
	<script src="static/bower_components/angular-ui-select/dist/select.min.js"></script>
	<script src="static/bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js"></script>
	<script src="static/bower_components/angular-multi-select/isteven-multi-select.js"></script> -->
        <script src="static/js/built/controllers.js"></script>
        <script src="static/js/built/services.js"></script>
	<script src="static/js/built/app.js"></script>
    </head>
    
    <body ng-app>
        <nav class="navbar navbar-default" role="navigation">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" ui-sref="ledger">GoV</a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li class="active"><a ui-sref="transactions">Transaction</a></li>
			<li><a ui-sref="reports">Reports</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container">
            <div class="row top-buffer">
                <div class="col-xs-8 col-xs-offset-2">
                    <div ui-view></div>
                </div>
            </div>
        </div>
    </body>
</html>
