// Contains a function ArrMax.arrMax that finds and returns the largest element in the array a of length b.
// a & b are both supplied as arguments

// Put your code here.
// ArrMax.vm

function ArrMax.arrMax2
push argument 0   // push m (pointer to the array)
pop pointer 1     //  store m in pointer "that"

push argument 1   // push n (number of elements in the array)
pop local 0       // store n in local variable 0

push constant 32767 // set max_value to the maximum possible value (32767)
not                // set value to min value 
pop local 1        // store min_value in local variable 1

push constant 0   // create counter "i" and set it to zero 
pop local 2       // store i in local variable 2

label LOOP        // start of the loop
push local 2      // push i
push local 0      // push n