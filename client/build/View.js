"use strict";
class Renderer {
    constructor() {
        this.candidatesTemplate = Handlebars.compile($("#candidates-template").html());
        this.jobsTemplate = Handlebars.compile($("#jobs-template").html());
        this.jobsDropdownTemplate = Handlebars.compile($("#jobsDropdown-template").html());
    }
    renderJobs(jobsData) {
        this.emptyAll();
        const inject = this.jobsTemplate({ "job": jobsData });
        $("#table-container").append(inject);
    }
    renderJobsDropDown(jobsData) {
        this.emptyJobDropDown();
        const inject = this.jobsDropdownTemplate({ "job": jobsData });
        $("#drop-pos-container").append(inject);
    }
    renderCandidates(candidatesData) {
        this.emptyAll();
        const inject = this.candidatesTemplate({ "candidate": candidatesData });
        $("#table-container").append(inject);
    }
    emptyAll() {
        $("#table-container").empty();
    }
    emptyJobDropDown() {
        $("#drop-pos-container").empty();
    }
}

Handlebars.registerHelper('ifEquals', function(arg1, arg2, options) {
    return (arg1 == arg2) ? options.fn(this) : options.inverse(this);
});
