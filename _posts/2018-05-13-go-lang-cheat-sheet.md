---
layout: post
title: "Go Lang Cheat Sheet"
date: 2018-05-13
categories: ['Programming']
excerpt_separator: <!--more-->
categories: ['golang']
---

This blog is a cheat sheet for Go lang. A quick reference for type of variables , loops, comments, conditional operators, strings, slices etc.

<!--more-->

## Packages: 
### fmt.Println:
- Println by default prints \n at the end of the output.

## Comments:
<pre>
// Single line comment
</pre>

<pre>
/*
Multiline
comment here
*/ 
</pre>

## Operators:
#### Increment Operators:
+=
a += b
means: a = a +b

i++ is same as i + 1 which is same as i += 1


#### Arithmetic Operators:
<pre>
+ Addition
- Substraction
* Multiplication
/ Division
% Remainder
</pre>

#### Logical Operators:
<pre>
&& - AND
|| - OR
!  - NOT
</pre>


#### Comparision Operators:
== To test the equality.

Example: x == y

## Reserved Words
- true and false are reserved words in go.

## Variables:
- Variable Declaration:
    var x string = "Vinayak" // You are declaring and assinging the variable a value
    var x string // Just declaring
    string = "vinayak" // And now assigning
    x := "Vinayak" // This is going to create variable x of type string and assign "Vinayak" to it
    x := 8 // In this case and integer var is created and assigned 8 as value
- camelCase or mixedCase or bumpyCaps or camelBack or HumpBack is preffered way to declared variables

- Scope of variable:
1. global variables are declared outside of Main.

- Defining multiple variables:
var (
a = 1
b = 3
c = 15
)

- You cannot just declare a variable in go and NOT use it. It will throw an error like: variable declared not used



## Data Types:
#### Numbers:
1. integers:
    - Unsigned (Only zero or positive numbers):
        uint8 : 2^8 = 0 - 255
        uint16 : 2^16 = 65536
        uint32 : 2^32 = 
        uint64 : 2^64 = 
    - Signed:
        int(8,16,32,64)

2. float:
    - float32
    - float64


#### Strings:
- Strings can be created using :
  "Hello World" : These allows special escape characters. \n, \t are replaced with newline and tab resp
  `Hello World` : These can contain newlines.

- Strings index start at 0

- concatenation: Can be done using + operator

- operations on strings:
1. len("vinayak")
2. "vinayak"[3] : This is going to return byte value of character at 3rd (4th position including 0) which is a in this case.


#### Booleans
- Boolean datatype is name after George Boole and is a 1 bit integer to represt on or off

#### Arrays:
- Arrays in Go store same type of elements laid our sequentially and have fixed length.
- Declaration syntax:
    var name_of_variable [length]type
    var x [5]int
- In the above example, all the five values of the array x are zeroed, initialized with 0 value
- Here x, does not denote pointer to the starting element of array, but the entire array itself.
- When you assign or pass around array value, the entire arrays contents is copied.
- Declaring and initializing Arrays
    x := [5]int{1,2,3,4,5}
    x := [...]int{1,2,3,4,5}
- In both the cases, x array is initialized with a count of 5 variables.
- Index start at 0
- Uninitialized elemets of INT type arrays are set to 0
- Length of array:
  len(x)
- Iterating over Arrays:
<pre>
    for i:=0 ; i < len(x) ; i++ {
    fmt.Println(x[i])
}
</pre>

#### Slices
- Slices are nothing but segment or piece of array and have indexes and length just like array.
- Difference between slice and array:
1. length of array is fixed at declaration time. Slices length varies.
2. 
- Declaration of slice:
    var slice_name []Type
    Note: There is not length specified here.
- Creation of empty Slices:
    make([]int, 5)
    make([]element_type, lenth, capacity)

- The above example is going to create a slice of length 5 of int type elements. When the capacity is omited, it defaults to length of the array.
- Finding length and capacity of arrays:
<pre>
slice1 := make([]int,5,6)
//length of array = len(slice1)
//capacity of array = cap(slice1)
</pre>

- Another way to use slices is to use the low:high as explained below:
array := [5]int{1,2,3,4,5}
slice1 := array[0:4]

- array[0:] is same as array[0:len(array)]
- array[:] is same as array[0:len(array)]

- Iterating over set of elements in slice
s[m:n] refer to elements m through n-1
os.Args[1:len(os.Args)] = os.Args[1:]

- Iterating over range of elements in slice

<pre>
    for _, arg := range os.Args[1:] {
        s = s + sep + arg
        sep = " "
    }
</pre>

In the above example, range os.Args[1:] will return, index and the element at that index.
Since we do not need the index we discard it by storing it in the blank identifier which is _ here.
The value for the index is stored in _ which is later on discarded or cleaned up by the garbage collector.

#### Maps/hash/dictionaries:
- Maps are unordered collection of key-value just like in Python
- Declaration:
1. var x map[string]int
- This is read as:
x is a map of strings to int
- var x map[type_for_key]type_for_value

- maps needs to be initialized before using them. This can be done using the make() function:
x := make(map[string]string)
This can be read as:

initialize an empty map x of key type string and value type string
- Maps can be declated and initialized like arrays as below:

nameToSurnameMap := map[string]string{
    "vinayak" : "lokhande",
    "poonam" : "gaikar",
    "aryansh" : "lokhande"
}

- Setting/updating elements in maps can be done as below:
x["key"] = 10

- maps also has length, with new values initialized, the length of maps increase
- We can delete items from MAP using the delete function
delete(key,1)

- Use of value, ok in maps. While accessing values in map, it returns two things: value, status
- This can be used as below:
value, status := x["key"]

## for loop:
- Only loop is go is for loop.
- Syntax
<pre>
    for initialization; condition; post {
    //Do whatever you want to do here
}

</pre>

- Opening brace should be on the same line as that of post
- Any of initialization/condition/post can be omitted

- while 1 loop:
<pre>
    for {
    //looping forever.
}

</pre>

- conditional loop:

<pre>
    for some_condition {
    //do something
}

</pre>

## FUNCTIONS:
- function are declared as :
    func function_name(arg type) returntype {}

- func function_name(arg type) (returnvarname returntype) {}

example:
<pre>
// func function_name(arg type) returntype {}
func getTotalnoRetName(x []int) int {
    xs := []int{1, 2, 3, 4, 5}
    total := 0
    for _, value := range xs {
        total += value
    }
    return total
}

// func function_name(arg type) (returnvarname returntype) {}
func getTotalRetName(x []int) (total int, count int) {
    xs := []int{1, 2, 3, 4, 5}
    total = 0
    i := 0
    for _, value := range xs {
        total += value
        i++
    }
    count = i
    return
}

func main() {
    a := []int{1, 2, 3, 4, 5}
    fmt.Println(getTotalnoRetName(a))
    t, c := getTotalRetName(a)
    fmt.Println(t, c)
}
</pre>

#### Variadic function
- You can pass zero or more arguments to a function.
- Example:

<pre>
    func variadicFunction(numbers ...int) (total int, count int) {
    total = 0
    i := 0
    for _, value := range numbers {
        total += value
        i++
    }
    count = i
    return
}


</pre>

- Slices can also be passed to the variadic functions as variables:


## Command line arguments:
package os

Usage:
os.Args
os.Args[0] will return the command name
os.Args[1:]

