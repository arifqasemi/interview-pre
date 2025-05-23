/***************************************************************************************
*                                                                                      *
*                  CODERBYTE BEGINNER CHALLENGE                                        *
*                                                                                      *
*  Dash Insert                                                                         *
*  Using the JavaScript language, have the function DashInsert(str) insert dashes      *
*  ('-') between each two odd numbers in str. For example: if str is 454793 the        *
*  output should be 4547-9-3. Don't count zero as an odd number.                       *
*                                                                                      *
*  SOLUTION                                                                            *
*  I am going to loop through each number in the string. Test if number is odd using   *
*  modulus. If odd then check if next number is also odd. I have two odd numbers then  *
*  insert dash into the string.
*                                                                                      *
*  Steps for solution                                                                  *
*    1) Initialize idx to zero since using this as our counter                         *
*    2) Use While loop to loop thru string since we will be adding dashes to it        *
*    3) If currrent character is odd and so is next character then insert dash         *
*    4) return modified string as answer                                               *
*                                                                                      *
***************************************************************************************/