class Canvas{
    constructor(){
        this.canvas = document.createElement("canvas");
        this.ctx = this.canvas.getContext("2d");

        document.body.append(this.canvas);


        window.addEventListener("resize",this.resize.bind(this));
        this.resize();

    }

    resize(){
        this.canvasWidth = document.body.clientWidth;
        this.canvasHeight = document.body.clientHeight;

        this.canvas.style.width = "100%";
        this.canvas.style.height = "70%";
    }
}