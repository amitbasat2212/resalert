class Filter {
    position:string
    status: string
    stage: string
    gender: string
    constructor(position: string , status: string , stage: string , gender: string ){
        this.position = position
        this.status = status
        this.stage = stage
        this.gender= gender

    }

    empty(){
        this.position = ""
        this.status = ""
        this.stage = ""
        this.gender = ""
    }
}