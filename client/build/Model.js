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
}
// `/jobs`, JSON.stringify(job_id));
