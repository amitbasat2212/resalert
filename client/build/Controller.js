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
}
const controller = new Controller();
$("body").on("click", ".dropdown-item", function () {
    console.log(this);
    if ($(this).hasClass('pos')) {
        controller.filters.position = this.innerHTML;
        console.log(controller.filters.position);
    }
    if ($(this).hasClass('stat')) {
        controller.filters.status = this.innerHTML;
        console.log('2');
    }
    if ($(this).hasClass('stage')) {
        controller.filters.stage = this.innerHTML;
        console.log('3');
    }
    if ($(this).hasClass('gender')) {
        controller.filters.gender = this.innerHTML;
        console.log('4');
    }
});
$('#pos-btn').on('click', function () {
    return __awaiter(this, void 0, void 0, function* () {
        const jobs = yield controller.Model.getJobs();
        controller.renderer.renderJobsDropDown(jobs);
    });
});
$('#search-btn').on('click', function () {
    return __awaiter(this, void 0, void 0, function* () {
        yield controller.loadCandidates();
    });
});
$('#clear-filters-btn').on('click', function () {
    controller.filters.empty();
    controller.loadCandidates();
});
$('#toJobs').on('click', function () {
    $('#table-name').text('Jobs');
    controller.loadJobsTable();
});
$('#toCandidates').on('click', function () {
    controller.filters.empty();
    $('#table-name').text('Candidates');
    controller.loadCandidates();
});
