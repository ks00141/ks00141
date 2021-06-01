function setUser(text){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve(text);
        },1000);
    })
}
async function test(){
    var user = await setUser("yh");
    console.log(user);
    console.log("end");
}

test();