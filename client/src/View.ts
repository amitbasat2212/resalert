class Renderer{
    candidatesTemplate: HandlebarsTemplateDelegate<any>
    jobsTemplate: HandlebarsTemplateDelegate<any>



    constructor() {
        this.candidatesTemplate = Handlebars.compile($("#candidates-template").html());
        this.jobsTemplate = Handlebars.compile($("#jobs-template").html());

    }

    renderJobs(jobsData:Job[]){
        this.emptyAll();
        const inject = this.jobsTemplate({"job": jobsData});
        $("#table-container").append(inject);
    }

    renderCandidates(candidatesData:Candidate[]){
        this.emptyAll();
        const inject = this.candidatesTemplate({"candidate": candidatesData});
        $("#table-container").append(inject);
    }
    
    private emptyAll():void {
        $("#table-container").empty();
    }
}   