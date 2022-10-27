class Controller {
  Model = new Model();
  renderer = new Renderer();
  filters = new Filter("", "", "", "");

  async loadCandidates() {
    const candidatesToRender: Candidate[] = await this.Model.getCandidates(
      controller.filters.position,
      controller.filters.status,
      controller.filters.stage,
      controller.filters.gender
    );
    this.renderer.renderCandidates(candidatesToRender);
  }

    async loadJobsTable(){
        const jobsToRender: Job[] = await this.Model.getJobs()
        this.renderer.renderJobs(jobsToRender)
    }

    async loadStatistics(){
        this.renderer.renderStatics()
        await this.Model.staticsForGender()
        await this.Model.staticsForEmploeyPerDeps()
        
    }
} 

const controller = new Controller();

$("body").on("click", ".dropdown-item", function () {
  console.log(this);
  if ($(this).hasClass("pos")) {
    controller.filters.position = this.innerHTML;
    console.log(controller.filters.position);
  }
  if ($(this).hasClass("stat")) {
    controller.filters.status = this.innerHTML;
    console.log("2");
  }
  if ($(this).hasClass("stage")) {
    controller.filters.stage = this.innerHTML;
    console.log("3");
  }
  if ($(this).hasClass("gender")) {
    controller.filters.gender = this.innerHTML;
    console.log("4");
  }
});

$("body").on('click', ".update-btn", async function(){
    const jobId = $(this).data('job')
    const candidateId = $(this).data('cand')
    await controller.Model.updateStatus(jobId, candidateId)
    controller.loadCandidates()
})

$('#pos-btn').on('click', async function(){
    const jobs: Job[] = await controller.Model.getJobs()
    controller.renderer.renderJobsDropDown(jobs)
})

$("#search-btn").on("click", async function () {
  await controller.loadCandidates();
});

$("#clear-filters-btn").on("click", function () {
  controller.filters.empty();
  controller.loadCandidates();
});

$('#toJobs').on('click', function(){
    $('#table-name').text('Jobs')
    controller.loadJobsTable()
    $('#search-btn').prop('disabled', true)
    $('#clear-filters-btn').prop('disabled', true)

})

$('#toCandidates').on('click', function(){
    controller.filters.empty()
    $('#table-name').text('Candidates')
    $('#search-btn').prop('disabled', false)
    $('#clear-filters-btn').prop('disabled', false)
    controller.loadCandidates()
   
})


$('#toDashboard').on('click', function(){
    controller.filters.empty()
    $('#table-name').text('Recruiting Statistics')
    $('#search-btn').prop('disabled', true)
    $('#clear-filters-btn').prop('disabled', true)
    controller.loadStatistics()
   
})

$("#table-container").on("click", ".close-position", function () {
  const id = $(this).data("id");
  controller.Model.deleteJob(id);
  controller.loadJobsTable();
});


