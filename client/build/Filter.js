"use strict";
class Filter {
    constructor(position, status, stage, gender) {
        this.position = position;
        this.status = status;
        this.stage = stage;
        this.gender = gender;
    }
    empty() {
        this.position = "";
        this.status = "";
        this.stage = "";
        this.gender = "";
    }
}
