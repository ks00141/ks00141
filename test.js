class A{
    constructor(){
        console.log("나는 A클래스의 자식")
    }
    show(){
        console.log("A메소드")
    }
}

class B{
    constructor(){
        console.log("나는 B클래스의 자식")
    }
    show(){
        console.log("B메소드")
    }
}

class C{
    constructor(type){
        if(type === "A"){
            this.__proto__ = A.prototype
        }
        else if(type === "B"){
            this.__proto__ = B.prototype
        }
    }

    method(){
        this.show()
    }
}

var c = new C("B");
c.show()