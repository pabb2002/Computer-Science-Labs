/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author abbaraju_924825
 */
public class DataTypes {
    public static void main(String[] args){
        // There are two parts when making a variable:
            // Declaration - setting aside memory for the data
                // 3 things needed for declaration:
                    // data type, identifier, and semicolon
            // Initialization - to give a variable a value
        
         int num; //declaration of an integer w/ num as memory location; declaration does not have a value
         //System.out.println(num); here gives an error because there is no value in num yet
         // Left side = right side: '=' is the assignment operator
         num = 15; // initialization: starting value
         System.out.println(num);
  
         // 7 primitive (they are lowercase) data types we will use in this class:
         int n; //simple integer
         double d; //2 decimal places
         long l; //long integer
         short s; //short integer
         boolean b; //true/false
         char c; //one character
         float f; //decimals
            // these are all declarations, because there is a data type and identifier
         
         //Object data type
         String name; //String is an Object because it is a Class
                      //Object is the main superclass of java; every Class is an Object
                      // still acts like a primitive data type; need declaration and initialization
         name = "Pranav"; 
         System.out.println(name);
         
         // Data structure - Array (list)
         // data structure is an Object w/methods it needs to function
         String[] list = new String[5]; // declaration and initialization are on the same line
                                        // list is a reference variable, not a variable itself
         System.out.println(list); // reference variables store address, not the actual value
    }
}
