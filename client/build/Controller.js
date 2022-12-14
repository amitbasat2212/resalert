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
class Controller {
    constructor() {
        this.Model = new Model();
        this.renderer = new Renderer();
        this.filters = new Filter("", "", "", "");
    }
    loadCandidates() {
        return __awaiter(this, void 0, void 0, function* () {
            const candidatesToRender = yield this.Model.getCandidates(controller.filters.position, controller.filters.status, controller.filters.stage, controller.filters.gender);
            this.renderer.renderCandidates(candidatesToRender);
        });
    }
    loadJobsTable() {
        return __awaiter(this, void 0, void 0, function* () {
            const jobsToRender = yield this.Model.getJobs();
            this.renderer.renderJobs(jobsToRender);
        });
    }
    loadStatistics() {
        return __awaiter(this, void 0, void 0, function* () {
            this.renderer.renderStatics();
            yield this.Model.staticsForGender();
            yield this.Model.staticsForEmploeyPerDeps();
        });
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
$("body").on('click', ".update-btn", function () {
    return __awaiter(this, void 0, void 0, function* () {
        const jobId = $(this).data('job');
        const candidateId = $(this).data('cand');
        const currentStage = $(this).closest('.candidate').find('.stage').text();
        if (currentStage === 'Rejected' || currentStage === 'Hired') {
            return;
        }
        yield controller.Model.updateStatus(jobId, candidateId);
        if (currentStage === 'Pending') {
            yield controller.Model.updateStage(jobId, candidateId, 'On process');
        }
        controller.loadCandidates();
    });
});
$("body").on('click', ".hire-btn", function () {
    return __awaiter(this, void 0, void 0, function* () {
        const jobId = $(this).data('job');
        const candidateId = $(this).data('cand');
        const currentStage = $(this).closest('.candidate').find('.stage').text();
        const candidateName = $(this).closest('.candidate').find('.name').text();
        if (currentStage === 'Rejected' || currentStage === 'Hired') {
            return;
        }
        alert(`You are going to hire ${candidateName}.\n
  Be aware, this process cannot be change!`);
        yield controller.Model.updateStage(jobId, candidateId, 'Hired');
        controller.loadCandidates();
    });
});
$("body").on('click', ".reject-btn", function () {
    return __awaiter(this, void 0, void 0, function* () {
        const jobId = $(this).data('job');
        const candidateId = $(this).data('cand');
        const currentStage = $(this).closest('.candidate').find('.stage').text();
        const candidateName = $(this).closest('.candidate').find('.name').text();
        if (currentStage === 'Rejected' || currentStage === 'Hired') {
            return;
        }
        alert(`You are going to postpone the hiring process of ${candidateName}.\n
  Be aware, this process cannot be change!`);
        yield controller.Model.updateStage(jobId, candidateId, 'Rejected');
        controller.loadCandidates();
    });
});
$('#pos-btn').on('click', function () {
    return __awaiter(this, void 0, void 0, function* () {
        const jobs = yield controller.Model.getJobs();
        controller.renderer.renderJobsDropDown(jobs);
    });
});
$("#search-btn").on("click", function () {
    return __awaiter(this, void 0, void 0, function* () {
        yield controller.loadCandidates();
    });
});
$("#clear-filters-btn").on("click", function () {
    controller.filters.empty();
    controller.loadCandidates();
});
$("#toJobs").on("click", function () {
    $("#table-name").text("Jobs");
    controller.loadJobsTable();
    $("#search-btn").prop("disabled", true);
    $("#clear-filters-btn").prop("disabled", true);
});
$("#toCandidates").on("click", function () {
    controller.filters.empty();
    $("#table-name").text("Candidates");
    $("#search-btn").prop("disabled", false);
    $("#clear-filters-btn").prop("disabled", false);
    controller.loadCandidates();
});
$("#toDashboard").on("click", function () {
    controller.filters.empty();
    $("#table-name").text("Recruiting Statistics");
    $("#search-btn").prop("disabled", true);
    $("#clear-filters-btn").prop("disabled", true);
    controller.loadStatistics();
});
$("#table-container").on("click", ".close-position", function () {
    const id = $(this).data("id");
    controller.Model.deleteJob(id);
    controller.loadJobsTable();
});
$("#table-container").on("click", ".add-new-job", function () {
    const id = $(this).closest(".add-new-job-table").find(".form-job-id").val();
    const position = $(this)
        .closest(".add-new-job-table")
        .find(".form-position-name")
        .val();
    const department = $(this)
        .closest(".add-new-job-table")
        .find(".form-department")
        .val();
    controller.Model.addNewJob(Number(id), String(position), String(department));
    console.log(department);
    controller.loadJobsTable();
});
