(function () {
    "use strict";
    angular
        .module('template')
        .component('userTemplate', {
            'templateUrl': 'static/html/user-templates.template.html',
            'controller': ['$window', '$routeParams', '$http', function ($window, $routeParams, $http) {
                var self = this;
                var ticketId = $routeParams.templateId;
                $http.get('templates/').then(function successCallback(response) {
                    self.templates = response.data;
                })
                this.selectTemplate = function (template) {
                    self.selectedTemplate = template;
                 };
            }]
        });
}());
