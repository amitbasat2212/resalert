class Model{
    static currentCandidates:Candidate[]
    static currentJobs:Job[]

    async logIn(userName:string, password:string){
        $.get(`/autantication/login?userName=${userName}&password=${password}`)
    }

    async getCandidates(jobName:string, status:string, stage:string, gender:string): Promise<Candidate[]>{
       Model.currentCandidates =  await $.get(`/candidates?job_name=${jobName}&status=${status}&stage=${stage}&gender=${gender}`)
       return Model.currentCandidates
    }

    async getJobs(): Promise<Job[]>{
        Model.currentJobs =  await $.get(`/jobs`)
        return Model.currentJobs
     }

    async addNewCandidate(newCandidate: Candidate ): Promise<Candidate>{
        return await $.post(`/candidates`,JSON.stringify(newCandidate))
     }
   
     updateStatus(jobId:string, candidateId:string){
      $.ajax({
         url: `/status?job_id=${jobId}&candidate_id=${candidateId}`,
         type: 'PUT'
       });
         
     }
     async addNewJob(newJob: Job ): Promise<Job>{
        return await $.post(`/jobs`,JSON.stringify(newJob))
     }
}