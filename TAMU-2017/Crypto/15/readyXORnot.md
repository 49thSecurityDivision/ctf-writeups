### Challenge Hint:  

**original data**: "El Psy Congroo"  
**encrypted data**: "IFhiPhZNYi0KWiUcCls="  
**encrypted flag**: "I3gDKVh1Lh4EVyMDBFo="

The flag is not in the traditional gigem{flag} format.

### Challenge Solution:

We have some **original data**, and the encrypted version of that data (**encrypted data**). Additionally, we have the encrypted version of some other data, but not the original (**encrypted flag**). So, the idea of this challenge is to identify what encryption was used to encrypt the **original data**.

I would bet that there are plenty of tools that solve things like this, but I like working with my ‘hands’ as much as possible.

I put the ‘**original data**’ into the following site: [https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html)

Here’s what that site gives back:

**ASCII text:**

El Psy Congroo

**Hex:**

45 6C 20 50 73 79 20 43 6F 6E 67 72 6F 6F

**Binary:**

01000101 01101100 00100000 01010000 01110011 01111001 00100000

01000011 01101111 01101110 01100111 01110010 01101111 01101111

**Decimal:**

69 108 32 80 115 121 32 67 111 110 103 114 111 111

**Base64:**

RWwgUHN5IENvbmdyb28=

This being the case (and because of the name of the challenge), I decided to check the XOR switches from the binary version of our **original data** against the binary version of the **encrypted data**.

  

Here is what that looks like:

**original data** in binary : 00100000 01011000 01100010 00111110 00010110 01001101 01100010 00101101 00001010 01011010 00100101 00011100 00001010 01011011

**encrypted data** in binary: 01000101 01101100 00100000 01010000 01110011 01111001 00100000 01000011 01101111 01101110 01100111 01110010 01101111 01101111

Flip (**F**)/Don't Flip (D): D**FF**DD**F**D**F** DD**FF**D**F**DD D**F**DDDD**F**D D**FF**D**FFF**D D**FF**DD**F**D**F** DD**FF**D**F**DD D**F**DDDD**F**D D**FF**D**FFF**D D**FF**DD**F**D**F** DD**FF**D**F**DD D**F**DDDD**F**D D**FF**D**FFF**D D**FF**DD**F**D**F** DD**FF**D**F**DD

The ‘D’s represent ‘don’t flip’ and the ‘**F**’s represent ‘flip.’ 

Here is what the **encrypted flag** looks like in binary:

00100011 01111000 00000011 00101001 01011000 01110101 00101110 00011110 00000100 01010111 00100011 00000011 00000100 01011010

And here is what it looks like with the Don't Flips (D’s) and the Flips (**F**’s) applied in the same order as applied previously:

01000110 01001100 01000001 01000110 00111101 01000001 01101100 01110000 01100001 01100011 01100001 01101101 01100001 01101110

And what is the ASCII version of this new binary? **FLAF=Alpacaman**

This must be a small type of ‘**FLAG=Alpacaman**.’ Entering **Alpacaman** into the solution field solves the challenge.
