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
    renderStatics() {
        this.emptyAll();
        const inject = `<canvas id="pie-chart" width="1200" height="380"></canvas>
        <canvas id="bar-chart" width="1200" height="380"></canvas>    
    <script>var exports = {};</script>
    
   `;
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
Handlebars.registerHelper('ifEquals', function (arg1, arg2, options) {
    return (arg1 == arg2) ? options.fn(this) : options.inverse(this);
});
