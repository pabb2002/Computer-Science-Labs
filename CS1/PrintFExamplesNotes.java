/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package data.types;

/**
 *
 * @author abbaraju_924825
 */
import java.util.*; //asterisk is a wild card like in python => all things are imported from the library


public class PrintFExamplesNotes {
    public static void main(String[] args){
        //List the five things required to declare and initialize variables:
        //1. data type, 2. identifier, 3. assignment operator (=), 4. actual value the variable is holding, 5. semicolon (;)
        int myAge = 15; //both declaration and initialization in one line
        char firstInitial; //declaration
        firstInitial = 'P'; //initialization
        System.out.printf("%d%n%c%n", myAge, firstInitial); //you need a string, and a value, and those values go into the string with a FORMAT SPECIFIER (%)
        //d for digit(int), n for new line, c for char
        //shift+F6 to run classes that are not the main class
        //creates the string that inserts values into the string at specific times
        //anything followed by percent must indicate one of the values listed later (unless its an escape sequence)
        
        //REASSIGNMENT:
        //reassignment is changing the value of a variable that has already been declared: override of the original value
        //How many times do you declare a variable? => only once
        myAge = 16;
        myAge = 17; //reassigning myAge => override of the original value
        firstInitial = 'O';
        System.out.printf("%d%n%c%n", myAge, firstInitial);
        
        //FORMAT SPECIFIERS start with a % followed by a letter, the letter represents a type of output specific value
        /*
            1. %s => String
            2. %d => int
            3. %f => decimal(float/double) - 6 decimal places
            4. %e => scientific notation - also 6 decimal places (e+01, etc)
            5. %g => displays 7 allocated spaces or significant figures 
            6. %b => boolean
            7. %c => char
            8. %% => prints %
            9. %n => newline 
            10. %t* => Calendar (asterisk represents many things that can go after %t)
            => 8 and 9 are not really format specifiers, but can be used within printf
        */
        double dec = 0.56458945;
        System.out.printf("%e%n%f%n%g%n%b%n%f%n%%%n", dec, dec, dec, dec, dec); //if you put %c, there is an illegal format convertion expception error
        System.out.printf("%s Washington %s %s %.2f", "George", "Carver", 56, 56.8756); //missing format argument exception error if you add more format specifiers than the values given afterword
        //if there are more values than format specifiers, there is no error, it just doesn't print out the extra values
        //you can use %s for a number, it will get converted into a string
        //%s can also be used for decimals, it jsut won't round to specific number of decimals if you add like .2 behind the s
        
        
        //Calendar (Java Class): time, date, 33 other things
        //two things needed to use Calendar:
            //1. import java.util.*; (side note: java.lang.*; is the only library preloaded)
            //2. create a Calendar instance
            //3.  
        Calendar cal = Calendar.getInstance(); //this line allows the use of Calendar methods
        System.out.printf("%n%tc%n", cal); //cal is a reference variable, while the ones previously used were normal variables
        //there are many format specifiers for Calendar (made up by %t and something after it)
        
        //String.format: same thing as printf but now you can save it in a variable and use a println to print it
        String middle = "middle";
        String output = String.format("%s%n%%\n", middle);
        System.out.println(output);
        
        //lexical, logic, syntax, and runtime are the 4 types of errors in Java
        
    }
}
