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
        // const statisticsToRender: Job[] = await this.Model.getJobs()
        this.renderer.renderStatistics()
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
    const currentStage: string = $(this).closest('.candidate').find('.stage').text()
  const candidateName: string = $(this).closest('.candidate').find('.name').text()

  if (currentStage === 'Rejected' || currentStage === 'Hired' ) {
    return;
  }
  
    await controller.Model.updateStatus(jobId, candidateId)
    controller.loadCandidates()
})

$("body").on('click', ".hire-btn", async function(){
  const jobId = $(this).data('job')
  const candidateId = $(this).data('cand')
  const currentStage: string = $(this).closest('.candidate').find('.stage').text()
  const candidateName: string = $(this).closest('.candidate').find('.name').text()

  if (currentStage === 'Rejected' || currentStage === 'Hired' ) {
    return;
  }
  alert(`You are going to hire ${candidateName}.\n
  Be aware, this process cannot be change!`)  
  
  await controller.Model.updateStage(jobId, candidateId, 'Hired')
  controller.loadCandidates()
})

$("body").on('click', ".reject-btn", async function(){
  const jobId = $(this).data('job')
  const candidateId = $(this).data('cand')
  const currentStage: string = $(this).closest('.candidate').find('.stage').text()
  const candidateName: string = $(this).closest('.candidate').find('.name').text()

  if (currentStage === 'Rejected' || currentStage === 'Hired' ) {
    return;
  }
  alert(`You are going to postpone the hiring process of ${candidateName}.\n
  Be aware, this process cannot be change!`)
  await controller.Model.updateStage(jobId, candidateId, 'Rejected')
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
