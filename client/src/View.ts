class Renderer{
    candidatesTemplate: HandlebarsTemplateDelegate<any>
    jobsTemplate: HandlebarsTemplateDelegate<any>
    jobsDropdownTemplate: HandlebarsTemplateDelegate<any>


    constructor() {
        this.candidatesTemplate = Handlebars.compile($("#candidates-template").html());
        this.jobsTemplate = Handlebars.compile($("#jobs-template").html());
        this.jobsDropdownTemplate = Handlebars.compile($("#jobsDropdown-template").html());
    }

    

    renderJobs(jobsData:Job[]){
        this.emptyAll();
        const inject = this.jobsTemplate({"job": jobsData});
        $("#table-container").append(inject);
    }

    renderStatics(){
        this.emptyAll();
        const inject = `<canvas id="pie-chart" width="1200" height="380"></canvas>
        <canvas id="bar-chart" width="1200" height="380"></canvas>    
    <script>var exports = {};</script>
    
   `
        $("#table-container").append(inject);
    }

    renderJobsDropDown(jobsData:Job[]){
        this.emptyJobDropDown();
        const inject = this.jobsDropdownTemplate({"job": jobsData});
        $("#drop-pos-container").append(inject);
    }

    renderCandidates(candidatesData:Candidate[]){
        this.emptyAll();
        const inject = this.candidatesTemplate({"candidate": candidatesData});
        $("#table-container").append(inject);
    }
    
    private emptyAll():void {
        $("#table-container").empty();
    }

    private emptyJobDropDown():void {
        $("#drop-pos-container").empty();
    }
}   



Handlebars.registerHelper('ifEquals', function(arg1, arg2, options) {
    return (arg1 == arg2) ? options.fn(this) : options.inverse(this);
});