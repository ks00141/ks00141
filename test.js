
import Ball from "./ball.js";

class App{
    constructor(){
        this.masterTotalDefectCnt = 0;
        this.masterDefectCnt = 0;
        this.testTotalDefectCnt = 0;
        this.testDefectCnt = 0;
        this.commonDefectCnt = 0;

        this.canvas = document.createElement("canvas");
        this.ctx = this.canvas.getContext("2d");


        this.masterForm = document.createElement("form");
        this.masterForm.style.width = "20%";

        this.Label1 = document.createElement("span");
        this.Label3 = document.createElement("span");
        this.Label5 = document.createElement("span");

        this.Label1.style.display = "block";
        this.Label3.style.display = "block";
        this.Label5.style.display = "block";
        
        this.masterTotalInput = document.createElement("input");
        this.testTotalInput = document.createElement("input");
        this.commonInput = document.createElement("input");
        this.commonInput.style.display = "block";
        
        this.masterBtn = document.createElement("button");
        this.masterBtn.innerText = "Show";
        this.masterBtn.style.width = '40%';
        this.masterBtn.style.display = "block";

        this.Label1.innerText = "Master Total Defect";
        this.Label3.innerText = "Test Total Defect"
        this.Label5.innerText = "Common Defect"

        this.masterBtn.addEventListener("click",(e)=>{
            e.preventDefault();
            this.masterTotalDefectCnt = this.masterTotalInput.value;
            this.testTotalDefectCnt = this.testTotalInput.value;
            this.commonDefectCnt = this.commonInput.value;
            this.masterRender();
        })
    
        this.masterForm.append(this.Label1);
        this.masterForm.append(this.masterTotalInput);

        this.masterForm.append(this.Label3);
        this.masterForm.append(this.testTotalInput);

        this.masterForm.append(this.Label5);
        this.masterForm.append(this.commonInput);


        this.masterForm.append(this.masterBtn);

        
        
        document.body.append(this.canvas);
        document.body.append(this.masterForm);
        
        
        window.addEventListener("resize",this.resize.bind(this));
        this.resize();


    }

    resize(){   
        this.canvasWidth = document.body.clientWidth;
        this.canvasHeight = document.body.clientHeight;

        this.canvas.width = this.canvasWidth * 1.5;
        this.canvas.height = this.canvasHeight * 2;
        
        this.canvas.style.width = "80%";
        this.canvas.style.height = "80%";
        this.masterRender();
    }
    masterRender(){
        this.ctx.clearRect(0,0,this.canvas.width,this.canvas.height);
        if(this.masterTotalDefectCnt >= 1){
            this.masterBall = new Ball(this.canvasWidth * 0.75 - (parseInt(this.masterTotalDefectCnt) / 2) * (1 - parseInt(this.commonDefectCnt) / parseInt(this.testTotalDefectCnt) * (parseInt(this.testTotalDefectCnt) / parseInt(this.masterTotalDefectCnt))) ,this.canvasHeight,this.masterTotalDefectCnt);
            console.log((1 - parseInt(this.commonDefectCnt) / parseInt(this.testTotalDefectCnt)));
            this.masterBall.draw(this.ctx,"master");
        }
        if(this.testTotalDefectCnt >= 1){
            this.testBall = new Ball(this.canvasWidth * 0.75 + (parseInt(this.testTotalDefectCnt) / 2) * (1 - parseInt(this.commonDefectCnt) / parseInt(this.testTotalDefectCnt)), this.canvasHeight,this.testTotalDefectCnt);
            console.log(this.canvasWidth)
            console.log(this.testDefectCnt);
            this.testBall.draw(this.ctx,"test");
        }

        
    }

}

window.onload = ()=>{
    new App();
}