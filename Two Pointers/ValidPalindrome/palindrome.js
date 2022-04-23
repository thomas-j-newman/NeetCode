/**
 * @param {string} s
 * @return {boolean}
 */
 var isPalindrome = function(s) {
    let regex = /[^A-Za-z0-9]/g;
    
    let newStr = s.replace(regex, "");
    let lowerStr = newStr.toLowerCase();
        let length = lowerStr.length;
        for(let i = 0; i< length; i++){
            if(lowerStr[i] !== lowerStr[length-(i+1)]){
                return false;
            }
        }
        return true;
    };