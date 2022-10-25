
class Controller {
    // renderer = new Renderer()
    Model = new Model()
    async logIn(userName: string, password:string ){
        
    }
    async loadRecipes(ingredient: string, gluten: boolean, dairy:boolean){
        const recipesToRender: Recipe[] = await this.Model.getRecipes(ingredient, dairy, gluten)
        this.renderer.render(recipesToRender)
    }
} 

const controller = new Controller() 


$('#search-btn').on('click', async function(){
    const gluten: boolean = $('#gluten-free').is(':checked')
    const dairy: boolean = $('#dairy-free').is(':checked')
    const ingredient = $("#ingredient").val() 
    if(typeof ingredient === 'string' ){
        await controller.loadRecipes(ingredient, gluten, dairy)
    }
})


$('#container').on('click','.recipe-image', async function(){
    const ingredientElement = $(this).closest('.recipe').find('.ingredient');
    alert(ingredientElement[0].innerHTML)
})