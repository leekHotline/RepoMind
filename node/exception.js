
async function riskFunction(){
    throw new Error("something went wrong");
}

try {
    await riskFunction();
} catch (error){

    console.error("caught an error:",error.message);
    process.exit(1);
}