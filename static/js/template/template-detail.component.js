(function () {
    "use strict";
    angular
        .module('template')
        .component('templateDetail', {
            'templateUrl': 'static/html/template-detail.template.html',
            'controller': ['$window', '$routeParams', '$http', function ($window, $routeParams, $http) {
                var self = this;
                var templateId = $routeParams.templateId;
                var url = 'template/'+templateId + '/'
                $http.get(url).then(function successCallback(response) {
                    self.template = response.data;
                })
            }]
        });
}());
