"use strict";
class Renderer {
    constructor() {
        this.candidatesTemplate = Handlebars.compile($("#candidates-template").html());
        this.jobsTemplate = Handlebars.compile($("#jobs-template").html());
    }
    renderJobs(jobsData) {
        this.emptyAll();
        const inject = this.jobsTemplate({ "job": jobsData });
        $("#table-container").append(inject);
    }
    renderCandidates(candidatesData) {
        this.emptyAll();
        const inject = this.candidatesTemplate({ "candidate": candidatesData });
        $("#table-container").append(inject);
    }
    emptyAll() {
        $("#table-container").empty();
    }
}
