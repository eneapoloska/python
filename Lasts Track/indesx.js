
// Pop Front

// Given an array, remove and return the value at the beginning of the array.
// Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!

// Examples:

// popFront([0,5,10,15]) => 0 returned, with [5,10,15] printed in the function
// popFront([4,5,7,9]) => 4 returned, with [5,7,9] printed in the function

function popFront(myList){
    var firstElement = myList[0]
    for(let i = 0;i<myList.length-1; i++){ // i<4
        myList[i]= myList[i+1] // [5,10,15]
    }
    myList.pop()
    console.log(myList)
    return firstElement
}

var lista = [52,5,10,15]
console.log(popFront(lista))

function addToBeginning(element, list) {
    for (let i = list.length; i > 0; i--) {
      list[i] = list[i - 1];
    }
    list[0] = element;
    return list;
  }
  
  // Example usage:
  let myList = [1, 2, 3];
  console.log(addToBeginning(20, myList)); // Output: [0, 1, 2, 3]
  
  // insert at given index

  function insertAt(lista, indeksi, vlera){

    for(let i = 0; i<lista.length; i++){
        if (i == indeksi){
            for (i=lista.length; i>indeksi; i--){
                lista[i] = lista[i - 1];
            }
            lista[i]=vlera
            return lista
        }
        else {
        }
    }
}

console.log(insertAt([9,33,7], 1, 42))