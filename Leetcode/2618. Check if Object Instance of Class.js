/**
 * @param {any} object
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj == null || obj == undefined || typeof classFunction != "function"){
        return false;
    }
    let curr = Object.getPrototypeOf(obj);
    while (curr){
        if (curr == classFunction.prototype) return true;
        curr = Object.getPrototypeOf(curr);
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
