
class Controller {
    // renderer = new Renderer()
    Model = new Model()
    renderer = new Renderer()
    

    async loadCandidates(jobName:string, status:string, stage:string, gender:string){
        const candidatesToRender: Candidate[] = await this.Model.getCandidates(jobName, status, stage, gender)
        this.renderer.renderCandidates(candidatesToRender)
    }

    async loadJobs(){
        const jobsToRender: Job[] = await this.Model.getJobs()
        this.renderer.renderJobs(jobsToRender)
    }
} 

const controller = new Controller() 

$("body").on("click", ".dropdown-item", function(){
    console.log("ffffffff")
    if($(this).hasClass('pos')){
        // controller.filters.position = this.innerHTML
        console.log('1')
    }
    if($(this).hasClass('stat')){
        // controller.filters.status = this.innerHTML
        console.log('2')
    }
    if($(this).hasClass('stage')){
        // controller.filters.stage = this.innerHTML
        console.log('3')
    }
    if($(this).hasClass('gender')){
        // controller.filters.gender = this.innerHTML
        console.log('4')
    }
})

// $('#search-btn').on('click', async function(){
//     const positionEvent: any = $('#pos-btn')
//     positionEvent.
//     const dairy: boolean = $('#dairy-free').is(':checked')
//     const ingredient = $("#ingredient").val() 
//     if(typeof ingredient === 'string' ){
//         await controller.loadRecipes(ingredient, gluten, dairy)
//     }
// })


// $('#container').on('click','.recipe-image', async function(){
//     const ingredientElement = $(this).closest('.recipe').find('.ingredient');
//     alert(ingredientElement[0].innerHTML)
// })