(function () {
    "use strict";
    angular
        .module('template')
        .component('createTemplate', {
            'templateUrl': 'static/html/create-template.template.html',
            'controller': ['$window', '$routeParams', '$location', '$http',
                           function ($window, $routeParams, $location, $http) {
                var self = this;
                var templateId = $routeParams.templateId;
                self.yearOptions = {'First': 'First', 'Second': 'Second', 'Third': 'Third',
                                    'Fourth': 'Fourth'};
                $http.get('departments/').then(function successCallback(response) {
                    self.departmentOptions = response.data;
                })
                this.createTemplate = function () {
                    var data = {'year': this.year, 'department': this.department.code,
                                'residential_status': this.residential_status, 'content': this.content,
                                'title': this.title}
                    $http({
                        url: 'templates/',
                        method: "POST",
                        data: data,
                    }).then(function successCallback(response) {
                        self.tickets = response.data;
                        $location.path('user-templates/');
                    }, function failureCallback(response) {
                        self.errors = response.data;
                    })
                };
            }]
        });
}());
