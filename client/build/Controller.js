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
        // renderer = new Renderer()
        this.Model = new Model();
        this.renderer = new Renderer();
    }
    loadCandidates(jobName, status, stage, gender) {
        return __awaiter(this, void 0, void 0, function* () {
            const candidatesToRender = yield this.Model.getCandidates(jobName, status, stage, gender);
            this.renderer.renderCandidates(candidatesToRender);
        });
    }
    loadJobs() {
        return __awaiter(this, void 0, void 0, function* () {
            const jobsToRender = yield this.Model.getJobs();
            this.renderer.renderJobs(jobsToRender);
        });
    }
}
const controller = new Controller();
$("body").on("click", ".dropdown-item", function () {
    console.log("ffffffff");
    if ($(this).hasClass('pos')) {
        // controller.filters.position = this.innerHTML
        console.log('1');
    }
    if ($(this).hasClass('stat')) {
        // controller.filters.status = this.innerHTML
        console.log('2');
    }
    if ($(this).hasClass('stage')) {
        // controller.filters.stage = this.innerHTML
        console.log('3');
    }
    if ($(this).hasClass('gender')) {
        // controller.filters.gender = this.innerHTML
        console.log('4');
    }
});
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
