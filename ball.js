export default class Ball{
    constructor(x,y,defectCnt){
        this.x = x;
        this.y = y;
        this.radius = defectCnt / 2;
    }

    draw(ctx,type){
        if(type == 'master'){
            ctx.fillStyle = "rgba(255,10,10,0.3)";
        }else{
            ctx.fillStyle = "rgba(10,255,10,0.2)";
        }   
        ctx.beginPath();
        ctx.arc(this.x,this.y,this.radius,0,Math.PI * 2);
        ctx.fill();
    }
}