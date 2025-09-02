// let rows = prompt('Enter rows count');


// for (let row = 0; row < rows; row++){
//     let stars = '';
//     for (let index = 0; index <= row; index++){
//         stars += '*';
//     }
//     console.log(stars);
// }

// function sum(times, ...args){
//     let result = 0;
//     for(let index of args)
//         result += index;
//     return times * result;

// }

// console.log(sum(2, 3, 6, 7, 2, 2, 10, 5));


// Prime numbers print (uncomplete)
// function isPrime(index){
    
//     if((index % 2 === 0 && index !== 2) || (index % 3 === 0 && index !==3)){
//         console.log(index, " not prime number!");
//     }
//     else {
//         console.log(index, ' is prime number')
//     }
// }

// let index = prompt("Enter a number");

// isPrime(index);


// Reversing Arrays
// let numbers = [1, 2, 3, 4, 5];

// let names = ['Naser', 'Zayed', 'Omar', 'Mohammad', 'Fares', 'Saad', 'Majed']

// let random = [true, 'Omar', 'Bassam', false, 25, 'Naser'];

// console.log(numbers);

// function reverse(array){
//     let x = [];
//     for (let i of array){
//         x.unshift(i);        
//     }
//     array = x;
//     return array;
// };

// console.log(reverse(random));


let randarray = [3, 6, 2, 20, 48, 5, 1];

function sortArray(arr){
    let swapped;

     do{
        swapped = false;
        for(let i = 0; i < arr.length; i++)
            if(arr[i] > arr[i+1]){
                let tmp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = tmp;
                swapped = true;
            }
    } while(swapped)
        
    return arr;
}

console.log(sortArray(randarray));