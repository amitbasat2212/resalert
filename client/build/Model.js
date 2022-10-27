"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
class Model {
    logIn(userName, password) {
        return __awaiter(this, void 0, void 0, function* () {
            $.get(`/autantication/login?userName=${userName}&password=${password}`);
        });
    }
    getCandidates(jobName, status, stage, gender) {
        return __awaiter(this, void 0, void 0, function* () {
            Model.currentCandidates = yield $.get(`/candidates?job=${jobName}&status=${status}&stage=${stage}&gender=${gender}`);
            return Model.currentCandidates;
        });
    }
    getJobs() {
        return __awaiter(this, void 0, void 0, function* () {
            Model.currentJobs = yield $.get(`/jobs`);
            return Model.currentJobs;
        });
    }
    addNewCandidate(newCandidate) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield $.post(`/candidates`, JSON.stringify(newCandidate));
        });
    }
    updateStatus(jobId, candidateId) {
        $.ajax({
            url: `/personjobs/status?job_id=${jobId}&candidate_id=${candidateId}`,
            type: 'PUT'
        });
    }
    addNewJob(newJob) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield $.post(`/jobs`, JSON.stringify(newJob));
        });
    }
    deleteJob(job_id) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield $.ajax({
                url: `/jobs/?job_id=${job_id}`,
                type: "DELETE",
                dataType: "json",
                contentType: "application/json",
            });
        });
    }
    staticsForGender() {
        return __awaiter(this, void 0, void 0, function* () {
            const graphs = new graph();
            const gender = yield $.get(`/statics/Gender`);
            const labels_gender = [];
            const values_gender = [];
            for (let i = 0; i < gender.length; i++) {
                labels_gender[i] = gender[i]["c_gender"];
                values_gender[i] = gender[i]["num_candidate"];
            }
            graphs.create_pie_chart(labels_gender, values_gender);
        });
    }
    staticsForEmploeyPerDeps() {
        return __awaiter(this, void 0, void 0, function* () {
            const graphs = new graph();
            const personperdep = yield $.get(`/statics/dep`);
            const labels_dep = [];
            const values_dep = [];
            for (let i = 0; i < personperdep.length; i++) {
                labels_dep[i] = personperdep[i]["dep_name"];
                values_dep[i] = personperdep[i]["member"];
            }
            graphs.create_bar_chart(labels_dep, values_dep);
        });
    }
}
