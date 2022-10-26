
class Controller {
    Model = new Model()
    renderer = new Renderer()
    filters = new Filter("","", "", "")

    async loadCandidates(position:string, status:string, stage:string, gender:string){
        const candidatesToRender: Candidate[] = await this.Model.getCandidates(position, status, stage, gender)
        this.renderer.renderCandidates(candidatesToRender)
    }

    async loadJobsTable(){
        const jobsToRender: Job[] = await this.Model.getJobs()
        this.renderer.renderJobs(jobsToRender)
    }
} 

const controller = new Controller() 

$("body").on("click", ".dropdown-item", function(){
    console.log(this)
    if($(this).hasClass('pos')){
        controller.filters.position = $(this).data('id')
        console.log('1')
    }
    if($(this).hasClass('stat')){
        controller.filters.status = this.innerHTML
        console.log('2')
    }
    if($(this).hasClass('stage')){
        controller.filters.stage = this.innerHTML
        console.log('3')
    }
    if($(this).hasClass('gender')){
        controller.filters.gender = this.innerHTML
        console.log('4')
    }
})

$('#pos-btn').on('click', async function(){
    const jobs: Job[] = await controller.Model.getJobs()
    controller.renderer.renderJobsDropDown(jobs)
})

$('#search-btn').on('click', async function(){
   await  controller.loadCandidates(controller.filters.position, controller.filters.status, controller.filters.stage, controller.filters.gender)
})

