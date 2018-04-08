public class DataTypeNotes {                          // class header, encapsulation
	public static void main(String[] args){           // lexical error if String is lowercase; syntax errors are just punctuation mistakes
		System.out.println("Hello");                  // String literal
		System.out.println(5);
		System.out.println(2.3);
		System.out.println(true);
		System.out.println(5 < 2); 				      // this is also a boolean
		System.out.println('A');	 				  // can only put one character because char - it would be a lexical error
		
		
		String hello = "Hello";
		System.out.println(hello);
		int num = 5; 								  // identifier must be useful indicator of what is being held
		System.out.println(num);
		double decimal = 2.3;
		System.out.println(decimal);
		boolean bool = 5<2;
		System.out.println(bool);
		char letter = 'A';
		System.out.println(letter);
		
		// declaration/initialization can also be on separate lines
		boolean b; //declaration
		b = 7>8; //initialization
		System.out.println(b);
		
		//Constant - add 'final' and all letters of identifier have to be capitalized
		final double AVA = 6.02;
		System.out.println(AVA);
		// AVA = 7; => doesn't work
		System.out.println(Math.PI); // 12 decimal places is double, 16 is float
		
		
		
		// printf is for formatting
		System.out.printf("%s is %d, %.2f%n", "Pranav", 15, 99.6942); // when putting a String into a printf, you can use the %s flag
											      // you can use this for all data types: %d for int (digit), %s for String, %f for float, etc.
												  // %.2f rounds the float to two decimal places 
												  // you can still type in letters like 'is' because it is still a string but with tags 
		System.out.println("next line"); //prints on the same line as the previous one, so printf does not make a new line - you can use %n or \n 
	}	
}