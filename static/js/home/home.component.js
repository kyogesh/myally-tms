(function () {
    "use strict";
    angular
        .module('home')
        .component('home', {
            'templateUrl': 'static/html/home.template.html',
            'controller': ['$window', '$http', function ($window, $http) {
                self = this;
                $http.get('templates/').then(function successCallback(response) {
                    self.templates = response.data;
                })
                this.selectTemplate = function (template) {
                    self.selectedTemplate = template;
                 };
                this.startCampaign = function () {
                    $http.post('start-campaign/').then(function successCallback(response) {
                        self.render = response.data;
                    });
                };
            }]
        });
}());
