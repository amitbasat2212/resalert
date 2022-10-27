class Model {
  static currentCandidates: Candidate[];
  static currentJobs: Job[];
 

  async logIn(userName: string, password: string) {
    $.get(`/autantication/login?userName=${userName}&password=${password}`);
  }

  async getCandidates(
    jobName: string,
    status: string,
    stage: string,
    gender: string
  ): Promise<Candidate[]> {
    Model.currentCandidates = await $.get(
      `/candidates?job_name=${jobName}&status=${status}&stage=${stage}&gender=${gender}`
    );
    return Model.currentCandidates;
  }

  async getJobs(): Promise<Job[]> {
    Model.currentJobs = await $.get(`/jobs`);
    return Model.currentJobs;
  }

  async addNewCandidate(newCandidate: Candidate): Promise<Candidate> {
    return await $.post(`/candidates`, JSON.stringify(newCandidate));
  }

  updateStatus(jobId: string, candidateId: string) {
    $.ajax({
      url: `/personjobs/status?job_id=${jobId}&candidate_id=${candidateId}`,
      type: 'PUT'
      });
      
   }

   updateStage(jobId:string, candidateId:string, stage: string){
    $.ajax({
       url: `/personjobs/stages?job_id=${jobId}&candidate_id=${candidateId}&stage=${stage}`,
       type: 'PUT'
       });
       
    }
   


   async staticsForGender(){
    const graphs=new graph();
    const gender:any = await $.get(`/statics/Gender`);    
    const labels_gender:String []=[]    
    const values_gender:String []=[]

    for(let i=0;i<gender.length;i++){
        labels_gender[i]=gender[i]["c_gender"]
        values_gender[i]=gender[i]["num_candidate"]
    }
    
    graphs.create_pie_chart(labels_gender,values_gender)
   
   } 
   async staticsForEmploeyPerDeps(){
    const graphs=new graph();   
    const personperdep:any =await $.get(`/statics/dep`);
    const labels_dep:String []=[]    
    const values_dep:String []=[]  

    for(let i=0;i<personperdep.length;i++){
        labels_dep[i]=personperdep[i]["dep_name"]
        values_dep[i]=personperdep[i]["member"]
    }
   
    graphs.create_bar_chart(labels_dep,values_dep)
   } 


  async addNewJob(id: number, name: string, dep_name: string) {
    const newJob = {
      oj_id: id,
      job_name: name,
      department_name: dep_name,
    };

    return await $.post(`/jobs`, JSON.stringify(newJob));
  }

  async deleteJob(job_id: number) {
    return await $.ajax({
      url: `/jobs/?job_id=${job_id}`,
      type: "DELETE",
      dataType: "json",
      contentType: "application/json",
    });
  }
}

